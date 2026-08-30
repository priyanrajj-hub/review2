# Paper Outline: IEEE Conference Format

**Title**: Cross-Morphology Microwave Dielectric Sensing for Low-Cost, Field-Robust Plant Water Stress Monitoring

**Abstract**

- Briefly describe the limitation of current (expensive THz or lab-bound capacitive) leaf moisture sensors.
- State the proposed solution: a sub-$150, field-deployable NanoVNA-based/capacitive sensor.
- Highlight the key novelty: conformal weatherproofing and cross-morphology ML calibration (Tomato/Chilli vs. Coconut).
- Summarize results (e.g., predicted vs actual R² values, capability to run in the field).

**I. Introduction**

- A. The need for continuous plant water status monitoring (irrigation efficiency).
- B. Traditional methods (porometry, destructive sampling) and their drawbacks.
- C. Shift towards dielectric/microwave sensing.
- D. Statement of Novelty / Main Contributions.

**II. Related Work**

- A. High-cost methodologies (THz-TDS).
- B. Low-cost dielectric/capacitive approaches (summarizing literature from 2015-2026).
- C. The gap: lack of studies on fibrous/large leaves (coconut) and lack of weatherproofed field deployment.

**III. Methodology & Sensor Design**

- A. **Hardware Architecture**: Detailed description of the ESP32 + NanoVNA/LDC1614 system.
- B. **Sensor Encapsulation**: Explanation of the conformal coating to prevent electrode corrosion and parasitic effects.
- C. **Attachment Physics**: Soft-clamp (Tomato) vs. strapped-plaque (Coconut).

**IV. Data Collection & Preprocessing**

- A. **Experimental Setup**: Dry-down cycle used to gather LWC ground truth.
- B. **Diurnal and Temperature Compensation**: How the BME280 data is synchronized.
- C. **Feature Extraction**: Extracting resonant frequencies, Smith Chart phase shifts, and capacitance vectors.

**V. Machine Learning Pipeline**

- A. **Algorithm Selection**: Why Random Forest / GBT was chosen over deep learning for the small n-sample biological dataset.
- B. **Hyperparameter Tuning & Cross-Validation**: LOPO-CV (Leave-One-Plant-Out Cross-Validation) to prevent data leakage.
- C. **TinyML Implementation**: (Optional stretch) Embedding the inference on the ESP32.

**VI. Results & Discussion**

- A. **Laboratory vs. Field Accuracy**: R² charts for Tomato, Chilli, and Coconut.
- B. **Temperature Compensation Analysis**: Proof that the BME280 fusion corrected drift.
- C. **Limitations**: (e.g., maximum wind-load the sensor can handle, long-term silicone degradation).

**VII. Conclusion**

- Final wrap-up of how this enables mass-deployment of precision irrigation in structurally diverse crops.

**VIII. References**
