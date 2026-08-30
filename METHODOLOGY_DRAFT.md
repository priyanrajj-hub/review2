# Methodology: Physics-Driven Capacitive Leaf Sensing

## 1. The Physics Chain of Dielectric Sensing

Our methodology relies on the fundamental relationship between volumetric water content and the bulk dielectric constant ($\epsilon_{mix}$) of a biological medium. We do not merely correlate "capacitance to stress"; we follow a strict physical chain:

**Step 1: Volumetric Water Content → Dielectric Permittivity**
Water is a highly polar molecule with a relative permittivity ($\epsilon_r$) of ~80 at ambient temperature. Dry plant tissue (cellulose, lignin) has an $\epsilon_r$ of roughly 2 to 3. According to the **Complex Refractive Index Method (CRIM)** or **Debye Relaxation Models** for biological mixtures, the bulk effective permittivity of the leaf is overwhelmingly dominated by the volume fraction of free water. As the leaf loses turgor pressure and dehydrates, the bulk $\epsilon_r$ drops non-linearly.

**Step 2: Dielectric Permittivity → Resolvable Capacitance (FDC1004)**
The sensor applies a low-frequency (e.g., 25 kHz for FDC1004) alternating electric field across interdigitated electrodes. The capacitance $C$ of an interdigitated structure is given approximately by the conformal mapping of the substrate and the superstrate (the leaf).
$$ C = f(Geometry) \cdot \epsilon_0 \cdot \epsilon_{effective} $$
Because the FDC1004 has an extreme resolution of **0.5 fF (femtofarads)** with an input range up to ±15 pF, it is mathematically capable of resolving the minute changes in the fringing electric field caused by an $\epsilon_r$ shift of even 1-2%, corresponding directly to early-stage drought stress before mechanical wilting occurs.

## 2. Sensor Geometry and Physics Modifications

- **Parylene-C Conformal Coating**: Directly exposing copper to the leaf surface introduces galvanic corrosion and massive measurement errors from conductive sap/dew. We coat the electrodes in Parylene-C ($\epsilon_r = 3.1$). This acts as a rigid series capacitor ($C_{coating}$). The total measured capacitance is $\frac{1}{C_{total}} = \frac{1}{C_{coating}} + \frac{1}{C_{leaf}}$. The high sensitivity of the FDC1004 is required to read through this series impedance block.
- **Probe Geometry for Specific Morphologies**:
  - **Tomato/Chilli**: Soft cuticles allow the fringing field (which decays exponentially with distance) to easily penetrate the water-bearing mesophyll. A soft clamp suffices.
  - **Coconut**: The thick, waxy cuticle physically acts as a massive dielectric spacer, pushing the water-bearing layers further from the electrodes into the weaker regions of the fringing field. This explains why standard grass/wheat capacitance matrices utterly fail on coconut, mandating our cross-morphology ML compensation to adjust the baseline sensitivity curve.

## 3. Machine Learning Compensation

*(Status: Currently SIMULATED in Python; requires physical validation)*
Because the fringing field interacts differently based on temperature (water's $\epsilon_r$ drops by ~0.4%/°C) and leaf morphology (cuticle thickness), analytical closed-form equations fail in the field. Our Random Forest pipeline ingests the raw FDC1004 capacitance and ambient BME280 temperature to regress the true Leaf Water Content, abstracting the complex geometry parameters into a learned morphological hyperparameter.
