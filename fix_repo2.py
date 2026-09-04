import re

# 1. Update SIMULATION_MODEL.py
path_sim = "ml_pipeline/SIMULATION_MODEL.py"
with open(path_sim, "r") as f:
    code = f.read()

code = code.replace(
    'plt.title("SIMULATED DATA (Not Hardware Validated): LWC Prediction")',
    'plt.title("SIMULATED — not yet validated against hardware")\n    plt.figtext(0.5, 0.01, "SIMULATED — not yet validated against hardware", ha="center", color="red", fontweight="bold")'
)

with open(path_sim, "w") as f:
    f.write(code)

# 2. Update DATASET_PLAN.md
path_dp = "DATASET_PLAN.md"
with open(path_dp, "r") as f:
    dp = f.read()

checklist = """

### Concrete Execution Checklist & Time Estimates

- [ ] **Procurement & Setup (Est. 2 days)**
  - [ ] Procure N=5 Chilli, N=5 Tomato, N=5 Coconut plants (Total 15 plants)
  - [ ] Connect FDC1004 to ESP32 via I2C
  - [ ] Attach Parylene-C coated copper interdigitated electrodes to 1 target leaf per plant
- [ ] **Baseline Hydration (Est. 3 days)**
  - [ ] Water all 15 plants fully to field capacity
  - [ ] Confirm baseline capacitance and steady-state readings
- [ ] **Dry-Down Phase (7-14 days)**
  - [ ] Cease all watering on Day 0
  - [ ] [Every 6 hours] Record 1-minute averaged capacitance, Temp_C, and RH
  - [ ] [Daily] Punch one small leaf area per plant for ground truth
  - [ ] [Daily] Measure Fresh Weight (FW) immediately
- [ ] **Ground Truth Processing (Est. 2 days post-sampling)**
  - [ ] Oven dry all leaf punches at 70°C for 48h
  - [ ] Measure Dry Weight (DW) for all samples
  - [ ] Calculate True LWC = (FW - DW) / FW
- [ ] **Dataset Assembly (Est. 1 day)**
  - [ ] Merge Time, Capacitance, Temp_C, RH, and True LWC into final `.csv` dataset
"""

if "Concrete Execution Checklist" not in dp:
    dp = dp + checklist
    with open(path_dp, "w") as f:
        f.write(dp)

print("Applied SIMULATION_MODEL.py and DATASET_PLAN.md updates.")
