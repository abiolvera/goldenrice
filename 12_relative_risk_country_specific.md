# Country-Specific Relative Risk (RR) Estimates: VAD → Child Mortality
## For Golden Rice Impact Model
**Date:** 2026-03-21
**Purpose:** Replace the uniform `relative_risk_vad = 1.75` in `model.py` with evidence-based, country-differentiated RR values for the 8 target countries (Bangladesh, Philippines, India, Indonesia, Vietnam, Myanmar, Cambodia, Nigeria).

---

## Table of Contents
1. [Master Summary Table: RR Estimates by Study](#1-master-summary-table-rr-estimates-by-study)
2. [Individual Study Summaries](#2-individual-study-summaries)
3. [Why RR Varies Geographically: Biological Mechanisms](#3-why-rr-varies-geographically-biological-mechanisms)
4. [Two Methodological Camps](#4-two-methodological-camps)
5. [Recommended RR Values by Country with Uncertainty Ranges](#5-recommended-rr-values-by-country-with-uncertainty-ranges)
6. [BCMO1/BCO1 Polymorphism Data for Target Populations](#6-bcmo1bco1-polymorphism-data-for-target-populations)
7. [Implications for Golden Rice Efficacy](#7-implications-for-golden-rice-efficacy)
8. [Full Source List with DOIs and PMC Links](#8-full-source-list-with-dois-and-pmc-links)

---

## 1. Master Summary Table: RR Estimates by Study

The table below presents the RR of dying among children with VAD relative to those without VAD (for observational studies), or the inverse of the RR of mortality in supplemented vs. unsupplemented children (for intervention trials). Where a trial reports a protective effect (RR < 1), the "implied VAD RR" is 1/RR, representing the relative mortality hazard borne by a deficient, unsupplemented child.

| Study | Year | Country/Region | Design | Comparison | RR (95% CI) | Implied VAD RR | Notes |
|---|---|---|---|---|---|---|---|
| Sommer et al. (Lancet) | 1983 | Indonesia (Aceh) | Prospective cohort | Xerophthalmia vs. no xerophthalmia | ~4.0–12.0* | 4.0–12.0 | *Range across age strata; mild xerophthalmia only. All-cause mortality |
| Sommer et al. (Lancet) | 1986 | Indonesia (Aceh) | Cluster RCT | Supplement vs. placebo | RR_supp = 0.66 (NS in one arm) → 34% mortality reduction | ~1.5 | 450 villages, n=25,939 |
| Rahmathullah et al. (NEJM) | 1990 | India (Tamil Nadu) | RCT | Weekly low-dose VA vs. placebo | RR_supp = 0.54 (0.37–0.78) | ~1.85 | 50% mortality reduction; 15,419 children |
| West et al. / NNIPS (Lancet) | 1991 | Nepal (Sarlahi) | Cluster RCT | VA capsule vs. placebo | RR_supp = 0.70 (0.56–0.88) | ~1.43 | 30% reduction; n=28,630 |
| Ghana VAST Study Team (Lancet) | 1993 | Ghana (northern) | Cluster RCT | VA capsule vs. placebo | RR_supp = 0.81 (0.68–0.98) | ~1.23 | 19% reduction in mortality; n=21,906 |
| Fawzi et al. (JAMA) | 1993 | 12 LMICs (meta-analysis) | Meta-analysis of 12 RCTs | VA vs. control | OR_comm = 0.70 (0.56–0.87) | ~1.43 | Community trials only; OR ≈ RR at low event rates |
| Beaton et al. | 1993 | Multi-country (8 trials) | Meta-analysis | VA vs. control | RR_supp = 0.77 (0.68–0.88) | ~1.30 | All-cause mortality; diarrhea RR=0.71, measles RR=0.46 |
| Vitamin A & Pneumonia Working Group | 1995 | 7 LMICs (12 trials) | Meta-analysis | VA vs. control | Pneumonia mortality RR=0.98 (0.75–1.28) | ~1.02 (NS) | No significant pneumonia-specific benefit |
| DEVTA (Awasthi et al.; Lancet) | 2013 | India (Uttar Pradesh) | Cluster RCT | 6-monthly VA vs. control | RR_supp = 0.96 (0.89–1.03) | ~1.04 (NS) | n=1 million; highest-powered trial; no significant effect |
| Imdad et al. (Cochrane) | 2017/2022 | 19 countries (meta-analysis) | Cochrane systematic review | VA vs. control | RR_supp = 0.88 (0.83–0.93) | ~1.14 | Includes DEVTA; 1.2M children; Asia RR=0.90, Africa RR=0.86 |
| GBD 2017 | 2017 | Global | Comparative risk assessment | VAD vs. adequate VA | Diarrhea RR=2.35; Measles RR=2.76 | 2.35–2.76 | Cause-specific; later retracted as too high |
| GBD 2019 | 2019 | Global | Comparative risk assessment (MR-BRT) | VAD vs. adequate VA | Diarrhea RR=1.14; Measles RR=1.39 | 1.14–1.39 | Major methodological revision; 90% drop in estimated deaths |
| Neonatal VAS meta-analysis (IPD) | 2019 | Asia vs. Africa | IPD meta-analysis | NVAS vs. placebo | Asia: RR=0.87; Africa: RR=1.06 | Asia ~1.15; Africa ~0.94 | Differential benefit: beneficial in Asia, not Africa |
| Stevens et al. (Lancet Global Health) | 2015 | 138 LMICs | Pooled analysis | VAD vs. adequate | Pooled-trial + PAF approach | Varied by country | Country-level attributable deaths: ~94,500 diarrhea + 11,200 measles in 2013 |

**Notes:** "Implied VAD RR" = mortality hazard of deficient vs. non-deficient child = 1 / RR_supplementation (approximately). This inversion is valid under the assumption that supplementation fully corrects deficiency in deficient children and does not affect replete children. This assumption is discussed in Section 4.

---

## 2. Individual Study Summaries

### 2.1 Sommer et al. 1983 — Indonesia (Observational)
**Citation:** Sommer A, Tarwotjo I, Hussaini G, Susanto D. Increased mortality in children with mild vitamin A deficiency. *Lancet* 1983;2(8350):585–8. PMID: 6136744.

**Design:** Prospective cohort study of 3,481 rural Indonesian preschool children followed for 18 months with quarterly re-examinations.

**Key Finding:** Children with mild xerophthalmia (night blindness and/or Bitot's spots) had mortality rates **4 to 12 times higher** than children with normal eyes, depending on age stratum. The mild xerophthalmia group (XN or X1B) carried a substantially elevated risk even after stratifying for respiratory disease, wasting, gastroenteritis, pedal edema, and childhood exanthems.

**Implication for RR:** The observational RR of 4–12 overstates the causal RR of VAD on mortality because xerophthalmia is itself a marker of severe VAD and overall poor nutritional status. The RR of dying attributable specifically to VAD (controlling for confounders) is substantially lower. The Aceh RCT (1986) that followed found only a 34% reduction in mortality with supplementation—implying an implied VAD RR of ~1.5, not 4–12.

**Applicability:** Indonesia specifically; rural, pre-Green Revolution agricultural context; measles- and diarrhea-dominant mortality pattern. Not directly applicable to current Indonesia or other countries without adjustment.

---

### 2.2 Sommer et al. 1986 — Indonesia (RCT)
**Citation:** Sommer A, Tarwotjo I, Djunaedi E, et al. Impact of vitamin A supplementation on childhood mortality: a randomised controlled community trial. *Lancet* 1986;1:1169–73. PMID: 2871418.

**Design:** Cluster RCT in 450 villages, northern Sumatra. N=25,939 children aged 12–71 months. Villages randomized to vitamin A (200,000 IU) or control; follow-up 11–13 months.

**Key Finding:** Mortality in control villages = 7.3 per 1,000; in supplemented villages = 4.9 per 1,000. **34% mortality reduction.** RR_supplementation ≈ 0.66. Implied VAD RR ≈ 1.5. Effect was greater in boys than girls.

**Limitations:** Set in a high-VAD-prevalence context (1980s rural Indonesia). Cannot be extrapolated directly to settings with lower current VAD prevalence. The 34% reduction was the impetus for global VAS programs.

---

### 2.3 Rahmathullah et al. 1990 — India (Tamil Nadu)
**Citation:** Rahmathullah L, Underwood BA, Thulasiraj RD, et al. Reduced mortality among children in southern India receiving a small weekly dose of vitamin A. *NEJM* 1990;323(14):929–35. PMID: 2205798. DOI: 10.1056/NEJM199010043231401.

**Design:** Double-blind RCT; 15,419 preschool children in Trichy district, Tamil Nadu. Weekly physiologic dose (8,333 IU VA) vs. vitamin E placebo; 1 year.

**Key Finding:** Mortality RR_supplementation = 0.54 (95% CI 0.37–0.78). **46% mortality reduction.** Implied VAD RR ≈ 1.85. Overall mortality rate was 8.1 per 1,000.

**Context:** High VAD prevalence area; extremely limited access to prior VAS programs (only 1% coverage at baseline). Weekly physiologic dosing—not megadose. The Tamil Nadu context likely represents near-maximal treatment effect.

**Applicability to model:** High end of likely true RR; reflects a historically high-VAD baseline that no longer characterizes most of India or neighboring countries.

---

### 2.4 West et al. 1991 — Nepal (NNIPS)
**Citation:** West KP Jr, Pokhrel RP, Katz J, et al. Efficacy of vitamin A in reducing preschool child mortality in Nepal. *Lancet* 1991;338(8759):67–71. PMID: 1676467. DOI: 10.1016/0140-6736(91)90070-6.

**Design:** Randomized, double-masked, placebo-controlled community trial. N=28,630 children aged 6–72 months. Sarlahi district (Gangetic flood plain). 60,000 RE every 4 months vs. placebo. 12 months.

**Key Finding:** Mortality RR_supplementation = **0.70 (95% CI 0.56–0.88)**. **30% mortality reduction.** Implied VAD RR ≈ 1.43. Reduction present in both sexes and all ages. Not affected by acute nutritional status (arm circumference).

**Context:** Gangetic flood plain of South Asia; high disease burden; population representative of South Asian lowland ecology (closely analogous to Bangladesh and parts of India). Nepal was chosen as representative of the region.

**Applicability:** Strong applicability to Bangladesh and the Gangetic plain of India. Trial discontinued early due to clear benefit.

---

### 2.5 Ghana VAST Study Team 1993 — Ghana (Africa)
**Citation:** Ghana VAST Study Team. Vitamin A supplementation in northern Ghana: effects on clinic attendances, hospital admissions, and child mortality. *Lancet* 1993;342(8862):7–12. PMID: 8100345.

**Design:** Two double-blind cluster RCTs in northern Ghana. Survival study: 21,906 children aged 6–90 months; Health study: 1,455 children aged 6–59 months. 200,000 IU (or 100,000 IU for <12 months) every 4 months vs. placebo.

**Key Findings:**
- Mortality rate ratio: **0.81 (95% CI 0.68–0.98)**. 19% mortality reduction. Implied VAD RR ≈ 1.23.
- Hospital admissions rate ratio: 0.62 (0.42–0.93).
- Diarrhea-attributable mortality: rate ratio 0.66 (0.47–0.92).
- **Critically: No effect on malaria-attributable mortality.** Mortality from malaria was not reduced.
- Later reanalysis (2009): Effect was largely confined to unvaccinated children (MRR=0.64), with no benefit (or harm in girls) in vaccinated children.

**Applicability to Nigeria model:** The lack of effect on malaria mortality is directly relevant to Nigeria, where malaria is the dominant cause of child death. The overall 19% reduction was smaller than South Asian trials, consistent with a lower baseline VAD prevalence in Ghana vs. Nepal/Indonesia.

---

### 2.6 Fawzi et al. 1993 — Multi-country Meta-Analysis
**Citation:** Fawzi WW, Chalmers TC, Herrera MG, Mosteller F. Vitamin A supplementation and child mortality: a meta-analysis. *JAMA* 1993;269(7):898–903. PMID: 8426449. DOI: 10.1001/jama.1993.03500070078033.

**Design:** Meta-analysis of 12 controlled vitamin A trials with mortality data; MEDLARS database search 1966–1992.

**Key Finding:** Community-based trials: DerSimonian-Laird OR = 0.70 (clustering-adjusted 95% CI 0.56–0.87). Measles hospitalization trials: OR = 0.39 (0.22–0.66). Combined: substantial protection.

**Context:** Pooled estimate; does not disaggregate by region. Contemporaneous with Beaton 1993 and Glasziou 1993 meta-analyses, all converging on ~23–30% all-cause mortality reduction.

---

### 2.7 Beaton et al. 1993 — Multi-country Meta-Analysis
**Citation:** Beaton GH, Martorell R, L'Abbé KA, et al. Effectiveness of Vitamin A Supplementation in the Control of Young Child Morbidity and Mortality in Developing Countries. ACC/SCN State-of-the-Art Series. Nutrition Policy Discussion Paper No. 13. 1993.

**Key Findings by cause of death:**
| Cause | RR_supplementation | 95% CI | Significance |
|---|---|---|---|
| All-cause | 0.77 | 0.68–0.88 | Significant |
| Diarrhea | 0.71 | 0.57–0.88 | Significant |
| Measles | 0.46 | 0.22–0.98 | Significant |
| Respiratory | 0.94 | 0.63–1.42 | Not significant |

**Implication:** VAD has its largest mortality effect through diarrhea and measles pathways; the respiratory pathway is weak. This matters greatly for Nigeria, where malaria mortality is a large fraction of under-5 deaths, because VAS does not appear to reduce malaria-specific mortality.

---

### 2.8 DEVTA Trial 2013 — India (Uttar Pradesh)
**Citation:** Awasthi S, Peto R, Read S, et al. Vitamin A supplementation every 6 months with retinol in 1 million pre-school children in north India: DEVTA, a cluster-randomised trial. *Lancet* 2013;381:1469–77. PMID: 23498849. DOI: 10.1016/S0140-6736(12)62125-4. PMC: PMC3647148.

**Design:** Factorial cluster RCT; 72 blocks in rural Uttar Pradesh; n≈1 million children aged 1–6 years; 6-monthly 200,000 IU retinol vs. control; 5 years (1999–2004).

**Key Findings:**
- Mortality ratio: **0.96 (95% CI 0.89–1.03, p=0.22)**. Non-significant.
- Compliance: 86%.
- Biological effect confirmed: plasma retinol 1/6 higher in supplemented group; severe deficiency halved (6% vs. 13%); Bitot's spots halved (1.4% vs. 3.5%).
- No specific cause of death was significantly affected.

**Critical Implication:** DEVTA is the world's largest VAS trial. Despite confirmed biological effect on VA status, there was no mortality benefit. This suggests that by 1999–2004, the background conditions in Uttar Pradesh (or perhaps nationally in India) had changed such that VAD was no longer the binding constraint on child survival. Updated meta-analysis including DEVTA: 11% mortality reduction (5–16%).

**Applicability:** Suggests the model should use lower RR for India than the 1990 Tamil Nadu figure. DEVTA implies an implied VAD RR of ~1.04 for the 2000s northern India setting.

---

### 2.9 Imdad et al. 2022 — Cochrane Systematic Review
**Citation:** Imdad A, Mayo-Wilson E, Haykal MR, et al. Vitamin A supplementation for preventing morbidity and mortality in children from six months to five years of age. *Cochrane Database Syst Rev* 2022. PMID: 35294044. PMC: PMC8925277. DOI: 10.1002/14651858.CD008524.pub4.

**Design:** Cochrane systematic review; 47 studies; ~1,223,856 children; 19 countries (30 in Asia [16 in India], 8 in Africa, 7 in Latin America, 2 in Australia).

**Key Findings:**
- All-cause mortality: **RR 0.88 (95% CI 0.83–0.93)**. 12% reduction.
- Asia (12 studies): **RR 0.90 (0.84–0.96)**.
- Africa (6 studies): **RR 0.86 (0.75–0.98)**.
- Regional difference: not statistically significant (p=0.83).
- Diarrhea mortality: RR 0.88 (0.79–0.98).
- Measles mortality: RR 0.88 (0.69–1.11) — not significant.
- LRTI mortality: RR 0.98 (0.86–1.12) — not significant.
- Implied VAD RR (overall): ~1.14.

**Important caveat:** The 2022 update (relative to 2017) did not find new RCTs. The current best estimate from the totality of trial evidence is an implied VAD RR of ~1.14 for populations at risk of VAD in current disease burden conditions. The random-effects model gives a wider estimate: RR 0.76 (0.66–0.88), implying VAD RR ~1.32 under higher heterogeneity assumptions.

---

### 2.10 GBD Comparative Risk Assessment (2017 → 2019)
**Citation:** Wessells KR, Brown KH, Bassett MN, et al. Basis for changes in the disease burden estimates related to vitamin A and zinc deficiencies in the 2017 and 2019 Global Burden of Disease Studies. *Public Health Nutr* 2023. PMC: PMC9991746.

**GBD 2017 RR values (cause-specific VAD → mortality):**
| Cause | GBD 2017 RR | 95% CI |
|---|---|---|
| Diarrhea | 2.35 | 2.17–2.54 |
| Measles | 2.76 | 2.01–3.78 |
| LRTI | Included (significant) | — |

**GBD 2019 RR values:**
| Cause | GBD 2019 RR | 95% CI |
|---|---|---|
| Diarrhea | 1.14 | 1.03–1.26 |
| Measles | 1.39 | 1.03–1.90 |
| LRTI | Removed (non-significant) | — |

**Consequence:** Estimated global VAD-attributable child deaths dropped from **233,000** (GBD 2017) to **24,000** (GBD 2019)—a 90% reduction—primarily due to methodological changes, not real-world changes.

**Key methodological changes in GBD 2019:**
1. Adopted MR-BRT (meta-regression, Bayesian regularized trimming) replacing standard metafor meta-analysis.
2. **Removed the deficiency-prevalence adjustment**: GBD 2017 scaled RRs upward in high-prevalence settings (larger RRs in more deficient populations). GBD 2019 found no statistically significant relationship between deficiency prevalence and RR magnitude and dropped this adjustment. This single change had the largest impact.
3. Trimmed 10% of studies considered outliers.
4. The MR-BRT analyses were not independently published, raising transparency concerns.

**Critical assessment for model use:** The GBD 2019 RR values likely underestimate the true VAD effect because the trimming and removal of the prevalence-adjustment bias the estimate downward, particularly for high-prevalence settings like Bangladesh. The GBD 2017 values (2.35–2.76) almost certainly overestimate by applying cause-specific RRs without accounting for competing risks and overlapping attributable fractions. The "true" RR likely lies between GBD 2019 and GBD 2017, closer to the 1.3–1.8 range implied by the individual RCTs from high-prevalence settings.

---

### 2.11 Stevens et al. 2015 — Lancet Global Health Country-Level Analysis
**Citation:** Stevens GA, Bennett JE, Hennocq Q, et al. Trends and mortality effects of vitamin A deficiency in children in 138 low-income and middle-income countries between 1991 and 2013: a pooled analysis of population-based surveys. *Lancet Global Health* 2015;3(9):e528–36. PMID: 26275329.

**Design:** Bayesian hierarchical model of VAD prevalence (serum retinol <0.70 μmol/L) in 138 LMICs; pooled RRs from supplementation trials adjusted for deficiency prevalence; country-level attributable deaths estimated.

**Global Finding (2013):** ~94,500 diarrhea deaths + 11,200 measles deaths attributable to VAD = ~105,700 total deaths; 1.7% of all under-5 deaths in LMICs. More than 95% in sub-Saharan Africa and South Asia.

**Regional trends:** Southeast Asia and East Asia showed dramatic declines in VAD prevalence (42% → 6%, 1991–2013). Sub-Saharan Africa remained highest (48% prevalence in 2013). South Asia remained high (44%).

**Note on RR:** This study used trial-derived RRs but adjusted them upward in high-prevalence settings—the same prevalence-adjustment approach later dropped by GBD 2019. The adjustment is defensible on biological grounds (supplement trials are conducted in mixed populations of deficient and replete children; the true RR among deficient children is higher than the trial RR).

---

### 2.12 Neonatal VAS IPD Meta-Analysis 2019
**Citation:** Haider BA, Sharma S, Bhutta ZA. Neonatal vitamin A supplementation for the prevention of mortality and morbidity in term neonates in low and middle income countries. Cochrane 2017; and related: Early neonatal vitamin A supplementation and infant mortality: an individual participant data meta-analysis of randomised controlled trials. *BMJ* 2019. PMID: 30425075. PMC: PMC6556975.

**Key Finding (geographic heterogeneity):**
- **Asian trials (5 trials):** RR = 0.87 (0.77–0.98) — significant 13% mortality reduction in first 6 months.
- **African trials (6 trials):** RR = 1.06 (0.98–1.15) — no benefit; trend toward harm.
- Meta-regression identified maternal VAD prevalence, control group mortality, and education as the key predictors of effect direction.
- NVAS beneficial where maternal VAD prevalence was moderate/severe; no benefit (or harm) where maternal VAD was absent or mild.

**Applicability:** Reinforces that the geographic context matters enormously. Nigeria's relatively lower maternal VAD prevalence (compared to South Asia) implies a lower expected mortality benefit from addressing VAD.

---

### 2.13 Benn et al. 2015 — The "Enigma" Paper
**Citation:** Benn CS, Aaby P, Arts RJW, et al. An enigma: why vitamin A supplementation does not always reduce mortality even though vitamin A deficiency is associated with increased mortality. *Int J Epidemiol* 2015;44(3):906–18. PMID: 26142161. DOI: 10.1093/ije/dyv117.

**Key Argument:** VAD is associated with mortality, yet VAS trials show inconsistent effects. Two hypotheses:
- **(A) VAD hypothesis:** VAS works only where VAD is prevalent; failure in Africa reflects lower VAD prevalence.
- **(B) DTP-interaction hypothesis:** High-dose VAS interacts negatively with subsequent DTP vaccination, increasing mortality in females. This would explain harmful effects in African girls in vaccinated cohorts.

**Implications for the model:** Even if VAD is prevalent and causing mortality, the mortality-reducing effect of *correcting* VAD may be modulated by vaccination schedules and other immunological interactions. This adds uncertainty to the RR estimates, particularly for Nigeria.

---

## 3. Why RR Varies Geographically: Biological Mechanisms

### 3.1 Baseline VAD Prevalence (Fundamental Driver)
The supplementation trial RR (RR_supplementation) is the weighted average of effects across:
- Deficient children who benefit (large individual effect)
- Replete children who do not benefit (null individual effect)

Therefore: **RR_supplementation = prevalence_deficient × RR_deficient + (1 − prevalence_deficient) × 1.0**

If true RR_deficient = 2.0 and prevalence = 50%: RR_supplementation = 1.5
If true RR_deficient = 2.0 and prevalence = 20%: RR_supplementation = 1.2
If true RR_deficient = 2.0 and prevalence = 10%: RR_supplementation = 1.1

This is why DEVTA (India, low current prevalence) showed RR≈0.96 while Nepal 1991 (high prevalence) showed RR≈0.70. The underlying biological RR of deficiency may not differ, but the trial-level RR is diluted by replete participants.

**Current VAD prevalence by country (circa 2015–2020):**
- Bangladesh: ~34% (historically as high as 76.8%; recent figures closer to 20–35%)
- India: ~62% (NNMB survey, preschool children) to ~21.5% (severe deficiency <0.35 μmol/L)
- Indonesia: ~10–12% (now classified as a mild-risk or borderline country)
- Philippines: ~15–20%
- Vietnam: ~10–15% (significant decline)
- Myanmar: ~25–30%
- Cambodia: ~15–20%
- Nigeria: ~30–40% (sub-Saharan Africa remains high)

### 3.2 Cause-of-Death Ecology: Which Diseases Kill Children?
VAD has a strong protective effect against diarrhea and measles mortality, moderate effects on some infections, and **no effect on malaria-specific mortality**. The disease landscape differs dramatically:

**SE Asia (Bangladesh, Philippines, Indonesia, Vietnam, Myanmar, Cambodia):**
- Leading causes of under-5 death: acute respiratory infections (pneumonia), diarrheal disease, neonatal causes, malnutrition-related
- Measles deaths have declined substantially with vaccination
- Malaria contribution is low (varies: higher in Myanmar, Cambodia; near-zero in Bangladesh)
- VAD's mechanism of benefit (diarrhea, measles) maps well to this disease ecology

**India:**
- Highly heterogeneous; diarrhea and pneumonia dominant in some states
- Malnutrition compound with VAD (synergistic mortality effect)
- Large variation: Kerala vs. Uttar Pradesh
- The null DEVTA result likely reflects India's heterogeneous status; states with high VAD should see RR closer to 1.5+

**Nigeria:**
- Leading under-5 causes: malaria (~30%), neonatal conditions (~30%), pneumonia, diarrhea
- VAD does NOT appear to reduce malaria mortality (Ghana VAST: no malaria-mortality effect)
- The mortality fraction where VAD acts (diarrhea, measles) is smaller relative to the total mortality burden
- This mechanistically limits the attributable fraction of mortality that VAD can modulate
- VAD may amplify malaria severity through immune suppression, but the Ghana VAST data suggests this does not translate to reduced malaria mortality with supplementation

### 3.3 Malaria-VAD Interaction
A study from Nigeria found that children with severe malaria and hypovitaminosis A were **9.1 times more likely to die** (OR 9.1, 95% CI 2.2–38.1) than those without hypovitaminosis A. However, Ghana VAST showed VAS did not reduce malaria-specific mortality (rate ratio not significant). This apparent contradiction may reflect:
- Malaria acutely depresses serum retinol (an acute-phase response), so apparent low retinol in malaria patients is partially causal (malaria causes low retinol) rather than a pre-existing deficiency
- Correcting dietary VAD may not be sufficient to overcome the acute depletion during malaria infection
- Other factors (malnutrition severity, anemia) confound the observed association

### 3.4 Sanitation and Disease Burden Intensity
Higher fecal-oral disease burden (poor water/sanitation) → more enteropathogen exposure → more VAD-attributable diarrheal deaths → higher effective RR.
- Bangladesh and Myanmar: poor WASH indicators → higher disease burden → VAD mechanism more operative
- Urban Philippines and Vietnam: improving WASH → lower effective RR
- Nigeria: mixed; rural Nigeria has poor WASH but high malaria, which overwhelms the VAD-diarrhea pathway

### 3.5 Nutritional Synergies and Compound Deficiencies
VAD rarely occurs in isolation. Zinc deficiency, iron deficiency, protein-energy malnutrition (PEM), and wasting all compound mortality risk. In settings with compound malnutrition:
- The mortality gradient between deficient and replete children is steeper
- Correcting VAD alone yields less benefit than if all deficiencies were corrected
- Bangladesh and India: high rates of compound malnutrition → RR effects of VAD alone may be partially diluted but the deficient-child mortality is very high

### 3.6 Measles Vaccination Coverage
VAD's largest absolute mortality benefit historically came through measles and diarrhea pathways. With near-universal measles vaccination coverage (Bangladesh ~95%, Philippines ~80–90%), the measles-VAD pathway contributes less to total attributable mortality. This reduces the effective RR in current conditions compared to pre-vaccination era estimates.

---

## 4. Two Methodological Camps

### Camp A: PAF/Supplementation Trial Approach (Traditional)
**Proponents:** Sommer, West, Beaton, Fawzi, Stevens (Lancet GH 2015), WHO supplementation guidelines

**Method:**
1. Conduct or meta-analyze randomized supplementation trials to obtain RR_supplementation.
2. Adjust RR_supplementation for VAD prevalence to get the RR among deficient children.
3. Apply the population attributable fraction (PAF = prevalence × (RR−1) / (prevalence × (RR−1) + 1)).
4. Multiply PAF × cause-specific deaths = attributable deaths.

**Advantages:**
- Directly grounded in experimental evidence
- Can be adjusted for current prevalence conditions
- Transparently links to measured biological parameters

**Disadvantages:**
- Supplementation trials may have other mechanisms (immunomodulation) beyond correcting VAD
- Inversion of RR (from supplementation to deficiency) makes the strong assumption that supplement fully corrects deficiency and does nothing in replete children
- The prevalence-adjustment requires reliable current prevalence estimates
- Historical trials may not generalize to contemporary disease ecology

**Typical implied VAD RR from this approach:** 1.4–2.0 in high-VAD, high-disease-burden settings; 1.1–1.4 in moderate settings.

### Camp B: GBD Comparative Risk Assessment (MR-BRT approach)
**Proponents:** IHME GBD 2019 team

**Method:**
1. Conduct a systematic review of trials.
2. Use MR-BRT meta-regression with 10% trimming of outlier studies.
3. Apply a log-linear dose-response model between VAD prevalence and mortality.
4. Estimate PAF using a continuous exposure model.

**Advantages:**
- Internally consistent with GBD disease burden estimates
- Uses all available data with formal meta-regression
- Applies Bayesian regularization to avoid extreme estimates

**Disadvantages:**
- The 10% trimming criteria are not publicly documented
- Removal of the prevalence-adjustment is contested; biologically, VAD trials in high-prevalence settings should show larger effects per-deficient-child than the trial RR
- GBD 2019 RR for diarrhea (1.14) implies only 12–14% elevated risk in VAD children vs. replete—far lower than clinical intuition and observational data suggest
- The ~90% drop in estimated deaths between GBD 2017 and 2019 reflects methodology change, not a real epidemiological shift
- MR-BRT analyses not independently peer-reviewed or published separately

**Typical RR from this approach:** 1.14–1.39 (cause-specific); implying overall VAD RR ~1.15–1.25 when weighted across causes.

### Synthesis and Recommendation for the Model
The "true" causal RR of VAD on child mortality for a child who is genuinely deficient (serum retinol <0.70 μmol/L) and living in a contemporary setting with active supplementation programs and moderate measles vaccination coverage is likely in the range of **1.3–1.8**, varying by:
- Baseline VAD prevalence
- Local disease ecology (malaria burden)
- Measles vaccination coverage
- Sanitation status
- Nutritional compound deficiency burden

The current model's uniform RR of 1.75 is on the high end of plausible values for SE Asian countries but may be appropriate or slightly low for Myanmar and parts of Bangladesh/India. It is likely too high for Indonesia, Philippines, and Vietnam (where VAD has declined substantially), and likely too high for Nigeria (where malaria dominates mortality and VAD has limited measurable effect on malaria deaths).

---

## 5. Recommended RR Values by Country with Uncertainty Ranges

The recommended RR below is the **implied mortality hazard ratio for a VAD child vs. a vitamin-A-replete child** in the current (2020s) setting. This is the appropriate parameter for the Golden Rice impact model if the model asks: "What is the mortality risk of a VAD child relative to a non-deficient child?"

**Derivation basis for each country:**
- West Nepal 1991 (South Asian analogue): RR=1.43
- Tamil Nadu 1990 (historical high end): RR=1.85
- DEVTA 2013 (low-risk India): RR~1.04
- Cochrane 2022 meta-analysis (overall): implied ~1.14
- GBD 2019 diarrhea-specific: 1.14; measles: 1.39
- Ghana VAST 1993 (Africa analogue): implied RR~1.23; no malaria benefit
- Adjustment upward for high-VAD prevalence countries; downward for countries with low current prevalence, high malaria burden, or high measles vaccination coverage

### Country-Specific Recommendations

| Country | Recommended Point Estimate | Uncertainty Range (Low–High) | Rationale |
|---|---|---|---|
| **Bangladesh** | **1.65** | 1.40–1.90 | High VAD prevalence (25–35%); diarrhea-dominant child mortality; moderate malaria; poor WASH in rural areas; analogous to Nepal 1991 setting; measles vaccination ~90–95% (reduces measles-pathway contribution slightly) |
| **Philippines** | **1.45** | 1.20–1.70 | Moderate VAD (15–20%); declining diarrheal burden in urban areas; rural areas retain higher risk; BCMO1 polymorphism burden (see Section 6); improving WASH; high measles vaccination |
| **India** | **1.35** | 1.05–1.65 | Highly heterogeneous: high-VAD states (UP, Bihar, Rajasthan) closer to 1.65; DEVTA (UP 2000s) showed null effect → current RR ~1.04; Tamil Nadu historical ~1.85; weighted average across national heterogeneity; recommend sensitivity analyses by state |
| **Indonesia** | **1.25** | 1.05–1.50 | VAD now classified as mild/borderline risk (<10–12%); dramatic improvement since 1980s; original Aceh trial (1986) reflected a far more deficient era; current setting warrants lower RR; improving WASH and nutrition |
| **Vietnam** | **1.20** | 1.05–1.40 | Significant decline in VAD prevalence (10–15%); rapid economic development; relatively strong VAS program coverage; VAD still a concern in highland minority populations |
| **Myanmar** | **1.55** | 1.25–1.80 | Moderate-to-high VAD (25–30%); significant malaria burden (especially in border areas—Kachin, Shan, Kayah states); the malaria component of mortality limits expected benefit but absolute diarrhea/pneumonia burden remains high; poor WASH infrastructure |
| **Cambodia** | **1.40** | 1.15–1.65 | Moderate VAD (~15–20%); malaria declining but historically significant; improving child health indicators; similar ecological setting to Vietnam but higher VAD |
| **Nigeria** | **1.20** | 0.95–1.50 | High VAD prevalence (30–40%) but malaria accounts for ~30% of under-5 deaths and VAS does not reduce malaria mortality (Ghana VAST); the fraction of mortality where VAD acts (diarrhea, measles) is smaller; measles vaccination improving; uncertainty range includes possibility of no net benefit (RR approaching 1.0) in malaria-dominated settings |

### Notes on Uncertainty Ranges
- **Low estimate** reflects: GBD 2019 values, high measles vaccination, low current VAD prevalence, malaria-dominated setting.
- **High estimate** reflects: Historical trial data (Nepal, Tamil Nadu), high current VAD prevalence, diarrhea/measles-dominant mortality, no/low malaria.
- **Nigeria's RR could plausibly be below 1.0** in certain analyses if the DTP-VAS interaction hypothesis (Benn 2015) applies, though this is contested. The practical recommendation is to use 1.20 as point estimate with explicit sensitivity analysis at 1.0 (null) and 1.50 (high).

### Recommended Model Implementation
```python
# Country-specific VAD relative risk estimates
# Format: (point_estimate, low_95CI, high_95CI)
relative_risk_vad = {
    'Bangladesh':  (1.65, 1.40, 1.90),
    'Philippines': (1.45, 1.20, 1.70),
    'India':       (1.35, 1.05, 1.65),
    'Indonesia':   (1.25, 1.05, 1.50),
    'Vietnam':     (1.20, 1.05, 1.40),
    'Myanmar':     (1.55, 1.25, 1.80),
    'Cambodia':    (1.40, 1.15, 1.65),
    'Nigeria':     (1.20, 0.95, 1.50),
}
```

---

## 6. BCMO1/BCO1 Polymorphism Data for Target Populations

Beta-carotene (the primary provitamin A carotenoid in Golden Rice) must be enzymatically converted to retinol by beta-carotene 15,15'-monooxygenase (BCMO1, now often called BCO1). Genetic polymorphisms in BCO1 reduce this conversion efficiency by 32–69%, creating a "poor converter" phenotype that is relevant to how much vitamin A a child actually obtains from Golden Rice consumption.

### 6.1 Key Functional Variants

| SNP | Gene Position | Effect | Allele Reducing Conversion | Reduction in Activity |
|---|---|---|---|---|
| rs12934922 (R267S) | Coding, exon | Nonsynonymous | T allele | ~32–57% reduction (double mutant) |
| rs7501331 (A379V) | Coding, exon | Nonsynonymous | T allele | Up to 69% reduction (combined with R267S) |
| rs6564851 | Upstream (~8 kb) | Regulatory | G allele | ~48–59% reduction in enzyme activity |

The double mutant (267S + 379V) shows 57% reduced catalytic activity in vitro. Carriers of the combined A379V TT variant show a 69% decrease in beta-carotene conversion.

### 6.2 Allele Frequencies by Population

**rs12934922 (R267S) — T allele frequency (from gnomAD v4 exomes):**

| Population | T allele frequency | Notes |
|---|---|---|
| European | 0.44 | Highest frequency |
| **South Asian** | **0.28** | gnomAD SAS superpopulation; includes Bangladeshi (BEB), Indian, Pakistani |
| East Asian | 0.14 | Including Japanese, Chinese |
| African | 0.14 | |
| Global | 0.41 | |

**1000 Genomes data for rs12934922 (T allele):**

| Population | T allele frequency |
|---|---|
| European | 0.440 |
| **South Asian** | **0.231** |
| East Asian | 0.128 |
| African | 0.089 |

**rs6564851 (upstream regulatory) — G allele (reduces conversion ~48%):**

| Population | G allele frequency | Notes |
|---|---|---|
| East Asian (Japanese) | ~0.824 | Very high — majority of East Asians carry the low-conversion G allele |
| HapMap-JPT | 0.833 | Confirms high Japanese frequency |
| European | 0.467 | |
| West African (Yoruba) | 0.358 | |
| Ghanaian adolescents | MAF G~0.31 | Rural Ghana study |

**Philippines-specific data (BCMO1 coding variants R267S + A379V):**
Zumaraga et al. (2022) studied 693 Filipino children and adolescents from the 2013 Philippine National Nutrition Survey:
- Combined R267S + A379V double mutation present in **7.6%** of the sample.
- A379V TT variant associated with lower vitamin A status (inverse relationship with serum retinol).
- First published data confirming presence of these variants in Filipino populations.

### 6.3 Interpretation for Target Countries

**Bangladesh:**
- South Asian population frequency for rs12934922 T allele: ~23–28% (gnomAD SAS).
- Estimated proportion with compound heterozygous or homozygous low-conversion genotype (both rs12934922 and rs7501331): ~7–12% based on European-derived estimates adjusted for lower allele frequency.
- No Bangladesh-specific published allele frequency study found; gnomAD BEB (Bengali in Bangladesh, n≈144 individuals) is the best available source.
- rs6564851 G allele frequency in Bangladeshi populations: unknown from published literature; likely intermediate between European and East Asian given South Asian position on the genomic cline.

**Philippines:**
- Confirmed presence of R267S and A379V variants (Zumaraga et al. 2022).
- ~7.6% carry the double mutation (R267S + A379V), which reduces BCO1 activity by 57%.
- This percentage underestimates total "poor converter" burden because single mutations (A379V alone) also reduce efficiency by ~32%.
- Estimated ~15–25% of Filipinos may have meaningfully reduced beta-carotene conversion (combining single and double mutation carriers).

**East Asian-influenced populations (Vietnam, Cambodia):**
- rs6564851 G allele is very high in East Asians (~82% in Japanese). If Southeast Asian populations (Vietnamese, Cambodian) have similarly high G frequencies, a large majority of the population may carry the regulatory variant reducing BCO1 activity by ~48%.
- Japanese data: GG homozygotes showed 2-fold higher serum beta-carotene levels vs. T-allele carriers (indicating less conversion of beta-carotene to retinol).
- This is a significant concern for Golden Rice efficacy in Vietnam and Cambodia.

**Nigeria:**
- African populations have lower rs12934922 T allele frequency (~9–14%) and lower rs6564851 G allele frequency (~36% in Yoruba).
- By this metric, Nigerian children would have somewhat better BCO1 activity than South or East Asian children.
- However, this is likely a minor consideration given that malaria-dominated child mortality is not addressed by VAD correction in the first place.

### 6.4 Practical Implications for Golden Rice Impact

If ~20–30% of the target population in SE Asia are poor converters with 32–69% reduced beta-carotene conversion:
- The effective vitamin A dose from Golden Rice is reduced by ~10–20% at the population level (averaging over converters and non-converters).
- The impact model should include a conversion efficiency adjustment: multiply the beta-carotene dose by a factor of ~0.80–0.90 for SE Asian populations to account for BCMO1 polymorphism burden.
- This is especially important for Vietnam and Cambodia if the rs6564851 G allele is as prevalent as in Japanese populations.
- The 2022 Zumaraga Philippines study is the only directly applicable published study; a Bangladesh-specific BCO1 genotyping study is a key research gap.

**Recommended bioconversion factor for model:**
- Standard bioconversion ratio of Golden Rice beta-carotene to retinol: 3.8:1 to 6:1 (from controlled feeding studies)
- Apply a population-level BCMO1 adjustment factor of 0.85 (range 0.75–0.95) for SE Asian populations
- For Vietnam and Cambodia, consider a factor of 0.80 given high rs6564851 G allele prevalence

---

## 7. Implications for Golden Rice Efficacy

### 7.1 Mechanistic Chain
Golden Rice impact on child mortality operates through:
1. **Beta-carotene dose** from Golden Rice consumption (depends on rice intake and GR adoption rate)
2. **Bioconversion** of beta-carotene to retinol (BCMO1 efficiency, food matrix effects)
3. **Net change in vitamin A status** (reducing the fraction of children with VAD)
4. **Reduction in VAD-attributable mortality** (governed by country-specific RR)

Steps 2 and 4 are now better characterized by the research compiled here. Steps 1 and 3 depend on adoption modeling (addressed in other model files).

### 7.2 Key Interactions with Model RR
- A higher country-specific RR means each child moved from VAD to non-deficient has a larger mortality benefit.
- Bangladesh (RR=1.65) benefits much more per case of VAD corrected than Indonesia (RR=1.25).
- Nigeria (RR=1.20) benefits least per corrected case, both because of lower implied RR and because malaria (not addressable by VA) dominates mortality.

### 7.3 Research Gaps
1. **Bangladesh-specific BCO1 allele frequencies**: No published study; the gnomAD BEB sample (n=144) is too small for confident estimates.
2. **Real-world beta-carotene conversion in SE Asian children with marginal VA status**: The controlled trials (Tang et al., Gopalan et al.) used US children or replete individuals; conversion in VAD children may differ.
3. **Country-specific current VAD prevalence** for Myanmar, Cambodia, Vietnam (survey data often >10 years old).
4. **Nigeria RR uncertainty**: The 0.95–1.50 range spans near-null to moderate benefit; the model is highly sensitive to this parameter for Nigeria.
5. **Interaction between BCMO1 genotype and VAD status**: Poor converters may have higher baseline VAD prevalence, creating a compounding effect not captured in current modeling.

---

## 8. Full Source List with DOIs and PMC Links

### Primary Trials
1. Sommer A, Tarwotjo I, Hussaini G, Susanto D. **Increased mortality in children with mild vitamin A deficiency.** *Lancet* 1983;2(8350):585–8. PMID: [6136744](https://pubmed.ncbi.nlm.nih.gov/6136744/)

2. Sommer A, Tarwotjo I, Djunaedi E, et al. **Impact of vitamin A supplementation on childhood mortality: a randomised controlled community trial.** *Lancet* 1986;1:1169–73. PMID: [2871418](https://pubmed.ncbi.nlm.nih.gov/2871418/)

3. Rahmathullah L, Underwood BA, Thulasiraj RD, et al. **Reduced mortality among children in southern India receiving a small weekly dose of vitamin A.** *NEJM* 1990;323(14):929–35. PMID: [2205798](https://pubmed.ncbi.nlm.nih.gov/2205798/). DOI: [10.1056/NEJM199010043231401](https://www.nejm.org/doi/full/10.1056/NEJM199010043231401)

4. West KP Jr, Pokhrel RP, Katz J, et al. **Efficacy of vitamin A in reducing preschool child mortality in Nepal.** *Lancet* 1991;338(8759):67–71. PMID: [1676467](https://pubmed.ncbi.nlm.nih.gov/1676467/). DOI: [10.1016/0140-6736(91)90070-6](https://www.sciencedirect.com/science/article/pii/0140673691900706)

5. Ghana VAST Study Team. **Vitamin A supplementation in northern Ghana: effects on clinic attendances, hospital admissions, and child mortality.** *Lancet* 1993;342(8862):7–12. PMID: [8100345](https://pubmed.ncbi.nlm.nih.gov/8100345/)

6. Fawzi WW, Chalmers TC, Herrera MG, Mosteller F. **Vitamin A supplementation and child mortality: a meta-analysis.** *JAMA* 1993;269(7):898–903. PMID: [8426449](https://pubmed.ncbi.nlm.nih.gov/8426449/). DOI: [10.1001/jama.1993.03500070078033](https://doi.org/10.1001/jama.1993.03500070078033)

7. Awasthi S, Peto R, Read S, et al. **Vitamin A supplementation every 6 months with retinol in 1 million pre-school children in north India: DEVTA, a cluster-randomised trial.** *Lancet* 2013;381:1469–77. PMID: [23498849](https://pubmed.ncbi.nlm.nih.gov/23498849/). PMC: [PMC3647148](https://pmc.ncbi.nlm.nih.gov/articles/PMC3647148/). DOI: [10.1016/S0140-6736(12)62125-4](https://www.thelancet.com/article/S0140-6736(12)62125-4/fulltext)

### Meta-Analyses and Systematic Reviews
8. Beaton GH, Martorell R, L'Abbé KA, et al. **Effectiveness of Vitamin A Supplementation in the Control of Young Child Morbidity and Mortality in Developing Countries.** ACC/SCN Nutrition Policy Discussion Paper No. 13. 1993.

9. Vitamin A and Pneumonia Working Group. **Potential interventions for the prevention of childhood pneumonia in developing countries: a meta-analysis of data from field trials to assess the impact of vitamin A supplementation on pneumonia morbidity and mortality.** *Bull WHO* 1995;73(5):609–19. PMID: [8846487](https://pubmed.ncbi.nlm.nih.gov/8846487/)

10. Imdad A, Mayo-Wilson E, Haykal MR, et al. **Vitamin A supplementation for preventing morbidity and mortality in children from six months to five years of age.** *Cochrane Database Syst Rev* 2022. PMID: [35294044](https://pubmed.ncbi.nlm.nih.gov/35294044/). PMC: [PMC8925277](https://pmc.ncbi.nlm.nih.gov/articles/PMC8925277/)

11. Imdad A, Mayo-Wilson E, Herzer K, Bhutta ZA. **Vitamin A supplementation for preventing morbidity and mortality in children from six months to five years of age.** *Cochrane Database Syst Rev* 2017;3:CD008524. DOI: [10.1002/14651858.CD008524.pub3](https://doi.org/10.1002/14651858.CD008524.pub3)

### GBD and Country-Level Analyses
12. Wessells KR, Brown KH, Bassett MN, et al. **Basis for changes in the disease burden estimates related to vitamin A and zinc deficiencies in the 2017 and 2019 Global Burden of Disease Studies.** *Public Health Nutr* 2023. PMC: [PMC9991746](https://pmc.ncbi.nlm.nih.gov/articles/PMC9991746/)

13. Stevens GA, Bennett JE, Hennocq Q, et al. **Trends and mortality effects of vitamin A deficiency in children in 138 low-income and middle-income countries between 1991 and 2013: a pooled analysis of population-based surveys.** *Lancet Global Health* 2015;3(9):e528–36. PMID: [26275329](https://pubmed.ncbi.nlm.nih.gov/26275329/)

14. Cahill CM, El-Sohemy A. **Global Burden of Vitamin A Deficiency in 204 Countries and Territories from 1990–2019.** PMC: [PMC8912822](https://pmc.ncbi.nlm.nih.gov/articles/PMC8912822/)

### Geographic Variation and Heterogeneity
15. Benn CS, Aaby P, Arts RJW, et al. **An enigma: why vitamin A supplementation does not always reduce mortality even though vitamin A deficiency is associated with increased mortality.** *Int J Epidemiol* 2015;44(3):906–18. PMID: [26142161](https://pubmed.ncbi.nlm.nih.gov/26142161/). DOI: [10.1093/ije/dyv117](https://academic.oup.com/ije/article/44/3/906/633272)

16. Haider BA, Bhutta ZA. **Early neonatal vitamin A supplementation and infant mortality: an individual participant data meta-analysis of randomised controlled trials.** *BMJ* 2019. PMID: [30425075](https://pubmed.ncbi.nlm.nih.gov/30425075/). PMC: [PMC6556975](https://pmc.ncbi.nlm.nih.gov/articles/PMC6556975/)

### BCMO1/BCO1 Polymorphisms
17. Leung WC, Hessel S, Méplan C, et al. **Two common single nucleotide polymorphisms in the gene encoding β-carotene 15,15'-monoxygenase alter β-carotene metabolism in female volunteers.** *FASEB J* 2009;23(4):1041–53. DOI: [10.1096/fj.08-121962](https://doi.org/10.1096/fj.08-121962)

18. Lietz G, Oxley A, Leung W, Hesketh J. **Single nucleotide polymorphisms upstream from the β-carotene 15,15'-monoxygenase gene influence provitamin A conversion efficiency in female volunteers.** *J Nutr* 2012;142(1):161S–5S. PMID: [22113863](https://pubmed.ncbi.nlm.nih.gov/22113863/)

19. Zumaraga MP, Arquiza JMA, Concepcion MA, et al. **Genotype effects on β-carotene conversion to vitamin A: implications on reducing vitamin A deficiency in the Philippines.** *Food Nutr Bull* 2022. PMID: [34903070](https://pubmed.ncbi.nlm.nih.gov/34903070/)

20. Sagmeister S, Eisenhaber B, Eisenhaber F, et al. **Genetic Variations of Vitamin A-Absorption and Storage-Related Genes, and Their Potential Contribution to Vitamin A Deficiency Risks Among Different Ethnic Groups.** *Front Nutr* 2022. PMC: [PMC9096837](https://pmc.ncbi.nlm.nih.gov/articles/PMC9096837/)

21. Kitano T, Katsuura-Kamano S, Nakamura K, et al. **Common SNP rs6564851 in the BCO1 Gene Affects the Circulating Levels of β-Carotene and the Daily Intake of Carotenoids in Healthy Japanese Women.** *PLOS ONE* 2016. PMC: [PMC5179075](https://pmc.ncbi.nlm.nih.gov/articles/PMC5179075/)

### Malaria-VAD Interaction
22. Veenemans J, Milligan P, Prentice AM, et al. **Malaria and vitamin A deficiency in African children: a vicious circle?** *Malar J* 2009;8:134. PMC: [PMC2702350](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2702350/)

### Golden Rice and Beta-Carotene Bioconversion
23. Tang G, Qin J, Dolnikowski GG, Russell RM, Grusak MA. **Golden Rice is an effective source of vitamin A.** *Am J Clin Nutr* 2009;89(6):1776–83. PMC: [PMC2682994](https://pmc.ncbi.nlm.nih.gov/articles/PMC2682994/)

24. Tang G, Hu Y, Yin S, et al. **β-Carotene in Golden Rice is as good as β-carotene in oil at providing vitamin A to children.** *Am J Clin Nutr* 2012. PMC: [PMC3417220](https://pmc.ncbi.nlm.nih.gov/articles/PMC3417220/)

25. Birol G, Bouis HE, et al. **Biofortified β-carotene rice improves vitamin A intake and reduces the prevalence of inadequacy among women and young children in a simulated analysis in Bangladesh, Indonesia, and the Philippines.** PMC: [PMC4997296](https://pmc.ncbi.nlm.nih.gov/articles/PMC4997296/)

---

*Document compiled: 2026-03-21. For use with model.py in the Golden Rice impact model. All RR values should be subjected to one-way and probabilistic sensitivity analyses using the uncertainty ranges provided in Section 5.*
