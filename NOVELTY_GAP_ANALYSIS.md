# Novelty Gap Analysis

## Current State of the Art

A review of dielectric, microwave, and capacitive sensing literature (2015-2026) for plant water stress monitoring reveals a distinct cluster of studies focused on:

1. **Thin, homogeneous leaves** (e.g., maize, wheat, potato, canola).
2. **Controlled environments** (lab benches or climate-controlled greenhouses).
3. **Contact sensors prone to drift**, rarely exposed to real weathering (rain, dew, harsh sunlight).

## Identified Gaps

### 1. Cross-Morphology Dielectric Calibration (The Biological Gap)

There is virtually no systematic dielectric response model that unifies **high-variance soft leaves** (Chilli, Tomato) and **thick, waxy, fibrous leaves** (Coconut).

- **Tomato & Chilli**: Have high transpiration rates and soft cuticles. Capacitive sensors face variable surface contact and local condensation issues.
- **Coconut**: Have thick, waxy fronds with significant structural biomass that dominates the bulk dielectric constant (lower relative water volume fraction compared to tomato). Existing calibration curves for grasses (wheat/corn) drastically fail here.

**Novel Contribution A**: Establishing a cross-morphology dielectric calibration model that classifies the leaf type (soft vs. fibrous) as a hyperparameter to correctly interpret the microwave impedance shift.

### 2. Field-Hardened Sensoring (The Hardware Gap)

Most existing capacitive/dielectric clamps fail in longitudinal studies due to electrode corrosion or parasitic capacitance induced by morning dew or rain.

- Existing research treats the sensor as ideal.
- Real-world deployment requires conformal encapsulation (e.g., Parylene-C or specific marine-grade epoxies) that inevitably dampens the sensor's sensitivity.

**Novel Contribution B**: We propose and evaluate an encapsulated, weatherproofed interdigitated capacitor/resonator design, explicitly measuring and compensating for the signal attenuation and drift over time in an outdoor field setting.

## Proposed Strategy for the Paper

Our project will address these two gaps simultaneously, evaluating a low-cost, encapsulated NanoVNA/LDC161x sensor suite across Tomato, Chilli, and Coconut in both controlled and simulated field (weather-exposed) environments, proving stability and morphological adaptability unmatched in current sub-$150 sensing architectures.
