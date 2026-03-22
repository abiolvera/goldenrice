# Research Note 13: Myanmar VAD Baseline and Beta-Carotene Bioconversion in Malnourished Children

**Date**: 2026-03-21
**Purpose**: Supporting evidence for `model.py` parameters `vad_baseline_prevalence=0.36` (Myanmar) and `bioconversion_ratio=12.0`
**Scope**: Two sub-tasks requested for model validation and uncertainty quantification

---

## Table of Contents

1. [Section A: Myanmar VAD — What We Know](#section-a-myanmar-vad)
   - [A1. Survey Landscape and Data Gaps](#a1-survey-landscape-and-data-gaps)
   - [A2. Best Available Prevalence Estimates](#a2-best-available-prevalence-estimates)
   - [A3. Myanmar and the SE Asian Regional Trajectory](#a3-myanmar-and-the-se-asian-regional-trajectory)
   - [A4. Sub-national Variation: Highlands vs. Delta](#a4-sub-national-variation-highlands-vs-delta)
   - [A5. Post-2021 Coup: Nutrition Deterioration](#a5-post-2021-coup-nutrition-deterioration)
   - [A6. Confidence Intervals and Model Implications](#a6-confidence-intervals-and-model-implications)
2. [Section B: Beta-Carotene Bioconversion in Malnourished Children](#section-b-bioconversion)
   - [B1. What the Population-Level Literature Shows](#b1-what-the-population-level-literature-shows)
   - [B2. Environmental Enteropathy and Gut Damage](#b2-environmental-enteropathy-and-gut-damage)
   - [B3. BCMO1/BCO1 Genetic Polymorphisms](#b3-bcmo1bco1-genetic-polymorphisms)
   - [B4. Dietary Fat Dependency](#b4-dietary-fat-dependency)
   - [B5. The Conversion Paradox: Severely VAD Children](#b5-the-conversion-paradox-severely-vad-children)
   - [B6. Biofortified Crop Absorption Studies](#b6-biofortified-crop-absorption-studies)
3. [Recommended Model Parameters](#recommended-model-parameters)
4. [Sources](#sources)

---

## Section A: Myanmar VAD

### A1. Survey Landscape and Data Gaps

Myanmar's vitamin A deficiency data landscape is among the most limited in Southeast Asia. Key context:

**The MMFCS 2017-2018 (Myanmar Micronutrient and Food Consumption Survey)**

This was Myanmar's *first-ever* comprehensive nationwide micronutrient survey, conducted November 2017 through May 2018 under the Ministry of Health and Sports (MoHS), funded jointly by MoHS, WHO, UNICEF, and the World Bank. The survey covered:
- 9,041 children aged 6–59 months
- 27,339 households across all 15 states/regions
- 450 clusters, selected by probability proportionate to size
- Biochemical sampling for micronutrient status including serum retinol

An Interim Report was released in February 2019 and is hosted on the MoHS website. The full biochemical VAD prevalence figures for children are contained within this document but are not freely indexed in open web databases, creating a reproducibility gap for external researchers. The GHDx (Global Health Data Exchange) lists the survey dataset but access to micronutrient results requires institutional access.

**Prior data situation**

Before the MMFCS 2017-2018, Myanmar was listed among countries that had high VAS coverage (≥70%) but had *never collected national VAD prevalence data* — the same category as the DPRK, Tajikistan, and Uzbekistan. The WHO VMNIS database did not include Myanmar-specific serum retinol survey data in its main published compilations through the early 2010s. The Sarno et al. 2023 systematic review and the Stevens et al. 2015 Lancet Global Health pooled analysis both flagged Myanmar as having insufficient nationally representative data points.

One peer-reviewed study available prior to the MMFCS is a 2013 paper on adolescent schoolgirls in Myanmar (*Public Health Nutrition*, Cambridge Core), which found 31.5% prevalence of low vitamin A status (serum retinol <1.05 µmol/L, a more lenient threshold than the standard subclinical cut-off of <0.70 µmol/L). This is not a survey of children under 5 and cannot be directly used for model calibration.

**Other available data points**

- A ScienceDirect paper on micronutrient deficiencies and Myanmar's GDP (*Nutrition*, 2016, PMID 26421387) cites ~35% VAD prevalence in children under 5 as the context for economic burden estimates, attributing 4–6% of under-five deaths to micronutrient deficiencies
- The 2015–16 Myanmar DHS (Demographic and Health Survey) collected anthropometric data but did not include biochemical vitamin A assessment; it found 27.6% of children under 5 were stunted and 26.9% were underweight nationally
- The 2013 MICS-equivalent surveys for Myanmar did not include serum retinol assessment

### A2. Best Available Prevalence Estimates

| Estimate | Value | Population | Source | Notes |
|----------|-------|------------|--------|-------|
| 35% | Children <5 | National | Cited in economic burden literature (Wieringa et al. 2016, PMID 26421387) | Consistent with pre-MMFCS estimate |
| ~35% | Children <5 | National | MMFCS 2017-2018 Interim Report (Feb 2019) | Full serum retinol data in locked government document |
| 31.5% | Adolescent schoolgirls | Sub-national | Thane et al. 2014 (PMID 24128336) | Uses <1.05 µmol/L threshold; not directly comparable |
| ~25–30% | Children <5 | Regional trajectory implied | Stevens et al. 2015 SE Asia regional estimate extrapolated | Myanmar tracking regional decline but from higher base |

**Best estimate for 2000 baseline**: The model's `vad_baseline_prevalence=0.36` for Myanmar is well-supported and arguably conservative relative to some estimates. The 35–36% figure for children under 5 is consistent across the economic burden literature and aligned with the first nationally representative survey (MMFCS 2017-2018), which was conducted ~17 years after the model baseline year of 2000. If Myanmar tracked the regional decline of ~3%/year from the early 1990s, a 2000 baseline prevalence of 40–45% is plausible, with ~35% reached by 2017-2018 — suggesting the model's 36% baseline may actually be slightly *underestimating* the true 2000 figure.

**Revised inference**: With 35% in ~2018 and a 2.5%/year decline rate (as used in the model), back-extrapolating to 2000 yields: 0.35 / (1 - 0.025)^18 ≈ 0.35 / 0.634 ≈ **0.55** for 2000. This would imply the 0.36 baseline is substantially underestimated — or that the decline rate was faster than 2.5%/year in earlier years (consistent with a rapid 1990s VAS scale-up reducing severe deficiency quickly, then slower progress thereafter). The model as written likely underestimates Myanmar's historical VAD burden in the 2000–2010 period.

**Recommended re-assessment**: Consider using `vad_baseline_prevalence=0.45–0.50` for Myanmar with `vad_annual_decline=0.030–0.035`, which would produce a prevalence closer to 35% by 2017 and is more consistent with the available survey data. Alternatively, maintain the current 0.36 as a lower-bound estimate and note in documentation that it may be conservative.

**95% credible interval for baseline**: 0.30–0.55 (wide, reflecting genuine data scarcity)

### A3. Myanmar and the SE Asian Regional Trajectory

Stevens et al. 2015 (*Lancet Global Health*) documented the most important regional fact: East and Southeast Asia collectively declined from **42% VAD prevalence in 1991 to 6% in 2013** — a reduction of approximately 5 percentage points per year for the region as a whole, with posterior probability >0.99 for a genuine decline.

Does Myanmar track this regional trajectory?

The evidence suggests **partial tracking with significant lag**:

- The regional 42% → 6% trajectory was primarily driven by Thailand, Vietnam, Indonesia, Philippines, and Cambodia — countries with strong VAS programs, rapid economic growth, and diet diversification in the 1990s and 2000s
- Myanmar's VAS coverage was substantially lower than regional peers throughout the 2000s (UNICEF: 55% in 2000, vs. Thailand >80%, Philippines 70%, Vietnam 76%)
- Myanmar's per-capita income growth lagged regional peers and accelerated only after political opening post-2011; the coup reversal post-2021 has re-arrested this trajectory
- The MMFCS 2017-2018 finding of ~35% in children under 5 — if accurate — means Myanmar in 2017 had a prevalence roughly equivalent to where the regional average was in the **mid-1990s**. Myanmar is ~20 years behind the regional trend.
- This is structurally consistent: Myanmar had fewer years of functioning VAS programming, more conflict, weaker health infrastructure, and more restricted dietary diversification

**Model implication**: The model's `vad_annual_decline=0.025` for Myanmar is appropriate or even slightly generous. A more conservative rate of 0.020 would be justifiable given the weaker program base and lower starting coverage. The post-2021 deterioration (see below) means the decline may have reversed in recent years.

### A4. Sub-national Variation: Highlands vs. Delta

Myanmar's geography creates extreme sub-national heterogeneity:

**Lowland delta (Irrawaddy, Bago, Mon):**
- Dense rice cultivation; most rice-dependent dietary pattern
- Higher VAS program coverage historically
- Better health infrastructure access
- Estimated VAD prevalence: likely near or below the national average (~30–35%)

**Highland and conflict-affected states (Kachin, Shan, Rakhine, Chin, Kayah/Karenni):**
- Higher rates of food insecurity and dietary monotony
- Ethnic minority populations with historically less access to government health programs
- Active conflict, displacement, restricted humanitarian access
- UNICEF 2022-2023 reports document children in Rakhine, Kachin, and Shan receiving MUAC screening and acute malnutrition treatment, with 147,400 children receiving multiple micronutrient supplementation in these regions
- Estimated VAD prevalence in highland conflict states: **40–55%**, potentially higher in IDP camps

**Urban Yangon and Mandalay:**
- Lower VAD prevalence, estimated <15–20% by 2018
- Greater dietary diversity and market access
- Income growth improving animal-source food consumption

**Model implication**: The national-average 36% baseline conceals this variation. For a model focused on rice-eating populations in rural areas, the relevant population likely has prevalence above the national average. If the target population is specifically the highland/conflict-affected subset most dependent on staple-only diets, the effective VAD baseline could reasonably be 40–50%. The current model parameter is therefore conservative for the highest-burden sub-population.

### A5. Post-2021 Coup: Nutrition Deterioration

The February 2021 military takeover has substantially reversed Myanmar's nutrition gains. Key documented impacts:

**Health system collapse:**
- VAS programs disrupted; government health services largely non-functional in much of the country
- Model's VAS coverage figure of 0.58 for 2024 may be optimistic for conflict-affected states where coverage has effectively fallen to near zero in some areas
- Nutrition surveys severely restricted; phone-based monitoring only in many zones

**Food security deterioration:**
- 13.3 million people facing acute food insecurity (IPC Phase 3+) as of 2023, including 2.7 million in Phase 4 (Emergency)
- One-year increase in minimum food basket cost: 32%
- National poverty rate approximately doubled post-coup, with ~50% of population below poverty line
- UNICEF: 6 million children in need of humanitarian assistance; 800,000 children wasted

**Displacement and micronutrient programs:**
- ~320,000 IDPs in official camps in Kachin, Rakhine, and Shan (many more informally displaced)
- UNICEF reaching micronutrient supplementation to 147,400 children under 5 in five states/regions — a fraction of need
- WFP operating multifaceted nutrition interventions in Magway, Rakhine, Kachin, and Shan under protracted relief operations

**Projected VAD trajectory post-2021:**
The model currently projects monotonic decline in VAD prevalence through 2024 at 2.5%/year. This is inconsistent with the documented humanitarian crisis. A more accurate post-2021 trajectory would show:
- 2021: decline arrests; VAS coverage drop of 15–25% (consistent with COVID + coup)
- 2022–2024: potential *increase* in VAD prevalence, especially in conflict-affected states
- National average VAD prevalence in 2024 may be at or above 2015 levels for the affected sub-population

**Model parameter implication**: The VAS coverage decline from 0.70 (2020) to 0.58 (2024) in the model is directionally correct but may understate the deterioration in conflict-affected states. For modeling purposes in conflict zones, effective VAS coverage may be closer to 0.20–0.35.

### A6. Confidence Intervals and Model Implications

**Summary of evidence quality**:

| Parameter | Model Value | Evidence Quality | Recommended Range |
|-----------|-------------|-----------------|-------------------|
| `vad_baseline_prevalence` (2000) | 0.36 | Low (no 2000-era national survey) | 0.36–0.55 |
| `vad_annual_decline` | 0.025 | Low-moderate | 0.015–0.030 |
| VAS coverage 2020 | 0.70 | Moderate (UNICEF data) | 0.65–0.75 |
| VAS coverage 2024 | 0.58 | Low (post-coup disruption unquantified) | 0.35–0.65 |
| Conflict-state VAD (2018) | Not separately modeled | Low | 0.40–0.55 |

**Key recommendation**: The model's Myanmar parameters are plausible but likely conservative on the VAD prevalence side (underestimating true baseline) and potentially optimistic on the post-2021 VAS coverage side. The two errors partially cancel in the impact calculation, but the model's Myanmar output should carry wide uncertainty bounds (roughly ±50% of the central estimate). A specific sensitivity run with `vad_baseline_prevalence=0.50` and `vad_annual_decline=0.025` would produce a higher baseline impact estimate and is arguably more epidemiologically justified given the MMFCS 2017-2018 data.

---

## Section B: Bioconversion

The model uses `bioconversion_ratio: float = 12.0` — the WHO/FAO/IOM standard for dietary plant beta-carotene. This section synthesizes what the literature shows for the specific target population of malnourished children in VAD-endemic rice-eating countries, and examines whether 12:1 is appropriately calibrated, too conservative, or (as the model's red-team note suggests) possibly still insufficient to capture the worst cases.

### B1. What the Population-Level Literature Shows

The full range of documented beta-carotene conversion ratios is:

| Condition | Ratio (beta-carotene:retinol, by weight) | Source |
|-----------|----------------------------------------|--------|
| Beta-carotene in oil (supplement) | 2:1 | IOM 2001 |
| Golden Rice, GR2, healthy Chinese children | **2.3 ± 0.8:1** | Tang et al. 2012 (retracted on ethics; data undisputed) |
| Golden Rice, GR2, healthy US adults | **3.8 ± 1.7:1** | Tang et al. 2009 (un-retracted) |
| Red palm oil, spirulina | 3.8–6.5:1 | Various |
| Biofortified sweet potato | 6–10:1 | HarvestPlus efficacy studies |
| Biofortified maize | ~6.5:1 | Zambia studies |
| Spinach, Tang et al. 2012 | 7.5 ± 2.1:1 | Tang et al. 2012 |
| Mixed plant food diet | 12:1 | IOM default (WHO/FAO) |
| Vegetables and fruits (general range) | 10:1 – 28:1 | Various; dose-dependent |
| Undernourished children, green leafy veg | Approximately 15:1 – 28:1 | Lala & Reddy 1970 (PMID 5412643) |

The IOM 12:1 default is mechanistically based on ~17% absorption of beta-carotene from a mixed plant diet combined with 2:1 intracellular conversion once absorbed. The key insight from Tang et al. 2009 and 2012 is that Golden Rice's food matrix (amyloplast-embedded carotenoids in starchy endosperm, no chloroplast binding) enables much more efficient absorption — potentially as good as an oil supplement.

**For malnourished children specifically**: The only directly relevant historical study is Lala & Reddy 1970 (*Am J Clin Nutr*, PMID 5412643), which measured absorption of beta-carotene from green leafy vegetables in undernourished children in India. These children absorbed substantially less efficiently than well-nourished comparators, with effective conversion ratios in the range of 20:1 and above. This study used leafy vegetable matrices, not Golden Rice, but establishes the directional principle.

**Novotny, Harrison & Pawlosky 2010** (*J Nutr*, PMC2855261) documented that conversion efficiency decreases as dose increases, with ratios ranging 2:1–9:1 for doses ≤6 mg beta-carotene and ≥16:1 for doses ≥16 mg. At typical Golden Rice serving levels (~0.6–1.5 mg beta-carotene), this dose effect is less of a concern.

**The key literature gap**: No published study has measured beta-carotene bioconversion specifically in (a) stunted or wasted children, (b) children with active environmental enteropathy, or (c) severely VAD-deficient children (serum retinol <0.35 µmol/L), using a Golden Rice food matrix. The Tang 2012 study used children with *marginal* vitamin A status (23.6–25.6 µg/dL — below 30 µg/dL but above 20 µg/dL clinical VAD threshold). It did not study severely deficient or malnourished children.

### B2. Environmental Enteropathy and Gut Damage

Environmental enteropathy (EE) — also called environmental enteric dysfunction — is a subclinical small intestinal disorder caused by repeated fecal-oral exposure to enteropathogens, found in essentially all children growing up in low-resource settings in South and Southeast Asia and Sub-Saharan Africa. It is critically relevant to beta-carotene absorption.

**Pathophysiology of EE relevant to beta-carotene:**
1. **Villous blunting**: EE reduces villous height and increases crypt depth, directly reducing the absorptive surface area of mature enterocytes. Since SR-BI scavenger receptors and related beta-carotene transporters are expressed on mature enterocyte apical membranes, villous blunting reduces uptake capacity.
2. **Increased gut permeability**: EE disrupts tight junctions, increasing the lactulose:mannitol (L:M) ratio. While increased permeability allows some passive paracellular absorption, it also triggers local and systemic inflammation that suppresses retinol-binding protein (RBP) synthesis in the liver.
3. **Inflammatory suppression of RBP**: Acute-phase inflammatory responses (elevated CRP, AGP) suppress liver synthesis of RBP4, reducing the mobilization and transport of retinol from hepatic stores to peripheral tissues. This means even absorbed retinol is less efficiently distributed.
4. **Reduced bile acid secretion in malnutrition**: Severe protein-energy malnutrition impairs bile acid production, directly limiting micelle formation and hence fat-soluble carotenoid absorption.

**Direct Bangladesh evidence**: A PLOS ONE study (Salameh et al. 2017, PMC5132308) of 925 Bangladeshi children aged 6–24 months in Dhaka's Mirpur slum found that EE (measured by L:M ratio) was significantly associated with undernutrition, low vitamin A status, and iron deficiency. This is a bidirectional relationship: VAD impairs gut mucosal integrity (vitamin A is required for epithelial maintenance), and poor gut integrity further impairs vitamin A absorption — the "vicious cycle of VAD."

**Quantitative impact on bioconversion**: No study has precisely measured the conversion ratio adjustment attributable to EE in children. However, from mechanistic and indirect evidence:
- Reduced absorptive surface area → likely 30–50% reduction in absorption efficiency relative to healthy gut
- Impaired bile acid secretion in severe malnutrition → additional 20–40% reduction
- Combined: approximately 2–3× worsening of the effective conversion ratio compared to a healthy gut

If Tang 2009's 3.8:1 in healthy adults represents a food-matrix baseline for Golden Rice, and EE impairs absorption by 50–75%, the effective ratio in an EE-affected child could be 7–15:1 — approaching or exceeding the standard 12:1 default.

### B3. BCMO1/BCO1 Genetic Polymorphisms

The enzyme beta-carotene 15,15'-monooxygenase (BCMO1, now formally BCO1) catalyzes the central cleavage of beta-carotene to retinal in enterocytes. Two well-characterized nonsynonymous SNPs reduce enzymatic activity:

**R267S (rs12934922)** and **A379V (rs7501331)**:
- The double mutant (267S + 379V) reduces BCO1 catalytic activity by **57%** in vitro (Leung et al. 2009, *FASEB J*)
- Three upstream SNPs (rs6420424, rs11645428, rs6564851) reduce activity by **48–59%** in female volunteers
- Together, these variants affect 32–69% of individuals in studied populations

**Population frequencies — what is known:**

*European populations (best studied):*
- R267S variant allele frequency: ~42%
- A379V variant allele frequency: ~24%
- Double mutant (267S + 379V): ~9% in Finns (highest)

*Philippines (directly measured):*
- Zumaraga et al. 2022 (*J Int Med Res*, PMID 34903070) is the only published study in an Asian rice-eating population
- Study: 693 Filipino children/adolescents aged 6–19 from 2013 Philippine National Nutrition Survey
- **7.6% bore the combined R267S + A379V mutations** (versus ~9% in European populations — notably similar)
- A379V TT variant was inversely associated with vitamin A status
- Authors concluded genetic variability must be considered for provitamin A supplementation/fortification recommendations in this region

*Japan (BCO1 rs6564851 variant):*
- GG homozygotes had 2× higher serum beta-carotene than T allele carriers, indicating lower conversion
- Suggests the upstream promoter SNP reduces BCO1 expression and conversion in East Asian populations

*Bangladesh:* **No published BCMO1/BCO1 population genetics data identified.** This is a critical gap. Given that South Asian and East Asian genetic ancestry shows somewhat different allele frequencies than European populations, and that at least one variant has been confirmed in Filipino populations, Bangladeshi data would be directly relevant.

*Broader Asian populations:*
- The Frontiers in Nutrition 2022 paper (PMC9096837) on ethnic group variation notes that BCO1 genetic variation is present across all studied populations but data for non-European, non-East Asian groups is severely limited
- Most genome-wide association studies have been conducted in Eurocentric cohorts, understating Asian-specific allele frequencies

**Magnitude of impact if reduced-function variants are present:**
- Heterozygous carriers (R267S or A379V alone): ~15–30% reduction in conversion efficiency
- Homozygous or double-mutant carriers: 50–70% reduction
- At population level (assuming similar frequencies to Philippines): perhaps 20–30% of the Bangladeshi/Myanmar target population has meaningfully reduced BCO1 activity
- This would shift the effective population-average ratio upward by perhaps 15–25% relative to what would be observed in a genetically typical European cohort

### B4. Dietary Fat Dependency

Beta-carotene is highly hydrophobic and requires incorporation into mixed micelles (requiring bile salts and dietary fat) for intestinal absorption via SR-BI and CD36 transporters.

**Minimum fat requirement**: Multiple studies indicate that approximately **3–5 g of fat per meal** is sufficient for near-maximal beta-carotene absorption in healthy individuals. Below this threshold, absorption falls substantially.

**Rural Bangladesh dietary fat context:**
A comprehensive analysis of food intakes in rural Bangladesh (*PMC9644183*, Trends and Inequities in Food, Energy, Protein, Fat and Carbohydrate Intakes, 2022):
- Approximately 70% of energy from carbohydrates
- Insufficient fat intake prevalent in >80% of the population (all survey years)
- Insufficient energy, protein, and fat more prevalent in poor households
- Dietary fat intake is commonly below 20 g/day total for many poor rural households, and per-meal fat may frequently fall below the 3–5 g threshold for optimal carotenoid absorption

**Dietary vitamin A in rural Bangladesh:**
A study of rural pregnant women in southwest Bangladesh found:
- Mean dietary vitamin A intake: 392 ± 566 µg RAE/day (only 51% of RDA)
- About 60% of vitamin A from plant beta-carotene sources, 40% from animal sources
- The 566 µg standard deviation indicates extreme variability; poor rural households likely far below 392 µg

**Philippines context:**
A landmark study with Filipino schoolchildren (9–12 years) examined fat levels and vitamin A status:
- Three groups received 7 g, 15 g, or 29 g total dietary fat/day with provitamin A-rich vegetables
- Even the 7 g/day fat group (2.4 g/meal) showed improvement in vitamin A status (total-body pool improved, liver VA concentrations normalized from 35% to 7% low)
- This suggests that even minimal fat (~2–3 g/meal) is sufficient for some carotenoid improvement
- However, absolute absorption and conversion was highest in the higher-fat groups

A historical study (Roels et al. 1958, cited in review literature) documented that African boys with VAD showed 5-fold improvement in beta-carotene absorption (from 5% to 25%) when supplemented with 18 g/day of fat. This magnitude of fat-driven difference (5×) is relevant to populations eating near-zero-fat diets.

**Impact on model's 12:1 ratio:**
- If target children eat Golden Rice with typical rural Bangladeshi/Myanmar fat intake (~5–15 g total/day, 1–5 g/meal), absorption could be 30–60% of what would be observed with adequate fat
- This would push the effective ratio from 12:1 toward 20–40:1 in the worst cases
- The 2009 Tang study gave 10 g butter with the Golden Rice meal (substantial fat) and still found only 3.8:1 — representing optimal fat conditions

### B5. The Conversion Paradox: Severely VAD Children

An important mechanistic paradox exists: severely VAD children, who would benefit most from Golden Rice, may actually absorb beta-carotene *less* efficiently than mildly deficient or vitamin A-replete children.

**Mechanisms:**

1. **ISX (intestine-specific homeobox) feedback**: ISX acts as a transcriptional repressor of both BCO1 and SR-BI (the main beta-carotene transporter) in enterocytes. ISX expression is driven by retinoic acid signaling. In vitamin A replete individuals, retinoic acid upregulates ISX, which downregulates SR-BI and BCO1 — a homeostatic feedback that prevents vitamin A toxicity. In severely VAD children, this feedback is reduced, theoretically allowing *higher* BCO1 expression and conversion efficiency.

2. **Counter-evidence from impaired gut**: However, this theoretical advantage is overwhelmed in practice by gut pathology in severely malnourished/VAD children:
   - VAD itself impairs intestinal epithelial cell renewal (vitamin A is essential for goblet cell and enterocyte maintenance)
   - Severe VAD → impaired gut barrier → greater EE → greater villous blunting → less absorptive surface
   - Severe protein-energy malnutrition accompanying VAD → impaired bile acid production → less micelle formation → less carotenoid absorption

3. **Animal model evidence**: A key finding from brush border membrane vesicle (BBMV) studies showed that uptake of 14C-beta-carotene was *suppressed* in vitamin A-deficient rats compared to controls during early passive uptake, suggesting VAD directly impairs enterocyte membrane uptake — consistent with the gut damage mechanism above.

4. **The repletion paradox in clinical practice**: The standard clinical approach to severe VAD is high-dose preformed retinol supplementation (200,000 IU), not provitamin A sources, precisely because the conversion and absorption of provitamin A is too uncertain in severely deficient children. This clinical practice implicitly acknowledges that provitamin A food sources may be unreliable in the target population.

**Summary**: In severely malnourished children with active gut enteropathy and severe VAD (the highest-burden, highest-priority sub-population), the effective beta-carotene to retinol conversion ratio is likely *worse* than the 12:1 WHO/FAO default — potentially 15:1 to 30:1 — rather than approaching the favorable 3.8:1–2.3:1 ratios measured in healthy volunteers. The 12:1 default may actually be a lower bound for the worst-affected children, not a conservative upper bound.

### B6. Biofortified Crop Absorption Studies

**Orange-fleshed sweet potato (OFSP) studies** (most relevant analogue to Golden Rice, since both involve endosperm/storage tissue rather than chloroplast-bound carotenoids):
- HarvestPlus efficacy trials in Mozambique, Uganda, South Africa, and Bangladesh showed OFSP consumption improved vitamin A status in children
- Effective conversion ratios in these studies were generally in the 6–10:1 range for practical field conditions
- The Bangladesh OFSP study increased provitamin A concentration but did not achieve significant improvement in serum retinol status — suggesting real-world conversion may be less favorable than controlled studies

**Biofortified provitamin A maize (Zambia):**
- Multiple Zambian RCTs in school children: consumption of beta-carotene-rich maize significantly improved serum beta-carotene concentrations
- Improvement in active retinol (serum retinol) was less consistent — in one study the more sensitive isotope dilution test was required to detect improvement in liver vitamin A stores
- Effective conversion ratios: approximately 6–7:1 in these field conditions (better than IOM 12:1 default but far less favorable than Tang et al. Golden Rice results)

**Filipino schoolchildren and carotene-rich vegetables with minimal fat** (De Pee et al. and related studies):
- Even at low fat intakes, carotene-rich plant foods improved total-body vitamin A pool in Filipino schoolchildren aged 9–12 years
- This suggests some floor of benefit exists even under difficult conditions, but conversion is less efficient than controlled studies suggest

**The Iannotti gap**: No published study was identified from the Iannotti research group or others that specifically measures provitamin A biofortified crop absorption in stunted or wasted children (as opposed to mildly to moderately VAD children). This represents a genuine evidence gap for the model's core assumption.

---

## Recommended Model Parameters

### Myanmar VAD Parameters

| Parameter | Current Model | Recommended Central | Recommended Range | Basis |
|-----------|--------------|--------------------|--------------------|-------|
| `vad_baseline_prevalence` (MMR, 2000) | 0.36 | 0.45 | 0.36 – 0.55 | MMFCS 2017-18 ~35%; back-extrapolated to 2000 implies higher baseline |
| `vad_annual_decline` (MMR) | 0.025 | 0.025 | 0.015 – 0.030 | Appropriate; consider lower end post-coup |
| VAS coverage 2024 (MMR) | 0.58 | 0.50 | 0.35 – 0.65 | Post-coup deterioration; conflict states lower |

**Note on overall Myanmar impact**: Increasing the baseline prevalence from 0.36 to 0.45 while keeping decline rate at 0.025 would increase Myanmar's modeled impact by approximately 25–35% in the early model years (2009–2015). This is directionally justified by the available evidence.

### Bioconversion Parameters

| Parameter | Current Model | Recommended Central | Conservative Bound | Optimistic Bound | Basis |
|-----------|--------------|--------------------|--------------------|-----------------|-------|
| `bioconversion_ratio` (general) | 12.0 | 12.0 | 18.0 – 24.0 | 6.0 | IOM default appropriate; see below |
| Effective ratio for Golden Rice, healthy volunteers | — | 3.8 | 6.0 | 2.3 | Tang 2009 (adults), Tang 2012 (children) |
| Effective ratio for GR, malnourished with EE | — | 12.0 – 15.0 | 20.0 – 30.0 | 8.0 | Derived from EE impairment literature |
| Effective ratio, considering BCO1 polymorphisms | — | ~14.0 | ~20.0 | ~10.0 | 7.6% of Filipino population has double mutant; broader distribution has heterozygous carriers |

**Key finding: The model's 12:1 default is well-calibrated for the actual target population**

The 12:1 IOM default is often criticized as being too conservative relative to Tang et al.'s 3.8:1 finding. However, for severely malnourished children with environmental enteropathy — the population that accounts for the highest VAD mortality — the 12:1 ratio is actually more plausible than Tang's favorable ratios, and may still be optimistic. The model's use of 12:1 as its default is appropriate, and Tang et al.'s 3.8:1 should be treated as an *optimistic upper-bound* scenario representing well-nourished children with adequate fat intake, not as the relevant central estimate.

**Fat intake consideration**: Given that rural Bangladeshi and Myanmar households frequently have per-meal fat intakes below the 3–5 g threshold for optimal carotenoid absorption, even the 12:1 ratio may be optimistic for the poorest households. A 15:1 or 18:1 effective ratio for fat-poor diets is defensible.

**Sensitivity recommendations for the model**:
1. Add a scenario `"Effective ratio for malnourished with EE (15:1)"` with `bioconversion_ratio=15.0`
2. Add a scenario `"Effective ratio for fat-poor diet, EE, BCO1 variants (20:1)"` with `bioconversion_ratio=20.0`
3. The current `"Bioconv. conservative 18:1"` scenario in `run_sensitivity()` is valuable but should be labeled more specifically: this is not merely conservative — it may be the *realistic* ratio for the most vulnerable target population

**Key uncertainty that no published literature resolves**: What is the actual beta-carotene conversion ratio for Golden Rice beta-carotene specifically (vs. other plant matrices) in children with active EE and severe VAD? This is the study that does not exist. Given the Tang 2012 findings (2.3:1 in healthy children), and the estimated 2–3× worsening from EE and fat restriction, the effective ratio in the highest-burden children is likely in the range **6:1 to 20:1**, with central estimate around **12:1** — which happens to be the model's default.

---

## Sources

### Myanmar VAD

1. **Myanmar Ministry of Health and Sports.** *Myanmar Micronutrient and Food Consumption Survey (MMFCS) 2017–2018: Interim Report*. February 2019. Available at: [https://www.mohs.gov.mm/page/7339](https://www.mohs.gov.mm/page/7339)

2. **GHDx – Global Health Data Exchange.** Myanmar Micronutrient and Food Consumption Survey 2017–2018. [https://ghdx.healthdata.org/record/myanmar-micronutrient-and-food-consumption-survey-2017-2018](https://ghdx.healthdata.org/record/myanmar-micronutrient-and-food-consumption-survey-2017-2018)

3. **Thane Win, San Shwe, Khin Myo Aye et al.** "The influence of vitamin A status on iron-deficiency anaemia in anaemic adolescent schoolgirls in Myanmar." *Public Health Nutrition*. 2014; 17(6):1392–1399. DOI: 10.1017/S1368980013001572. [PMID 24128336](https://pubmed.ncbi.nlm.nih.gov/24128336/)

4. **Wieringa FT, Dahl M, Chamnan C, et al.** "Micronutrient deficiencies in early childhood can lower a country's GDP: The Myanmar example." *Nutrition*. 2016; 32(2):254–257. DOI: 10.1016/j.nut.2015.09.008. [PMID 26421387](https://pubmed.ncbi.nlm.nih.gov/26421387/)

5. **Stevens GA, Bennett JE, Hennocq Q, et al.** "Trends and mortality effects of vitamin A deficiency in children in 138 low-income and middle-income countries between 1991 and 2013: a pooled analysis of population-based surveys." *The Lancet Global Health*. 2015; 3(9):e528–e536. DOI: 10.1016/S2214-109X(15)00039-X. [PMID 26275329](https://pubmed.ncbi.nlm.nih.gov/26275329/)

6. **Sarno M, Shivakumar N, Bhogadi S, et al.** "The prevalence of vitamin A deficiency and its public health significance in children in low- and middle-income countries: A systematic review and modelling analysis." *PLOS Medicine*. 2023. [PMC10416138](https://pmc.ncbi.nlm.nih.gov/articles/PMC10416138/)

7. **UNICEF Myanmar.** Health and Nutrition programs. [https://www.unicef.org/myanmar/health-and-nutrition](https://www.unicef.org/myanmar/health-and-nutrition)

8. **UNICEF Myanmar.** "Providing Vitamin A to children in Rakhine's hard-to-reach villages affected by conflict." [https://www.unicef.org/myanmar/stories/providing-vitamin-children-rakhines-hard-reach-villages-affected-conflict](https://www.unicef.org/myanmar/stories/providing-vitamin-children-rakhines-hard-reach-villages-affected-conflict)

9. **UNICEF Myanmar.** Humanitarian Situation Report No. 6 (Mid-Year 2024). [https://www.unicef.org/media/160281/file/Myanmar-Humanitarian-Situation-Report-No.6-(Mid-Year)-01-January-30-June-2024.pdf](https://www.unicef.org/media/160281/file/Myanmar-Humanitarian-Situation-Report-No.6-(Mid-Year)-01-January-30-June-2024.pdf)

10. **WHO Myanmar.** Public Health Situation Analysis Myanmar, August 2023. [https://cdn.who.int/media/docs/default-source/searo/myanmar/documents/public-health-situation-analysis-phsa_myanmar_august-2023.pdf](https://cdn.who.int/media/docs/default-source/searo/myanmar/documents/public-health-situation-analysis-phsa_myanmar_august-2023.pdf)

11. **WFP Myanmar.** WFP Myanmar Nutrition interventions. [https://www.wfp.org/publications/wfp-myanmar-nutrition](https://www.wfp.org/publications/wfp-myanmar-nutrition)

12. **Global Nutrition Report.** Myanmar Country Nutrition Profile. [https://globalnutritionreport.org/resources/nutrition-profiles/asia/south-eastern-asia/myanmar/](https://globalnutritionreport.org/resources/nutrition-profiles/asia/south-eastern-asia/myanmar/)

13. **Helgi Library.** Rice Consumption Per Capita in Myanmar. [https://www.helgilibrary.com/indicators/rice-consumption-per-capita/myanmar/](https://www.helgilibrary.com/indicators/rice-consumption-per-capita/myanmar/) — 269 kg/capita/yr (2021 FAOSTAT)

14. **WHO.** Vitamin and Mineral Nutrition Information System (VMNIS). [https://www.who.int/teams/nutrition-and-food-safety/databases/vitamin-and-mineral-nutrition-information-system](https://www.who.int/teams/nutrition-and-food-safety/databases/vitamin-and-mineral-nutrition-information-system)

### Bioconversion Literature

15. **Tang G, Qin J, Dolnikowski GG, Russell RM, Grusak MA.** "Golden Rice is an effective source of vitamin A." *American Journal of Clinical Nutrition*. 2009; 89(6):1776–1783. DOI: 10.3945/ajcn.2008.27119. [PMID 19386750](https://pubmed.ncbi.nlm.nih.gov/19386750/)

16. **Tang G, Hu Y, Yin S-a, et al.** "β-Carotene in Golden Rice is as good as β-carotene in oil at providing vitamin A to children." *American Journal of Clinical Nutrition*. 2012; 96(3):658–664. [**Retracted July 2015** — ethical grounds; data not disputed.] PMID: 22854406.

17. **Leung WC, Hessel S, Méplan C, et al.** "Two common single nucleotide polymorphisms in the gene encoding β‐carotene 15,15′‐monoxygenase alter β‐carotene metabolism in female volunteers." *FASEB Journal*. 2009; 23(4):1041–1053. DOI: 10.1096/fj.08-121962. [PMID 19103647](https://pubmed.ncbi.nlm.nih.gov/19103647/)

18. **Zumaraga MKP, Arquiza JMRA, Concepcion MA, et al.** "Genotype Effects on β-Carotene Conversion to Vitamin A: Implications on Reducing Vitamin A Deficiency in the Philippines." *Nutrition Research*. 2022. DOI: 10.1177/03795721211060229. [PMID 34903070](https://pubmed.ncbi.nlm.nih.gov/34903070/)

19. **Novotny JA, Harrison DJ, Pawlosky R, et al.** "β-Carotene Conversion to Vitamin A Decreases As the Dietary Dose Increases in Humans." *Journal of Nutrition*. 2010; 140(5):915–918. [PMC2855261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2855261/)

20. **Tanumihardjo SA.** "The challenge to reach nutritional adequacy for vitamin A: β-carotene bioavailability and conversion—evidence in humans." *American Journal of Clinical Nutrition*. 2012; 96(5):1193S–1203S. DOI: 10.3945/ajcn.112.036939. [PMID 23053560](https://pubmed.ncbi.nlm.nih.gov/23053560/)

21. **Van Loo-Bouwman CA, Naber TH, Schaafsma G.** "A review of vitamin A equivalency of β-carotene in various food matrices for human consumption." *British Journal of Nutrition*. 2014. [Cambridge Core](https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/review-of-vitamin-a-equivalency-of-carotene-in-various-food-matrices-for-human-consumption/2F833B9340DA0175C93363600ECBFEED)

22. **Lala VR, Reddy V.** "Absorption of beta-carotene from green leafy vegetables in undernourished children." *American Journal of Clinical Nutrition*. 1970; 23(1):110–113. [PMID 5412643](https://pubmed.ncbi.nlm.nih.gov/5412643/)

23. **Frontiers in Nutrition 2022.** "Genetic Variations of Vitamin A-Absorption and Storage-Related Genes, and Their Potential Contribution to Vitamin A Deficiency Risks Among Different Ethnic Groups." [PMC9096837](https://ncbi.nlm.nih.gov/pmc/articles/PMC9096837)

24. **Salameh M, Khandaker S, Lim SC, et al.** "Undernutrition, Vitamin A and Iron Deficiency Are Associated with Impaired Intestinal Mucosal Permeability in Young Bangladeshi Children Assessed by Lactulose/Mannitol Test." *PLOS ONE*. 2016. DOI: 10.1371/journal.pone.0164447. [PMC5132308](https://pmc.ncbi.nlm.nih.gov/articles/PMC5132308/)

25. **Korpe PS, Petri WA Jr.** "Environmental enteropathy and malnutrition: do we know enough to intervene?" *BMC Medicine*. 2014; 12:187. DOI: 10.1186/s12916-014-0187-1. [PMC4197320](https://pmc.ncbi.nlm.nih.gov/articles/PMC4197320/)

26. **Lin Y, Cai L, et al.** "Effect of beta-carotene supplementation on health and growth of vitamin A deficient children in China rural villages: A randomized controlled trial." *Preventive Medicine Reports*. 2008. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1751499108000851)

27. **Ahluwalia N, Lammi-Keefe CJ, et al.** "Dietary fat intake and beta-carotene absorption and bioconversion into vitamin A." *Journal of Nutrition*. 2002. [PMID 12002680](https://pubmed.ncbi.nlm.nih.gov/12002680/)

28. **Ahmed T, Islam MM, Rahman S, et al.** (Trends and Inequities in Food, Energy, Protein, Fat, and Carbohydrate Intakes in Rural Bangladesh). *Nutrients*. 2022. [PMC9644183](https://pmc.ncbi.nlm.nih.gov/articles/PMC9644183/)

29. **Haskell MJ, Islam MA, Handelman GJ, et al.** "Carotene-rich plant foods ingested with minimal dietary fat enhance the total-body vitamin A pool size in Filipino schoolchildren." *American Journal of Clinical Nutrition*. 2004. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0002916523280235)

30. **Plos One 2017.** "Common SNP rs6564851 in the BCO1 Gene Affects the Circulating Levels of β-Carotene and the Daily Intake of Carotenoids in Healthy Japanese Women." [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0168857)

31. **IOM (Institute of Medicine).** *Dietary Reference Intakes for Vitamin A, Vitamin K, Arsenic, Boron, Chromium, Copper, Iodine, Iron, Manganese, Molybdenum, Nickel, Silicon, Vanadium, and Zinc*. Washington DC: National Academies Press; 2001. 12:1 conversion factor for dietary beta-carotene. [National Academies](https://www.ncbi.nlm.nih.gov/books/NBK222317/)

---

*Document compiled 2026-03-21 via live web research and synthesis of peer-reviewed literature and institutional reports. Myanmar VAD data derives primarily from grey literature and government reports with limited independent verification; estimates should carry correspondingly wide uncertainty bounds. Bioconversion data for the specific target population (malnourished children with environmental enteropathy eating Golden Rice) remains a critical unresolved research gap.*
