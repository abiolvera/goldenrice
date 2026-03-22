# Vitamin A Supplementation (VAS) Coverage: Annual Series for Golden Rice Impact Model

**Date:** 2026-03-21
**Purpose:** Compile year-specific VAS coverage data (2000–2024) for eight target countries used in the Golden Rice impact model, document structural fragility, and provide recommended model parameters with uncertainty ranges.

---

## Table of Contents

1. [Background and Methodology](#1-background-and-methodology)
2. [Country-by-Country Data Sections](#2-country-by-country-data-sections)
   - [Bangladesh (BGD)](#21-bangladesh-bgd)
   - [Philippines (PHL)](#22-philippines-phl)
   - [India (IND)](#23-india-ind)
   - [Indonesia (IDN)](#24-indonesia-idn)
   - [Vietnam (VNM)](#25-vietnam-vnm)
   - [Myanmar (MMR)](#26-myanmar-mmr)
   - [Cambodia (KHM)](#27-cambodia-khm)
   - [Nigeria (NGA)](#28-nigeria-nga)
3. [Combined Cross-Country Table](#3-combined-cross-country-table)
4. [Structural Fragility Analysis](#4-structural-fragility-analysis)
5. [Key Events Causing Sharp Discontinuities](#5-key-events-causing-sharp-discontinuities)
6. [Delivery Mechanisms and VAS–Polio Linkage](#6-delivery-mechanisms-and-vas-polio-linkage)
7. [Data Gaps and Interpolation Guidance](#7-data-gaps-and-interpolation-guidance)
8. [Recommended Model Parameters by Country and Year](#8-recommended-model-parameters-by-country-and-year)
9. [Sources](#9-sources)

---

## 1. Background and Methodology

### What VAS Coverage Measures

VAS two-dose coverage is defined as the percentage of children aged 6–59 months who received **two** high-dose vitamin A supplements in a calendar year (one per semester). UNICEF is the primary aggregator; data flow from country administrative reports, validated against household surveys (DHS, MICS) when available. The World Bank re-publishes the UNICEF series under indicator `SN.ITK.VITA.ZS`.

### Data Sources Consulted

- **UNICEF Global VAS Coverage Database** — the gold-standard administrative series, updated annually; dataset covers 2000–2023 as of 2025.
- **World Bank Development Indicators** (indicator SN.ITK.VITA.ZS) — mirrors the UNICEF series.
- **IndexMundi** — publishes the UNICEF/World Bank series in tabular form through ~2018.
- **CEIC Data** — Cambodia and selected country series.
- **DHS Program** — nationally-representative household surveys (Bangladesh BDHS 2004, 2007, 2011, 2014, 2017; Philippines NDHS 2022).
- **WHO Public Health Situation Analysis – Myanmar (August 2023)** — post-coup VAS data.
- **FNRI (Philippines Food and Nutrition Research Institute)** — COVID-19 impact study.
- **Published peer-reviewed literature** — country-specific studies cited below.
- **Nutrition International Annual Reports** — programmatic context.

### Caveats

1. **Zero values in the UNICEF/World Bank series for some years almost certainly mean "no data reported," not actual zero coverage.** The UNICEF methods paper explicitly states that missing semesters result in missing annual two-dose estimates, which database consumers sometimes record as zero. The documented Bangladesh 2014 collapse (to ~62% by DHS) was real but not to zero; the UNICEF administrative series showing "0" for 2010, 2011, 2014, and 2018 for Bangladesh likely reflects reporting failures in one or both semesters, not total program cessation.

2. **Administrative data overestimates true coverage** compared to household surveys by a margin that varies by country and year. India's administrative data frequently showed 70%+ while DHS surveys showed 55–63%.

3. **Two-dose coverage is lower than single-dose coverage** because it requires successful delivery in both semesters of the same calendar year.

4. **Data for 2023–2024** is sparse and mostly extrapolated from regional totals.

---

## 2. Country-by-Country Data Sections

### 2.1 Bangladesh (BGD)

**Program Structure:** National Vitamin A Plus Campaign (NVAC), twice per year, run by the Directorate General of Health Services (DGHS) / Institute of Public Health Nutrition (IPHN). Distribution on fixed national days (typically February and July). NOT linked to polio campaigns. Delivered through fixed-site distribution at health facilities and community sites.

**Historical trend:** Bangladesh achieved some of the highest VAS coverage in the world (85–97%) through most of the 2000s using a well-organized biannual mass campaign. Coverage collapsed in 2010–2011 and 2014 due to reporting failures and political disruption. Recovery occurred quickly (99% reported in 2015–2017, 2019–2021). Post-2021 data show continued high administrative coverage with ongoing UNICEF support.

**Bangladesh DHS Survey Data vs. Administrative Data:**

| Year | DHS/Survey % | Admin % (UNICEF) | Notes |
|------|-------------|-----------------|-------|
| 2004 | 78.7 | 83 | BDHS 2004 |
| 2007 | 83.5 | 94 | BDHS 2007 |
| 2011 | 62.1 | 0 (no report) | BDHS 2011; admin data missing |
| 2014 | 62.1 | 0 (no report) | BDHS 2014; political unrest 2013–14 |
| 2017 | 79.3 | 99 | BDHS 2017-18 survey; admin high |

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 85 | Fair | UNICEF admin |
| 2001 | 89 | Fair | UNICEF admin |
| 2002 | 81 | Fair | UNICEF admin |
| 2003 | 87 | Fair | UNICEF admin |
| 2004 | 83 | Good | Corroborated by DHS (~79%) |
| 2005 | 82 | Fair | UNICEF admin |
| 2006 | 89 | Fair | UNICEF admin |
| 2007 | 94 | Good | DHS ~84%; admin likely slightly inflated |
| 2008 | 97 | Fair | UNICEF admin |
| 2009 | 91 | Fair | UNICEF admin |
| 2010 | 0 | Missing | Reporting failure; actual ~85–90% estimated |
| 2011 | 0 | Missing | DHS shows 62%; survey likely caught low-season |
| 2012 | 94 | Fair | UNICEF admin; recovery |
| 2013 | 97 | Fair | UNICEF admin |
| 2014 | 0 | Low | DHS 62%; political unrest + reporting gap |
| 2015 | 99 | Fair | UNICEF admin; post-disruption recovery |
| 2016 | 99 | Fair | UNICEF admin |
| 2017 | 99 | Good | DHS 2017-18 ~73–74% (surveys capture only recent 6 months) |
| 2018 | 0 | Missing | Reporting gap; actual likely 90–95% |
| 2019 | 99 | Fair | UNICEF admin |
| 2020 | 97 | Fair | COVID-19 year; modest disruption |
| 2021 | 96 | Fair | UNICEF admin |
| 2022 | 0 | Missing | Reporting gap; actual likely high (UNICEF HTR program active) |
| 2023 | 99 | Fair | UNICEF admin; NVAC ran June 2023 |

**Key context on the 2014 "collapse":**
The 2014 DHS recorded 62.1% national VAS receipt (any dose in past 6 months), down from 83.5% in 2007. Causes were multi-factorial: (a) political unrest and hartals (political strikes) in 2013–14 disrupting campaign logistics; (b) the 2011 DHS also recorded 62%, but that survey was conducted 6 months after the campaign, capturing the inter-campaign low; (c) urban hard-to-reach populations systematically missed. The UNICEF administrative "0" for 2014 indicates a reporting failure in one or both semesters, not zero actual coverage. The true 2014 two-dose rate was likely ~55–65%.

---

### 2.2 Philippines (PHL)

**Program Structure:** Garantisadong Pambata (GP), twice per year (April and October), run by the Department of Health (DOH). GP is a mass-campaign-style fixed-day distribution integrated with other child health services. NOT linked to polio campaigns. Delivered through barangay health stations and community mobilization.

**Coverage trajectory:** Rose from ~69–78% in 2000 to a peak of 91% in 2009–2011, then declined steadily from 2014 onward. The 2017–2019 Dengvaxia vaccine scandal severely eroded public trust in government health campaigns generally, reducing participation in GP rounds. COVID-19 (2020) further reduced coverage by at least 16 percentage points. By 2022–2023, UNICEF administrative data shows only 10–26%, an extraordinarily low figure that likely reflects continued program dysfunction and data quality issues following multiple disruptions.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 69 | Fair | UNICEF admin |
| 2001 | 76 | Fair | |
| 2002 | 76 | Fair | |
| 2003 | 75 | Fair | |
| 2004 | 85 | Fair | |
| 2005 | 85 | Fair | |
| 2006 | 86 | Fair | |
| 2007 | 83 | Fair | |
| 2008 | 86 | Fair | |
| 2009 | 91 | Good | Peak period |
| 2010 | 91 | Good | |
| 2011 | 91 | Good | |
| 2012 | 90 | Good | |
| 2013 | 89 | Good | |
| 2014 | 83 | Good | Begins gradual decline |
| 2015 | 72 | Good | |
| 2016 | 68 | Good | |
| 2017 | ~65 est. | Estimated | No UNICEF data reported; Dengvaxia scandal breaks Nov 2017 |
| 2018 | ~55 est. | Estimated | Dengvaxia aftermath; vaccine hesitancy peak |
| 2019 | ~50 est. | Estimated | Continued trust deficit; measles outbreak 2019 |
| 2020 | 29 | Fair | COVID-19; FNRI reports ≥16% reduction vs 2019 |
| 2021 | ~30 est. | Estimated | Partial recovery; continued disruption |
| 2022 | 26 | Low | UNICEF admin; very low credibility |
| 2023 | 10 | Very Low | UNICEF admin; data quality concerns |

**Note on 2022–2023 figures:** The figure of 10% in 2023 and 26% in 2022 from UNICEF administrative data may reflect: (a) actual severe program collapse; (b) reporting methodology changes; or (c) the Philippines transitioning VAS delivery away from mass campaigns toward routine health contacts, where reporting coverage denominators differ. A 2022 NDHS showed 79% of children aged 6–59 months received vitamin A, suggesting the administrative series significantly undercounts true coverage or covers only campaign-specific delivery. This discrepancy requires careful handling in the model.

---

### 2.3 India (IND)

**Program Structure:** National Vitamin A Prophylaxis Programme (NVAPP), implemented through the National Health Mission (NHM). Biannual mass campaign in 15 high-burden states, supplemented by routine delivery. NOT linked to polio campaigns; delivered through ICDS (Integrated Child Development Services) anganwadi workers and sub-health centres. India has an ongoing policy debate about shifting from universal to geographically targeted VAS, which has introduced programmatic uncertainty.

**Coverage trajectory:** Started very low (~10%) in 2000, rose steeply to 68% by 2009, then fluctuated between 35–71%. The high variability reflects administrative data quality issues across 15 states reporting separately. The 2016 peak (71%) coincides with intensified NHM implementation. Coverage in 2020 (54%) shows modest COVID-19 impact relative to global averages, possibly because India's VAS is delivered partly through routine anganwadi contacts rather than mass campaigns.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 10 | Low | Very low baseline |
| 2001 | 23 | Low | |
| 2002 | 30 | Low | |
| 2003 | 34 | Low | |
| 2004 | 35 | Low | |
| 2005 | 49 | Fair | |
| 2006 | 25 | Low | Data irregularity |
| 2007 | 36 | Low | |
| 2008 | 57 | Fair | |
| 2009 | 68 | Fair | Peak; NFHS-3 corroborates mid-60s% |
| 2010 | 35 | Low | Unexplained drop; likely reporting artifact |
| 2011 | 58 | Fair | |
| 2012 | 55 | Fair | |
| 2013 | 54 | Fair | |
| 2014 | 61 | Fair | |
| 2015 | 53 | Fair | |
| 2016 | 71 | Fair | NFHS-4 (2015-16): 59.7% — admin inflated |
| 2017 | ~60 est. | Estimated | No data reported |
| 2018 | 56 | Fair | CNNS 2016-18 corroborates ~56% |
| 2019 | ~61 est. | Estimated | NFHS-5 (2019-21) suggests ~71.2% aged 9-35 mo |
| 2020 | 54 | Fair | COVID-19 year; routine delivery more resilient |
| 2021 | ~65 est. | Estimated | Recovery; NFHS-5 published |
| 2022 | ~65 est. | Estimated | Continued routine delivery |
| 2023 | ~68 est. | Estimated | South Asia regional avg = 83%; India may lag |

**Survey cross-checks:**
- NFHS-4 (2015–16): 59.7% received vitamin A in past 6 months
- CNNS 2016–18: ~56%
- NFHS-5 (2019–21): 71.2% among 9–35 months, ~64% for full 9–59 month range

---

### 2.4 Indonesia (IDN)

**Program Structure:** National VAS Programme run by the Ministry of Health (Kementerian Kesehatan). Biannual distribution in February and August through Posyandu (community health posts) and Puskesmas (community health centers). NOT linked to polio campaigns. Vegetable oil fortification with vitamin A made mandatory in 2013 (full effect by 2015), creating an alternative pathway reducing VAS program urgency.

**Coverage trajectory:** Rose from 64–68% in 2000 to a peak of 87% in 2007, then declined gradually to 73–84% range through 2015. A significant drop to 62% is reported for 2017, and 54% for 2020 (COVID-19 impact). Indonesia may be systematically transitioning away from mass VAS campaigns given low measured VAD prevalence (<5% by 2011 national survey), which could explain declining administrative reporting in later years.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 68 | Fair | |
| 2001 | 57 | Fair | |
| 2002 | 61 | Fair | |
| 2003 | 62 | Fair | |
| 2004 | 73 | Fair | |
| 2005 | 76 | Fair | |
| 2006 | 82 | Good | |
| 2007 | 87 | Good | Peak |
| 2008 | 86 | Good | |
| 2009 | 84 | Good | |
| 2010 | 80 | Good | |
| 2011 | 76 | Good | |
| 2012 | 73 | Good | |
| 2013 | 82 | Good | |
| 2014 | 84 | Good | |
| 2015 | 82 | Good | Oil fortification fully in effect |
| 2016 | ~75 est. | Estimated | No UNICEF data |
| 2017 | 62 | Fair | Significant drop; cause unclear |
| 2018 | ~60 est. | Estimated | Riskesdas 2018 national survey year |
| 2019 | ~62 est. | Estimated | No UNICEF data |
| 2020 | 54 | Fair | COVID-19 disruption |
| 2021 | ~55 est. | Estimated | Partial recovery |
| 2022 | ~58 est. | Estimated | Continued recovery |
| 2023 | ~60 est. | Estimated | Indonesia reviewing VAS policy; biomarker study 2023 |

**Note:** Indonesia's 2023 Ministry of Health integrated a serum retinol survey into the Indonesia Health Survey, with results under analysis. This may lead to a formal policy decision on continued VAS prioritization.

---

### 2.5 Vietnam (VNM)

**Program Structure:** National Vitamin A Supplementation Programme, run by the National Institute of Nutrition (NIN). Twice per year. Delivered through commune health stations and routine contacts. NOT linked to polio campaigns. Vietnam achieved near-universal coverage (94–99%) for almost two decades through a strong state-managed health system, making it one of the globally exceptional cases.

**Coverage trajectory:** After a low baseline (~55%) in 1999, Vietnam rapidly scaled to 99% by 2000 and maintained this level almost continuously through 2017. This is a remarkably stable program. Post-2017 data is sparse; the last UNICEF-reported figure is 99% in 2017. Given Vietnam's health system strength and the fact that its VAS is delivered through routine contacts rather than campaign infrastructure, COVID-19 impact was likely modest. However, as VAD prevalence has fallen, there is growing debate about discontinuing or scaling back VAS.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 99 | Good | Major program scale-up complete |
| 2001 | 99 | Good | |
| 2002 | 99 | Good | |
| 2003 | 99 | Good | |
| 2004 | 99 | Good | |
| 2005 | 99 | Good | |
| 2006 | 99 | Good | |
| 2007 | 98 | Good | |
| 2008 | 98 | Good | |
| 2009 | 99 | Good | |
| 2010 | 95 | Good | Slight dip |
| 2011 | 99 | Good | |
| 2012 | 98 | Good | |
| 2013 | — | Missing | No data reported |
| 2014 | 94 | Good | |
| 2015 | 97 | Good | |
| 2016 | 99 | Good | |
| 2017 | 99 | Good | Last confirmed UNICEF data point |
| 2018 | ~95 est. | Estimated | Assumed slight decline as VAD programs reassessed |
| 2019 | ~90 est. | Estimated | Some literature suggests declining emphasis |
| 2020 | ~85 est. | Estimated | COVID-19; routine delivery more resilient than campaigns |
| 2021 | ~85 est. | Estimated | |
| 2022 | ~80 est. | Estimated | |
| 2023 | ~75 est. | Estimated | Regional South Asia context; Vietnam may be winding down |

**Critical uncertainty:** The 2021 figure from the UNICEF WorldBank series appeared as 19.5% in embedded data, which is either a data error, a major program change, or reflects Vietnam's possible removal from the UNICEF priority country list. Given Vietnam's VAD prevalence has fallen well below the 10% public health threshold, Vietnam may have exited the UNICEF priority list, making comparisons before/after that exit misleading. **Models should flag Vietnam post-2018 as high-uncertainty.**

---

### 2.6 Myanmar (MMR)

**Program Structure:** National VAS Programme run by the Department of Public Health, Ministry of Health. Twice per year, delivered through township-level health systems. NOT linked to polio campaigns. Program was functioning well (86–96%) through the mid-2010s.

**Coverage trajectory:** Consistently high coverage (86–96%) from 2001 through 2018, with the 2021 military coup causing catastrophic disruption. Coverage crashed to 37% in 2021, partially recovered to 71% in 2022, but remains far below pre-coup levels. By August 2023, WHO estimated nearly 5 million children were still missing VAS. Pre-coup figure of 93% in 2019 serves as the best comparison baseline.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 66 | Fair | |
| 2001 | 86 | Good | |
| 2002 | 92 | Good | |
| 2003 | 87 | Good | |
| 2004 | 96 | Good | |
| 2005 | 96 | Good | |
| 2006 | 95 | Good | |
| 2007 | 93 | Good | |
| 2008 | 94 | Good | |
| 2009 | 95 | Good | |
| 2010 | 94 | Good | |
| 2011 | 96 | Good | |
| 2012 | 86 | Good | |
| 2013 | 93 | Good | |
| 2014 | 94 | Good | |
| 2015 | 88 | Good | |
| 2016 | 96 | Good | |
| 2017 | 89 | Good | |
| 2018 | 83 | Good | Slight declining trend begins |
| 2019 | 93 | Good | UNICEF/World Bank; Global Nutrition Report confirms |
| 2020 | ~80 est. | Estimated | COVID-19 year; civilian government still in place |
| 2021 | 37 | Good | WHO confirmed; military coup February 2021 |
| 2022 | 71 | Good | WHO confirmed; partial recovery |
| 2023 | ~71 est. | Estimated | WHO Aug 2023 report implies continued constraint |
| 2024 | ~65 est. | Estimated | Continued conflict; 1,087+ attacks on healthcare |

**Myanmar post-coup structural assessment:** Health worker arrests (880+), healthcare facility attacks (180+ damaged), blockades of aid in opposition areas, and collapse of routine health system access make sustained recovery unlikely without political change. The 71% figure for 2022 may reflect heroic efforts by NGOs and remaining public health infrastructure in government-controlled areas, while millions in conflict zones remain unreached.

---

### 2.7 Cambodia (KHM)

**Program Structure:** National VAS Programme run by Ministry of Health (National Maternal and Child Health Center). Twice per year. Delivered through health centers and community outreach. NOT historically linked to polio campaigns. UNICEF has been supporting expanded outreach across 8 provinces since 2022.

**Coverage trajectory:** Cambodia started at low coverage (30%) in 2000 and built rapidly to a peak of 98% in 2009 and 2012 through strong government-UNICEF partnership. Coverage began declining after 2013, reaching the 60–73% range by the late 2010s. COVID-19 did not dramatically worsen Cambodia's VAS compared to other countries (71% in 2020 vs. 72% in 2019). Post-2020 figures remain at 61%, suggesting structural challenges in program reach rather than acute disruption.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 30 | Fair | Low baseline |
| 2001 | 57 | Fair | |
| 2002 | 34 | Fair | Dip |
| 2003 | 47 | Fair | |
| 2004 | 72 | Fair | |
| 2005 | 65 | Fair | |
| 2006 | 78 | Good | |
| 2007 | 76 | Good | |
| 2008 | 88 | Good | |
| 2009 | 98 | Good | Peak; strong program |
| 2010 | 95 | Good | |
| 2011 | 92 | Good | |
| 2012 | 98 | Good | Second peak |
| 2013 | 90 | Good | |
| 2014 | 71 | Good | Decline begins |
| 2015 | 63 | Good | |
| 2016 | 69 | Good | |
| 2017 | 73 | Good | |
| 2018 | ~72 est. | Estimated | No UNICEF data; interpolated from 2017 and 2019 |
| 2019 | 72 | Good | UNICEF confirmed |
| 2020 | 71 | Good | COVID-19 minimal impact; routine delivery resilient |
| 2021 | 61 | Good | Decline; cause unclear (possibly denominator changes) |
| 2022 | 61 | Good | UNICEF admin; flat |
| 2023 | ~65 est. | Estimated | UNICEF support to 8 provinces active; modest improvement expected |

---

### 2.8 Nigeria (NGA)

**Program Structure:** Historically linked to polio National Immunization Days (NIDs) — vitamin A was bundled as a "plus" during polio campaigns since the early 2000s. With polio eradication progress and wind-down of polio NIDs, Nigeria transitioned toward the biannual Maternal, Newborn and Child Health (MNCH) Week delivery model, implemented by state Primary Health Care Development Agencies (PHCDAs) in partnership with UNICEF and Nutrition International. Nigeria also uses Seasonal Malaria Chemoprevention (SMC) campaigns in the north as a potential new VAS delivery platform.

**Coverage trajectory:** Extremely volatile due to dependency on campaign infrastructure. Multiple years of near-zero coverage in the early 2000s (2000, 2003, 2008) when polio campaigns were suspended or missed. Reached a peak of 91% in 2010. Declined to 56% in 2016 with polio NID wind-down; partially recovered to 80–83% in 2017–2018 using MNCH weeks. COVID-19 (2020) likely caused a significant drop (appears as "0" in World Bank data, likely a reporting failure; actual coverage from campaign data in Borno state confirms some activity). By 2021, coverage estimated at 57% nationally, with UNICEF database figure of 89% for 2023 appearing high and potentially reflecting recovered administrative reporting.

**Annual UNICEF Administrative Data:**

| Year | Coverage (%) | Data Quality | Notes |
|------|-------------|-------------|-------|
| 2000 | 0 | Missing | Polio NID not conducted; reporting gap |
| 2001 | 64 | Fair | |
| 2002 | 31 | Low | Partial NID coverage |
| 2003 | 0 | Missing | |
| 2004 | 76 | Fair | |
| 2005 | 40 | Low | |
| 2006 | 61 | Fair | |
| 2007 | 55 | Fair | |
| 2008 | 0 | Missing | |
| 2009 | 78 | Fair | |
| 2010 | 91 | Good | Peak; multiple polio NIDs with bundled VAS |
| 2011 | 73 | Fair | |
| 2012 | 78 | Fair | |
| 2013 | 70 | Fair | |
| 2014 | 80 | Fair | |
| 2015 | 76 | Fair | Polio NID phase-down begins |
| 2016 | 56 | Fair | Polio NID wind-down; transition gap |
| 2017 | 83 | Fair | MNCH weeks recovery |
| 2018 | 80 | Fair | Stable via MNCH; some sources report 45% (DHS-comparable) |
| 2019 | 62 | Fair | UNICEF admin; downtrend resumes |
| 2020 | 0 | Missing | COVID-19 + reporting failure; Borno campaign confirmed |
| 2021 | 57 | Fair | Significant decline confirmed; peer-reviewed sources |
| 2022 | ~65 est. | Estimated | Partial recovery; SMC integration efforts |
| 2023 | 89 | Low-Fair | UNICEF admin; possibly inflated |

**Critical note on 2018 discrepancy:** A 2019 journal publication using DHS-comparable data reported 45% coverage in 2018, while UNICEF administrative data shows 80%. This ~35 percentage point gap is among the largest in the dataset and underscores the known problem with Nigerian administrative VAS data — campaigns are reported as conducted but actual child reach may be far lower.

---

## 3. Combined Cross-Country Table

Coverage (%) by country and year. Values marked with an asterisk (*) are estimates or interpolations; blank cells indicate no data. Zeros in the original UNICEF/World Bank series are treated as missing and not shown.

| Year | BGD | PHL | IND | IDN | VNM | MMR | KHM | NGA |
|------|-----|-----|-----|-----|-----|-----|-----|-----|
| 2000 | 85 | 69 | 10 | 68 | 99 | 66 | 30 | — |
| 2001 | 89 | 76 | 23 | 57 | 99 | 86 | 57 | 64 |
| 2002 | 81 | 76 | 30 | 61 | 99 | 92 | 34 | 31 |
| 2003 | 87 | 75 | 34 | 62 | 99 | 87 | 47 | — |
| 2004 | 83 | 85 | 35 | 73 | 99 | 96 | 72 | 76 |
| 2005 | 82 | 85 | 49 | 76 | 99 | 96 | 65 | 40 |
| 2006 | 89 | 86 | 25 | 82 | 99 | 95 | 78 | 61 |
| 2007 | 94 | 83 | 36 | 87 | 98 | 93 | 76 | 55 |
| 2008 | 97 | 86 | 57 | 86 | 98 | 94 | 88 | — |
| 2009 | 91 | 91 | 68 | 84 | 99 | 95 | 98 | 78 |
| 2010 | 85* | 91 | 35 | 80 | 95 | 94 | 95 | 91 |
| 2011 | 70* | 91 | 58 | 76 | 99 | 96 | 92 | 73 |
| 2012 | 94 | 90 | 55 | 73 | 98 | 86 | 98 | 78 |
| 2013 | 97 | 89 | 54 | 82 | — | 93 | 90 | 70 |
| 2014 | 60* | 83 | 61 | 84 | 94 | 94 | 71 | 80 |
| 2015 | 99 | 72 | 53 | 82 | 97 | 88 | 63 | 76 |
| 2016 | 99 | 68 | 71 | 75* | 99 | 96 | 69 | 56 |
| 2017 | 99 | 65* | 60* | 62 | 99 | 89 | 73 | 83 |
| 2018 | 90* | 55* | 56 | 60* | 95* | 83 | 72* | 80 |
| 2019 | 99 | 50* | 61* | 62* | 90* | 93 | 72 | 62 |
| 2020 | 97 | 29 | 54 | 54 | 85* | 80* | 71 | 55* |
| 2021 | 96 | 30* | 65* | 55* | 85* | 37 | 61 | 57 |
| 2022 | 90* | 26 | 65* | 58* | 80* | 71 | 61 | 65* |
| 2023 | 99 | 10 | 68* | 60* | 75* | 71* | 65* | 89 |
| 2024 | 95* | 15* | 68* | 60* | 70* | 65* | 65* | 85* |

**Notes:**
- BGD 2010, 2011: UNICEF shows "0" (reporting gap); estimates based on DHS data trend and program continuity knowledge.
- BGD 2014: UNICEF shows "0"; DHS 2014 shows 62% any-dose; estimated two-dose ~55–65%.
- PHL 2017–2019: No UNICEF data; estimates based on Dengvaxia impact trajectory and FNRI COVID study baseline.
- VNM 2018–2024: UNICEF data ends 2017; estimates based on program structure and regional trends.
- MMR 2020: No confirmed data; estimated based on COVID-19 global patterns and pre-coup government functioning.
- NGA 2020: UNICEF shows "0" (reporting failure); Borno state campaign confirmed some activity; estimated 55%.
- NGA 2023: UNICEF admin shows 89%, which may overestimate actual two-dose coverage; model should treat with caution.

---

## 4. Structural Fragility Analysis

### Why VAS Coverage Has Collapsed and Can Collapse Again

VAS programs are uniquely fragile among childhood nutrition interventions because they share none of the self-sustaining properties of dietary change or food fortification. The following structural vulnerabilities apply to all eight target countries to varying degrees.

#### 4.1 Platform Dependency

**The VAS-polio linkage (most critical for Nigeria):**
For decades, vitamin A was bundled with oral polio vaccine (OPV) during National Immunization Days in Nigeria and other countries with active polio eradication campaigns. This created a powerful delivery platform with dedicated funding, logistics, and community mobilization. As polio has been eliminated (wild poliovirus) from Africa and Asia, the polio NID infrastructure has been systematically dismantled. The UNICEF "Coverage at a Crossroads" report (2018) documented that this was a primary driver of the 2015–2016 global collapse, when the number of unprotected children tripled from 19 million to 62 million. West and Central Africa coverage fell from 79% (2015) to 54% (2016).

Nigeria's VAS history is a clear illustration: years with active polio NIDs show high coverage (76–91%), years where NIDs were suspended or reduced show coverage near zero or very low (0%, 31%, 40%, 55%).

**Other campaign platforms:**
Bangladesh's NVAC, Cambodia's biannual health day, and Philippines' Garantisadong Pambata are all dedicated campaigns that require independent annual funding cycles, logistics, and community mobilization. Campaigns are inherently more fragile than routine health services because they can be cancelled, delayed, or defunded in a single budget decision, a political disruption, or a public health emergency.

**Routine delivery:**
India and Vietnam deliver VAS substantially through routine health system contacts (anganwadi workers, commune health stations). This is more resilient to acute shocks but less efficient for reaching hard-to-reach populations and depends on sustained frontline health worker capacity. India's VAS coverage fluctuations (10–71%) reflect the difficulty of coordinating biannual campaigns across 15 major states with different administrative capacities.

#### 4.2 Acute Shock Vulnerabilities

**Political disruption (Myanmar):**
The February 2021 military coup reduced Myanmar's VAS coverage from 93% (2019) to 37% (2021) — a 56 percentage point collapse in a single year. The mechanism was multi-channel: health worker strikes and arrests, attacks on health facilities, conflict-zone access restrictions, and population displacement. Recovery to 71% (2022) is partial and potentially illusory for conflict areas.

**Vaccine/health program confidence loss (Philippines):**
The Dengvaxia scandal (2017–2019) eroded trust in government health programs generally, not just the dengue vaccine specifically. VAS is delivered alongside other GP services; parental hesitancy to attend community health events reduced all GP service uptake. This is an example of how a scandal in one health program can spill over to unrelated interventions. Coverage in the Philippines declined from 68% (2016) to an estimated 29–50% range by 2019–2020.

**Pandemic disruption (COVID-19):**
The global 19 percentage point drop in 2020 was driven by suspension of mass health campaigns in the first half of 2020. Routine-delivery-dependent programs (India, Vietnam) were more resilient. Campaign-dependent programs (Philippines, Nigeria) were more severely disrupted. Sub-Saharan Africa coverage fell to approximately 40% in 2020, and some high-mortality countries reached only 24% two-dose coverage.

**Political unrest (Bangladesh 2013–2014):**
Hartals and political strikes in Bangladesh in 2013–14 disrupted campaign logistics and health worker deployment. The DHS-measured coverage drop from ~84% (2007) to 62% (2014) coincided with this period of instability.

#### 4.3 Funding Fragility

VAS programs in most countries depend on a combination of government budget (capsule procurement, health worker time) and donor funding (UNICEF, Nutrition International, GAVI-related). Gaps in either stream can interrupt campaigns. Bangladesh's NVAC has historically benefited from strong donor support but hard-to-reach areas remained uncovered until UNICEF introduced the GMP card system in 2022. Nigeria's MNCH Week campaigns require state-level political commitment and often depend on Nutrition International technical assistance.

#### 4.4 Denominator and Transition Issues

Some apparent coverage declines may reflect transitions in delivery model or reporting methodology rather than actual child reach. Indonesia's 2017 drop from 82% to 62% may partly reflect a shift in how coverage is calculated as the program transitioned and oil fortification reduced program urgency. The Philippines' 10% figure in 2023 is almost certainly affected by program restructuring. These transitions introduce artificial discontinuities in the administrative data series.

---

## 5. Key Events Causing Sharp Discontinuities

| Event | Year(s) | Countries | Estimated Coverage Impact |
|-------|---------|-----------|--------------------------|
| Polio NID wind-down | 2015–2016 | Nigeria, W/C Africa broadly | Nigeria: −20%; W/C Africa: −25% (78→54%) |
| Bangladesh political unrest | 2013–2014 | BGD | −20 to −30 pp vs. peak |
| Dengvaxia scandal | 2017–2019 | PHL | Estimated −20 to −30 pp |
| COVID-19 (global) | 2020 | All countries | −19 pp globally; campaign-dependent −25 to −40 pp |
| Myanmar military coup | 2021 | MMR | −56 pp (93% → 37%) |
| Myanmar partial recovery | 2022 | MMR | +34 pp (37% → 71%); fragile |
| Philippines program collapse | 2020–2023 | PHL | From ~50% → 10–29% (severe) |
| Vietnam data gap/policy change | 2018+ | VNM | Unknown; potentially −15 to −25 pp |

---

## 6. Delivery Mechanisms and VAS–Polio Linkage

| Country | Primary Delivery | Polio-linked? | Secondary Delivery | Resilience to Shock |
|---------|-----------------|-------------|-------------------|-------------------|
| Bangladesh (BGD) | Biannual national campaign (NVAC) | No | Fixed-site + outreach | Moderate |
| Philippines (PHL) | Biannual mass campaign (GP) | No | Routine health contacts | Low (demonstrated collapse) |
| India (IND) | Biannual campaign (NHM/ICDS) | No | Routine anganwadi workers | Moderate |
| Indonesia (IDN) | Biannual posyandu distribution | No | Puskesmas routine | Moderate-High |
| Vietnam (VNM) | Biannual campaign + routine | No | Commune health stations | High (historically) |
| Myanmar (MMR) | Biannual township health | No | Community outreach | Low (post-coup) |
| Cambodia (KHM) | Biannual health day + outreach | No | Health center routine | Moderate |
| Nigeria (NGA) | MNCH Week + SMC (N) | Historically yes; now transitioning | State PHCDA campaigns | Low-Moderate |

**Key finding:** None of the eight target countries now delivers VAS primarily through polio campaigns. However, Nigeria's entire coverage pattern from 2000–2015 was structured around OPV delivery platforms, and the dismantling of that infrastructure remains the primary explanation for Nigeria's volatile 2015–2021 coverage. For the Golden Rice model, Nigeria's structural delivery fragility is the highest of all eight countries.

---

## 7. Data Gaps and Interpolation Guidance

### 7.1 Countries with High-Quality Continuous Data (2000–2022)

- **Cambodia:** Good series 2000–2022 with only 2018 missing; interpolate linearly.
- **Indonesia:** Good series 2000–2017 with 2016 missing; 2020 confirmed; 2018–2019 and 2021–2023 estimated.
- **Myanmar:** Excellent series 2000–2019; 2020–2024 from WHO post-coup reports.
- **Nigeria:** Series 2000–2021 with multiple missing years (treat zeros as missing, not zero); interpolate within confirmed data brackets.

### 7.2 Countries with Data Gaps Requiring Careful Handling

- **Bangladesh:** Multiple reporting gaps (2010, 2011, 2014, 2018, 2022) where UNICEF shows "0." DHS data provides survey-based anchors for 2004, 2007, 2011, 2014, 2017. For 2010–2011, estimate ~85% (program continued, DHS timing issue). For 2014, estimate ~60% (DHS confirmed). For 2018 and 2022, estimate 90–95% based on pre/post trend.
- **Philippines:** Data ends at 2016 in the reliable series; 2020, 2022, 2023 available but anomalously low; 2017–2019 must be estimated using Dengvaxia impact documented trajectory.
- **India:** Irregular data with 2017, 2019, 2021–2024 missing; India's NFHS survey anchors (2015-16, 2019-21) provide verification; India's coverage is genuinely volatile, so interpolation uncertainty is high.
- **Vietnam:** Data ends at 2017 in confirmed UNICEF series; all subsequent years are estimates; Vietnam may have exited UNICEF priority list as VAD fell below threshold.

### 7.3 Interpolation Rules

1. **Linear interpolation** between confirmed anchor points is appropriate for countries with stable programs (Vietnam 2000–2017, Cambodia 2000–2020, Indonesia 2000–2015).
2. **Step-change models** are needed at documented discontinuity events: Myanmar 2021 (sharp drop), Philippines 2020 (sharp drop), Nigeria 2016 (structural change). Do NOT use linear interpolation across these breaks.
3. **Survey data overrides administrative data** when both exist and conflict. DHS provides the better true-coverage estimate; administrative data systematically overcounts.
4. **Missing-as-missing vs. missing-as-zero:** Treat all UNICEF/World Bank zero values with caution. Only Bangladesh 2014 and Nigeria's early-2000s years have a plausible argument for genuinely low (though not zero) coverage. All other zeros should be imputed from trend.
5. **Post-2021 Vietnam:** Without confirmed data, use declining trajectory from 99% (2017) toward an estimated 70–80% by 2023, reflecting program de-emphasis as VAD falls below public health threshold.

---

## 8. Recommended Model Parameters by Country and Year

The following table provides best-estimate central values and uncertainty ranges for use in the Golden Rice impact model. Uncertainty is expressed as ±percentage points around the central estimate. Where the UNICEF administrative figure is used, a systematic downward correction of approximately 10 pp is applied for countries where DHS surveys consistently show lower values.

**Confidence levels:** H = High (confirmed data, multiple sources), M = Medium (single data source or extrapolated), L = Low (estimated from indirect evidence).

### Bangladesh (BGD)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 82 | 8 | M | UNICEF admin 85; slight survey adjustment |
| 2002 | 81 | 8 | M | UNICEF admin |
| 2004 | 80 | 6 | H | DHS 79% + admin 83% |
| 2007 | 88 | 6 | H | DHS 84% + admin 94% (admin inflated) |
| 2009 | 88 | 8 | M | Admin 91% |
| 2010 | 83 | 10 | L | Estimated; reporting gap |
| 2011 | 63 | 12 | M | DHS 62%; admin missing |
| 2013 | 90 | 8 | M | Admin 97%; DHS between surveys |
| 2014 | 60 | 12 | M | DHS 62%; admin missing (political disruption) |
| 2015 | 90 | 8 | M | Admin 99%; slight adjustment |
| 2017 | 75 | 10 | H | DHS 73-74%; admin 99% (inflated) |
| 2019 | 90 | 8 | M | Admin 99%; slight adjustment |
| 2020 | 88 | 8 | M | Admin 97%; modest COVID impact |
| 2021 | 87 | 8 | M | Admin 96% |
| 2023 | 90 | 8 | M | Admin 99%; UNICEF HTR program active |

### Philippines (PHL)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 69 | 8 | M | UNICEF admin |
| 2004 | 85 | 6 | H | Admin stable period |
| 2009 | 91 | 5 | H | Peak; consistent admin series |
| 2012 | 90 | 5 | H | |
| 2014 | 83 | 6 | H | Admin |
| 2015 | 72 | 6 | H | Admin |
| 2016 | 68 | 6 | H | Admin |
| 2017 | 60 | 12 | L | Estimated; Dengvaxia begins Nov 2017 |
| 2018 | 50 | 15 | L | Estimated; peak hesitancy year |
| 2019 | 45 | 15 | L | Estimated; measles outbreak context |
| 2020 | 35 | 12 | M | FNRI: ≥16% drop from 2019; admin 29% |
| 2021 | 30 | 15 | L | Estimated |
| 2022 | 28 | 15 | L | Admin 26%; NDHS 2022 shows 79% (major discrepancy) |
| 2023 | 25 | 20 | L | Admin 10%; possibly methodology-driven |

**Critical modeling note for Philippines:** The 2022 NDHS shows 79% of children received vitamin A, while UNICEF administrative data shows 26%. The model should consider treating these as measuring different things (NDHS = any dose in past 6 months vs. two-dose in calendar year) and use a best-estimate two-dose rate of approximately 50–60% for 2022 based on the NDHS figure discounted for two-dose compliance.

### India (IND)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 10 | 8 | M | Admin; very low baseline |
| 2005 | 49 | 10 | M | Admin |
| 2009 | 58 | 12 | M | Admin 68%; survey data likely 55-60% |
| 2012 | 55 | 10 | M | Admin; NFHS corroboration |
| 2015 | 56 | 10 | H | NFHS-4 (2015-16): 59.7%; admin 53-71% |
| 2016 | 62 | 10 | H | Midpoint admin (71%) and NFHS (59%) |
| 2018 | 56 | 10 | H | Admin 56%; CNNS 2016-18 corroborates |
| 2019 | 62 | 10 | M | NFHS-5 upper bound suggests ~65% |
| 2020 | 54 | 10 | M | Admin; COVID modest impact on routine delivery |
| 2021 | 63 | 10 | M | NFHS-5 2019-21 upper range |
| 2023 | 66 | 12 | L | Estimated; South Asia avg 83% but India lags |

### Indonesia (IDN)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 68 | 8 | M | Admin |
| 2005 | 76 | 8 | M | Admin |
| 2007 | 87 | 6 | H | Admin peak; credible |
| 2010 | 80 | 8 | H | Admin |
| 2014 | 84 | 6 | H | Admin |
| 2015 | 82 | 6 | H | Admin |
| 2017 | 62 | 10 | M | Admin; unexplained drop |
| 2020 | 54 | 10 | M | Admin; COVID |
| 2023 | 58 | 15 | L | Estimated; policy review underway |

### Vietnam (VNM)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 99 | 3 | H | Admin; sustained program |
| 2005 | 99 | 3 | H | |
| 2010 | 95 | 5 | H | Admin dip |
| 2015 | 97 | 5 | H | Admin |
| 2017 | 99 | 3 | H | Last confirmed UNICEF point |
| 2018 | 92 | 12 | L | Estimated; program assessment period |
| 2020 | 83 | 15 | L | Estimated; routine delivery resilient |
| 2022 | 78 | 18 | L | Estimated; possible priority list exit |
| 2023 | 73 | 20 | L | Estimated |

### Myanmar (MMR)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 66 | 8 | M | Admin |
| 2005 | 96 | 4 | H | Admin; sustained strong program |
| 2010 | 94 | 4 | H | Admin |
| 2015 | 88 | 6 | H | Admin |
| 2017 | 89 | 6 | H | Admin |
| 2019 | 93 | 5 | H | Admin; Global Nutrition Report confirmed |
| 2020 | 78 | 12 | L | Estimated; COVID + civilian govt |
| 2021 | 37 | 8 | H | WHO confirmed; post-coup collapse |
| 2022 | 71 | 8 | H | WHO confirmed; partial recovery |
| 2023 | 68 | 12 | M | Estimated; WHO Aug 2023 context |
| 2024 | 62 | 15 | L | Estimated; continued conflict |

### Cambodia (KHM)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2000 | 30 | 10 | M | Admin |
| 2004 | 72 | 8 | M | Admin |
| 2009 | 98 | 3 | H | Admin peak; two-source confirmation |
| 2012 | 98 | 3 | H | Admin |
| 2015 | 63 | 8 | H | Admin |
| 2017 | 73 | 8 | H | Admin |
| 2019 | 72 | 8 | H | Admin; CEIC confirmed |
| 2020 | 71 | 8 | H | Admin |
| 2021 | 61 | 8 | H | Admin |
| 2022 | 61 | 8 | H | Admin |
| 2023 | 64 | 10 | M | Estimated; UNICEF 8-province program |

### Nigeria (NGA)

| Year | Central (%) | ±pp | Conf. | Basis |
|------|------------|-----|-------|-------|
| 2001 | 64 | 15 | L | Admin; NID-dependent; high uncertainty |
| 2004 | 76 | 12 | M | Admin |
| 2009 | 78 | 10 | M | Admin |
| 2010 | 85 | 10 | M | Admin 91%; true two-dose likely lower |
| 2014 | 72 | 12 | M | Admin 80%; DHS-comparable sources lower |
| 2015 | 68 | 12 | M | Admin 76%; NID wind-down begins |
| 2016 | 50 | 15 | M | Admin 56%; transition gap |
| 2017 | 70 | 15 | M | Admin 83%; MNCH Week recovery |
| 2018 | 50 | 15 | M | Admin 80% vs. survey ~45%; use midpoint |
| 2019 | 55 | 12 | M | Admin 62% |
| 2020 | 45 | 20 | L | Estimated; COVID + reporting gap |
| 2021 | 52 | 15 | M | Literature confirms ~57% |
| 2022 | 60 | 15 | L | Estimated; recovery with SMC integration |
| 2023 | 70 | 15 | L | Admin 89%; likely overstated; best est. 65–75% |

---

## 9. Sources

### Primary Data Sources

1. **UNICEF Global Vitamin A Supplementation Database** — country-level annual two-dose coverage, 2000–2023. Updated August 2025.
   URL: https://data.unicef.org/resources/dataset/vitamin-supplementation/

2. **World Bank Development Indicators** — Vitamin A supplementation coverage rate (% of children ages 6–59 months), indicator SN.ITK.VITA.ZS. Sourced from UNICEF Global Databases.
   URL: https://data.worldbank.org/indicator/SN.ITK.VITA.ZS

3. **IndexMundi** — UNICEF/World Bank VAS coverage rate data by country, 1999–2018 tabular extractions.
   URL: https://www.indexmundi.com/facts/indicators/SN.ITK.VITA.ZS

4. **CEIC Data** — Cambodia VAS coverage time series.
   URL: https://www.ceicdata.com/en/cambodia/social-health-statistics/kh-vitamin-a-supplementation-coverage-rate--of-children-aged-659-months

### Key Reports and Publications

5. **UNICEF (2018). "Coverage at a Crossroads: New Directions for Vitamin A Supplementation Programmes."**
   Documents the 2015–2016 global collapse, polio NID linkage, and trajectory of VAS programs. This is the foundational reference for structural fragility analysis.
   URL: https://www.unicef.org/media/48031/file/Vitamin-A-report-ENG.pdf
   Also at: https://data.unicef.org/resources/vitamin-a-coverage/

6. **UNICEF (2020). "Methods and Processes for the UNICEF Global Database: Estimates of Vitamin A Supplementation Coverage in Preschool-age Children."**
   Explains why zero values may mean missing data, and how administrative data is validated.
   URL: https://data.unicef.org/wp-content/uploads/2020/03/Vitamin-a-methods-paper.pdf

7. **WHO (2023). "Public Health Situation Analysis – Myanmar. August 2023."**
   Provides confirmed 2021 (37%) and 2022 (71%) Myanmar VAS coverage figures.
   URL: https://cdn.who.int/media/docs/default-source/searo/myanmar/documents/public-health-situation-analysis-phsa_myanmar_august-2023.pdf

8. **ReliefWeb / BMJ Global Health (2021). "COVID-19 caused significant declines in regular vitamin A supplementation for young children in 2020."**
   Documents the 19 percentage point global decline and country-specific impacts.
   URL: https://reliefweb.int/report/world/covid-19-caused-significant-declines-regular-vitamin-supplementation-young-children

9. **Islam et al. (2021). "Trends and Socioeconomic Inequalities in Receiving Vitamin A Supplementation Among Children Aged 6–59 Months in Bangladesh: Analysis of Nationwide Cross-Sectional Data from 2004 to 2017." PMC11773645.**
   Provides Bangladesh DHS-based annual coverage: 2004 (78.7%), 2007 (83.5%), 2011 (62.1%), 2014 (62.1%), 2017 (79.3%).
   URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11773645/

10. **Victora et al. (2017). "Vitamin A Supplementation Programs and Country-Level Evidence of Vitamin A Deficiency." Nutrients 9(3):190. PMC5372853.**
    Country-level VAS coverage and VAD status for 2014; documents Bangladesh 0% reporting anomaly.
    URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5372853/

11. **Oddo VM et al. (2023). "COVID-19 concerns among caregivers and vitamin A supplementation coverage among children aged 6–59 months in four countries in Western sub-Saharan Africa." Public Health Nutrition. PMC10564591.**
    URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10564591/

12. **Castillo-Lancellotti C et al. (2023). "Sub-national estimates of vitamin A supplementation." medRxiv preprint.**
    URL: https://www.medrxiv.org/content/10.1101/2023.05.09.23289711v1.full.pdf

13. **FNRI Philippines (2023). "Food and Nutrition Security in the Philippines During the COVID-19 Pandemic." PMC10336346.**
    Documents ≥16% VAS coverage decline in Philippines in 2020; Operation Timbang drop from 83% to 51%.
    URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10336346/

14. **Gates Foundation (2018). "The Danger of Complacency: Lost Progress in Vitamin A Distribution."**
    URL: https://www.gatesfoundation.org/ideas/articles/lost-progress-in-vitamin-a-distribution

15. **Lancet (2018). "Vitamin A Distribution in Danger." Vol. 391(10138).**
    URL: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)31035-3/fulltext

16. **Science Direct (2016). "Experience of Integrating Vitamin A Supplementation into Polio Campaigns in the African Region."** Vaccine 34(43).
    URL: https://www.sciencedirect.com/science/article/pii/S0264410X16303826

17. **Dengvaxia controversy and Philippines vaccine hesitancy.**
    Multiple sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC6214489/

18. **UNICEF Bangladesh (2024). "UNICEF's Vitamin A Supplementation Programme Achieved 100% Coverage Reaching Vulnerable Children in Hard-to-Reach Areas."**
    URL: https://bangladesh.un.org/en/273027-unicef%E2%80%99s-vitamin-supplementation-programme-achieved-100-coverage-reaching-vulnerable

19. **Insecurity Insight / Human Rights Watch (2024). "A Tragic Milestone: More Than 1,000 Attacks on Health Care in Myanmar Since February 2021 Coup."**
    URL: https://reliefweb.int/report/myanmar/tragic-milestone-more-1000-attacks-health-care-myanmar-february-2021-military-coup

20. **Nutrition International (2023). Annual Report 2022–2023: Vitamin A Programming.**
    URL: https://www.nutritionintl.org/annual-report-2022-2023/2022-vitamin-a-programming/

21. **Global Nutrition Report. Country nutrition profiles for Myanmar, Vietnam, Cambodia, Indonesia.**
    URLs:
    https://globalnutritionreport.org/resources/nutrition-profiles/asia/south-eastern-asia/myanmar/
    https://globalnutritionreport.org/resources/nutrition-profiles/asia/south-eastern-asia/viet-nam/
    https://globalnutritionreport.org/resources/nutrition-profiles/asia/south-eastern-asia/cambodia/
    https://globalnutritionreport.org/resources/nutrition-profiles/asia/south-eastern-asia/indonesia/

22. **WHO/UNICEF UNICEF data.unicef.org topic page on Vitamin A Deficiency.**
    Reports 2023 global coverage = 75%; South Asia = 83%.
    URL: https://data.unicef.org/topic/nutrition/vitamin-a-deficiency/

23. **Our World in Data. "Share of Children Receiving Vitamin A Supplementation."**
    URL: https://ourworldindata.org/grapher/vitamin-a-supplementation-coverage-rate-children-ages-6-59-months

24. **NHM India. Vitamin A Supplementation Programme Overview.**
    URL: https://nhm.gov.in/index1.php?lang=1&level=3&sublinkid=1452&lid=801

25. **India NFHS-4 (2015–16) and NFHS-5 (2019–21)** — national survey anchors for India VAS coverage.

---

*File compiled: 2026-03-21. Research based on web-accessible databases and published literature as of that date. The UNICEF downloadable dataset (https://data.unicef.org/resources/dataset/vitamin-supplementation/) contains the most authoritative annual figures and should be downloaded directly for model implementation; values shown here represent a curated synthesis for model anchor points.*
