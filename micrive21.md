# Microwave Dielectric Leaf Sensing for Plant Water Stress

## Project Overview

This repository structures a low-cost, field-robust plant water stress monitoring system using sub-THz electromagnetic and capacitive (FDC1004) sensing.

**STATUS: Review 2 Milestone Achieved. (Documentation & Emulation Phase)**

- The hardware blocks and physical methodology are fully mapped out.
- The machine learning pipelines are fully coded but currently operate on **SIMULATED** physical models.
- **Physical hardware data collection is pending and required before Review 3.**

### Documentation Directory

- `LITERATURE_SURVEY.md`: Matrix awaiting insertion of 15 verified, real PDFs, detailing the dielectric crop data gap.
- `NOVELTY_GAP_ANALYSIS.md`: Strict gap analysis explicitly claiming cuticle variance modeling and conformal coating attenuation analysis.
- `DATASET_PLAN.md`: **Not a data report**. Details the exact dry-down protocol needed to gather real FDC1004 data for Tomato, Chilli, and Coconut.
- `HARDWARE_MODEL.md` / `HARDWARE_FEASIBILITY.md`: System block diagrams, ESP32 wiring instructions, and BOM.
- `METHODOLOGY_DRAFT.md`: Articulates the physics sequence: from volumetric water content, to relative permittivity via standard mixture models, to the FDC1004's capacitance field capture.
- `PRESENTATION_SLIDES_DRAFT.md`: Exact guide on how to present Review 2 honestly, without making claims regarding the simulated ML output that cannot be physically defended today.

## Machine Learning Pipeline (`/ml_pipeline`)

The ML models (Random Forest with LOPO-CV) are complete. Run `python SIMULATION_MODEL.py` to generate the placeholder accuracy charts.
*Note: Any output graph from this script must explicitly be labeled "SIMULATED — not yet validated against hardware" in your presentation until the physical dataset from `DATASET_PLAN.md` is collected.*
