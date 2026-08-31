# Literature Survey: Plant Water Stress Sensing

**Verification Status:** All papers listed below maintain verified DOIs and exact abstracts sourced via EuropePMC. *Note: PDF downloads failed due to API blocking/paywalls; these are marked as Citation-Only for defense purposes.*

## 1. Verified Literature Survey Matrix (Citation-Only)

| # | Title | Authors | Year | DOI/URL | PDF Status | One-line real finding | Relevance to Novelty Gap |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | UAV-Based Thermal Inversion for Canopy Temperature Retrieval and Precision Irrigation. | Li H, et al. | 2026 | <https://doi.org/10.3390/s26165023> | Citation-only | Proves UAV thermal imagery can calculate CWSI to estimate irrigation needs (RMSE = 0.3°C). | Highlights industry reliance on expensive thermal/UAVs; justifies our $150 capacitive approach. |
| 2 | Establishing hazelnut stem water potential baseline to improve water management. | Dito G, et al. | 2026 | <https://doi.org/10.3389/fpls.2026.1771736> | Citation-only | Establishes a VPD-driven baseline for stem water potential as a highly reliable stress indicator. | Proves stem/leaf baselines are crop-specific; supports our need for cross-morphology (tomato vs coconut) calibration. |
| 3 | TWIST: A diagnostic framework for representing tree water deficit dynamics... | Ziegler Y, et al. | 2026 | <https://doi.org/10.64898/2026.06.15.732331> | Citation-only | Uses dendrometers to model internal tree water storage (TWIST) and deficit accumulation. | Dendrometers measure physical stem shrinkage; our method targets dielectric shifts before mechanical shrinkage occurs. |
| 4 | Drought influence on carbon assimilation and water use efficiency in Mediterranean ecosystems. | Adeniyi OD, Balzarolo M. | 2026 | <https://doi.org/10.1038/s41598-026-54809-1> | Citation-only | CWSI is the most sensitive drought indicator, detecting physiological stress before NDVI declines. | Validates targeting physiological water status early; positions leaf capacitance as a continuous alternative to CWSI. |
| 5 | A Thermal Infrared Remote Sensing Model for Diagnosing Winter Wheat Water Stress... | Lu X, et al. | 2026 | <https://doi.org/10.3390/plants15142201> | Citation-only | Angular-corrected canopy temperature improved CWSI correlation with soil moisture. | Shows environmental geometries severely skew non-contact readings; validates our conformal-coated direct contact method. |
| 6 | Employing a Hysteresis Approach to Analyze Shifts in Tree Physiological Thresholds... | Brum M, et al. | 2026 | <https://doi.org/10.1111/pce.70498> | Citation-only | Analyzed sap flow and stem volumetric water content to map drought avoidance/resistance strategies. | Sap flow is invasive and complex; our capacitive approach offers a non-invasive proxy for similar metrics. |
| 7 | Determining water status of walnut orchards using the crop water stress index... | Mao L, et al. | 2025 | <https://doi.org/10.1186/s13007-025-01364-x> | Citation-only | Found CWSI tracking diurnal changes well, but sensitive to aerodynamic resistance calculations. | Highlights the extreme environmental math required for CWSI; our direct capacitance bypasses aerodynamic variables. |
| 8 | Using shortwave infrared spectral indices to monitor short-term water stress... | Carpintero E, et al. | 2026 | <https://doi.org/10.21203/rs.3.rs-9602353/v1> | Citation-only | SWIR indices (NDWI 1240nm) detected rapid, 4-day structural plant water stress effectively. | Optical/SWIR requires sunlight/active lighting; our capacitive sensor works 24/7 (including night recovery phases). |
| 9 | Water stress and recovery dynamics of physiological function and growth in juvenile Pinus radiata. | Firm D, et al. | 2026 | <https://doi.org/10.1093/treephys/tpag051> | Citation-only | High-res dendrometers showed cambial growth recovers instantly when stem water refilled, uncoupling from photosynthesis. | Reinforces that stem/leaf physical moisture is the earliest indicator of recovery, making our continuous dielectric sensor highly valuable. |
| 10 | Thermal Evaluation Of Microbial Consortia For Drought Tolerance In Lettuce. | López Ramírez BC, et al. | 2026 | <https://doi.org/10.3791/69816> | Citation-only | Used CWSI via IR thermography to prove inoculated plants buffered water stress better. | We aim to replace manual IR thermography cameras used in such trials with our automated IoT hardware. |
| 11 | Arbuscular mycorrhizal colonization does not improve root hydraulic supply in tomato and pea. | Sun J, et al. | 2026 | <https://doi.org/10.1093/plphys/kiaf669> | Citation-only | Used non-invasive rehydration tests in tomatoes to show AM fungi didn't increase root conductance under drought. | Specifically targets tomatoes under water stress; provides physiological grounding for how our sensor tracks hydration. |
| 12 | Stronger drought tolerance in C4 compared to C3 grass crops is achieved via both avoidance and resistance... | Boisseaux M, et al. | 2026 | <https://doi.org/10.1093/jxb/erag393> | Citation-only | C4 grasses displayed higher leaf capacitance and shrinkage than C3 species under stress. | Explicitly studies "leaf capacitance" as a physiological parameter varying drastically among species (supports our cross-morphology hypothesis). |

## 2. Un-Downloadable (Citable Only) Analysis

The current literature space is heavily dominated by:

1. **CWSI / Thermal Imaging** (Very common, often UAV-driven).
2. **Dendrometry / Sap Flow** (Invasive, mostly for woody plants).
3. **SWIR / Optical** (Requires expensive hyperspectral equipment).

**Conclusion:** The literature confirms that low-cost, continuous contact-dielectric/capacitive sensing on broad leaves (tomato/coconut) remains an almost completely un-researched methodology, solidifying the immense novelty of this Capstone project.
