# Microwave Dielectric Leaf Sensing for Plant Water Stress

## Project Overview

This repository contains the architecture, hardware feasibility, and machine learning pipeline for a low-cost, field-robust plant water stress monitoring system. It replaces expensive ($50k+) THz-TDS laboratory setups with an affordable (<$150) dielectric/microwave impedance sensing approach using hardware like NanoVNA or capacitive LDC161x chips.

### Key Innovations

1. **Cross-Morphology Calibration**: First rigorous attempt to bridge calibration models between thin/soft leaves (Tomato, Chilli) and thick/fibrous/waxy leaves (Coconut).
2. **Weatherproofed Sensoring**: Utilizing conformal coatings (Parylene-C/Silicone) to prevent electrode corrosion in field conditions without destroying capacitive sensitivity.
3. **TinyML Edge Inference**: Compensating for temperature-induced dielectric drift directly on an ESP32 using Random Forest & 1D-CNN regression pipelines.

## Repository Structure & Documentation

All background research and hardware designs necessary for the IEEE paper have been scaffolded:

- `LITERATURE_SURVEY.md`: Complete review of 2015-2026 dielectric/capacitive sensing applied to vegetation, focusing on the gap regarding specific cash crops.
- `NOVELTY_GAP_ANALYSIS.md`: Explicit justification of the cross-morphology and field-hardening novelty claims for the research paper.
- `DATASET_REPORT.md`: Findings on existing open-source data availability, setting the protocol for required in-house physical data collection to train the model.
- `HARDWARE_FEASIBILITY.md`: Detailed BOM and engineering mechanics for mounting the sensors on fragile vs robust fronds, addressing temperature cross-sensitivity.
- `PAPER_OUTLINE.md`: Structure for the final IEEE-compliant publication.

## Machine Learning Pipeline (`/ml_pipeline`)

The repository contains a fully scaffolded Python pipeline configured for the specific requirements of agricultural impedance data:

- `data_ingestion.py`: Loads raw `.s1p` Touchstone files from the NanoVNA and correlates them with environmental (BME280) metadata logs.
- `feature_extraction.py`: Computes resonant frequency shifts, S-band magnitude dips, and heuristic dielectric constants from raw complex vectors.
- `train_baseline.py`: Implements **Leave-One-Plant-Out Cross-Validation (LOPO-CV)** using a Random Forest Regressor to ensure zero data leakage between biological samples.
- `train_cnn.py`: Contains a stretch-goal 1D-CNN architecture capable of absorbing raw frequency sweep matrices without manual feature engineering, complete with standard TensorFlow Lite Micro export routines (`.tflite`) for deployment onto the ESP32 microcontroller.

## Workflow Instructions

1. **Data Collection Phase**: Following the dry-down protocol in `DATASET_REPORT.md`, collect samples matching NanoVNA sweeps to destructive LWC measurements.
2. **Data Integration**: Place the raw files in a `/data` folder and run `data_ingestion.py`.
3. **Training & Validation**: Run `train_baseline.py` to evaluate the Random Forest using LOPO-CV. Tune features in `feature_extraction.py` to handle temperature-induced drift.
4. **Publish**: Begin writing the experimental findings into the `PAPER_OUTLINE.md` scaffold.
