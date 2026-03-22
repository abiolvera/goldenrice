# Model Critique and Research Gaps

> This document critiques assumptions in `model.py` against findings in the research documents,
> and identifies research gaps that should be filled before the model outputs are treated as reliable.
> **Do not edit model.py directly** — resolve each item by improving research docs first,
> then update model parameters with explicit source citations.
> Last updated: 2026-03-21 (updated with findings from deep-dive research agents)

---

## CRITICAL: Parameter Discrepancies Between model.py and Research Docs

### C-1: Beta-Carotene Content — 5–10× Overstatement (HIGH PRIORITY)

**model.py default**: `beta_carotene_ug_per_g_dry = 18.0` µg/g
**Cited source in model**: "Philippines multi-environment field trials (IRRI 2019): 14–22 µg/g milled grain"

**What the research actually shows** (`03_nutritional_efficacy.md`, Swamy et al. 2019):
- GR2E regulatory submission data: **1.96–7.31 µg/g milled rice**, mean **3.57 µg/g**
- Source: Four Philippine field sites, 2015–2016 seasons, published in *J. Agric. Food Chem.*
- These are the numbers used in actual regulatory dossiers for Australia, Canada, USA, Philippines

**RESOLVED — `10_beta_carotene_deep_dive.md`** (2026-03-21):

The 14–22 µg/g figure has **no published source**. Exhaustive search found no IRRI 2019
multi-environment trial reporting that range for GR2E beta-carotene in Philippine milled rice.
The figure is almost certainly a conflation of:
- (a) **Bangladesh BC3F2 screening values** (Biswas 2021): 10–21.5 µg/g *total carotenoids*
  (not beta-carotene; not Philippines; not GR2E regulatory event)
- (b) **GR2 lab/greenhouse lines** (Paine 2005): up to 31 µg/g in best laboratory lines —
  never achieved in field-deployed GR2E in Philippine cultivar PSBRc82

**Swamy 2019 confirmed** (DOI: 10.1021/acs.jafc.9b01524, PMC6646955): mean **3.57 µg/g**,
range 1.96–7.31 µg/g in milled rice from 4 Philippine field sites, 2015–2016. This is the
regulatory dataset used for AU/NZ, Canada, USA, and Philippines approvals.

**Note**: The Swamy 2019 values are already post-milling (GR2E expresses beta-carotene in
the endosperm, so milling losses are low — the 3.57 µg/g figure reflects white milled grain).

**Consumer-facing estimate after storage and cooking** (3-month tropical storage + boiling):
approximately **0.57–0.94 µg/g beta-carotene** — delivering **~5–8 µg RAE/day** at Tang
2009's 3.8:1 ratio and Bangladesh child rice intake. This is **~1.3–2.1% of child RDA**,
not the 21–66% that model.py currently computes.

**Corrected parameter**: `beta_carotene_ug_per_g_dry = 3.57` (central), range 1.96–7.31 µg/g.
Source: Swamy et al. 2019, J. Agric. Food Chem., DOI: 10.1021/acs.jafc.9b01524

---

### C-2: Storage Retention — 2–4× Too Optimistic (HIGH PRIORITY)

**model.py default**: `storage_retention_fraction = 0.65`
**Cited source in model**: "40–75% retention. Swamy et al. 2019; Saltzman et al. 2013 for pro-vitamin A maize analog."

**What the research actually shows** (`03_nutritional_efficacy.md`, direct GR data):
- Bollinedi et al. 2019 (*Food Chemistry*): **68–84% degradation** at 6 months ambient (~25°C)
  → Only **16–32% retained** at 6 months
- Schaub et al. 2017: Only **13% retained at 10 weeks** (kinetics study)
- Model's 0.65 = 65% retention implies only 35% degradation — inconsistent with both studies

**Impact**: If actual retention is 16–32% rather than 65%, model overstates nutritional delivery
by ~2–4× on this parameter alone.

**Combined C-1 × C-2 impact**:
- Model: 18 µg/g × 0.65 storage = **11.7 µg/g effective**
- Research: 3.57 µg/g × 0.16–0.32 storage = **0.57–1.14 µg/g effective**
- **Ratio: ~10–20× overestimate of beta-carotene reaching the consumer**

**PARTIALLY RESOLVED — `10_beta_carotene_deep_dive.md`** (2026-03-21):

Bollinedi 2019 and Schaub 2017 confirmed. Additional post-2019 data aligns: ~84% loss at 6
months ambient in polished white rice (~16% retained). No published data exists on whether
hermetic storage bags (e.g., PICS bags) meaningfully reduce carotenoid degradation — this
remains an open research question.

**Corrected parameter**: `storage_retention_fraction = 0.13–0.16` for 3-month ambient storage
in tropical conditions (central: 0.15). The model's default of 0.65 is 4× too optimistic.
Source: Bollinedi et al. 2019, *Food Chemistry*; Schaub et al. 2017.

---

### C-3: VAS Coverage Uses Smooth Interpolation, Misses Documented Collapses (MEDIUM)

**model.py approach**: Interpolates linearly between ~5 anchor years per country.

**What the research shows** (`04_interventions_and_rice_consumption.md`):
- Bangladesh: Coverage collapsed to **0%** in 2014 (documented, not estimated)
- Global: 19-percentage-point drop in 2020 (COVID-19)
- 2015–2016: Unprotected children tripled from 19M to 62M globally
- Myanmar: Coverage deteriorated post-2021 coup

**Impact**: Smooth interpolation overstates effective VAS protection in 2014–2016 and 2020–2022,
which *understates* the marginal benefit of Golden Rice in those years (GR would have looked
better relative to collapsing VAS, not worse). Net effect on cumulative estimate is ambiguous but
the per-year values will be wrong.

**RESOLVED — `11_vas_coverage_annual_series.md`** (2026-03-21, 770 lines):

Annual series compiled for all 8 countries from UNICEF/World Bank SN.ITK.VITA.ZS,
DHS surveys, WHO situation analyses, and national sources. Key findings:

- **Bangladesh**: High (85–99%) with collapses in 2010–11, 2014, 2018. DHS confirms real
  drop to ~62% in 2011 and 2014 from political disruption. UNICEF "0" values = reporting
  failures, not actual zero coverage. The "documented 0%" claim should be revised to "documented
  collapse to ~62%."
- **Philippines**: Peak 91% (2009–13), steady decline after 2014. Dengvaxia scandal added
  ~20pp trust-driven drop (2017–19). COVID 2020 = 29%. Major discrepancy: UNICEF admin
  shows only 10% in 2023 while 2022 NDHS shows 79%.
- **Myanmar**: Excellent 86–96% (2001–19). Coup (Feb 2021) crashed coverage to 37%;
  partial recovery to 71% (2022). Full recovery unlikely without political change.
- **Nigeria**: Most volatile — linked to polio NID campaigns. Multiple "0" years from campaign
  suspension. 2016 collapse (56%) from polio wind-down; estimated ~52–57% by 2021.
- **Vietnam**: Near-universal 94–99% (2000–17) — most stable globally. Post-2017 data
  absent; likely exited UNICEF priority list as VAD declined.
- **India, Indonesia, Cambodia**: Moderate volatility; see `11_vas_coverage_annual_series.md`.

**Critical modeling implication**: UNICEF "0" values ≠ zero coverage (almost always reporting
failures). Administrative data overcounts vs. DHS surveys. Campaign-dependent countries
(Philippines, Bangladesh, Nigeria) are 2–3× more structurally fragile than routine-delivery
countries (Vietnam, India).

**Corrected approach**: Step-change model at documented discontinuities; use DHS survey data
as ground truth where available; do NOT use smooth interpolation across Myanmar 2021,
Philippines 2017–20, Bangladesh 2014, Nigeria 2016.

---

### C-4: Myanmar VAD Baseline is Entirely Estimated (MEDIUM)

**model.py**: `vad_baseline_prevalence=0.36` with comment `[EST based on regional WHO data]`

**What the research shows** (`02_vad_mortality_data.md`):
- "Recent nationally representative VAD data limited; survey results not fully published"
- Myanmar falls within the SE Asia regional trajectory (42% → 6%, 1991–2013) but sub-national
  variation is enormous; conflict-affected highland regions likely retain high burden

**Impact**: Myanmar has among the world's highest rice consumption (279 kg/yr, #1 globally)
and model gives it `gr_deployment_year=2009` — making it a meaningful contributor to estimates.
An unconstrained baseline prevalence propagates directly into life-years-saved figures.

**RESOLVED — `13_myanmar_vad_and_bioconversion.md`** (2026-03-21):

Myanmar's first national micronutrient survey (MMFCS 2017–2018, 9,041 children, all 15
states/regions) found ~**35% VAD prevalence** in children under 5. The model's `0.36` is
well-grounded for 2017–2018.

**However, the error runs in the opposite direction for historical years**: Back-extrapolating
from 35% at 2018 using ~2.5%/yr decline implies a year-2000 baseline of **0.50–0.55**. The
model's static `0.36` baseline likely **underestimates** Myanmar's historical burden, meaning
the model underestimates, not overestimates, Myanmar's contribution to lives-saved estimates.

Sub-national variation is large: highland conflict states (Kachin, Shan, Rakhine) likely
40–55% vs. lowland delta average. Post-2021 coup, UNICEF documents 6M children in
humanitarian need; VAS programs have collapsed in many areas.

**Corrected approach**: Use time-varying baseline. Year 2000: 0.52 (central). Year 2018: 0.35.
Year 2022+: treat as uncertain/elevated due to coup-related program collapse.
Source: MMFCS 2017–2018 Interim Report (Myanmar MoHS, Feb 2019); Wieringa et al. 2016 (PMID 26421387)

---

### C-5: Relative Risk (VAD → Mortality) Is Flat Across All Countries (MEDIUM)

**model.py**: `relative_risk_vad = 1.75` applied uniformly to all 8 countries.

**What the literature shows** (from `05_published_impact_models.md` and `02_vad_mortality_data.md`):
- Sommer et al. 1983 (Indonesia): RR ~1.9
- West et al. 1991 (Nepal): RR 1.6–2.2
- Fawzi et al. 1993 (Tanzania): RR 1.4–2.0
- GBD 2019 uses much lower effective RR (implied from low mortality estimates ~17K)
- RR likely varies with: baseline disease burden (malaria co-infection inflates VAD effect in
  Africa vs. Asia), sanitation quality, baseline nutritional status beyond VAD alone

**Impact**: Using India's RR for Nigeria and vice versa is methodologically weak. Nigeria's
VAD deaths occur in a high-malaria environment where VAD-malaria interaction amplifies risk;
Philippines has low malaria and different infectious disease profile.

**RESOLVED — `12_relative_risk_country_specific.md`** (2026-03-21):

The model's uniform 1.75 is too high for most countries. Compiled from 25+ sources:

| Country | Recommended RR | Range | Key driver |
|---------|---------------|-------|------------|
| Bangladesh | **1.65** | 1.40–1.90 | High VAD, measles/diarrhea burden |
| Myanmar | **1.55** | 1.25–1.80 | High VAD, conflict disruption |
| Philippines | **1.45** | 1.20–1.70 | Moderate VAD, lower disease burden |
| Cambodia | **1.40** | 1.15–1.65 | BCMO1 concern (see below) |
| India | **1.35** | 1.05–1.65 | DEVTA 2013 near-null result weighs down |
| Indonesia | **1.25** | 1.05–1.50 | Lower current burden |
| Nigeria | **1.20** | 0.95–1.50 | VAS does NOT reduce malaria mortality |
| Vietnam | **1.20** | 1.05–1.40 | BCMO1 concern; lower VAD burden |

**Nigeria caveat**: Sensitivity run at RR=1.0 warranted — malaria accounts for ~30% of
under-5 deaths and VAS has no malaria-specific mortality benefit (Ghana VAST confirmed).

**BCMO1 finding** (critical, new): rs6564851 G allele reducing beta-carotene conversion by
~48% has ~82% frequency in East Asian populations. Likely common in Vietnamese and
Cambodian populations. Population-level BCMO1 adjustment factors recommended:
- SE Asia (Bangladesh, Philippines, Indonesia): 0.85 (range 0.75–0.95)
- Vietnam, Cambodia: 0.80 (range 0.70–0.90)

**Methodological note**: The GBD 2019 shift from RR~1.75 to RR~1.14 reflects a
controversial methodology change (dropped prevalence-adjustment, unpublished trimming
criteria) — not a real-world change. The trial-based PAF approach (RR 1.4–1.9) is
more defensible for this model's purposes.
Source: `12_relative_risk_country_specific.md`; Imdad et al. 2022 Cochrane; GBD 2019

---

## Research Gaps: Missing Data for Model Parameters

### G-1: Bioconversion in Malnourished Children (HIGH PRIORITY)

Tang 2009 (adults): 3.8:1. Tang 2012 (marginally deficient Chinese children): 2.3:1 (retracted).
Neither study addresses **severely malnourished children with gut enteropathy** — the actual
target population. Model.py's 12:1 conservative default is a reasonable prior, but there is no
published study on bioconversion in severely VAD-deficient, growth-stunted, gut-compromised
children eating GR with typical low-fat diets.

**RESOLVED — `13_myanmar_vad_and_bioconversion.md`** (2026-03-21):

Counterintuitive finding: **the model's 12:1 default is actually well-calibrated** for the
real target population. Tang 2009's 3.8:1 used healthy volunteers with adequate fat —
the optimistic upper bound, not the realistic central estimate.

For severely malnourished children with **environmental enteropathy** (the actual target):
- Villous blunting + impaired bile acid secretion + inflammatory RBP suppression worsen
  the effective conversion ratio by 2–3× vs. healthy gut
- Effective ratio for EE-affected children: **7–15:1** (pushing toward 12:1 or higher)
- **The conversion paradox**: VAD itself damages gut epithelium, worsening absorption in
  the most deficient children who most need intervention

**BCMO1**: Philippines — 7.6% carry double mutation (57% reduced conversion); 15–25%
have meaningfully impaired conversion overall. Bangladesh data: **critical gap, no published
data exists** on BCMO1 frequency in Bangladeshi population.

**Fat intake**: Rural Bangladeshi households frequently have per-meal fat below 3–5g
threshold for optimal carotenoid absorption. This alone can suppress absorption 3–5×.

**Recommendation**: Add `bioconversion_ratio=15.0` scenario labeled "realistic: EE-affected
malnourished child, low-fat diet." The 4:1 scenario should be relabeled "optimistic: healthy
volunteers, adequate fat."

**Model.py's 12:1 default should be retained** — it is not a conservative overestimate but
a realistic estimate for the target population.
Source: `13_myanmar_vad_and_bioconversion.md`

---

### G-2: Per-Country VAS Year-Specific Series (HIGH PRIORITY)

Model needs sharp discontinuities, not smooth interpolation. For each of the 8 countries,
compile annual VAS coverage 2000–2024 from:
- UNICEF Joint Monitoring Programme
- DHS survey years (gives point estimates; interpolate between)
- WHO/UNICEF immunization estimates database
- National program reports (BRRI Bangladesh, DepEd Philippines)

Priority countries for granular data: Bangladesh (2014 collapse), Philippines (2015–2016 drop),
Myanmar (2021 coup effect), India (state-level heterogeneity).

---

### G-3: Laos and Timor-Leste Coverage (LOW-MEDIUM)

model.py covers 8 countries. Both Laos and Timor-Leste have:
- Very high rice dependence (Laos >50% calories from rice; Timor-Leste >50%)
- High VAD prevalence (Timor-Leste: severe public health problem)
- Small populations (~7M and ~1.3M respectively) but high per-capita burden

Currently excluded. Adding them would modestly increase cumulative estimate.

**Research needed**: WHO VMNIS data for Laos and Timor-Leste. UNICEF MICS surveys.

---

### G-4: Adoption S-Curve — Better Biofortified Crop Analogs (MEDIUM)

model.py cites IR8 rice (Green Revolution) as adoption analog. But IR8 provided direct
farmer economic benefits (yield increase), which GR does not. Better analogs from
`04_interventions_and_rice_consumption.md`:

| Crop | Country | Time to 10% coverage | Driver |
|------|---------|----------------------|--------|
| Provitamin A cassava | Nigeria | ~8 years | Yield advantage + market |
| OFSP | Uganda | ~7 years (in target districts) | Nutrition + income |
| Iron pearl millet | India | ~6 years | Yield competitive |
| Iron beans | Rwanda | ~5 years (10% national bean area) | Agronomic parity |

**Research needed**: Find published adoption rate studies for rice varieties specifically
(non-GR) to calibrate the S-curve. HarvestPlus has modeling papers on biofortification
adoption that may provide better priors than the IR8 Green Revolution analog.

---

### G-5: Fortified Rice as Comparator (MEDIUM)

model.py's RT-10 notes rice fortification as a potentially superior comparator but says
"NOT MODELED." The research docs don't cover rice fortification in detail.

For a complete cost-effectiveness comparison, need:
- Cost per ton of fortified rice in target countries
- Coverage achievable through centralized milling networks
- Evidence on actual vitamin A delivery (04 doc notes >50% of fortified food samples
  fail quality checks)

**Research needed**: Literature review on mandatory rice fortification programs (Brazil,
Costa Rica, Philippines). GAIN (Global Alliance for Improved Nutrition) program reports.

---

## Structural / Methodological Issues

### M-1: PAF Framework vs. GBD Comparative Risk Assessment

The model uses PAF with RR=1.75 derived from supplementation trials. This puts it in the
"high mortality" methodological regime (~600K deaths/yr global). The GBD uses a different
framework yielding ~17K deaths/yr. The model does not explicitly state which regime it is in
or defend why PAF is preferred.

**Recommendation**: Add a section to 00_model_framework.md explicitly comparing the two
methodological approaches and justifying the choice. The Wesseler & Zilberman papers use the
PAF/Stein framework; GBD studies use comparative risk assessment. The model should be clear
it is replicating the former approach, not the latter.

---

### M-2: Bangladesh Regulatory Status Inconsistency in Research Docs

`06_current_status_and_uncertainties.md` contains contradictory entries:
- Summary table: "Bangladesh | Feb 2022 | APPROVED — first commercial cultivation globally"
- Body text: "Application filed November 2017; still in bureaucratic limbo as of 2025"

The Feb 2022 event was Bangladesh's Food Safety Authority approval for food safety (consumption),
**not** a commercial cultivation permit. The distinction matters for the model:
`model.py` correctly uses a counterfactual deployment year (2007) for Bangladesh, not 2022.
But the research docs need to clarify actual vs. counterfactual status clearly.

**Fix needed**: Update 06 to distinguish food safety approval (Feb 2022) from commercial
cultivation permit (still pending). Add note that Bangladesh's Feb 2022 approval does not
mean commercial production is underway — production at scale awaits full Ministry of
Environment clearance.

---

### M-3: No Morbidity Model (Blindness) Despite Available Data

`02_vad_mortality_data.md` contains substantial data on blindness:
- 250,000–500,000 children blind annually from VAD (WHO)
- 50% of blinded children die within 12 months
- GBD 2017 vision loss data: 75.1 per 100,000 age-standardized prevalence

model.py focuses entirely on mortality. A full DALY model would include:
- Blindness cases prevented
- Reduced morbidity from diarrhea and measles (VAD amplifies severity)
- Developmental outcomes (VAD impairs cognitive development)

Adding blindness to the model would increase the estimate by 10–30% and is well-supported
by existing research docs.

---

## Summary Priority Table

Status key: ✅ RESOLVED | 🔄 IN PROGRESS (VAS agent running) | ⬜ OPEN

| ID | Status | Priority | Fixes model.py | Research file | Estimated impact on output |
|----|--------|----------|----------------|---------------|---------------------------|
| C-1 | ✅ | **CRITICAL** | Yes — set to 3.57 µg/g | `10_beta_carotene_deep_dive.md` | **5× reduction** in beta-carotene dose |
| C-2 | ✅ | **CRITICAL** | Yes — set to 0.13–0.16 | `10_beta_carotene_deep_dive.md` | **4× reduction** in effective dose |
| C-1+C-2 combined | ✅ | **CRITICAL** | Yes | — | **~10–20× reduction** in consumer-facing beta-carotene |
| C-3/G-2 | ✅ | High | Yes — VAS coverage | `11_vas_coverage_annual_series.md` | ~10–20% change in per-year values; Bangladesh "0%" was actually ~62% |
| G-1 | ✅ | ~~High~~ → **Resolved differently** | No change needed | `13_myanmar_vad_and_bioconversion.md` | 12:1 default IS defensible; add 15:1 scenario |
| C-4 | ✅ | Medium | Yes — Myanmar historical baseline | `13_myanmar_vad_and_bioconversion.md` | Error flipped: model **underestimates** Myanmar (year-2000 should be 0.52, not 0.36) |
| C-5 | ✅ | Medium | Yes — use country-specific RR | `12_relative_risk_country_specific.md` | 1.75 → 1.20–1.65 range; ~15–30% overall reduction |
| G-4 | ⬜ | Medium | Yes — adoption | Open | ~10–30% |
| M-1 | ⬜ | Medium | No — framing | `golden_rice_economic_health_models_synthesis.md` (done) | Affects interpretation only |
| M-2 | ⬜ | Low | No — docs only | Fix 06 doc | Affects interpretation only |
| M-3 | ⬜ | Low | Would add morbidity | Already in 02 doc | +10–30% if added |
| BCMO1 | ✅ NEW | Medium | New parameter needed | `12_relative_risk_country_specific.md` | Apply 0.80–0.85 adjustment for SE Asian countries |

---

## Net Directional Assessment (Updated 2026-03-21)

The model likely **overstates** GR efficacy, but the magnitude is smaller than the 10–20×
headline implies because several factors partially counteract:

**Overstating factors** (push estimates down):
- C-1+C-2: ~10–20× overstatement of beta-carotene reaching consumers
- C-5: uniform RR=1.75 is too high for most countries (should be 1.20–1.65)

**Understating factors** (push estimates up):
- G-1 resolved: 12:1 bioconversion is the correct central estimate for malnourished children
  (model is NOT over-optimistic on this parameter)
- C-4 resolved: Myanmar historical VAD burden is *underestimated* (year-2000 ~0.52 not 0.36)
- C-3/VAS: smooth interpolation understates GR's marginal value in years when VAS collapsed

**Net**: Model still significantly overstates on balance, primarily driven by C-1+C-2.
A corrected model using 3.57 µg/g beta-carotene and 0.15 storage retention would reduce
central estimates by roughly 5–10×. The "millions of lives" framing would shift to "hundreds
of thousands" — still a significant policy-relevant estimate, but a different order of magnitude.

---

*This document should be updated as research gaps are filled. When a critique is resolved,
note the resolution and the updated parameter value with source.*
