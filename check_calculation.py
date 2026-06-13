#!/usr/bin/env python3
"""
Golden Rice "cost of delay" — full calculation.

Run: python3 check_calculation.py

Four outputs, matching the four places numbers appear on the page:
  PART A — vitamin A delivered per child per day, and % of daily need   (table)
  PART B — deaths prevented per year if ALL domestic rice were Golden    (table)
  PART C — cumulative children's lives lost 2006–2024                    (headline)
  PART D — blindness and years-of-healthy-life-lost                      (headline)
"""

import math

# ============================================================================
# 1. PARAMETERS  (sources cited on the web page)
# ============================================================================
BETA_CAROTENE_UG_PER_G   = 6.0     # µg beta-carotene per gram of GR2E grain (field-realistic)
STORAGE_RETENTION        = 0.65    # fraction surviving 3–6 months tropical storage
COOKING_RETENTION        = 0.60    # fraction surviving cooking
BIOCONVERSION            = 3.8     # µg beta-carotene -> 1 µg retinol (Tang 2009, GR-specific)
CHILD_RDA_UG             = 400.0   # µg RAE/day recommended for a young child (WHO)
CHILD_RICE_FRACTION      = 0.30    # a child under 5 eats ~30% of the per-capita adult portion

RELATIVE_RISK_VAD        = 1.75    # a VAD child's risk of death vs. a vitamin-A-replete child
EFFECTIVE_VAS_MULTIPLIER = 0.70    # share of "supplement-covered" kids actually protected
DOSE_RESPONSE_CONCAVITY  = 0.60    # partial vitamin A -> less-than-proportional benefit

ADOPTION_CEILING         = 0.70    # max adoption in the realistic S-curve scenario
ADOPTION_MIDPOINT_YEARS  = 8.0     # years after launch to reach half the ceiling
ADOPTION_STEEPNESS       = 0.45    # S-curve slope

MODEL_START_YEAR         = 2000
MODEL_END_YEAR           = 2024    # last year with real, filled-in data

# Years-of-life constants (WHO; used only for PART D)
YEARS_LOST_PER_DEATH     = 28.0    # discounted life-years lost per under-5 death (raw ~55-60)
QALYS_PER_BLIND_CHILD    = 21.0    # ~35 remaining years × 0.6 disability weight

# Blindness multiplier: WHO says 2–4x as many children go blind from VAD as die from it
BLINDNESS_LOW_MULT       = 2.0
BLINDNESS_HIGH_MULT      = 4.0

# How strongly does vitamin A actually cut child deaths? (the GiveWell / Cochrane question)
# The same Cochrane meta-analysis gives two numbers: a 24% reduction (random-effects model)
# and a 12% reduction (fixed-effects model, which gives full weight to DEVTA, the single
# largest trial). 24% matches the model's built-in RELATIVE_RISK_VAD = 1.75, so we use it
# as the central case; 12% is the conservative floor. GiveWell uses this same 12–24% range.
MORTALITY_EFFECT_CENTRAL = 1.00   # 24%, random-effects (the model's built-in assumption)
MORTALITY_EFFECT_FLOOR   = 0.50   # 12%, fixed-effects — half as strong

# ============================================================================
# 2. COUNTRY DATA  (inputs; sources cited on the page)
# ============================================================================
# under5_deaths: anchor years, linearly interpolated between
# vad_baseline: (year, prevalence fraction), declines at vad_decline per year
# vas: anchor years of vitamin-A-supplement coverage, interpolated
# rice_kg: per-capita milled rice, kg/year
# domestic: fraction of consumed rice grown domestically (reachable by seed system)
# deploy: counterfactual Golden Rice launch year in this country
# rice_eating_vad: fraction of VAD-affected children who actually live on rice
COUNTRIES = {
    "India": dict(
        under5={2000: 2_300_000, 2005: 1_900_000, 2010: 1_450_000, 2015: 1_000_000, 2020: 700_000, 2024: 560_000},
        vad_year=2000, vad_base=0.57, vad_decline=0.020,
        vas={2000: 0.44, 2005: 0.50, 2010: 0.55, 2015: 0.57, 2020: 0.55, 2024: 0.54},
        rice_kg=145.0, domestic=1.00, deploy=2009, rice_eating_vad=0.55),
    "Indonesia": dict(
        under5={2000: 290_000, 2005: 225_000, 2010: 160_000, 2015: 112_000, 2020: 80_000, 2024: 65_000},
        vad_year=2000, vad_base=0.50, vad_decline=0.030,
        vas={2000: 0.70, 2005: 0.78, 2010: 0.82, 2015: 0.80, 2020: 0.77, 2024: 0.75},
        rice_kg=135.0, domestic=0.95, deploy=2008, rice_eating_vad=1.00),
    "Nigeria": dict(
        under5={2000: 850_000, 2005: 780_000, 2010: 700_000, 2015: 610_000, 2020: 490_000, 2024: 420_000},
        vad_year=2000, vad_base=0.30, vad_decline=0.015,
        vas={2000: 0.40, 2005: 0.50, 2010: 0.55, 2015: 0.52, 2020: 0.50, 2024: 0.48},
        rice_kg=40.0, domestic=0.55, deploy=2012, rice_eating_vad=0.35),
    "Myanmar": dict(
        under5={2000: 120_000, 2005: 90_000, 2010: 59_000, 2015: 37_000, 2020: 25_000, 2024: 20_000},
        vad_year=2000, vad_base=0.36, vad_decline=0.025,
        vas={2000: 0.55, 2005: 0.65, 2010: 0.73, 2015: 0.74, 2020: 0.70, 2024: 0.58},
        rice_kg=195.0, domestic=1.00, deploy=2009, rice_eating_vad=1.00),
    "Bangladesh": dict(
        under5={2000: 250_000, 2005: 180_000, 2010: 115_000, 2015: 70_000, 2020: 48_000, 2024: 36_000},
        vad_year=2000, vad_base=0.21, vad_decline=0.035,
        vas={2000: 0.75, 2005: 0.87, 2010: 0.93, 2015: 0.92, 2020: 0.89, 2024: 0.87},
        rice_kg=175.0, domestic=0.97, deploy=2007, rice_eating_vad=1.00),
    "Vietnam": dict(
        under5={2000: 85_000, 2005: 61_000, 2010: 42_000, 2015: 27_000, 2020: 19_000, 2024: 16_000},
        vad_year=2000, vad_base=0.45, vad_decline=0.040,
        vas={2000: 0.76, 2005: 0.84, 2010: 0.87, 2015: 0.85, 2020: 0.83, 2024: 0.80},
        rice_kg=165.0, domestic=1.00, deploy=2007, rice_eating_vad=1.00),
    "Cambodia": dict(
        under5={2000: 50_000, 2005: 35_000, 2010: 21_000, 2015: 13_000, 2020: 8_500, 2024: 6_500},
        vad_year=2000, vad_base=0.45, vad_decline=0.030,
        vas={2000: 0.65, 2005: 0.78, 2010: 0.82, 2015: 0.83, 2020: 0.81, 2024: 0.79},
        rice_kg=200.0, domestic=1.00, deploy=2010, rice_eating_vad=1.00),
    "Philippines": dict(
        under5={2000: 65_000, 2005: 51_000, 2010: 37_000, 2015: 25_000, 2020: 17_000, 2024: 13_500},
        vad_year=2003, vad_base=0.38, vad_decline=0.040,
        vas={2000: 0.70, 2005: 0.80, 2010: 0.85, 2015: 0.83, 2020: 0.82, 2024: 0.80},
        rice_kg=115.0, domestic=0.85, deploy=2006, rice_eating_vad=1.00),
    "Laos": dict(
        under5={2000: 22_000, 2005: 16_000, 2010: 11_000, 2015: 7_000, 2020: 4_800, 2024: 3_800},
        vad_year=2000, vad_base=0.42, vad_decline=0.025,
        vas={2000: 0.55, 2005: 0.68, 2010: 0.74, 2015: 0.75, 2020: 0.72, 2024: 0.70},
        rice_kg=190.0, domestic=1.00, deploy=2011, rice_eating_vad=1.00),
    "Tanzania": dict(
        under5={2000: 225_000, 2005: 200_000, 2010: 160_000, 2015: 115_000, 2020: 78_000, 2024: 60_000},
        vad_year=2000, vad_base=0.33, vad_decline=0.018,
        vas={2000: 0.50, 2005: 0.62, 2010: 0.70, 2015: 0.70, 2020: 0.67, 2024: 0.63},
        rice_kg=32.0, domestic=0.60, deploy=2013, rice_eating_vad=0.28),
    "Nepal": dict(
        under5={2000: 55_000, 2005: 40_000, 2010: 26_000, 2015: 16_000, 2020: 10_500, 2024: 8_000},
        vad_year=2000, vad_base=0.31, vad_decline=0.030,
        vas={2000: 0.70, 2005: 0.85, 2010: 0.89, 2015: 0.87, 2020: 0.83, 2024: 0.80},
        rice_kg=120.0, domestic=0.90, deploy=2009, rice_eating_vad=0.65),
}

# ============================================================================
# 3. HELPER FUNCTIONS
# ============================================================================
def value_for_year(anchor_points, year):
    """Linear interpolation between anchor years; flat outside the range.
    e.g. if we know deaths in 2020 and 2024, estimate 2022 as the midpoint."""
    years = sorted(anchor_points)
    if year <= years[0]:  return float(anchor_points[years[0]])
    if year >= years[-1]: return float(anchor_points[years[-1]])
    for earlier_year, later_year in zip(years, years[1:]):
        if earlier_year <= year <= later_year:
            how_far_between = (year - earlier_year) / (later_year - earlier_year)
            return anchor_points[earlier_year] + how_far_between * (anchor_points[later_year] - anchor_points[earlier_year])
    return float(anchor_points[years[-1]])

def vitamin_a_delivered_per_day(rice_kg_per_year):
    """µg of vitamin A (RAE) a young child gets per day from Golden Rice."""
    rice_grams_per_person_per_day = rice_kg_per_year * 1000.0 / 365.0   # kg/yr -> g/day (×1000 is kg->g)
    rice_grams_a_child_eats       = rice_grams_per_person_per_day * CHILD_RICE_FRACTION
    beta_carotene_micrograms      = (rice_grams_a_child_eats
                                     * BETA_CAROTENE_UG_PER_G
                                     * STORAGE_RETENTION
                                     * COOKING_RETENTION)
    return beta_carotene_micrograms / BIOCONVERSION

def fraction_of_daily_need_met(rice_kg_per_year):
    """How much of a child's daily vitamin A requirement Golden Rice fills (capped at 100%)."""
    return min(vitamin_a_delivered_per_day(rice_kg_per_year) / CHILD_RDA_UG, 1.0)

def share_of_deaths_caused_by_vad(vad_rate):
    """Of all under-5 deaths, the fraction attributable to vitamin A deficiency.
    Standard epidemiology formula (the 'population attributable fraction')."""
    extra_risk = vad_rate * (RELATIVE_RISK_VAD - 1.0)
    return extra_risk / (1.0 + extra_risk)

def vad_rate_for_year(country, year):
    """Share of children who are vitamin-A-deficient in a given year (declines over time)."""
    rate = country["vad_base"] * ((1.0 - country["vad_decline"]) ** (year - country["vad_year"]))
    return max(rate, 0.02)   # floor: 2% residual in hard-to-reach populations

def adoption_s_curve(years_since_launch):
    """Share of the reachable crop that has switched to Golden Rice, 0..1.
    Slow at first, fast in the middle, leveling off — how new seeds really spread."""
    if years_since_launch <= 0:
        return 0.0
    return 1.0 / (1.0 + math.exp(-ADOPTION_STEEPNESS * (years_since_launch - ADOPTION_MIDPOINT_YEARS)))

# ============================================================================
# PART A — vitamin A per day & % of daily need  (the table's middle columns)
# ============================================================================
print("=" * 70)
print("PART A — Vitamin A delivered per child per day")
print("=" * 70)
print(f"{'Country':12} {'rice kg/yr':>10} {'µg RAE/day':>11} {'% of 400µg':>11}")
for country_name, country in COUNTRIES.items():
    vitamin_a            = vitamin_a_delivered_per_day(country["rice_kg"])
    percent_of_daily_need = vitamin_a / CHILD_RDA_UG * 100
    print(f"{country_name:12} {country['rice_kg']:>10.0f} {vitamin_a:>11.0f} {percent_of_daily_need:>10.0f}%")

# ============================================================================
# PART B — deaths prevented per year IF ALL DOMESTIC RICE WERE GOLDEN RICE
# ============================================================================
# This is the table's right-hand column. It is a "today" steady-state number:
#   - use the most recent year (2024) deaths and prevalence
#   - assume FULL reach: every domestically grown grain is Golden Rice, so the
#     adoption term = domestic_rice_fraction × rice_eating_vad_fraction
#     (NOT the 0.70 S-curve ceiling — this is the theoretical maximum)
print()
print("=" * 70)
print("PART B — Deaths prevented / year at 100% domestic adoption (2024)")
print("=" * 70)
YEAR = 2024
print(f"{'Country':12} {'deaths/yr':>10}")
total_deaths_prevented_per_year = 0.0
for country_name, country in COUNTRIES.items():
    under5_deaths_this_year         = value_for_year(country["under5"], YEAR)
    vad_rate_this_year              = vad_rate_for_year(country, YEAR)
    deaths_caused_by_vad            = under5_deaths_this_year * share_of_deaths_caused_by_vad(vad_rate_this_year)
    share_protected_by_supplements  = value_for_year(country["vas"], YEAR) * EFFECTIVE_VAS_MULTIPLIER
    deaths_not_prevented_by_supps   = deaths_caused_by_vad * (1.0 - share_protected_by_supplements)
    share_reachable_by_golden_rice  = country["domestic"] * country["rice_eating_vad"]   # full reach, no 0.70 ceiling
    golden_rice_effectiveness       = fraction_of_daily_need_met(country["rice_kg"]) ** DOSE_RESPONSE_CONCAVITY
    lives_saved_per_year            = (deaths_not_prevented_by_supps
                                       * share_reachable_by_golden_rice
                                       * golden_rice_effectiveness)
    total_deaths_prevented_per_year += lives_saved_per_year
    print(f"{country_name:12} {lives_saved_per_year:>10,.0f}")
print(f"{'TOTAL':12} {total_deaths_prevented_per_year:>10,.0f}")

# ============================================================================
# PART C — cumulative lives lost 2006–2024  (the realistic S-curve scenario)
# ============================================================================
# Same per-year logic as PART B, but now adoption ramps up along the S-curve
# starting from each country's launch year (capped at 0.70 × domestic × rice_eating),
# and we add up every single year from 2000 to 2024.
print()
print("=" * 70)
print("PART C — Cumulative children's lives lost, realistic adoption")
print("=" * 70)
print(f"{'Country':12} {'cumulative':>12}")
total_lives_lost = 0.0
for country_name, country in COUNTRIES.items():
    max_adoption              = ADOPTION_CEILING * country["domestic"] * country["rice_eating_vad"]
    golden_rice_effectiveness = fraction_of_daily_need_met(country["rice_kg"]) ** DOSE_RESPONSE_CONCAVITY
    country_total = 0.0
    for year in range(MODEL_START_YEAR, MODEL_END_YEAR + 1):
        under5_deaths_this_year        = value_for_year(country["under5"], year)
        vad_rate_this_year             = vad_rate_for_year(country, year)
        deaths_caused_by_vad           = under5_deaths_this_year * share_of_deaths_caused_by_vad(vad_rate_this_year)
        share_protected_by_supplements = value_for_year(country["vas"], year) * EFFECTIVE_VAS_MULTIPLIER
        deaths_not_prevented_by_supps  = deaths_caused_by_vad * (1.0 - share_protected_by_supplements)
        adoption_this_year             = adoption_s_curve(year - country["deploy"]) * max_adoption
        country_total += deaths_not_prevented_by_supps * adoption_this_year * golden_rice_effectiveness
    total_lives_lost += country_total
    print(f"{country_name:12} {country_total:>12,.0f}")
print(f"{'TOTAL':12} {total_lives_lost:>12,.0f}")

# ============================================================================
# PART D — blindness and years of healthy life lost
# ============================================================================
print()
print("=" * 70)
print("PART D — Death range, blindness, and healthy-life-years lost")
print("=" * 70)
children_dead_central = total_lives_lost                          # 24% effect
children_dead_floor   = total_lives_lost * MORTALITY_EFFECT_FLOOR  # 12% effect
children_blinded_low   = children_dead_central * BLINDNESS_LOW_MULT
children_blinded_high  = children_dead_central * BLINDNESS_HIGH_MULT
healthy_years_lost_low  = children_dead_central * YEARS_LOST_PER_DEATH + children_blinded_low  * QALYS_PER_BLIND_CHILD
healthy_years_lost_high = children_dead_central * YEARS_LOST_PER_DEATH + children_blinded_high * QALYS_PER_BLIND_CHILD
print(f"Children dead (central, 24% effect): {children_dead_central:>13,.0f}")
print(f"Children dead (floor,   12% effect): {children_dead_floor:>13,.0f}")
print(f"Children blinded (2–4x):             {children_blinded_low:>13,.0f}  –  {children_blinded_high:,.0f}")
print(f"Healthy-life-years lost:             {healthy_years_lost_low:>13,.0f}  –  {healthy_years_lost_high:,.0f}")
print()
print("The 12% floor gives full weight to DEVTA, the largest trial (GiveWell's lower")
print("bound). Blindness is NOT scaled down by it: the vitamin-A->blindness link is")
print("direct and not in dispute.")
