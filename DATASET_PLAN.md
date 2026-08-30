# Dataset Generation Plan

**CRITICAL NOTICE**: This document is a **DATASET PLAN**, not a report of collected data. As of Review 2, **no real-world FDC1004/NanoVNA data has been collected yet**. The current ML pipelines are trained on **SIMULATED** values to prove the algorithm architecture works. Real data collection is pending and required before Review 3.

## 1. Why a Custom Dataset is Required

We conducted extensive searches across academic repositories (IEEE Xplore, Kaggle, Figshare, MDPI Open Data) for datasets meeting the following criteria:

- **Target Variable**: Leaf Water Content (LWC)
- **Sensor Modality**: Sub-MHz Capacitance (FDC1004/LDC1614) or Microwave S-parameters.
- **Target Crops**: Chilli, Tomato, Coconut.

**Result**: No such public dataset exists for Chilli or Coconut capacitance mapping. We must collect it ourselves.

## 2. Real Data Collection Protocol (Action Items for Review 3)

To build the verifiable dataset, we will execute the following physical, hardware-validated protocol:

**Hardware Setup**:

- **Sensor**: FDC1004 capacitance-to-digital converter interfaced via I2C to an ESP32.
- **Electrodes**: Parylene-C coated interdigitated copper PCB.

**Procedure**:

1. **Selection**: Select N=5 healthy plants of each type (Chilli, Tomato, Coconut).
2. **Drying Cycle**: Subject the plants to a controlled dry-down period by withholding watering for 7-14 days.
3. **Sampling Rate**: Take a 1-minute averaged capacitance read every 6 hours.
4. **Ground Truth Validation**: Concurrent to the sensor read, use destructive gravimetric sampling. We will punch out a known leaf area, weigh it (Fresh Weight), oven dry at 70°C for 48h, and weigh it again (Dry Weight) to calculate true LWC.
5. **Sensor Matrix**: Record Ambient Temperature (Temp_C) and Relative Humidity (RH) concurrently to build the temperature cross-sensitivity compensation matrix.
