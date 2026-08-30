# Methodology: Cross-Morphology Microwave Dielectric Sensing

## 1. Introduction to the Methodology

Our approach replaces traditional, laboratory-bound Terahertz Time-Domain Spectroscopy (THz-TDS) with a field-deployable, sub-THz electromagnetic method. The system leverages Vector Network Analysis (VNA) and interdigitated capacitive sensing to measure the electrical impedance of a leaf in-vivo. Since the relative permittivity of water ($\epsilon_r \approx 80$) is massively higher than dry plant material ($\epsilon_r \approx 2-3$), any fluctuation in Leaf Water Content (LWC) dominates the macroscopic dielectric signature of the leaf.

## 2. Sensor Design and Hardware Configuration (60% Implementation)

The hardware architecture is predicated on generating radio frequency (RF) sweeps across the leaf tissue without puncturing the epidermis.

- **Microwave Circuit**: We utilize a NanoVNA-based S-parameter sweep from 500 MHz to 3 GHz. The sensor head acts as a parallel-plate or coplanar resonator.
- **Capacitive Base**: An LDC161x or FDC1004 capacitive-to-digital converter measures the raw bulk capacitance at sub-MHz frequencies.
- **Environmental Encapsulation**: A core novelty is the application of a thin Parylene-C conformal coating over the copper electrodes. This yields a weatherproof barrier against morning dew, shifting the baseline impedance but preventing electrode corrosion.

## 3. Cross-Morphology Calibration

Traditional capacitive sensors are calibrated strictly for thin grasses (e.g., wheat, maize). We extend this to structurally complex crops:

- **Tomato & Chilli**: These represent 'soft' morphology with high surface transpiration. They require a soft-clamping mechanism (pressure < 0.5 N) to avoid crushing the xylem.
- **Coconut**: Represents 'fibrous/waxy' morphology. The thick cuticle acts as a large series dielectric, drastically damping the capacitance. Here, we utilize a strapped conformal proximity approach rather than a crushing clamp.

## 4. Signal Processing and Feature Extraction

The raw complex scattering parameters ($S_{11}$) are pulled via an ESP32 microcontroller over UART. We extract three primary features:

1. **Resonant Frequency Shift ($\Delta f_r$)**: The frequency at which $S_{11}$ magnitude hits an absolute minimum.
2. **Phase Angle at Center Frequency ($\theta_{fc}$)**: Readily maps to the capacitive reactance.
3. **Thermally Compensated Capacitance**: Given the thermal drift of water's dielectric constant (-0.4% per °C), we fuse data from a localized BME280 sensor.

## 5. Machine Learning Regression Model (60% Simulation Ready)

Due to the non-linear relationship introduced by the plant's internal structure and the conformal coating, a closed-form electromagnetic equation is insufficient. We utilize a **Random Forest Regressor** trained via **Leave-One-Plant-Out Cross-Validation (LOPO-CV)**.
By injecting the mathematical output of the sensor sweep alongside the Plant Type (Hyperparameter) and ambient temperature, the ML model maps the unified dielectric impedance tensor back to genuine Leaf Water Content percentage.
