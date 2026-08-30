# Dataset Search and Evaluation

## 1. Search Methodology & Findings

We conducted extensive searches across academic repositories (IEEE Xplore, Kaggle, Figshare, MDPI Open Data, Elsevier) for datasets meeting the following criteria:

- **Target Variable**: Leaf Water Content (LWC) or physiological water stress indicators.
- **Sensor Modality**: Microwave (NanoVNA S-parameters), Dielectric constant, or Capacitance/Impedance (LDC1614/FDC1004).
- **Target Crops**: Chilli (Capsicum), Tomato (Solanum lycopersicum), Coconut (Cocos nucifera).

### Findings

- **Model Crops Available**: There are abundant datasets for Tomato (often used as a generic dicot model in agricultural IoT), but very few specifically map *raw microwave/capacitive* spectra to LWC in open-source. Most are limited to RGB/Multispectral or soil moisture.
- **Chilli & Coconut**: **No public datasets** currently exist that map microwave S-parameters or sub-MHz impedance spectra to leaf water content for these specific crops. Coconut, due to its size and growth environment, is virtually absent from high-frequency dielectric literature.

## 2. Requirement for Self-Collection

Because the explicitly targeted novel crops (Chilli, Coconut) and the requested sensor modalities lack public datasets, **this project must collect its own dataset.** This is actually a major strength for a publication, rather than a drawback.

### Proposed Data Collection Protocol

To build the required dataset, we will implement the following procedure:

1. **Selection**: Select N=5 healthy plants of each type (Chilli, Tomato, Coconut).
2. **Drying Cycle**: Subject the plants to a controlled dry-down period (withholding watering for 7-14 days).
3. **Measurement Iterations**: Every 12 hours:
   - Attach the sensor to 3 marked leaves per plant.
   - Record S11/Impedance sweep (NanoVNA) or raw Capacitance (LDC161x).
   - *Ground Truth Calibration*: Use destructive gravimetric sampling (weighing a nearby leaf, oven-drying it at 70°C for 48h, re-weighing) or a commercial leaf porometer to establish true LWC.
4. **Environmental Logging**: Record ambient Temp and Relative Humidity (RH) concurrently to allow for compensation models.

## 3. Pretraining Alternatives

While exact datasets don't exist, we can use synthetic augmentation (injecting Gaussian noise, simulating diurnal drift) to scaffold and debug the machine learning pipelines (`ml_pipeline/`) prior to the physical dataset collection. Once real data is ingested, the models will be fine-tuned.
