"""
Proxy dataset: 4-class plant stress with IMMEDIATELY visible signatures.

Scenario: Sensors deployed on plants that are ALREADY in different conditions,
not a gradual onset experiment. This models a field-deployment survey where the
system must classify existing conditions on arrival.
"""
import numpy as np
import pandas as pd
import os

os.makedirs('data_sandbox', exist_ok=True)
np.random.seed(42)

N = 672  # 7 days at 15-min intervals
t = np.arange(N)
hours = t / 4.0
times = pd.date_range("2026-08-01", periods=N, freq="15min")

# ── Environment ──
temp  = 28 + 8 * np.sin(2 * np.pi * hours / 24 - np.pi / 2)
light = np.clip(60000 * np.sin(2 * np.pi * hours / 24 - np.pi / 2), 0, 60000)

# ── Diurnal capacitance swing ──
diurnal = 0.18 * (temp - 28) + 0.00004 * light

# ── CLASS 0: Control ──
# Stable around 15 pF baseline
cap_ctrl = 15.0 + diurnal + np.random.normal(0, 0.08, N)

# ── CLASS 1: Underwater (drought) ──
# ALREADY dehydrated: baseline at ~11 pF and slowly dropping further
drought_offset = -4.0  # already 4 pF below healthy baseline
drought_trend  = np.linspace(0, 2.0, N)  # drops another 2 pF over 7 days
cap_under = 15.0 + drought_offset + diurnal - drought_trend + np.random.normal(0, 0.12, N)

# ── CLASS 2: Overwater (root hypoxia) ──
# ALREADY waterlogged: baseline at ~18 pF with HIGH variance (membrane damage)
waterlog_offset = 3.0
cap_over = 15.0 + waterlog_offset + diurnal + np.random.normal(0, 0.7, N)

# ── CLASS 3: Nutrient deficit ──
# Lower baseline at ~12.5 pF + damped diurnal amplitude (poor stomatal control)
cap_nutr = 12.5 + 0.35 * diurnal + np.random.normal(0, 0.06, N)

df = pd.DataFrame({
    'timestamp':         times.strftime('%Y-%m-%d %H:%M:%S'),
    'ambient_temp_C':    np.round(temp, 2),
    'light_lux':         np.round(light, 1),
    'cap_control_pF':    np.round(cap_ctrl, 3),
    'cap_underwater_pF': np.round(cap_under, 3),
    'cap_overwater_pF':  np.round(cap_over, 3),
    'cap_nutrient_pF':   np.round(cap_nutr, 3),
})
df.to_csv('data_sandbox/synthetic_proxy_dataset.csv', index=False)
print(f"Written {len(df)} rows")
print(f"  Control   mean: {cap_ctrl.mean():.2f} pF")
print(f"  Underwater mean: {cap_under.mean():.2f} pF  (should be ~11 pF)")
print(f"  Overwater mean: {cap_over.mean():.2f} pF  (should be ~18 pF)")
print(f"  Nutrient  mean: {cap_nutr.mean():.2f} pF  (should be ~12.5 pF)")
