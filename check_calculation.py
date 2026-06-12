#!/usr/bin/env python3
"""
Golden Rice "cost of delay" — full calculation, written to be double-checked.
================================================================================
This reproduces every number on the web page from scratch. Run it:

    python3 check_calculation.py

Nothing fancy, no imports beyond the standard library. Every step is spelled
out so you (or anyone) can follow the arithmetic by hand.

There are FOUR outputs, matching the four places numbers appear on the page:
  PART A — vitamin A delivered per child per day, and % of daily need   (table)
  PART B — deaths prevented per year if ALL domestic rice were Golden    (table)
  PART C — cumulative children's lives lost 2006–2024                    (headline)
  PART D — blindness and years-of-healthy-life-lost                      (headline)
"""

import math

# ============================================================================
# 1. PARAMETERS  (the knobs; every one is cited on the web page)
# ============================================================================
BETA_CAROTENE_UG_PER_G   = 18.0    # µg beta-carotene per gram of GR2E grain (field-realistic)
STORAGE_RETENTION        = 0.65    # fraction surviving 3–6 months tropical storage
COOKING_RETENTION        = 0.60    # fraction surviving cooking
BIOCONVERSION            = 3.8     # µg beta-carotene -> 1 µg retinol (Tang 2009, GR-specific)
CHILD_RDA_UG             = 400.0   # µg RAE/day recommended for a young child (WHO)
CHILD_RICE_FRACTION      = 0.30    # a child under 5 eats ~30% of the per-capita adult portion

RELATIVE_RISK_VAD        = 1.75    # VAD child's mortality risk vs. a replete child
EFFECTIVE_VAS_MULTIPLIER = 0.70    # share of "VAS-covered" kids actually protected
DOSE_RESPONSE_CONCAVITY  = 0.60    # partial RDA -> less-than-proportional mortality benefit

ADOPTION_CEILING         = 0.70    # max adoption in the realistic S-curve scenario
ADOPTION_MIDPOINT_YEARS  = 8.0     # years after launch to reach half the ceiling
ADOPTION_STEEPNESS       = 0.45    # S-curve slope

MODEL_START_YEAR         = 2000
MODEL_END_YEAR           = 2024

# Years-of-life constants (WHO; used only for PART D)
YEARS_LOST_PER_DEATH     = 28.0    # avg life expectancy lost per under-5 death
QALYS_PER_BLIND_CHILD    = 21.0    # ~35 remaining years × 0.6 disability weight

# Blindness multiplier: WHO says 2–4x as many children go blind from VAD as die from it
BLINDNESS_LOW_MULT       = 2.0
BLINDNESS_HIGH_MULT      = 4.0

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
def interpolate(anchors, year):
    """Linear interpolation between anchor years; flat outside the range."""
    yrs = sorted(anchors)
    if year <= yrs[0]:  return float(anchors[yrs[0]])
    if year >= yrs[-1]: return float(anchors[yrs[-1]])
    for y0, y1 in zip(yrs, yrs[1:]):
        if y0 <= year <= y1:
            t = (year - y0) / (y1 - y0)
            return anchors[y0] + t * (anchors[y1] - anchors[y0])
    return float(anchors[yrs[-1]])

def vitamin_a_per_day(rice_kg):
    """µg RAE delivered to a child per day from Golden Rice."""
    daily_rice_g = rice_kg * 1000.0 / 365.0          # per-capita grams/day
    child_rice_g = daily_rice_g * CHILD_RICE_FRACTION # child's portion
    beta_carotene = child_rice_g * BETA_CAROTENE_UG_PER_G * STORAGE_RETENTION * COOKING_RETENTION
    return beta_carotene / BIOCONVERSION

def efficacy_fraction(rice_kg):
    """Fraction of the child's daily vitamin A need that Golden Rice fills (capped at 1.0)."""
    return min(vitamin_a_per_day(rice_kg) / CHILD_RDA_UG, 1.0)

def paf(prevalence):
    """Population attributable fraction: share of under-5 deaths due to VAD."""
    excess = prevalence * (RELATIVE_RISK_VAD - 1.0)
    return excess / (1.0 + excess)

def vad_prevalence(c, year):
    prev = c["vad_base"] * ((1.0 - c["vad_decline"]) ** (year - c["vad_year"]))
    return max(prev, 0.02)   # floor: 2% residual in hard-to-reach populations

def logistic_adoption(years_since_deploy):
    if years_since_deploy <= 0:
        return 0.0
    s = 1.0 / (1.0 + math.exp(-ADOPTION_STEEPNESS * (years_since_deploy - ADOPTION_MIDPOINT_YEARS)))
    return s   # returns 0..1; caller multiplies by the ceiling

# ============================================================================
# PART A — vitamin A per day & % of daily need  (the table's middle columns)
# ============================================================================
print("=" * 70)
print("PART A — Vitamin A delivered per child per day")
print("=" * 70)
print(f"{'Country':12} {'rice kg/yr':>10} {'µg RAE/day':>11} {'% of 400µg':>11}")
for name, c in COUNTRIES.items():
    rae = vitamin_a_per_day(c["rice_kg"])
    pct = rae / CHILD_RDA_UG * 100
    print(f"{name:12} {c['rice_kg']:>10.0f} {rae:>11.0f} {pct:>10.0f}%")

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
total_annual = 0.0
for name, c in COUNTRIES.items():
    u5      = interpolate(c["under5"], YEAR)
    prev    = vad_prevalence(c, YEAR)
    vad_d   = u5 * paf(prev)
    eff_vas = interpolate(c["vas"], YEAR) * EFFECTIVE_VAS_MULTIPLIER
    unprot  = vad_d * (1.0 - eff_vas)
    reach   = c["domestic"] * c["rice_eating_vad"]              # full adoption, no 0.70 ceiling
    eff     = efficacy_fraction(c["rice_kg"]) ** DOSE_RESPONSE_CONCAVITY
    saved   = unprot * reach * eff
    total_annual += saved
    print(f"{name:12} {saved:>10,.0f}")
print(f"{'TOTAL':12} {total_annual:>10,.0f}")

# ============================================================================
# PART C — cumulative lives lost 2006–2024  (the realistic S-curve scenario)
# ============================================================================
# Same per-year formula, but now adoption follows the logistic S-curve starting
# from each country's deployment year, capped at 0.70 × domestic × rice_eating.
# Summed over every year 2000–2024.
print()
print("=" * 70)
print("PART C — Cumulative children's lives lost, realistic adoption")
print("=" * 70)
print(f"{'Country':12} {'cumulative':>12}")
grand_total = 0.0
by_country_cum = {}
for name, c in COUNTRIES.items():
    ceiling = ADOPTION_CEILING * c["domestic"] * c["rice_eating_vad"]
    eff = efficacy_fraction(c["rice_kg"]) ** DOSE_RESPONSE_CONCAVITY
    country_cum = 0.0
    for year in range(MODEL_START_YEAR, MODEL_END_YEAR + 1):
        u5      = interpolate(c["under5"], year)
        prev    = vad_prevalence(c, year)
        vad_d   = u5 * paf(prev)
        eff_vas = interpolate(c["vas"], year) * EFFECTIVE_VAS_MULTIPLIER
        unprot  = vad_d * (1.0 - eff_vas)
        adopt   = logistic_adoption(year - c["deploy"]) * ceiling
        country_cum += unprot * adopt * eff
    by_country_cum[name] = country_cum
    grand_total += country_cum
    print(f"{name:12} {country_cum:>12,.0f}")
print(f"{'TOTAL':12} {grand_total:>12,.0f}")

# ============================================================================
# PART D — blindness and years of healthy life lost
# ============================================================================
print()
print("=" * 70)
print("PART D — Blindness and healthy-life-years lost")
print("=" * 70)
deaths = grand_total
blind_low  = deaths * BLINDNESS_LOW_MULT
blind_high = deaths * BLINDNESS_HIGH_MULT
qaly_low   = deaths * YEARS_LOST_PER_DEATH + blind_low  * QALYS_PER_BLIND_CHILD
qaly_high  = deaths * YEARS_LOST_PER_DEATH + blind_high * QALYS_PER_BLIND_CHILD
print(f"Children dead:            {deaths:>14,.0f}")
print(f"Children blinded (2–4x):  {blind_low:>14,.0f}  –  {blind_high:,.0f}")
print(f"Healthy-life-years lost:  {qaly_low:>14,.0f}  –  {qaly_high:,.0f}")
print(f"  (deaths × {YEARS_LOST_PER_DEATH:.0f} life-years) + (blind × {QALYS_PER_BLIND_CHILD:.0f} QALYs)")
