# Novelty Gap Analysis

**WARNING**: This gap analysis must be directly defended alongside the 15 specific papers collected in `LITERATURE_SURVEY.md`. Use this document to demonstrate *why* your project is uniquely publishable compared to those exact papers.

## 1. Cross-Morphology Dielectric Failure (The Biological Gap)

Reviewing standard literature (e.g., papers focusing on Maize or Wheat capacitive sensing), capacitive models treat leaves as uniform dielectric slabs.

- **The Gap**: None of the 15 verified references account for extreme cuticle variance—specifically the thick, waxy, highly resistive cuticle of **Coconut fronds**, which acts as a massive series dielectric spacer that destroys the sensitivity of standard interdigitated capacitive curves calibrated on thin leaves.
- **Our Novelty**: By categorizing morphology as a distinct regression parameter (soft/high-transpiration [Tomato] vs waxy/fibrous [Coconut]), this project provides the first unified cross-morphology calibration curve that mathematically compensates for the distance attenuation of fringing electric fields caused by cuticle thickness.

## 2. The Unweathered Sensor Fallacy (The Hardware/Field Gap)

- **The Gap**: Most open-source capacitive studies (e.g., papers utilizing Au@PET or bare copper traces) conduct their validation inside climate-controlled greenhouses. When exposed to outdoor dew point condensation or rain, the parasitic capacitance across bare electrodes causes the FDC1004 readings to saturate or short-circuit, rendering longitudinal outdoor studies impossible.
- **Our Novelty**: We implement and mathematically characterize the impact of a Parylene-C/Silicone conformal encapsulation layer. Our research will explicitly quantify how much this series dielectric dampens the absolute sensitivity of the FDC1004, and prove that the Random Forest model can successfully recover the Leaf Water Content despite this necessary field-hardening attenuation.
