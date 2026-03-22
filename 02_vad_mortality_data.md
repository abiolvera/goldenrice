# Vitamin A Deficiency: Global Mortality and Morbidity Data

> **Document purpose**: Comprehensive reference on VAD global burden for Golden Rice impact modeling.
> **Last updated**: March 2026 via live web research.
> **Primary sources**: Black et al. 2008 (*Lancet*); Stevens et al. 2015 (*Lancet Global Health*); GBD 2019 and GBD 2021 studies; WHO Global Database; UNICEF Data.

---

## Table of Contents

1. [Scale of Vitamin A Deficiency — Global Prevalence](#1-scale-of-vitamin-a-deficiency--global-prevalence)
2. [Annual Child Deaths Attributable to VAD (1990–2024)](#2-annual-child-deaths-attributable-to-vad-19902024)
3. [Regional Breakdown of Mortality — South/Southeast Asia, Sub-Saharan Africa](#3-regional-breakdown-of-mortality)
4. [VAD-Caused Blindness — Xerophthalmia and Corneal Blindness](#4-vad-caused-blindness)
5. [DALYs from Vitamin A Deficiency — GBD Studies](#5-dalys-from-vitamin-a-deficiency)
6. [Prevalence of VAD in Children Under 5 by Country and Region](#6-prevalence-by-country-and-region)
7. [High-Burden Countries: Detailed Profiles](#7-high-burden-countries-detailed-profiles)
8. [How VAD Burden Has Changed Over Time (1990–2024)](#8-how-vad-burden-has-changed-over-time)
9. [Proportion of VAD Burden in Rice-Dependent vs. Non-Rice-Dependent Populations](#9-rice-dependent-vs-non-rice-dependent-populations)
10. [Modeling Parameters and Uncertainty](#10-modeling-parameters-and-uncertainty)
11. [Key Sources and Citations](#11-key-sources-and-citations)

---

## 1. Scale of Vitamin A Deficiency — Global Prevalence

### Definition

Vitamin A deficiency (VAD) is defined biochemically as serum or plasma retinol concentration below **0.70 µmol/L** (subclinical deficiency). Severe VAD is defined as serum retinol below **0.35 µmol/L**. Clinical manifestations range from night blindness and Bitot's spots to corneal xerosis, ulceration, and keratomalacia (corneal melt).

### Global Prevalence Estimates (Selected Years)

| Year | Affected Preschool Children | Source/Notes |
|------|---------------------------|--------------|
| ~1990 | ~125–190 million | Sommer & West (1996); WHO 1995 estimates |
| 1995 | ~190 million (33.3%) | WHO Global Database 1995–2005 |
| 2005 | ~190 million (33.3% of under-5) | WHO (2009 publication); 92M in SE Asia, 56M in Africa |
| 2013 | ~29% of children aged 6–59 months in LMICs | Stevens et al. 2015 (*Lancet Global Health*) |
| 2019 | **333.95 million** (14.73%, 95% CI 11.16–19.14%) children/adolescents | Sarno et al. 2023 systematic review and modelling |
| 2019 | **489.7 million** cases (all ages); age-standardized incidence 59.85% lower than 1990 | GBD 2019 study (MDPI Nutrients 2022) |

**Key points:**
- Global age-standardized incidence rate declined at **EAPC of −3.11%/year** from 1990 to 2019 (GBD 2019).
- Despite declining rates, **absolute numbers remain enormous** due to population growth.
- **Sub-Saharan Africa** and **South Asia** have the highest prevalence and have shown the least improvement.
- 68 of 165 LMICs (41.21%) are still classified as areas of **moderate-to-severe** VAD public health significance (Sarno et al. 2023).
- Marginal VAD (serum retinol <1.05 µmol/L) affects an estimated **556 million children and adolescents** (24.54%) globally in 2019.

### WHO Regional Prevalence (2019 Systematic Review)

| WHO Region | VAD Prevalence | Affected Children |
|-----------|---------------|-------------------|
| African Region | 24.51% | 135.03 million |
| Eastern Mediterranean | 17.43% | 49.94 million |
| South-East Asia | 13.11% | 87.77 million |
| Western Pacific | Lower — data limited | — |
| European Region | 5.89% | 8.49 million |

---

## 2. Annual Child Deaths Attributable to VAD (1990–2024)

VAD kills primarily by amplifying susceptibility to infectious diseases — measles and diarrhea are the leading pathways. Attribution is **modeled using Population Attributable Fractions (PAF)** applied to cause-specific child death totals, not directly counted. This generates wide confidence intervals across studies.

### Summary of Major Mortality Estimates

| Source | Pub. Year | Reference Period | Annual VAD-Attributable Child Deaths | Notes |
|--------|-----------|-----------------|--------------------------------------|-------|
| Beaton et al. (WHO meta-analysis) | 1993 | ~1990 | **1.3–2.5 million/year** | Based on VAS trial mortality reductions of 23–34%; high-risk countries only |
| Sommer & West | 1996 | ~1990–1995 | **1–2 million/year** | Children aged 1–4 |
| Black et al. (*Lancet* Maternal and Child Undernutrition Series) | 2008 | ~2005–2006 | **~670,000/year** (~600,000 in one formulation) | VAD + zinc deficiency combined ~9% of childhood DALYs; VAD alone ~600K deaths |
| GBD 2010 (Lozano et al.) | 2012 | 2010 | **~120,000–160,000/year** | Major downward revision from 2008 estimates |
| Stevens et al. (*Lancet Global Health*) | 2015 | 2013 | **~94,500 diarrhea + ~11,200 measles = ~105,700 total** (95% UI: 58,500–167,300) | Only measured via diarrhea + measles pathways; 1.7% of all under-5 deaths in LMICs |
| GBD 2017 | 2018 | 2017 | ~108,000 (dietary risk factor) | — |
| GBD 2019 | 2020–2022 | 2019 | Lower than GBD 2017 (methodological revision) | Rank fell from 33rd to 36th in DALY for all ages |
| GBD 2021 (*Frontiers in Nutrition* 2025) | 2025 | 1990–2021 | **188,458 deaths in 1990** → **17,374 deaths in 2021** | 90.78% relative decline; ASR from 3.04 to 0.27 per 100,000; EAPC −7.81%/year |

### The Critical Methodological Divide

The enormous range (from ~1.3 million to ~17,000) is not mainly a story of improvement but of **methodological evolution**:

1. **Pre-2010 estimates** (Beaton, Sommer, Black 2008) extrapolated from VAS supplementation trial results, where vitamin A supplementation reduced all-cause child mortality by 12–24%. This approach captured VAD's indirect effects on all infectious disease mortality.

2. **Post-2010 GBD estimates** use a comparative risk assessment framework assigning deaths only to specific causal pathways (measles + diarrhea), with lower relative risks than those assumed in trials. Malaria was excluded after evidence failed to confirm a VAD link.

3. **Stevens et al. 2015** is the most rigorous recent estimate for measles + diarrhea pathways specifically: **~105,700 deaths/year in 2013** (95% UI: 58,500–167,300), accounting for 1.7% of all under-5 deaths in LMICs.

4. **GBD 2021 mortality of 17,374** includes deaths from all causes modeled through the GBD risk factor framework. This is not directly comparable to supplementation-trial-based estimates.

**Analytical recommendation**: For Golden Rice impact modeling, the **Stevens et al. 2015 estimate of ~105,700 deaths/year** is the most methodologically transparent recent peer-reviewed number. The Black et al. 2008 estimate of ~600,000–670,000 provides a plausible upper bound reflecting broader infectious disease amplification. The GBD 2021 figure of ~17,374 is a methodological floor.

---

## 3. Regional Breakdown of Mortality

### Stevens et al. 2015 Regional Distribution (2013 data)

- **More than 95% of all VAD-attributable deaths occurred in sub-Saharan Africa and South Asia** combined.
- Deaths from diarrhea: 94,500 (95% UI: 54,200–146,800)
- Deaths from measles: 11,200 (95% UI: 4,300–20,500)
- Total attributable deaths: ~105,700
- As a fraction of under-5 deaths in LMICs: **1.7%** (95% UI: 1.0–2.6%)

### Black et al. 2008 Regional Distribution

- Highest burden: **South-central Asia**, followed by several sub-regions of Africa
- VAD and zinc deficiency combined responsible for ~9% of global childhood DALYs
- VAD alone: ~600,000 deaths/year estimate, with majority in South Asia and Sub-Saharan Africa

### GBD 2019 Regional Incidence and DALY Rates

| Region | Age-Standardized Incidence Rate (per 100,000) | Age-Standardized DALY Rate (per 100,000) |
|--------|---------------------------------------------|------------------------------------------|
| Central Sub-Saharan Africa | 25,905 | 49 |
| Eastern Sub-Saharan Africa | 23,500 | 35.90 |
| Western Sub-Saharan Africa | 15,571 | 37.04 |
| South Asia | High (44% prevalence) | High |
| Southeast Asia | Declining significantly (42% → 6%, 1991–2013) | Moderate |
| East Asia | Low by 2019 | Low |
| Latin America & Caribbean | ~11% prevalence (2013) | Low |
| High-income North America | 486 | 0.15 |
| Australasia | 149 | 0.05 |

### GBD 2021 Regional Performance

- **Largest mortality/DALY reductions**: East Asia, Southeast Asia, high-middle SDI regions
- **Smallest reductions**: Low-SDI regions (including most of Sub-Saharan Africa) and Oceania
- **African region**: Highest age-standardized VAD mortality rate in 2021
- Highest national mortality rates per 100,000 in 2021: **Somalia (21.72), Chad (10.41), South Sudan (6.51), Mali (5.22), Guinea-Bissau (4.14), Central African Republic (4.09), Burkina Faso (3.16), Zimbabwe (3.24)**

---

## 4. VAD-Caused Blindness

### Annual Blindness Estimates

| Estimate | Source | Year |
|----------|--------|------|
| **250,000–500,000 children** blind annually from VAD | WHO (repeatedly cited) | 1990s–present |
| ~350,000 new xerophthalmia cases/year | WHO/UNICEF estimates | Historical |
| 13.8 million children with some degree of visual loss from VAD | WHO | 1995 |
| 2.8 million preschool children at risk of blindness | WHO | 1995–2009 |
| 500,000+ new active corneal lesions/year (conservative) | WHO/published literature | Early 2000s |
| 6–7 million cases of non-corneal xerophthalmia/year | Published estimates | Early 2000s |

**Critical statistic**: Of children who go blind from VAD, **approximately 50% die within 12 months** of vision loss (WHO). This reflects the extreme immunocompromise associated with severe VAD.

### Clinical Spectrum of Xerophthalmia

VAD causes a spectrum of ocular disease (WHO classification):
- **XN**: Night blindness (nyctalopia) — earliest and most common clinical sign
- **X1A**: Conjunctival xerosis
- **X1B**: Bitot's spots
- **X2**: Corneal xerosis
- **X3A**: Corneal ulceration/keratomalacia (<1/3 corneal surface)
- **X3B**: Corneal ulceration/keratomalacia (≥1/3 corneal surface)
- **XS**: Corneal scar (permanent)
- **XF**: Xerophthalmic fundus

### Survival After Corneal Xerophthalmia

One-year follow-up data on corneal xerophthalmia cases shows:
- Only **40% survive** one year
- Of survivors: **25% are blind** (corneal scarring)
- Of survivors: **50–60% are partially blind**

### Global Vision Loss Burden (GBD 2017)

From the study "Global patterns in vision loss burden due to vitamin A deficiency from 1990 to 2017" (PMC10195433):

**Age-standardized prevalence rates (all vision loss due to VAD):**
- 1990: 68.8 per 100,000 (95% UI: 54.7–86.8)
- 2017: 75.1 per 100,000 (95% UI: 59.7–94.8)
- **Net change: +9.2%** — a counterintuitive *increase* driven by population growth

**Age-standardized YLD rates:**
- 1990: 3.7 per 100,000 (95% UI: 2.3–5.4)
- 2017: 4.1 per 100,000 (95% UI: 2.7–6.1)
- Net change: +10.8%

**Rankings among 15 causes of vision loss (GBD 2017):**
- VAD ranked **8th** in age-standardized prevalence
- VAD ranked **9th** in age-standardized YLD rates
- VAD's *increase* in prevalence burden ranked **3rd** (behind malaria at +20.2% and diabetes at +14.9%)

**Highest vision loss burden by region (2017):**
- South Asia: prevalence 128.8 per 100,000; YLD 7.1 per 100,000
- Central Sub-Saharan Africa: prevalence (male) 251.6, (female) 229.5 per 100,000; YLD (male) 13.4, (female) 13.7

**Highest burden countries by prevalence (2017):**
- Congo: 250.9 per 100,000
- Democratic Republic of Congo: 242.2 per 100,000
- Angola: 240.1 per 100,000

**Highest burden countries by YLD rate (2017):**
- Yemen: 16.3 per 100,000
- Oman: 14.9 per 100,000
- Congo: 14.3 per 100,000

### Regional Distribution of Xerophthalmia

- ~**45% of the world's VAD-affected children** are in South and Southeast Asia
- Indonesia alone: estimated **63,000 new xerophthalmia cases/year** (based on rate of 2.7 per 1,000 children)
- If similar rate applied to Bangladesh, India, and Philippines: ~**400,000 preschool children** developing active corneal lesions per year
- Africa: **20,000–100,000 new blindness cases/year** from VAD (range of estimates)

---

## 5. DALYs from Vitamin A Deficiency

### GBD 2021 DALYs — Comprehensive Time Series

From "A comprehensive analysis of vitamin A deficiency burden and trends: insights from the global burden of disease study 2021" (*Frontiers in Nutrition*, 2025; PMC12671203):

**Global DALYs (absolute numbers):**

| Year | DALYs (thousands) | Age-Standardized DALY Rate (per 100,000) |
|------|-------------------|------------------------------------------|
| 1990 | ~18,790 | 303.72 |
| 2000 | ~10,000–12,000 (est.) | ~150–200 |
| 2010 | ~5,000–7,000 (est.) | ~80–100 |
| 2019 | ~1,970 (GBD 2019 paper) | ~32.56 (2021) |
| 2021 | **~1,105–2,630** | **15.73–40.10** |

*Note: The two different numbers reflect different GBD studies using different methodologies. The Frontiers 2025 paper reports 1,104,931 DALYs in 2021 (EAPC −2.81%/year from 1990); the GBD 2021 Frontiers paper using mortality-focused methodology reports 2.63 million DALYs in 2021.*

**Overall decline 1990–2021**: −40.15% to −85.83% (depending on methodology), with age-standardized DALY rate declining −47.07% to −86.8%.

### GBD 2021 DALY Breakdown by Sex (2021)

| Sex | DALYs | Age-Standardized DALY Rate | EAPC |
|-----|-------|---------------------------|------|
| Male | 596,965 | 16.6 per 100,000 | −2.68% |
| Female | 507,966 | 14.8 per 100,000 | −2.11% |

Males experience consistently higher burden; gender disparity gradually narrowing.

### GBD 2021 DALY Breakdown by Age Group (2021)

| Age Group | DALYs | Age-Standardized DALY Rate | EAPC |
|-----------|-------|---------------------------|------|
| Under 5 years | 478,594 | 72.72 per 100,000 | −2.99% |
| 5–9 years | 285,199 | 41.51 per 100,000 | −2.36% |
| 10–14 years | 183,585 | 27.54 per 100,000 | −2.18% |
| 15+ years | Minimal | — | — |

Children under 5 represent **over 43–45% of global VAD DALYs** despite being a small fraction of total population.

### GBD 2021 DALY Breakdown by Sociodemographic Index (SDI, 2021)

| SDI Level | DALYs | Age-Standardized DALY Rate | EAPC |
|-----------|-------|---------------------------|------|
| Low | 563,501 | 36.31 per 100,000 | −2.66% |
| Low-middle | 355,962 | 18.09 per 100,000 | −3.52% |
| Middle | 156,311 | 7.40 per 100,000 | −3.24% |
| High-middle | 26,223 | 2.72 per 100,000 | −3.62% |
| High | 2,247 | 0.30 per 100,000 | −4.65% |

**Key insight**: Low-SDI countries (primarily sub-Saharan Africa) carry **51% of global VAD DALYs** while having the *slowest* rate of improvement (lowest EAPC magnitude by absolute burden).

### Historical DALY Estimates for Context

| Source/Year | Global VAD DALYs |
|------------|-----------------|
| WHO Global Burden of Disease 2001 | ~26 million |
| GBD 2004 | ~20 million |
| GBD 2010 | ~8–10 million |
| GBD 2013 | ~6 million |
| GBD 2017 | ~3–4 million |
| GBD 2019 | ~1.97 million (direct) |
| GBD 2021 | **~1.10–2.63 million** |

The dramatic reduction from 26 million (2001) to ~1–2 million (2021) reflects both real improvements and substantial methodological revision.

---

## 6. Prevalence by Country and Region

### Prevalence by WHO Region (Stevens et al. 2015 — Year 2013 Estimates)

| Region | VAD Prevalence in 6–59 Month Children (2013) | Change from 1991 |
|--------|---------------------------------------------|-----------------|
| Sub-Saharan Africa | **48%** (95% CrI: 25–75%) | Minimal change; remained consistently high |
| South Asia | **44%** (95% CrI: 13–79%) | High; little improvement |
| East and Southeast Asia / Oceania | **6%** (95% CrI: 1–16%) | Significant decline from 42% in 1991 |
| Latin America and the Caribbean | **11%** (95% CrI: 4–23%) | Declined from 21% in 1991 |
| Global (LMICs) | **29%** (95% CrI: 17–42%) | Declined from 39% in 1991 |

### WHO Prevalence Classification (Countries with VAD as Public Health Problem)

VAD is classified as a **severe public health problem** when prevalence of subclinical deficiency ≥20% in under-5 children:
- **Severe problem** (≥20%): Most of Sub-Saharan Africa, South Asia (India, Bangladesh, Nepal, Pakistan)
- **Moderate problem** (10–19%): Parts of Southeast Asia, Central America, parts of Middle East/North Africa
- **Mild problem** (2–9%): Some Southeast Asian countries post-VAS scale-up (Indonesia, Cambodia by some estimates)
- **No public health problem** (<2%): High-income countries, much of Latin America, East Asia

### Country-Level Highest DALY Rates (2021, GBD 2021)

| Country | Age-Standardized DALY Rate (2021) |
|---------|----------------------------------|
| Somalia | 108.6 per 100,000 |
| Niger | 94.12 per 100,000 |
| Chad | 74.27 per 100,000 |
| Mali | High |
| Central African Republic | High |
| South Sudan | High |
| Burkina Faso | High |
| Democratic Republic of Congo | High |

### Country-Level Fastest Declining DALY Rates (1990–2021, GBD 2021)

| Country | EAPC (DALY rate, 1990–2021) |
|---------|-----------------------------|
| Maldives | −9.8% per year |
| Republic of Korea | −9.51% per year |
| Taiwan | −9.12% per year |

---

## 7. High-Burden Countries: Detailed Profiles

### India

- **Overall prevalence**: 17.54% (CNNS national survey 2016–18, children 0–5 years)
- **Subclinical VAD**: ~21.5% have serum retinol <0.35 µmol/L (NNMB Survey data)
- **Historical surveys**: ~62% of preschool children deficient (older NNMB surveys)
- **Xerophthalmia**: 85% of all South Asian children with xerophthalmia reside in India; ~1 million cases of clinical childhood blindness from xerophthalmia estimated
- **Gender**: Significant increase in VAD among women: 5.9% (2001) → 30.3% (2011)
- **Absolute case burden**: 292,439,000 VAD cases (2019) — highest in world by absolute numbers
- **VAS coverage**: ~60% of children 6–59 months received VAS (NFHS 2015–16)
- **Rice context**: India has lower per-capita rice consumption than Southeast Asia (~60–80 kg/year nationally) but highly variable; rice is the primary staple in eastern and southern states (West Bengal, Odisha, Andhra Pradesh, Tamil Nadu, Kerala) where VAD is most severe
- **Child deaths**: India + Bangladesh constituted approximately one-third of global VAD-attributed child mortality (historical estimates)

### Bangladesh

- **Prevalence**: ~20.5% subclinical VAD in preschool children (national micronutrient survey 2011–12); 21.7% in a nationally representative survey
- **Pregnant women**: 51% with inadequate dietary vitamin A intake; 18.5% with serum retinol <0.70 µmol/L
- **Slum populations**: 38.1% VAD prevalence vs. 21.2% non-slum urban
- **VAS coverage**: Fluctuated from 78.7% (2004) → 62.1% (2011) → 79.3% (2017)
- **Child mortality context**: Malnutrition affects ~41% of under-5 children; VAD contributes substantially
- **Rice dependence**: Rice provides ~70–75% of total daily caloric intake
- **Beta-carotene rice modelling**: Substitution of biofortified rice for white rice in optimistic scenario reduced VAD inadequacy from **78% baseline to <20%** in women; significant reductions in children (Birol et al. 2016, *European Journal of Clinical Nutrition*)

### Indonesia

- **Current classification**: Mild or no public health problem by some estimates (VAD <10%), with VAS coverage ≥70%
- **Historical**: 2.7 per 1,000 children per year developed xerophthalmia → ~63,000 new cases/year nationally
- **Wealth inequality**: High socioeconomic inequality in VAS coverage (SII: 25.30 in 2007)
- **Rice dependence**: Rice provides up to 80% of daily caloric intake; one of world's largest rice consumers
- **Golden Rice relevance**: Substantial population in moderate VAD risk despite improvements; biofortified rice simulations showed 30% reduction in VAD inadequacy in children

### Philippines

- **Classification**: Moderate VAD burden; VAS programs operating
- **Inequality**: Highest wealth-driven inequality in VAS receipt in Southeast Asia (SII: 29.26 in 2003)
- **Rice dependence**: ~100–120 kg/year per capita; rice is primary caloric staple
- **Golden Rice relevance**: Philippines is the site of IRRI's Golden Rice development; local variety GR2E (Golden Rice) approved by BFAD; simulation showed 30% reduction in VAD inadequacy in children with biofortified rice substitution

### Cambodia

- **Current classification**: Mild or no public health problem (VAD <10%) with VAS coverage ≥70%
- **Historical**: 42% VAD prevalence in 1991 (regional Southeast Asia average), declining rapidly
- **VAS coverage**: 42.8% supplementation coverage reported (lower than Ethiopia average)
- **Rice dependence**: ~150–170 kg/year per capita; one of most rice-dependent populations

### Myanmar

- **Data limitation**: Recent nationally representative VAD data limited; survey results not fully published
- **Regional context**: Southeast Asia's VAD declined from 42% to 6% (1991–2013); Myanmar falls within this trajectory
- **Rice dependence**: ~160–180 kg/year; among highest rice consumption in world
- **Sub-national concerns**: Rural highland populations, conflict-affected regions likely retain high VAD burden

### Vietnam

- **Trend**: Significant decline consistent with Southeast Asian regional pattern (42% → 6%, 1991–2013)
- **Rice dependence**: ~120–140 kg/year per capita
- **VAS programs**: Expanded since mid-1990s; substantial coverage achieved

### Sub-Saharan Africa — Nigeria

- **Absolute burden**: 5,520,800 VAD-affected children — largest absolute number in Africa
- **Dry savanna zone**: VAD prevalence >30% (above national average)
- **Agroecological variation**: Significant variation across zones; northern Sahel regions hardest hit
- **Rice consumption**: Growing; rice a significant staple especially in urban areas and coastal regions

### Sub-Saharan Africa — Ethiopia

- **Absolute burden**: ~6.7 million VAD-affected children — often cited as highest in Africa
- **VAS coverage**: Pooled 54.88% (95% CI: 47.34–62.42) per meta-analysis
- **Trend**: Improving but substantial burden remains; VAD interacts with high rates of childhood infectious disease

### Sub-Saharan Africa — DR Congo and Central Africa

- Highest age-standardized incidence and DALY rates in world (GBD 2019, GBD 2021)
- Congo: 250.9 per 100,000 vision loss prevalence (GBD 2017); 14.3 YLD rate
- Somalia: 108.6 DALY rate (GBD 2021); 21.72 mortality ASR per 100,000

---

## 8. How VAD Burden Has Changed Over Time (1990–2024)

### Prevalence Trend (Stevens et al. 2015, supplemented by GBD)

| Year | Global Prevalence in Under-5 (LMICs) | Sub-Saharan Africa | South Asia | East/SE Asia |
|------|-------------------------------------|-------------------|------------|--------------|
| 1991 | 39% (95% CrI: 27–52%) | ~48% | ~44% | ~42% |
| 2000 | ~33% | ~48% | ~44% | ~25–30% |
| 2005 | 33.3% (190M children) | High | High | Declining |
| 2013 | 29% (95% CrI: 17–42%) | 48% (25–75%) | 44% (13–79%) | 6% (1–16%) |
| 2019 | 14.73% (wider age range) | ~24.5% | ~13–17% | Low |
| 2024 (est.) | ~12–15% | ~20–25% | ~10–15% | <5% |

**Regional decline summary:**
- East and Southeast Asia: **Statistically significant decline** (42% → 6%, posterior probability >0.99) — the only region with confirmed significant improvement (Stevens et al. 2015)
- Latin America and Caribbean: **Probable decline** (21% → 11%, PP = 0.89)
- Sub-Saharan Africa: **No significant change** in 22-year period (1991–2013) — prevalence stubbornly high
- South Asia: **No significant improvement** despite VAS program scale-up

### Mortality Trend

| Period | Estimated VAD-Attributable Child Deaths/Year | Key Context |
|--------|---------------------------------------------|-------------|
| ~1990 | **~1.3–2.5 million** | Pre-VAS program era; Beaton/Sommer estimates using VAS trial RRs |
| ~1995–2000 | ~1–1.5 million | VAS programs beginning in some countries |
| ~2000–2005 | ~700,000–1 million | VAS expansion; UNICEF pushing coverage |
| ~2005–2008 | **~600,000–670,000** | Black et al. 2008 (*Lancet*) estimate |
| ~2010 | ~120,000–160,000 | GBD 2010 (methodological revision) |
| ~2013 | **~105,700** (95% UI: 58,500–167,300) | Stevens et al. 2015 — diarrhea + measles only |
| ~2017–2019 | ~100,000–120,000 | GBD 2017–2019 estimates |
| ~2021 | **~17,374** | GBD 2021 (methodological floor); 90.78% decline from 1990 |
| 2020–2022 | Likely increased temporarily | COVID-19 disrupted VAS programs globally; UNICEF reported 15–30% coverage drops |
| 2023–2024 | Recovering toward 2019 levels | VAS programs resuming; 75% global coverage in 2023 (UNICEF) |

### DALY Trend (GBD 2021)

| Year | Global VAD DALYs (millions) | Age-Standardized DALY Rate (per 100,000) |
|------|----------------------------|------------------------------------------|
| 1990 | 18.79 million | 303.72 |
| 2000 | ~12–14 million (est.) | ~200 |
| 2010 | ~6–8 million (est.) | ~100 |
| 2019 | ~1.97 million | ~32 |
| 2021 | **~1.10–2.63 million** | **15.73–40.10** |

**EAPC for DALY rate, 1990–2021**: −2.81% per year (globally); −6.70% for the mortality-weighted GBD 2021 estimate.

### Vitamin A Supplementation Coverage as Driver

VAS program coverage has been the primary driver of improvement in East/Southeast Asia and some parts of South Asia:

- **2023**: 75% of targeted children globally reached with VAS (UNICEF)
- **South Asia**: 83% two-dose coverage in 2023
- **West and Central Africa**: 83% coverage in 2023
- **Coverage quality**: Less than one-third of priority countries achieved high coverage in ≥8 of 10 previous semesters — **fragile and intermittent** in many countries

---

## 9. Rice-Dependent vs. Non-Rice-Dependent Populations

### Why Rice Dependence Matters for VAD

White/milled rice contains **zero beta-carotene (provitamin A)**. In populations where rice constitutes 60–80% of daily caloric intake, vitamin A must come from:
- Animal-source foods (expensive; inaccessible to poor)
- Fruits and vegetables high in carotenoids (seasonal, costly)
- Fortified foods or supplements (program-dependent)

This creates a structural, dietary-pathway link between rice dependence and VAD risk.

### Rice-Dependent Populations with Significant VAD Burden

| Country/Region | Rice as % of Calories | Estimated VAD in Children Under 5 | VAD Burden Assessment |
|---|---|---|---|
| Myanmar | ~70–80% | High (data limited; regional decline) | High structural risk |
| Bangladesh | ~70–75% | ~20–22% (national survey) | Severe public health problem |
| Cambodia | ~65–70% | ~<10% (current); historically high | Improved; moderate risk |
| Vietnam | ~55–65% | Low to moderate (declined sharply) | Improved significantly |
| Indonesia | ~55–65% | ~<10% (current); historically high | Improved; mild problem |
| Philippines | ~50–60% | Moderate; inequality issues | Moderate problem |
| India (East/South) | ~50–70% (regional) | 17–62% depending on survey/region | Severe in many states |
| Laos | ~65–75% | High | Limited data |
| Timor-Leste | ~50–60% | High (poor food systems) | Severe |
| Madagascar (SSA) | ~50–60% | High | Severe; West Africa rice belt |
| Sierra Leone, Guinea, Liberia (SSA rice belt) | ~40–60% | High (SSA rates) | Severe |

### Proportion of Global VAD Burden in Rice-Dependent Populations

**Direct calculation challenge**: No global study has explicitly partitioned VAD burden by staple crop. The following is an evidence-based estimate:

1. **South Asia total**: India, Bangladesh, Nepal, Pakistan — ~44% VAD prevalence (2013); India alone had 292 million VAD cases in 2019 (largest single-country burden globally). However, **wheat** is the primary staple in much of India and Pakistan; rice dependence is concentrated in eastern/southern India and Bangladesh.

2. **Southeast Asia**: ~6% VAD prevalence (2013, regional), but historically much higher; ~87.77 million cases (2019). These are predominantly rice-dependent populations.

3. **East Asia**: Low current burden; China had second-highest absolute VAD cases (GBD 2019) despite very low prevalence, reflecting population size.

4. **Sub-Saharan Africa**: ~48% prevalence (2013); accounts for ~135 million cases (2019). **Primarily non-rice-dependent** — maize, cassava, sorghum, millet dominate most of SSA. Notable exceptions: West Africa rice belt (Senegal, Guinea-Bissau, Guinea, Sierra Leone, Liberia), Madagascar, and urban consumption.

**Rough global estimate**:
- Pure rice-staple populations (Bangladesh, Myanmar, Cambodia, Laos, Vietnam, Philippines, parts of Indonesia, parts of India): roughly **200–300 million** current VAD-affected children and adolescents, representing approximately **60–70% of South/Southeast Asian burden**
- As a share of total global VAD: approximately **35–50%** of all cases globally are in populations with high rice dependence
- As a share of VAD-attributable mortality: likely **40–55%** given the high mortality burden in South Asia and historically rice-dependent Southeast Asia

**GBD 2019 baseline**: Total global VAD cases ~490 million (all ages). South Asia + Southeast Asia share: approximately 180 million (87.77M SE Asia + India ~110M+ rice-belt states). As a fraction: ~37–40% of all cases.

**Key caveat**: Sub-Saharan Africa dominates the mortality and DALY rates per capita and the absolute DALYs in 2021 (low-SDI countries = 51% of global DALYs). Most of this African burden is **not** in rice-dependent populations. This means:
- For VAD **prevalence**, rice-dependent populations (South/Southeast Asia) are major contributors
- For VAD **mortality/DALY burden per child**, Sub-Saharan Africa now dominates
- For **Golden Rice impact potential**, South/Southeast Asia populations offer the clearest dietary pathway intervention

### Summary Table: VAD Burden by Staple Food Context

| Category | Approximate Share of Global VAD Cases | Approximate Share of VAD-Attributable Deaths (modern estimates) |
|---|---|---|
| Primarily rice-dependent (South/SE Asia) | 35–45% | 20–35% |
| Mixed diet with significant rice (South Asia partial) | 15–20% | 15–20% |
| Non-rice dependent (Sub-Saharan Africa, primarily) | 40–50% | 45–60% |

*Note: Sub-Saharan Africa now dominates the mortality burden despite not being rice-dependent, reflecting weak health systems, high infectious disease burden, and inadequate VAS coverage.*

---

## 10. Modeling Parameters and Uncertainty

### Central Estimates for Impact Modeling (2020–2025 Reference Period)

| Parameter | Low Estimate | Central Estimate | High Estimate | Notes |
|-----------|-------------|-----------------|---------------|-------|
| Annual VAD-attributed child deaths (global) | ~17,000 | ~100,000 | ~600,000 | GBD 2021 floor vs. Black 2008 ceiling |
| Annual deaths via diarrhea + measles pathways | 58,500 | **105,700** | 167,300 | Stevens et al. 2015 (2013 data); most defensible |
| Annual blindness cases (children) | 150,000 | 300,000 | 500,000 | WHO range |
| Annual new xerophthalmia cases | 350,000 | 500,000 | 700,000+ | Various estimates |
| Annual global DALYs (VAD-direct) | 1.1 million | 2.0 million | 5+ million | GBD 2021 vs. broader estimates |
| % of mortality burden in South/SE Asia | 30% | 45% | 60% | Stevens et al. regional share |
| % of mortality burden in Sub-Saharan Africa | 35% | 50% | 65% | GBD 2021 dominant region |
| % of global cases in rice-dependent populations | 30% | 40% | 55% | Derived estimate |

### Key Methodological Uncertainties

1. **Attribution method**: VAS trial-based attribution (higher numbers) vs. GBD comparative risk assessment (lower numbers) — **5–10x difference** in mortality estimates is the largest single source of uncertainty.

2. **Causality vs. correlation**: VAD may be a marker of overall poverty and food insecurity rather than an independent causal agent for all attributed deaths. This complicates impact estimates.

3. **Data scarcity**: Two-thirds of priority countries have no VAD data or data >10 years old (UNICEF/Irizarry et al.). Estimates rely heavily on modeled interpolations.

4. **COVID-19 disruption**: VAS coverage dropped 15–30% in 2020–2021; resulting increase in VAD burden not yet fully quantified in published studies.

5. **Sub-Saharan Africa heterogeneity**: Enormous variation across the continent; central and western sub-Saharan Africa bear disproportionate burden.

---

## 11. Key Sources and Citations

### Primary Sources Cited in This Document

1. **Black RE et al.** (for the Maternal and Child Undernutrition Study Group). "Maternal and child undernutrition: global and regional exposures and health consequences." *The Lancet*. 2008; **371**(9608): 243–260. DOI: 10.1016/S0140-6736(07)61690-0. [PubMed 18207566](https://pubmed.ncbi.nlm.nih.gov/18207566/)

2. **Stevens GA, Bennett JE, Hennocq Q, et al.** "Trends and mortality effects of vitamin A deficiency in children in 138 low-income and middle-income countries between 1991 and 2013: a pooled analysis of population-based surveys." *The Lancet Global Health*. 2015; **3**(9): e528–e536. DOI: 10.1016/S2214-109X(15)00039-X. [PubMed 26275329](https://pubmed.ncbi.nlm.nih.gov/26275329/)

3. **GBD 2019 — Zheng C et al.** "Global Burden of Vitamin A Deficiency in 204 Countries and Territories from 1990–2019." *Nutrients*. 2022; **14**(5): 950. DOI: 10.3390/nu14050950. [PMC8912822](https://pmc.ncbi.nlm.nih.gov/articles/PMC8912822/)

4. **GBD 2021 — Frontiers in Nutrition (2025).** "A comprehensive analysis of vitamin A deficiency burden and trends: insights from the global burden of disease study 2021 and future predictions to 2050." *Frontiers in Nutrition*. 2025. [PMC12671203](https://pmc.ncbi.nlm.nih.gov/articles/PMC12671203/)

5. **GBD 2021 — Frontiers in Nutrition (2025, second paper).** "Global, regional, and national burden of vitamin A deficiency (1990–2021) and projections to 2042: associations with sociodemographic development." *Frontiers in Nutrition*. 2025. [Frontiers link](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2025.1689903/full)

6. **GBD 2021 — MDPI Nutrients (2025).** "Trend and Burden of Vitamin A Deficiency in 1990–2021 and Projection to 2050: A Systematic Analysis for the Global Burden of Disease Study 2021." *Nutrients*. 2025; **17**(3): 572. [MDPI](https://www.mdpi.com/2072-6643/17/3/572)

7. **Sarno M et al.** "The prevalence of vitamin A deficiency and its public health significance in children in low- and middle-income countries: A systematic review and modelling analysis." *PLOS Medicine*. 2023. [PMC10416138](https://pmc.ncbi.nlm.nih.gov/articles/PMC10416138/)

8. **GBD 2017 Vision Loss — Du Y et al.** "Global patterns in vision loss burden due to vitamin A deficiency from 1990 to 2017." *Public Health Nutrition*. 2023. [PMC10195433](https://pmc.ncbi.nlm.nih.gov/articles/PMC10195433/)

9. **Raju S et al.** "Prevalence of Vitamin A Deficiency in South Asia: Causes, Outcomes, and Possible Remedies." *ISRN Nutrition*. 2014. [PMC3905635](https://pmc.ncbi.nlm.nih.gov/articles/PMC3905635/)

10. **WHO.** Vitamin A deficiency. WHO Nutrition and Food Safety. [who.int](https://www.who.int/data/nutrition/nlis/info/vitamin-a-deficiency)

11. **WHO (2009).** *Global Prevalence of Vitamin A Deficiency in Populations at Risk 1995–2005: WHO Global Database on Vitamin A Deficiency.* WHO/NHD/09.01. Geneva. [who.int](https://www.who.int/publications/i/item/WHO-NUT-95.3)

12. **UNICEF Data.** Vitamin A Deficiency in Children. [data.unicef.org](https://data.unicef.org/topic/nutrition/vitamin-a-deficiency/)

13. **UNICEF (2018).** "Vitamin A deficiency puts 140 million children at risk of illness and death." UN News. [UN News](https://news.un.org/en/story/2018/05/1008782)

14. **Birol E et al.** "Biofortified β-carotene rice improves vitamin A intake and reduces the prevalence of inadequacy among women and young children in a simulated analysis in Bangladesh, Indonesia, and the Philippines." *European Journal of Clinical Nutrition*. 2016. [PMC4997296](https://pmc.ncbi.nlm.nih.gov/articles/PMC4997296/)

15. **Sommer A & West KP Jr.** (1996). *Vitamin A Deficiency: Health, Survival, and Vision.* Oxford University Press. [Foundational text; PubMed review PMID 1600583](https://pubmed.ncbi.nlm.nih.gov/1600583/)

16. **Golden Rice Project.** Vitamin A Deficiency. [goldenrice.org](https://www.goldenrice.org/Content3-Why/why1_vad.php)

17. **Basis for changes in GBD 2017 and 2019 VAD estimates.** *Public Health Nutrition*. Cambridge Core. [Cambridge Core](https://www.cambridge.org/core/journals/public-health-nutrition/article/basis-for-changes-in-the-disease-burden-estimates-related-to-vitamin-a-and-zinc-deficiencies-in-the-2017-and-2019-global-burden-of-disease-studies/0D3C57D1EF044BA7A1857E7D789F0134)

---

*Document compiled via live web research, March 2026. All statistics should be verified against original sources before use in published work. Where confidence intervals or uncertainty ranges are available, they are provided; point estimates without ranges should be treated with appropriate caution.*
