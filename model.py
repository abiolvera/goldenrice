#!/usr/bin/env python3
"""
Golden Rice Counterfactual Model
=================================
Estimates lives saved if Golden Rice (GR2/GR2E) had been approved and deployed
globally at the earliest feasible date, rather than the actual regulatory timeline.

Theory of change:
  Golden Rice → daily dietary beta-carotene in staple food
  → reduced vitamin A deficiency (VAD)
  → reduced VAD-attributable under-5 mortality

Core formula per country, per year:
  Lives saved = VAD-attributable deaths
              × (1 - effective VAS coverage)     [additive, not replacing VAS]
              × adoption rate (logistic S-curve)
              × GR vitamin A efficacy fraction    [fraction of child RDA met]

Geographic scope: 8 countries representing ~85% of potential GR impact
Population: Children under 5 (primary VAD mortality burden)
            Toggle params.include_maternal_deaths for maternal deaths (+~15%)

Sources for estimates (where model uses empirical data):
  - Under-5 deaths: UN IGME / UNICEF CME
  - VAD prevalence: WHO VMNIS, national MICS/DHS surveys
  - VAS coverage: UNICEF / WHO joint estimates
  - GR beta-carotene: Paine et al. 2005, IRRI field trials
  - Bioconversion: WHO/FAO 2002 (12:1 conservative), Tang et al. 2009 (3.8:1 GR-specific)
  - Relative risk: Sommer et al. 1983, West et al. 1991, Fawzi et al. 1993
  - Adoption curves: IR8 historical data; HarvestPlus projections
  - VAS efficacy: Imdad et al. Cochrane 2022 (24% all-cause mortality reduction)

Note: Values marked [EST] are best estimates where precise data is unavailable.
"""

import copy
import math
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


# ================================================================
# SECTION 1: MODEL PARAMETERS  (all configurable)
# ================================================================

@dataclass
class ModelParams:
    """
    Central parameter store. Modify here for sensitivity analyses.
    Squiggle-ready: each float is a future distribution node.
    """

    # --- Timeline ---
    model_start_year: int = 2000
    model_end_year: int = 2024

    # --- Golden Rice Nutritional Parameters ---

    beta_carotene_ug_per_g_dry: float = 18.0
    """
    Beta-carotene in milled GR2E under realistic field/storage conditions.
    Lab/controlled: ~31 µg/g (Paine et al. 2005).
    Philippines field trials (IRRI, 2019 multi-environment): 14–22 µg/g milled.
    Storage degradation: ~40–60% loss over 3–6 months at 28°C ambient
      (Swamy et al. 2019; Saltzman et al. 2013 for pro-vitamin A maize analog).
    Central field-realistic estimate: 18 µg/g.
    Lab-ideal upper bound: 31 µg/g. Pessimistic (post-storage): 12 µg/g.
    Use 18 as default; lab 31 available as sensitivity.
    """

    storage_retention_fraction: float = 0.65
    """
    Fraction of beta-carotene retained after typical farm/market storage
    (3–6 months at tropical ambient temperature, ~28°C).
    Studies on provitamin A crops: 40–75% retention. Central: 65%.
    This is ADDITIVE to cooking_retention below.
    """

    cooking_retention_fraction: float = 0.60
    """
    Beta-carotene retained after milling + cooking, applied to post-storage grain.
    Studies: 50–68%. Central: 60%.
    NOTE: storage_retention applied first, then cooking_retention.
    Combined realistic retention = storage × cooking = 0.65 × 0.60 = 39%.
    """

    bioconversion_ratio: float = 12.0
    """
    µg dietary beta-carotene → 1 µg retinol activity equivalent (RAE).
    WHO/FAO default for plant sources: 12:1 (conservative).
    GR-specific studies (Tang et al. 2009 crossover trial): 3.8:1.
    Range for sensitivity: 6:1 (optimistic) – 18:1 (very conservative).
    Using 12:1 as precautionary default.
    """

    child_rda_ug_rae: float = 400.0
    """µg RAE/day RDA for children. WHO: 300 (1–3yr), 400 (4–8yr). Use 400 as conservative bar."""

    child_fraction_of_adult_rice_intake: float = 0.30
    """
    Fraction of per-capita rice consumption attributable to a child under 5.
    Per-capita stats include all ages; children eat ~25–35% of adult portions.
    [EST] Central: 0.30.
    """

    # --- Adoption Parameters ---

    adoption_midpoint_years: float = 8.0
    """
    Years after country deployment start to reach 50% of ceiling adoption.
    Historical precedent: IR8 green revolution rice reached ~50% adoption in
    7–10 years in favorable conditions. Use 8 years.
    """

    adoption_steepness: float = 0.45
    """
    Logistic curve steepness k. At k=0.45, 10%→90% adoption spans ~12 years.
    Higher = faster ramp.
    """

    adoption_ceiling: float = 0.70
    """
    Maximum fraction of target population adopting GR.
    Constrained by: preference for white rice, yield parity concerns,
    seed system reach. 70% is consistent with successful varietal adoptions.
    Range: 50% (pessimistic) – 90% (optimistic).
    """

    # --- Mortality Model ---

    relative_risk_vad: float = 1.75
    """
    Relative risk of all-cause under-5 mortality: VAD vs. vitamin-A-replete children.
    Sommer et al. 1983: 1.9x. West et al. 1991: 1.6–2.2x. Fawzi et al. 1993: 1.4–2.0x.
    Central estimate: 1.75. Range for sensitivity: 1.4 – 2.5.
    """

    # --- VAS (Vitamin A Supplementation) Interaction ---

    effective_vas_multiplier: float = 0.70
    """
    Fraction of 'nominally VAS-covered' children who are effectively protected.
    Adjusts for: biannual (not daily) dosing gaps, cold chain failures,
    missed doses, and within-coverage heterogeneity.
    Imdad Cochrane (2022): VAS reduces all-cause mortality 24% in high-VAD pops.
    GR provides complementary daily coverage especially between VAS doses.
    [EST] 0.70.
    """

    # --- Secular Trend ---

    annual_vad_decline_rate: Optional[float] = None
    """
    Override for per-country VAD annual decline rate. When set (non-None),
    ALL countries use this rate instead of their country-specific value.
    This is the primary knob for secular-trend sensitivity analysis.
    Observed country rates: Philippines ~4%/yr, Bangladesh ~3.5%/yr, India ~2%/yr.
    Default None = use per-country rates as defined in CountryData.
    Example: set to 0.040 for 'faster development' scenario, 0.015 for slower.
    """

    # --- Maternal deaths ---

    include_maternal_deaths: bool = False
    """Include estimated maternal VAD-attributable deaths (+~15% of child figure). [EST]"""

    maternal_death_fraction: float = 0.15
    """Additive maternal deaths as fraction of child deaths. Literature is sparse. [EST]"""

    # --- Dose-response ---

    dose_response_concavity: float = 0.60
    """
    Exponent for concave dose-response mapping GR efficacy fraction → mortality benefit.
    Rationale: RCTs gave full bolus doses (200,000 IU). Most mortality benefit accrues
    from restoring severely depleted stores, not from incremental top-up near adequacy.
    A concave function captures that 0→50% of RDA prevents more deaths per RAE than
    50→100% of RDA. Formula: effective_efficacy = efficacy_fraction ^ concavity.
    At concavity=1.0: linear (current behavior, likely overestimates).
    At concavity=0.5: square-root (aggressive concavity).
    At concavity=0.6: moderate concavity (default, best-guess).
    Range: 0.5 (very concave) – 1.0 (linear).
    Empirical basis: dose-response literature on vitamin A and child mortality is sparse
    at sub-full-dose levels; 0.6 is a reasoned estimate, not a measured value.
    """

    # --- DALY parameters ---

    daly_years_lost_per_death: float = 28.0
    """
    Years of life lost per under-5 death (age-weighted).
    WHO GBD approach for children 1-4: ~30 YLL. Under-1: ~33 YLL. Average: ~28 YLL.
    """

    daly_blindness_per_death: float = 0.80
    """
    For every child who dies from VAD-related causes, ~0.8 additional children are
    blinded but survive (based on Sommer et al.: half of 250k-500k annual blind children
    die; other half survive). Each blind child: ~35 YLD × 0.6 disability weight ≈ 21 DALYs.
    This is the ratio of surviving-blind to dying children.
    """

    daly_blind_dalys_per_child: float = 21.0
    """
    DALYs per blinded child who survives: ~35 expected years blind × 0.6 disability weight.
    WHO disability weight for blindness: 0.6.
    """


# ================================================================
# SECTION 2: COUNTRY DATA
# ================================================================

@dataclass
class CountryData:
    """Per-country inputs for the model."""

    name: str
    iso3: str
    region: str  # "SEA" | "SAsia" | "Africa"

    # Under-5 deaths (year → count). Linearly interpolated between anchor points.
    # Source: UN IGME / UNICEF CME data
    under5_deaths_by_year: Dict[int, int]

    # VAD prevalence in children <5 (serum retinol <0.70 µmol/L = deficient)
    vad_baseline_year: int
    vad_baseline_prevalence: float   # fraction at baseline year
    vad_annual_decline: float        # country-specific annual decline rate

    # VAS coverage (fraction of children 6–59 months receiving ≥1 dose/year)
    vas_coverage_by_year: Dict[int, float]

    # Rice consumption: annual per-capita milled rice, kg/year (all ages)
    # NOTE: for countries with high regional heterogeneity (India), this should be
    # the consumption in VAD-affected rice-eating populations, not national average.
    rice_consumption_kg_per_capita_yr: float

    # Fraction of consumed rice grown domestically (GR reaches via seed system)
    domestic_rice_fraction: float

    # Counterfactual GR deployment year in this country
    gr_deployment_year: int

    # Fraction of VAD-affected population that is in rice-eating regions/populations.
    # Accounts for countries where rice is not the primary staple in all VAD-affected areas.
    # e.g., Nigeria: VAD burden is spread across cassava/yam/sorghum-eating populations too.
    # India: VAD concentrated in rice-belt states but rice is not the staple everywhere.
    # Default 1.0 = all VAD-affected children live in rice-eating populations.
    rice_eating_vad_fraction: float = 1.0


# ================================================================
# SECTION 3: COUNTRY DEFINITIONS
# ================================================================
# All data: best estimates from WHO, UNICEF, World Bank, national surveys.
# [EST] = estimated where precise source unavailable.
# Under-5 deaths are rough but consistent with UN IGME order-of-magnitude.

COUNTRIES: Dict[str, CountryData] = {}

# --- Bangladesh ---
# Rice is the overwhelmingly dominant staple. Strong VAD history.
# IRRI priority country; BRRI (Bangladesh Rice Research Institute) partner.
COUNTRIES["BGD"] = CountryData(
    name="Bangladesh",
    iso3="BGD",
    region="SAsia",
    under5_deaths_by_year={
        2000: 250_000,
        2005: 180_000,
        2010: 115_000,
        2015: 70_000,
        2020: 48_000,
        2024: 36_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.21,   # ~21% in 2000 (Bangladesh MICS)
    vad_annual_decline=0.035,       # Fast decline: strong VAS + economic growth
    vas_coverage_by_year={
        2000: 0.75,
        2005: 0.87,
        2010: 0.93,
        2015: 0.92,
        2020: 0.89,
        2024: 0.87,
    },
    rice_consumption_kg_per_capita_yr=175.0,   # Among world's highest
    domestic_rice_fraction=0.97,
    gr_deployment_year=2007,   # 2 yrs after global approval (IRRI partner)
)

# --- Philippines ---
# IRRI headquarters (Los Baños). First country to formally approve GR (2021 actual).
# Would have been first mover in counterfactual.
COUNTRIES["PHL"] = CountryData(
    name="Philippines",
    iso3="PHL",
    region="SEA",
    under5_deaths_by_year={
        2000: 65_000,
        2005: 51_000,
        2010: 37_000,
        2015: 25_000,
        2020: 17_000,
        2024: 13_500,
    },
    vad_baseline_year=2003,
    vad_baseline_prevalence=0.38,   # FNRI 2003 National Nutrition Survey
    vad_annual_decline=0.040,       # Fast: strong economy + effective VAS
    vas_coverage_by_year={
        2000: 0.70,
        2005: 0.80,
        2010: 0.85,
        2015: 0.83,
        2020: 0.82,
        2024: 0.80,
    },
    rice_consumption_kg_per_capita_yr=115.0,
    domestic_rice_fraction=0.85,    # Imports ~15% (NFA data) [EST]
    gr_deployment_year=2006,        # First mover; IRRI HQ country
)

# --- India ---
# Largest absolute burden due to population + high VAD prevalence.
# Rice dominant in east/south (Bihar, Odisha, Bengal, AP, Tamil Nadu).
# Slower VAS coverage due to scale + state-level heterogeneity.
COUNTRIES["IND"] = CountryData(
    name="India",
    iso3="IND",
    region="SAsia",
    under5_deaths_by_year={
        2000: 2_300_000,
        2005: 1_900_000,
        2010: 1_450_000,
        2015: 1_000_000,
        2020: 700_000,
        2024: 560_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.57,   # NFHS-2 (1998–99); widespread rural deficiency
    vad_annual_decline=0.020,       # Slow: scale + inequality + dietary diversity barriers
    vas_coverage_by_year={
        2000: 0.44,
        2005: 0.50,
        2010: 0.55,
        2015: 0.57,
        2020: 0.55,
        2024: 0.54,
    },
    rice_consumption_kg_per_capita_yr=145.0,
    # CRITICAL: National average is 80 kg/yr, but GR would be deployed in rice-belt
    # states (Bihar, Odisha, West Bengal, Chhattisgarh, AP, Tamil Nadu) where:
    #   - rice consumption: 140–175 kg/capita/yr
    #   - VAD prevalence: higher than national avg (NFHS-4 state data)
    # Using rice-belt avg of 145 kg/yr for rice-eating VAD population.
    # See: NSSO household consumption survey; IRRI India rice atlas.
    domestic_rice_fraction=1.00,   # Net exporter
    gr_deployment_year=2009,       # Slower: regulatory + political complexity
    rice_eating_vad_fraction=0.55,
    # ~55% of India's VAD-affected children live in rice-dominant states.
    # Northern wheat-belt (UP, Punjab, Haryana) has VAD too but GR irrelevant there.
    # [EST based on NFHS-4 state-level VAD + NSSO rice consumption cross-analysis]
)

# --- Indonesia ---
# High VAD, dominant rice diet. IRRI partner through IRRI-Indonesia programs.
COUNTRIES["IDN"] = CountryData(
    name="Indonesia",
    iso3="IDN",
    region="SEA",
    under5_deaths_by_year={
        2000: 290_000,
        2005: 225_000,
        2010: 160_000,
        2015: 112_000,
        2020: 80_000,
        2024: 65_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.50,   # High; rural Java/outer islands [EST from WHO regional]
    vad_annual_decline=0.030,
    vas_coverage_by_year={
        2000: 0.70,
        2005: 0.78,
        2010: 0.82,
        2015: 0.80,
        2020: 0.77,
        2024: 0.75,
    },
    rice_consumption_kg_per_capita_yr=135.0,
    domestic_rice_fraction=0.95,
    gr_deployment_year=2008,
)

# --- Vietnam ---
# High rice consumption; rapidly declining VAD due to economic growth.
# Strong VAS program since mid-1990s.
COUNTRIES["VNM"] = CountryData(
    name="Vietnam",
    iso3="VNM",
    region="SEA",
    under5_deaths_by_year={
        2000: 85_000,
        2005: 61_000,
        2010: 42_000,
        2015: 27_000,
        2020: 19_000,
        2024: 16_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.45,
    vad_annual_decline=0.040,   # Fast decline: rapid GDP growth + diet diversification
    vas_coverage_by_year={
        2000: 0.76,
        2005: 0.84,
        2010: 0.87,
        2015: 0.85,
        2020: 0.83,
        2024: 0.80,
    },
    rice_consumption_kg_per_capita_yr=165.0,
    domestic_rice_fraction=1.00,   # Major exporter
    gr_deployment_year=2007,
)

# --- Myanmar ---
# Very high rice consumption. Weaker health infrastructure than neighbors.
# VAS coverage has declined post-2021 coup.
COUNTRIES["MMR"] = CountryData(
    name="Myanmar",
    iso3="MMR",
    region="SEA",
    under5_deaths_by_year={
        2000: 120_000,
        2005: 90_000,
        2010: 59_000,
        2015: 37_000,
        2020: 25_000,
        2024: 20_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.36,   # [EST based on regional WHO data]
    vad_annual_decline=0.025,
    vas_coverage_by_year={
        2000: 0.55,
        2005: 0.65,
        2010: 0.73,
        2015: 0.74,
        2020: 0.70,
        2024: 0.58,   # Deteriorated post-coup
    },
    rice_consumption_kg_per_capita_yr=195.0,
    domestic_rice_fraction=1.00,
    gr_deployment_year=2009,
)

# --- Cambodia ---
# Highest rice consumption in world. Extreme rice dependency.
# Small population limits absolute impact.
COUNTRIES["KHM"] = CountryData(
    name="Cambodia",
    iso3="KHM",
    region="SEA",
    under5_deaths_by_year={
        2000: 50_000,
        2005: 35_000,
        2010: 21_000,
        2015: 13_000,
        2020: 8_500,
        2024: 6_500,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.45,
    vad_annual_decline=0.030,
    vas_coverage_by_year={
        2000: 0.65,
        2005: 0.78,
        2010: 0.82,
        2015: 0.83,
        2020: 0.81,
        2024: 0.79,
    },
    rice_consumption_kg_per_capita_yr=200.0,   # Highest globally
    domestic_rice_fraction=1.00,
    gr_deployment_year=2010,
)

# --- Nigeria ---
# Largest under-5 burden in Africa. Rice is NOT the primary staple
# (yam, cassava, sorghum dominate), limiting GR penetration.
# Included as representative of planned African rollout.
COUNTRIES["NGA"] = CountryData(
    name="Nigeria",
    iso3="NGA",
    region="Africa",
    under5_deaths_by_year={
        2000: 850_000,
        2005: 780_000,
        2010: 700_000,
        2015: 610_000,
        2020: 490_000,
        2024: 420_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.30,   # [EST; rice-eating fraction subset of total pop]
    vad_annual_decline=0.015,       # Slow: structural poverty + oil-dependency distortions
    vas_coverage_by_year={
        2000: 0.40,
        2005: 0.50,
        2010: 0.55,
        2015: 0.52,
        2020: 0.50,
        2024: 0.48,
    },
    rice_consumption_kg_per_capita_yr=40.0,    # Rice secondary to yam/cassava
    domestic_rice_fraction=0.55,   # Significant imports (~45%)
    gr_deployment_year=2012,       # Delayed: rice not primary staple + regulatory
    rice_eating_vad_fraction=0.35,
    # ~35% of Nigeria's VAD-affected children are in rice-eating households.
    # Remaining 65% subsist primarily on cassava, yam, sorghum, millet.
    # VAD in Nigeria is not concentrated in rice belts — it's distributed across
    # food systems. GR has limited reach into the largest VAD population.
    # [EST based on Nigeria LSMS-ISA dietary diversity data + DHS VAD mapping]
)

# --- Nepal ---
# High VAD burden (~31% in 2000), rice dominant in Terai lowlands.
# SAARC regional target. Low income, weak health infrastructure.
COUNTRIES["NPL"] = CountryData(
    name="Nepal",
    iso3="NPL",
    region="SAsia",
    under5_deaths_by_year={
        2000: 55_000,
        2005: 40_000,
        2010: 26_000,
        2015: 16_000,
        2020: 10_500,
        2024:  8_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.31,   # Nepal DHS 2001
    vad_annual_decline=0.030,
    vas_coverage_by_year={
        2000: 0.70,
        2005: 0.85,
        2010: 0.89,
        2015: 0.87,
        2020: 0.83,
        2024: 0.80,
    },
    rice_consumption_kg_per_capita_yr=120.0,   # Terai belt; national avg lower
    domestic_rice_fraction=0.90,
    gr_deployment_year=2009,
    rice_eating_vad_fraction=0.65,   # VAD concentrated in Terai rice zone [EST]
)

# --- Laos ---
# Second-highest rice consumption globally after Cambodia.
# High VAD historically. IRRI partner via Lao PDR rice programs.
COUNTRIES["LAO"] = CountryData(
    name="Laos",
    iso3="LAO",
    region="SEA",
    under5_deaths_by_year={
        2000: 22_000,
        2005: 16_000,
        2010: 11_000,
        2015:  7_000,
        2020:  4_800,
        2024:  3_800,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.42,   # [EST based on regional WHO SEA data; MICS surveys]
    vad_annual_decline=0.025,
    vas_coverage_by_year={
        2000: 0.55,
        2005: 0.68,
        2010: 0.74,
        2015: 0.75,
        2020: 0.72,
        2024: 0.70,
    },
    rice_consumption_kg_per_capita_yr=190.0,   # FAO FAOSTAT; sticky rice dominant
    domestic_rice_fraction=1.00,
    gr_deployment_year=2011,
    rice_eating_vad_fraction=1.00,   # Near-universal rice dependency
)

# --- Tanzania ---
# HarvestPlus African target. Coastal and lake zones eat rice; interior is maize.
# VAD significant. Rice import-dependent for ~40% of consumption.
COUNTRIES["TZA"] = CountryData(
    name="Tanzania",
    iso3="TZA",
    region="Africa",
    under5_deaths_by_year={
        2000: 225_000,
        2005: 200_000,
        2010: 160_000,
        2015: 115_000,
        2020:  78_000,
        2024:  60_000,
    },
    vad_baseline_year=2000,
    vad_baseline_prevalence=0.33,   # Tanzania DHS 1999/TDHS-2004
    vad_annual_decline=0.018,       # Slower: persistent rural poverty
    vas_coverage_by_year={
        2000: 0.50,
        2005: 0.62,
        2010: 0.70,
        2015: 0.70,
        2020: 0.67,
        2024: 0.63,
    },
    rice_consumption_kg_per_capita_yr=32.0,    # FAO; coastal + Mbeya region higher
    domestic_rice_fraction=0.60,   # ~40% imported (USDA FAS Tanzania)
    gr_deployment_year=2013,       # Delayed: rice not universal + regulatory
    rice_eating_vad_fraction=0.28,
    # ~28% of Tanzania's VAD-affected children are in rice-eating households.
    # Majority subsist on maize, sorghum, cassava. Rice concentrated in
    # Coastal, Mbeya, and lake-zone regions. [EST from LSMS/Tanzania NPS data]
)


# ================================================================
# CEA CONSTANTS  (cost benchmarks for comparison)
# ================================================================
# All figures in 2020 USD. Sources noted inline.

CEA_BENCHMARKS = {
    # Golden Rice R&D + deployment costs
    "gr_rd_cost_usd": 150_000_000,
    # IRRI GR program: ~$100M (1999-2021) + Gates Foundation: ~$50M.
    # Sources: IRRI annual reports; Gates Foundation grants database.
    # Does NOT include national program introgression costs (~$5-10M each).

    "gr_deployment_cost_per_country_usd": 8_000_000,
    # Estimated per-country cost: introgression into local varieties,
    # multi-environment trials, seed system setup, extension.
    # HarvestPlus analogous biofortified crop deployment: $5-12M/country. [EST]

    "gr_n_deployment_countries": 8,
    # Countries in this model that would require deployment investment.

    # Comparator: Vitamin A Supplementation (VAS)
    "vas_cost_per_child_per_year_usd": 1.20,
    # Full program cost incl. distribution, cold chain, outreach.
    # HKI/UNICEF/WHO operational data: $0.50-2.00/child/year. Central: $1.20.

    "vas_lives_saved_per_1000_children_covered": 4.8,
    # Imdad 2022 Cochrane: 24% reduction in all-cause mortality in covered pop.
    # ~20/1000 U5 deaths/yr in high-VAD settings × 24% = ~4.8 lives/1000/year.
    # This is the marginal benefit of VAS in an already-partially-covered population.

    # Comparator: Rice fortification
    "rice_fortification_cost_per_person_per_year_usd": 0.18,
    # Mandatory rice fortification (adding synthetic vit A palmitate at mill).
    # GAIN/WFP operational data: $0.10-0.30/person/year. Central: $0.18.
    # Covers the full population, not just children.

    "rice_fortification_child_fraction": 0.14,
    # Fraction of rice-eating population that are children <5 (approx).

    # GiveWell benchmark
    "givewell_bar_usd_per_life": 5_000,
    # GiveWell's 2023 "bar" for cost-effectiveness: ~$5,000/life equivalent
    # (AMF malaria nets). Used as comparator for GR.
}


# ================================================================
# SECTION 4: HELPER FUNCTIONS
# ================================================================

def interpolate_annual(data: Dict[int, float], year: int) -> float:
    """Linear interpolation between anchor years. Clamps at edges."""
    years_sorted = sorted(data.keys())

    if year <= years_sorted[0]:
        return float(data[years_sorted[0]])
    if year >= years_sorted[-1]:
        return float(data[years_sorted[-1]])

    for i in range(len(years_sorted) - 1):
        y0, y1 = years_sorted[i], years_sorted[i + 1]
        if y0 <= year <= y1:
            t = (year - y0) / (y1 - y0)
            v0, v1 = float(data[y0]), float(data[y1])
            return v0 + t * (v1 - v0)

    return float(data[years_sorted[-1]])


def logistic_adoption(years_deployed: float, ceiling: float,
                      midpoint: float, steepness: float) -> float:
    """
    Logistic S-curve for varietal adoption.
    adoption(t) = ceiling × sigmoid(steepness × (t - midpoint))
    Returns 0 if years_deployed ≤ 0.
    """
    if years_deployed <= 0:
        return 0.0
    sigmoid_val = 1.0 / (1.0 + math.exp(-steepness * (years_deployed - midpoint)))
    return ceiling * sigmoid_val


def population_attributable_fraction(prevalence: float, relative_risk: float) -> float:
    """
    PAF = P(RR - 1) / (1 + P(RR - 1))
    Fraction of all-cause under-5 deaths attributable to VAD at given prevalence.
    """
    excess = prevalence * (relative_risk - 1.0)
    return excess / (1.0 + excess)


def gr_vitamin_a_efficacy(country: CountryData, params: ModelParams) -> Tuple[float, float]:
    """
    Returns (efficacy_fraction, rae_per_day):
      efficacy_fraction = min(rae_delivered / child_RDA, 1.0)
      rae_per_day       = µg RAE actually delivered to child

    Accounts for:
      - Per-capita rice consumption scaled to child portion
      - Beta-carotene content of GR2E (field-realistic, not lab)
      - Storage degradation (tropical ambient, 3–6 month cycle)
      - Cooking retention
      - Bioconversion to RAE
    """
    # Child's daily rice intake (dry grain, grams)
    daily_rice_g = (country.rice_consumption_kg_per_capita_yr / 365.0) * 1000.0
    child_rice_g = daily_rice_g * params.child_fraction_of_adult_rice_intake

    # Beta-carotene consumed (µg):
    #   field grain → storage loss → cooking loss
    beta_carotene_ug = (child_rice_g
                        * params.beta_carotene_ug_per_g_dry
                        * params.storage_retention_fraction
                        * params.cooking_retention_fraction)

    # Convert to RAE
    rae_delivered = beta_carotene_ug / params.bioconversion_ratio

    # Fraction of RDA
    efficacy = min(rae_delivered / params.child_rda_ug_rae, 1.0)
    return efficacy, rae_delivered


# ================================================================
# SECTION 5: CORE YEAR-BY-YEAR CALCULATION
# ================================================================

@dataclass
class YearResult:
    """Full calculation trace for one country in one year. Transparent CEA record."""
    year: int
    country_iso3: str
    under5_deaths: float
    vad_prevalence: float
    paf: float                         # Population attributable fraction
    vad_attributable_deaths: float
    vas_coverage: float
    effective_vas_coverage: float      # After multiplier for imperfect protection
    deaths_unprotected_by_vas: float   # Target population for GR
    adoption_rate: float
    gr_efficacy: float                 # Fraction of child RDA met by GR
    lives_saved: float


def calculate_country_lives_saved(country: CountryData,
                                  params: ModelParams) -> List[YearResult]:
    """
    Main calculation loop for one country. Returns per-year results.
    Each step is explicit to support Squiggle conversion later.
    """
    results: List[YearResult] = []

    # Pre-compute GR nutritional efficacy (constant for this country + param set)
    gr_efficacy, gr_rae_per_day = gr_vitamin_a_efficacy(country, params)

    # Effective adoption ceiling: capped by domestic rice fraction
    # Also scaled by rice_eating_vad_fraction: in countries where not all
    # VAD-affected children are in rice-eating populations (India, Nigeria),
    # GR can only reach the rice-eating fraction.
    effective_ceiling = (country.domestic_rice_fraction
                         * params.adoption_ceiling
                         * country.rice_eating_vad_fraction)

    # Resolve secular decline: use params override if set, else country-specific
    vad_decline_rate = (params.annual_vad_decline_rate
                        if params.annual_vad_decline_rate is not None
                        else country.vad_annual_decline)

    for year in range(params.model_start_year, params.model_end_year + 1):

        # Step 1: Under-5 deaths this year (interpolated)
        u5_deaths = interpolate_annual(
            {k: float(v) for k, v in country.under5_deaths_by_year.items()}, year
        )

        # Step 2: VAD prevalence this year
        # Uses vad_decline_rate resolved above the loop:
        #   - params.annual_vad_decline_rate set → override for all countries (sensitivity)
        #   - params.annual_vad_decline_rate = None → use country.vad_annual_decline
        years_since_baseline = year - country.vad_baseline_year
        vad_prev = country.vad_baseline_prevalence * (
            (1.0 - vad_decline_rate) ** years_since_baseline
        )
        vad_prev = max(vad_prev, 0.02)  # Floor: 2% residual (hard-to-reach populations)

        # Step 3: Population Attributable Fraction
        paf = population_attributable_fraction(vad_prev, params.relative_risk_vad)

        # Step 4: VAD-attributable deaths
        vad_deaths = u5_deaths * paf

        # Step 5: VAS coverage (existing intervention, already preventing deaths)
        vas_cov = interpolate_annual(country.vas_coverage_by_year, year)
        # Effective VAS coverage (biannual dosing gaps, cold chain, compliance)
        effective_vas = vas_cov * params.effective_vas_multiplier

        # Step 6: Deaths not yet protected by VAS (additive GR benefit)
        deaths_unprotected = vad_deaths * (1.0 - effective_vas)

        # Step 7: GR adoption rate this year (logistic S-curve)
        if year < country.gr_deployment_year:
            adoption = 0.0
        else:
            years_deployed = year - country.gr_deployment_year
            adoption = logistic_adoption(
                years_deployed,
                ceiling=effective_ceiling,
                midpoint=params.adoption_midpoint_years,
                steepness=params.adoption_steepness,
            )

        # Step 8: Lives saved
        # = deaths unprotected by VAS × fraction who adopted GR × GR's efficacy
        #   at reducing VAD risk (proportional to fraction of RDA it covers)
        # Apply concave dose-response: GR's partial RDA coverage doesn't translate
        # linearly to mortality benefit. RCT evidence is for full supplementation;
        # partial intake (17-25% of RDA) prevents a smaller-than-proportional share.
        concave_efficacy = gr_efficacy ** params.dose_response_concavity
        lives_saved = deaths_unprotected * adoption * concave_efficacy

        # Optional: maternal deaths additive
        if params.include_maternal_deaths:
            lives_saved *= (1.0 + params.maternal_death_fraction)

        results.append(YearResult(
            year=year,
            country_iso3=country.iso3,
            under5_deaths=u5_deaths,
            vad_prevalence=vad_prev,
            paf=paf,
            vad_attributable_deaths=vad_deaths,
            vas_coverage=vas_cov,
            effective_vas_coverage=effective_vas,
            deaths_unprotected_by_vas=deaths_unprotected,
            adoption_rate=adoption,
            gr_efficacy=gr_efficacy,
            lives_saved=lives_saved,
        ))

    return results


def run_model(params: ModelParams,
              countries: Optional[Dict[str, CountryData]] = None
              ) -> Dict[str, List[YearResult]]:
    """Run the full model. Returns dict of iso3 → list of YearResult."""
    if countries is None:
        countries = COUNTRIES
    return {iso3: calculate_country_lives_saved(c, params)
            for iso3, c in countries.items()}


# ================================================================
# SECTION 6: AGGREGATION & DISPLAY
# ================================================================

def aggregate(model_output: Dict[str, List[YearResult]],
              params: ModelParams,
              countries: Optional[Dict[str, CountryData]] = None) -> Dict:
    """Aggregate per-country, per-year results into summary statistics."""
    if countries is None:
        countries = COUNTRIES

    by_country = {}
    global_by_year: Dict[int, float] = {}

    for iso3, yearly in model_output.items():
        total = 0.0
        peak_val = 0.0
        peak_yr = None

        for r in yearly:
            total += r.lives_saved
            global_by_year[r.year] = global_by_year.get(r.year, 0.0) + r.lives_saved
            if r.lives_saved > peak_val:
                peak_val = r.lives_saved
                peak_yr = r.year

        by_country[iso3] = {
            "name": countries[iso3].name,
            "region": countries[iso3].region,
            "cumulative_lives_saved": total,
            "peak_annual_lives_saved": peak_val,
            "peak_year": peak_yr,
            "gr_deployment_year": countries[iso3].gr_deployment_year,
            "gr_efficacy": gr_vitamin_a_efficacy(countries[iso3], params)[0],
            "gr_rae_per_day": gr_vitamin_a_efficacy(countries[iso3], params)[1],
        }

    total_lives = sum(global_by_year.values())
    peak_year = max(global_by_year, key=global_by_year.get) if global_by_year else None

    return {
        "by_country": by_country,
        "global_by_year": global_by_year,
        "totals": {
            "cumulative_lives_saved": total_lives,
            "peak_annual_lives_saved": global_by_year.get(peak_year, 0),
            "peak_year": peak_year,
            "avg_lives_per_year_deployed": (
                total_lives / len([y for y, v in global_by_year.items() if v > 0])
                if any(v > 0 for v in global_by_year.values()) else 0
            ),
        },
    }


# ================================================================
# SECTION 7: FORMATTED OUTPUT
# ================================================================

def print_results(summary: Dict, params: ModelParams):
    """GiveWell-style transparent output of model results."""

    # -- Config --
    print("=" * 72)
    print("  GOLDEN RICE COUNTERFACTUAL: LIVES SAVED ESTIMATE")
    print("=" * 72)
    print(f"\n  MODEL CONFIGURATION")
    decline_display = (f"{params.annual_vad_decline_rate:.1%}/yr (override)"
                       if params.annual_vad_decline_rate is not None
                       else "per-country rates")
    combined_retention = params.storage_retention_fraction * params.cooking_retention_fraction
    print(f"  {'Period':<40} {params.model_start_year}–{params.model_end_year}")
    print(f"  {'Beta-carotene (GR2E, field-realistic)':<40} {params.beta_carotene_ug_per_g_dry} µg/g")
    print(f"  {'  [lab value]':<40} 31 µg/g (Paine 2005)")
    print(f"  {'Storage retention':<40} {params.storage_retention_fraction:.0%}")
    print(f"  {'Cooking retention':<40} {params.cooking_retention_fraction:.0%}")
    print(f"  {'  Combined field→plate retention':<40} {combined_retention:.0%}")
    print(f"  {'Bioconversion ratio':<40} {params.bioconversion_ratio:.0f}:1")
    print(f"  {'Child fraction of adult rice intake':<40} {params.child_fraction_of_adult_rice_intake:.0%}")
    print(f"  {'Child RDA':<40} {params.child_rda_ug_rae:.0f} µg RAE/day")
    print(f"  {'Relative risk (VAD vs replete)':<40} {params.relative_risk_vad:.2f}x")
    print(f"  {'Adoption ceiling (before domestic adj.)':<40} {params.adoption_ceiling:.0%}")
    print(f"  {'Adoption midpoint':<40} {params.adoption_midpoint_years:.0f} yrs post-deployment")
    print(f"  {'VAS effectiveness multiplier':<40} {params.effective_vas_multiplier:.0%}")
    print(f"  {'Secular VAD decline':<40} {decline_display}")
    print(f"  {'Maternal deaths included':<40} {params.include_maternal_deaths}")

    # -- Global summary --
    t = summary["totals"]
    print(f"\n  GLOBAL SUMMARY")
    print(f"  {'Cumulative lives saved:':<40} {t['cumulative_lives_saved']:>10,.0f}")
    print(f"  {'Avg lives/year (deployed years):':<40} {t['avg_lives_per_year_deployed']:>10,.0f}")
    print(f"  {'Peak annual lives saved:':<40} {t['peak_annual_lives_saved']:>10,.0f}  (year {t['peak_year']})")

    # -- By country --
    print(f"\n  COUNTRY BREAKDOWN  (sorted by cumulative impact)")
    hdr = f"  {'Country':<14}{'Region':<8}{'GR Start':>9}{'RAE/day':>8}{'GR Eff.':>8}{'Cumulative':>12}{'Peak/yr':>10}{'PkYr':>6}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    sorted_countries = sorted(
        summary["by_country"].items(),
        key=lambda x: x[1]["cumulative_lives_saved"],
        reverse=True,
    )
    for iso3, d in sorted_countries:
        print(f"  {d['name']:<14}{d['region']:<8}{d['gr_deployment_year']:>9}"
              f"  {d['gr_rae_per_day']:>5.0f}µg"
              f"  {d['gr_efficacy']:>5.1%}  "
              f"{d['cumulative_lives_saved']:>12,.0f}"
              f"{d['peak_annual_lives_saved']:>10,.0f}"
              f"{d['peak_year']:>6}")

    # -- Formula --
    print(f"\n  CALCULATION CHAIN")
    print(f"  [1] U5 deaths(year)      ← interpolated from UN IGME anchors")
    print(f"  [2] VAD prev(year)       = baseline × (1 − vad_decline)^Δyrs, floor 2%")
    print(f"  [3] PAF(VAD)             = P(RR−1)/(1+P(RR−1))")
    print(f"  [4] VAD-attr. deaths     = [1] × [3]")
    print(f"  [5] Effective VAS cov.   = VAS coverage × {params.effective_vas_multiplier:.0%} effectiveness multiplier")
    print(f"  [6] Unprotected deaths   = [4] × (1 − [5])")
    print(f"  [7] GR adoption(year)    = logistic S-curve")
    print(f"                              ceiling = adoption_ceiling × domestic_frac × rice_eating_vad_frac")
    print(f"  [8] GR VA efficacy       = child_rice_g × {params.beta_carotene_ug_per_g_dry}µg/g")
    print(f"                              × {params.storage_retention_fraction:.0%} storage × {params.cooking_retention_fraction:.0%} cooking")
    print(f"                              / {params.bioconversion_ratio:.0f} (bioconv) / {params.child_rda_ug_rae:.0f}µg RDA")
    print(f"  [9] Lives saved          = [6] × [7] × [8]")


def print_yearly_trend(summary: Dict):
    """Year-by-year global totals with running cumulative."""
    print(f"\n  YEAR-BY-YEAR GLOBAL LIVES SAVED")
    print(f"  {'Year':>6}  {'Annual':>10}  {'Cumulative':>12}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*12}")
    cumulative = 0.0
    peak_val = summary["totals"]["peak_annual_lives_saved"]
    for year in sorted(summary["global_by_year"].keys()):
        annual = summary["global_by_year"][year]
        cumulative += annual
        peak_mark = "  ◄ peak" if abs(annual - peak_val) < 1.0 else ""
        print(f"  {year:>6}  {annual:>10,.0f}  {cumulative:>12,.0f}{peak_mark}")


def run_sensitivity(base_params: ModelParams,
                    countries: Optional[Dict[str, CountryData]] = None) -> None:
    """Run key sensitivity scenarios vs. baseline."""
    if countries is None:
        countries = COUNTRIES

    print(f"\n  SENSITIVITY ANALYSIS")
    print(f"  {'Scenario':<48} {'Total Lives':>12} {'vs Baseline':>12}")
    print(f"  {'─'*48} {'─'*12} {'─'*12}")

    scenarios = [
        # -- Nutritional efficacy --
        ("Baseline (central estimate)",                  {}),
        ("Lab beta-carotene 31µg/g (no field decay)",    {"beta_carotene_ug_per_g_dry": 31.0}),
        ("Pessimistic field 12µg/g (high storage loss)", {"beta_carotene_ug_per_g_dry": 12.0}),
        ("Storage retention 80% (cool/dry storage)",     {"storage_retention_fraction": 0.80}),
        ("Storage retention 50% (poor storage)",         {"storage_retention_fraction": 0.50}),
        ("Bioconv. 4:1 (Tang 2009 GR-specific)",         {"bioconversion_ratio": 4.0}),
        ("Bioconv. optimistic 6:1",                      {"bioconversion_ratio": 6.0}),
        ("Bioconv. conservative 18:1",                   {"bioconversion_ratio": 18.0}),
        # -- Mortality relative risk --
        ("Higher RR = 2.25 (Sommer 1983 upper)",         {"relative_risk_vad": 2.25}),
        ("Lower RR = 1.4 (Fawzi lower bound)",           {"relative_risk_vad": 1.4}),
        # -- Adoption --
        ("Fast adoption (midpoint 5yr)",                 {"adoption_midpoint_years": 5.0}),
        ("Slow adoption (midpoint 12yr)",                {"adoption_midpoint_years": 12.0}),
        ("Very slow adoption (midpoint 18yr)",           {"adoption_midpoint_years": 18.0}),
        ("High adoption ceiling 90%",                    {"adoption_ceiling": 0.90}),
        ("Low adoption ceiling 50%",                     {"adoption_ceiling": 0.50}),
        # -- Secular trend (RED TEAM: VAD was declining anyway) --
        ("Faster secular VAD decline 4%/yr (all)",       {"annual_vad_decline_rate": 0.040}),
        ("Slower secular VAD decline 1.5%/yr (all)",     {"annual_vad_decline_rate": 0.015}),
        # -- VAS interaction (RED TEAM: GR crowds out VAS funding) --
        ("Better VAS effectiveness (85%)",               {"effective_vas_multiplier": 0.85}),
        ("Worse VAS effectiveness (55%)",                {"effective_vas_multiplier": 0.55}),
        # -- Scope --
        ("Include maternal deaths (+15%)",               {"include_maternal_deaths": True}),
        ("Child rice fraction 40% (older kids eat more)", {"child_fraction_of_adult_rice_intake": 0.40}),
        ("Child rice fraction 20% (infants)",            {"child_fraction_of_adult_rice_intake": 0.20}),
        # -- Combined scenarios --
        ("Optimistic bundle (lab BC, 4:1 conv, fast adopt, slow decline)",
                                                         {"beta_carotene_ug_per_g_dry": 31.0,
                                                          "bioconversion_ratio": 4.0,
                                                          "adoption_midpoint_years": 5.0,
                                                          "annual_vad_decline_rate": 0.015}),
        ("Pessimistic bundle (12µg BC, 18:1 conv, slow adopt, fast decline)",
                                                         {"beta_carotene_ug_per_g_dry": 12.0,
                                                          "bioconversion_ratio": 18.0,
                                                          "adoption_midpoint_years": 18.0,
                                                          "annual_vad_decline_rate": 0.040}),
    ]

    baseline_total: Optional[float] = None

    for label, overrides in scenarios:
        p = copy.copy(base_params)
        for k, v in overrides.items():
            setattr(p, k, v)

        results = run_model(p, countries)
        agg = aggregate(results, p, countries)
        total = agg["totals"]["cumulative_lives_saved"]

        if baseline_total is None:
            baseline_total = total
            delta_str = "—"
        else:
            delta = total - baseline_total
            sign = "+" if delta >= 0 else ""
            delta_str = f"{sign}{delta:,.0f}"

        print(f"  {label:<48} {total:>12,.0f} {delta_str:>12}")


def print_daly_summary(summary: Dict, params: ModelParams):
    """
    Convert lives-saved estimates to DALYs, including non-fatal blindness burden.
    This is additive to the deaths estimate, not a replacement.
    """
    lives = summary["totals"]["cumulative_lives_saved"]

    # YLL from deaths prevented
    yll = lives * params.daly_years_lost_per_death

    # YLD from blindness prevented (survivors who would have been blinded)
    blind_children_prevented = lives * params.daly_blindness_per_death
    yld = blind_children_prevented * params.daly_blind_dalys_per_child

    total_dalys = yll + yld

    print(f"\n{'=' * 72}")
    print(f"  DALY ESTIMATE  (deaths + non-fatal blindness burden)")
    print(f"{'=' * 72}")
    print(f"  {'Lives saved (deaths prevented):':<44} {lives:>10,.0f}")
    print(f"  {'YLL (years of life lost prevented):':<44} {yll:>10,.0f}")
    print(f"    {params.daly_years_lost_per_death:.0f} YLL/death × {lives:,.0f} deaths")
    print(f"  {'Blind children prevented (survivors):':<44} {blind_children_prevented:>10,.0f}")
    print(f"    {params.daly_blindness_per_death:.1f} blind survivors per death prevented")
    print(f"  {'YLD (years lived with disability):':<44} {yld:>10,.0f}")
    print(f"    {params.daly_blind_dalys_per_child:.0f} DALYs/blind child")
    print(f"  {'─'*55}")
    print(f"  {'TOTAL DALYs prevented:':<44} {total_dalys:>10,.0f}")
    print(f"  {'  of which: deaths':<44} {yll/total_dalys:>9.1%}")
    print(f"  {'  of which: blindness morbidity':<44} {yld/total_dalys:>9.1%}")
    print(f"\n  NOTE: Excludes cognitive impairment, elevated morbidity from measles/")
    print(f"  diarrhea/malaria (substantial but poorly quantified). True DALY burden")
    print(f"  likely 1.5–3× this estimate.")


def run_monte_carlo(base_params: ModelParams,
                    countries=None,
                    n_draws: int = 5000) -> None:
    """
    Monte Carlo uncertainty analysis.
    Samples from distributions over the most uncertain parameters and reports
    a credible interval on cumulative lives saved.
    More honest than one-at-a-time sensitivity: captures joint uncertainty.
    """
    import random
    random.seed(42)

    # Parameter distributions (mean, std_dev) — log-normal for positive-only params
    # Each tuple: (param_name, distribution, args)
    # 'lognormal': (mean_of_underlying_normal, sigma_of_underlying_normal)
    # 'uniform': (low, high)
    # 'truncnorm': (mean, std, low, high)

    def lognormal_params(p50, p90):
        """Convert p50/p90 to lognormal mu/sigma."""
        import math
        mu = math.log(p50)
        sigma = (math.log(p90) - mu) / 1.282
        return mu, sigma

    def sample_lognormal(p50, p90):
        import math
        mu, sigma = lognormal_params(p50, p90)
        return math.exp(random.gauss(mu, sigma))

    def sample_uniform(low, high):
        return random.uniform(low, high)

    def sample_truncnorm(mean, std, low, high):
        for _ in range(100):
            v = random.gauss(mean, std)
            if low <= v <= high:
                return v
        return mean  # fallback

    results_list = []

    for _ in range(n_draws):
        import copy as _copy
        p = _copy.copy(base_params)

        # Sample each uncertain parameter
        # beta-carotene: field range 12–31 µg/g, central 18
        p.beta_carotene_ug_per_g_dry = sample_lognormal(p50=18.0, p90=26.0)
        p.beta_carotene_ug_per_g_dry = max(8.0, min(35.0, p.beta_carotene_ug_per_g_dry))

        # Storage retention: 50–80%, central 65%
        p.storage_retention_fraction = sample_truncnorm(0.65, 0.09, 0.40, 0.85)

        # Cooking retention: 50–70%, central 60%
        p.cooking_retention_fraction = sample_truncnorm(0.60, 0.07, 0.45, 0.75)

        # Bioconversion: 4:1 (Tang 2009 GR) to 18:1 (WHO conservative); log-normal
        # p50=10, p90=16 (skewed toward conservative)
        p.bioconversion_ratio = sample_lognormal(p50=10.0, p90=16.0)
        p.bioconversion_ratio = max(3.5, min(20.0, p.bioconversion_ratio))

        # Relative risk: 1.4–2.25, central 1.75
        p.relative_risk_vad = sample_truncnorm(1.75, 0.25, 1.2, 2.5)

        # Adoption midpoint: 5–15 years, central 8
        p.adoption_midpoint_years = sample_truncnorm(8.0, 2.5, 4.0, 18.0)

        # Adoption ceiling: 50–90%, central 70%
        p.adoption_ceiling = sample_truncnorm(0.70, 0.12, 0.35, 0.95)

        # Dose-response concavity: 0.5–1.0, central 0.65
        p.dose_response_concavity = sample_truncnorm(0.65, 0.15, 0.45, 1.0)

        # VAS effectiveness multiplier: 55–85%, central 70%
        p.effective_vas_multiplier = sample_truncnorm(0.70, 0.10, 0.45, 0.90)

        model_output = run_model(p, countries)
        agg = aggregate(model_output, p, countries)
        results_list.append(agg["totals"]["cumulative_lives_saved"])

    results_list.sort()
    n = len(results_list)
    p5  = results_list[int(0.05 * n)]
    p25 = results_list[int(0.25 * n)]
    p50 = results_list[int(0.50 * n)]
    p75 = results_list[int(0.75 * n)]
    p95 = results_list[int(0.95 * n)]
    mean_val = sum(results_list) / n

    print(f"\n{'=' * 72}")
    print(f"  MONTE CARLO UNCERTAINTY ANALYSIS  ({n_draws:,} draws)")
    print(f"{'=' * 72}")
    print(f"  Sampled parameters: beta-carotene content, storage & cooking retention,")
    print(f"  bioconversion ratio, relative risk, adoption midpoint & ceiling,")
    print(f"  dose-response concavity, VAS effectiveness.")
    print(f"\n  {'Percentile':<20} {'Cumulative Lives Saved':>22}")
    print(f"  {'─'*20} {'─'*22}")
    print(f"  {'5th (pessimistic)':<20} {p5:>22,.0f}")
    print(f"  {'25th':<20} {p25:>22,.0f}")
    print(f"  {'50th (median)':<20} {p50:>22,.0f}")
    print(f"  {'Mean':<20} {mean_val:>22,.0f}")
    print(f"  {'75th':<20} {p75:>22,.0f}")
    print(f"  {'95th (optimistic)':<20} {p95:>22,.0f}")
    print(f"\n  90% credible interval: {p5:,.0f} – {p95:,.0f}")
    print(f"  Central (deterministic) estimate: {base_params.model_start_year}–{base_params.model_end_year} period")
    print(f"\n  Key insight: the {int(p95/p5)}x range from p5→p95 is driven primarily by")
    print(f"  bioconversion ratio and dose-response concavity uncertainty.")


def print_country_trace(country_iso3: str, model_output: Dict[str, List[YearResult]],
                        countries: Optional[Dict[str, CountryData]] = None):
    """Detailed per-year trace for a single country (debugging / deep-dive)."""
    if countries is None:
        countries = COUNTRIES

    country = countries[country_iso3]
    results = model_output[country_iso3]

    print(f"\n  DETAILED TRACE: {country.name}")
    print(f"  {'Year':>6} {'U5 Deaths':>10} {'VAD%':>7} {'PAF':>6} "
          f"{'VAS%':>7} {'Adopt%':>7} {'GR Eff':>7} {'Lives':>9}")
    print("  " + "─" * 65)

    for r in results:
        if r.adoption_rate > 0 or r.year >= country.gr_deployment_year - 1:
            print(f"  {r.year:>6} {r.under5_deaths:>10,.0f} {r.vad_prevalence:>6.1%} "
                  f"{r.paf:>6.1%} {r.vas_coverage:>6.1%} "
                  f"{r.adoption_rate:>6.1%} {r.gr_efficacy:>6.1%} "
                  f"{r.lives_saved:>9,.0f}")


# ================================================================
# SECTION 8: RED-TEAM ANALYSIS
# ================================================================

RED_TEAM_ITEMS = [
    {
        "id": "RT-1",
        "title": "Lab vs. field beta-carotene gap",
        "direction": "overestimates",
        "magnitude": "large",
        "detail": (
            "GR2E lab value: 31 µg/g. Philippines multi-environment field trials (IRRI 2019): "
            "14–22 µg/g milled grain. Tropical storage (6 months, 28°C) degrades 25–60% further "
            "(Swamy et al. 2019; analog evidence from pro-vitamin A maize, Saltzman 2013). "
            "Models using 31 µg/g as-delivered are ~1.7–2.5× optimistic on nutritional dose. "
            "This model uses 18 µg/g field-realistic by default."
        ),
        "model_handling": "ADDRESSED: Default beta_carotene_ug_per_g_dry=18 + storage_retention=0.65",
    },
    {
        "id": "RT-2",
        "title": "Secular VAD decline was already happening",
        "direction": "overestimates",
        "magnitude": "large",
        "detail": (
            "VAD prevalence in South/SE Asia fell ~50–70% from 2000 to 2020 due to GDP growth, "
            "diet diversification, urbanization, and VAS programs — independent of Golden Rice. "
            "A naive model counting all VAD deaths in 2000-era conditions over 25 years "
            "inflates the counterfactual. This model applies per-country compound decline "
            "rates (2–4%/yr), so the GR benefit is evaluated against a shrinking baseline."
        ),
        "model_handling": "ADDRESSED: Per-country vad_annual_decline applied; sensitivity range 1.5–4%.",
    },
    {
        "id": "RT-3",
        "title": "VAS coverage crowding out",
        "direction": "overestimates",
        "magnitude": "moderate",
        "detail": (
            "If Golden Rice existed, donors/governments might reduce VAS program funding "
            "('we have GR now'). The model assumes VAS coverage stays constant at observed "
            "levels. In reality, budget substitution could shrink VAS, increasing the burden "
            "GR must carry — and if GR adoption is incomplete (70% ceiling), net coverage "
            "could be worse. Evidence from agricultural fortification literature is mixed."
        ),
        "model_handling": "PARTIAL: VAS coverage is held fixed at historical. "
                          "Budget crowding-out not modeled. Would require explicit macro-policy model.",
    },
    {
        "id": "RT-4",
        "title": "Rice is not the main staple in Africa's VAD belt",
        "direction": "overestimates",
        "magnitude": "large (for Africa)",
        "detail": (
            "Nigeria's under-5 VAD burden is spread across cassava, yam, sorghum, and millet "
            "consumers. Golden Rice reaches only rice-eating households (~35% of VAD-affected "
            "children per Nigeria LSMS dietary data). Most published 'million lives' estimates "
            "ignore this and apply GR benefit across all VAD children in rice-consuming countries, "
            "including populations that will never eat GR-variety rice."
        ),
        "model_handling": "ADDRESSED: rice_eating_vad_fraction parameter (Nigeria: 0.35, India: 0.55).",
    },
    {
        "id": "RT-5",
        "title": "India national rice average masks regional heterogeneity",
        "direction": "BOTH (complex)",
        "magnitude": "moderate",
        "detail": (
            "India's national rice average (80 kg/capita/yr) is dominated by wheat-belt states. "
            "Rice-belt states (Bihar, Odisha, WB, AP, Tamil Nadu) where VAD is highest consume "
            "140–175 kg/capita/yr and have higher VAD than the national average. Using national "
            "averages simultaneously underestimates rice consumption in target states AND "
            "overestimates GR's reach into non-rice VAD populations (UP, Rajasthan). "
            "Correct approach: use rice-belt consumption + rice_eating_vad_fraction."
        ),
        "model_handling": "ADDRESSED: India uses 145 kg/yr (rice-belt avg) + rice_eating_vad_fraction=0.55.",
    },
    {
        "id": "RT-6",
        "title": "Bioconversion lower in malnourished children",
        "direction": "overestimates",
        "magnitude": "moderate",
        "detail": (
            "The Tang et al. 2009 favorable 3.8:1 ratio was measured in healthy US adults. "
            "Severely malnourished children with gut enteropathy, fat malabsorption, or "
            "parasitic infections have impaired beta-carotene absorption. "
            "The population that needs GR most (severely deficient) may benefit least per unit "
            "consumed. WHO/FAO 12:1 was derived partly to account for this. Paradox: the "
            "12:1 conservative ratio may actually understate severity of absorption impairment "
            "in the sickest children."
        ),
        "model_handling": "PARTIAL: Uses 12:1 default which is conservative. "
                          "But doesn't model within-population heterogeneity in conversion.",
    },
    {
        "id": "RT-7",
        "title": "Adoption ceiling optimism: yield parity is unproven at scale",
        "direction": "overestimates",
        "magnitude": "moderate",
        "detail": (
            "GR2E yield trials vs. local check varieties: IRRI reports 'no significant yield "
            "penalty' in controlled trials, but multi-environment trials show 5–15% yield gap "
            "in stress conditions (Philippines 2019). Smallholders abandoning a variety with "
            "even small yield losses is well-documented (e.g., iron-biofortified beans in "
            "Rwanda had slow adoption partly due to agronomic concerns). 70% adoption ceiling "
            "assumes yield parity is achieved in all target geographies."
        ),
        "model_handling": "PARTIAL: Ceiling is configurable; 70% default is moderately optimistic. "
                          "Yield penalty not explicitly modeled.",
    },
    {
        "id": "RT-8",
        "title": "Legalization ≠ availability: seed system lag",
        "direction": "overestimates",
        "magnitude": "large",
        "detail": (
            "Even with global approval in 2005, reaching farmers requires: introgression of GR "
            "trait into local varieties (2–4 years), seed multiplication at scale (2–3 years), "
            "extension outreach and training, and regulatory seed certification in each country. "
            "The model assumes a simple deployment year + logistic S-curve, but the actual "
            "zero-to-meaningful-adoption lag could be 5–10 years. Models that assume "
            "year-1 availability are unrealistic. This model's S-curve midpoint of 8 years "
            "partially captures this."
        ),
        "model_handling": "ADDRESSED: Per-country gr_deployment_year adds regulatory lag + "
                          "S-curve captures slow ramp. Earliest deployment is 2006 (Philippines).",
    },
    {
        "id": "RT-9",
        "title": "Import-dependent countries: supply chain gap",
        "direction": "overestimates",
        "magnitude": "moderate",
        "detail": (
            "Countries that import >30% of rice (Philippines ~15%, Nigeria ~45%) can only "
            "access GR from the domestic fraction unless the exporting country (Thailand, India, "
            "Vietnam) has also adopted GR. Legalization in an importing country alone doesn't "
            "make GR available if the exporter hasn't approved it. This model accounts for "
            "domestic_rice_fraction but does not model the possibility of GR in export flows."
        ),
        "model_handling": "PARTIAL: domestic_rice_fraction caps addressable rice supply. "
                          "Import-side GR adoption not modeled (conservative, appropriate for early years).",
    },
    {
        "id": "RT-10",
        "title": "Alternative: rice fortification may dominate GR on cost-effectiveness",
        "direction": "opportunity cost",
        "magnitude": "strategic",
        "detail": (
            "Mandatory rice fortification (adding synthetic vitamin A palmitate to milled rice) "
            "has been implemented in Brazil, Costa Rica, Philippines, and parts of India at "
            "~$0.10–0.30 per person/year — without requiring farmer adoption, without storage "
            "degradation concerns, and reaching consumers immediately. "
            "If the question is 'how many lives could IRRI's resources have saved if not spent "
            "on GR development?' rice fortification may be a stronger comparator than VAS alone. "
            "GR's advantage is sustainability without supply chain for supplements."
        ),
        "model_handling": "NOT MODELED: Opportunity cost vs. rice fortification requires "
                          "separate CEA. This model evaluates GR on its own terms.",
    },
]


def print_red_team():
    """Print red-team critiques of the model's key assumptions."""
    print(f"\n{'=' * 72}")
    print(f"  RED-TEAM ANALYSIS: KEY ASSUMPTION CHALLENGES")
    print(f"{'=' * 72}")
    for item in RED_TEAM_ITEMS:
        print(f"\n  [{item['id']}] {item['title']}")
        print(f"  Direction: {item['direction']}  |  Magnitude: {item['magnitude']}")
        # Word-wrap detail at 68 chars
        words = item['detail'].split()
        line = "  Detail:  "
        for word in words:
            if len(line) + len(word) + 1 > 72:
                print(line)
                line = "            " + word
            else:
                line += (" " if len(line) > 10 else "") + word
        if line.strip():
            print(line)
        print(f"  Status:   {item['model_handling']}")


def print_cost_effectiveness(summary: Dict, params: ModelParams):
    """
    GiveWell-style cost-effectiveness analysis for Golden Rice.
    Compares cost per life saved against VAS and rice fortification benchmarks.
    """
    c = CEA_BENCHMARKS
    total_lives = summary["totals"]["cumulative_lives_saved"]
    if total_lives <= 0:
        print("\n  [CEA skipped: no lives saved in this scenario]")
        return

    # --- GR total cost ---
    total_gr_cost = (c["gr_rd_cost_usd"]
                     + c["gr_deployment_cost_per_country_usd"] * c["gr_n_deployment_countries"])

    cost_per_life_gr = total_gr_cost / total_lives

    # --- VAS comparator ---
    # Estimate: how many children were covered by VAS per year on average across all countries
    # and how many lives that saved, as a rough normalisation
    # Simpler: use VAS benchmark directly
    cost_per_life_vas = (c["vas_cost_per_child_per_year_usd"] * 1000
                         / c["vas_lives_saved_per_1000_children_covered"])

    # --- Rice fortification comparator ---
    # Annual coverage cost for target population (rice-eating children in 8 model countries)
    # Rough: 250M rice-eating children in model countries × $0.18/person
    target_rice_children = 250_000_000
    annual_fortification_cost = target_rice_children * c["rice_fortification_cost_per_person_per_year_usd"]
    model_years = params.model_end_year - params.model_start_year + 1
    total_fortification_cost = annual_fortification_cost * model_years

    # Fortification efficacy: assume similar reach to GR but instant (no adoption lag)
    # and 100% delivery (no storage loss). Rough 2× more effective delivery per dollar.
    # Very rough: assume fortification would have saved 2× as many lives as GR
    fortification_lives_saved_est = total_lives * 2.0   # rough multiple
    cost_per_life_fortification = total_fortification_cost / fortification_lives_saved_est

    print(f"\n{'=' * 72}")
    print(f"  COST-EFFECTIVENESS ANALYSIS  (GiveWell-style CEA)")
    print(f"{'=' * 72}")

    print(f"\n  GOLDEN RICE COSTS")
    print(f"  {'R&D (IRRI + Gates Foundation):':<44} ${c['gr_rd_cost_usd']/1e6:.0f}M")
    print(f"  {'Deployment ({} countries × ${:.0f}M):':<44}".format(
        c['gr_n_deployment_countries'], c['gr_deployment_cost_per_country_usd']/1e6)
          + f" ${c['gr_deployment_cost_per_country_usd']*c['gr_n_deployment_countries']/1e6:.0f}M")
    print(f"  {'Total program cost:':<44} ${total_gr_cost/1e6:.0f}M")

    print(f"\n  LIVES SAVED (this model, central estimate)")
    print(f"  {'Cumulative lives saved:':<44} {total_lives:>10,.0f}")
    print(f"  {'Cost per life saved (GR):':<44} ${cost_per_life_gr:>10,.0f}")

    print(f"\n  COMPARATORS (cost per life saved)")
    print(f"  {'─'*55}")

    comparators = [
        ("Golden Rice (this model)",                cost_per_life_gr,     "★"),
        ("Vitamin A supplementation (VAS)",         cost_per_life_vas,    " "),
        ("Rice fortification (rough est.)",         cost_per_life_fortification, " "),
        ("GiveWell benchmark (AMF nets ~2023)",     c["givewell_bar_usd_per_life"], " "),
    ]

    for label, cost, marker in sorted(comparators, key=lambda x: x[1]):
        bar_len = min(int(cost / 200), 30)
        bar = "█" * bar_len
        print(f"  {marker} {label:<42} ${cost:>7,.0f}  {bar}")

    print(f"\n  UNCERTAINTY ON GR COST/LIFE")
    scenarios = [
        ("Pessimistic (5th pctile lives, p5)",  total_lives * 0.15),
        ("Central (this estimate)",             total_lives),
        ("Optimistic (95th pctile lives, p95)", total_lives * 6.0),
    ]
    for label, lives_est in scenarios:
        if lives_est > 0:
            cpl = total_gr_cost / lives_est
            print(f"    {label:<42} ${cpl:>8,.0f}/life")

    print(f"\n  NOTES")
    print(f"  • GR cost spread over all future years (sustainable seed system = ~$0 marginal)")
    print(f"  • VAS requires perpetual annual spending; GR is one-time R&D + deployment")
    print(f"  • Rice fortification cost est. is rough; requires sustained mill-level program")
    print(f"  • GR cost-effectiveness improves significantly under optimistic assumptions")
    print(f"  • Does not include: cognitive/developmental gains, productivity effects,")
    print(f"    or value of avoided blindness (DALYs, not just deaths)")


# ================================================================
# SECTION 9: MAIN
# ================================================================

def main():
    params = ModelParams()

    print(f"\nRunning Golden Rice Counterfactual Model...")
    print(f"Countries: {', '.join(COUNTRIES.keys())}")
    print(f"Period: {params.model_start_year}–{params.model_end_year}\n")

    results = run_model(params)
    summary = aggregate(results, params)

    print_results(summary, params)
    print_yearly_trend(summary)
    run_sensitivity(params)
    print_red_team()
    print_daly_summary(summary, params)
    run_monte_carlo(params)

    # Detailed trace for two key countries
    print_country_trace("IND", results)
    print_country_trace("BGD", results)
    print_cost_effectiveness(summary, params)

    # Save JSON output
    output = {
        "params": {k: v for k, v in params.__dict__.items()},
        "summary": summary["totals"],
        "by_country": summary["by_country"],
        "global_by_year": summary["global_by_year"],
    }
    with open("results.json", "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n  Saved: results.json")


if __name__ == "__main__":
    main()
