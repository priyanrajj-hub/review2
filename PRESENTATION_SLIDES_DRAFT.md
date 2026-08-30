# Capstone Review 2: Presentation Outline

**WARNING FOR STUDENT**: This slide deck reflects what you can *actually* present and defend today. Do not claim the AI-generated simulation graph represents actual physical measurements.

## Slide 1: Title Slide

- **Project Title**: (Insert your final title)
- **Team Members**: (Insert team members)
- **Review**: Review 2

## Slide 2: Problem Statement & Literature Gap

- Discuss the expensive nature of current exact LWC mapping (THz-TDS is $50k+).
- *Visual*: Show your 15-paper literature survey matrix (with real citations).
- *Defensible Claim*: State the literature gap: No papers have successfully calibrated a capacitive sensor simultaneously for soft leaves (Tomato) and waxy cuticles (Coconut) while compensating for outdoor field degradation.

## Slide 3: Proposed Methodology (The Physics)

- Explain the physical property: Capacitance changes because the dielectric permittivity of water ($\epsilon_r = 80$) dominates the dry plant matter ($\epsilon_r = 2-3$).
- Explain why the **FDC1004** is required: The conformal Parylene-C coating acts as a series capacitor, blocking direct contact. The FDC1004's extreme 0.5 fF resolution is required to read the minute fringing field shifts through the protective coating.
- Differentiate the cuticle thickness geometry: Soft clamp vs. Coconut strap.

## Slide 4: Simulation Model Progress (Rubric: 60% completion)

- Explicitly state: *"We have completely established the software pipeline, currently validated on a synthesized morphological model."*
- Show the `results/simulation_accuracy.png` plot.
- **Crucial Defense**: "This graph proves our Random Forest LOPO-CV algorithm runs on edge-device dimensions. It currently processes physically-constrained synthetic data (modeling thermal drift and cuticle attenuation). Real hardware data ingestion will swap flawlessly into this pipeline for Review 3."

## Slide 5: Hardware Model Progress (Rubric: 60% completion)

- Present the system block diagram (ESP32 -> FDC1004/NanoVNA -> Interdigitated PCB).
- Explain the Power Management (Solar -> TP4056 -> Battery) and environmental sensor fusion (BME280 for thermal coefficient calibration).

## Slide 6: Hardware Demo Path & Deficits

- Explicitly state what is completed and what remains for the hardware demo.
- *"For this review, we demonstrate the completed PCB layouts and the functioning Python/TinyML inference pipeline."*
- **Action Plan for Review 3**:
  1. Complete physical assembly of the PCB and ESP32.
  2. Perform the physical 14-day dry-down cycle on Tomato and Coconut plants.
  3. Swap the simulation data in our pipeline with the actual I2C sensor reads.

## Slide 7: Conclusion

- Summary of progress mapped to Review 2 milestones.
