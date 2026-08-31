import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Generate a hyper-realistic proxy dataset simulating diurnal capacitive curves
os.makedirs('docs/images', exist_ok=True)
os.makedirs('data_sandbox', exist_ok=True)

hours = np.arange(0, 120, 1) # 5 days
times = pd.date_range("2026-08-01", periods=120, freq="h")

# Environment
ambient_temp = 25 + 8 * np.sin(2 * np.pi * hours / 24 - np.pi/2) + np.random.normal(0, 0.5, 120)

# Plant baselines
base_cap = 15.0

# Stressed plant loses capacitance over the 5 days
stress_factor = np.linspace(0, 4.5, 120) 

cap_control = base_cap + 2 * np.sin(2 * np.pi * hours / 24 - np.pi/2) + np.random.normal(0, 0.2, 120)
cap_underwater = base_cap + 2 * np.sin(2 * np.pi * hours / 24 - np.pi/2) - stress_factor + np.random.normal(0, 0.25, 120)

plt.figure(figsize=(10, 6))
plt.plot(times, cap_control, label='Control (Well Watered)', color='#2ca02c', linewidth=2)
plt.plot(times, cap_underwater, label='Stressed (Underwatered)', color='#d62728', linewidth=2)

plt.title('Phase 3 Emulation: Multi-Day Capacitive Signal (SIMULATED)', fontsize=14, fontweight='bold')
plt.ylabel('FDC1004 Capacitance (pF)', fontsize=12)
plt.xlabel('Time', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right')

# Add watermark to ensure absolute academic honesty
plt.text(times[10], 17.5, "SIMULATED ENVIRONMENTAL PROXY DATA\nPending Physical Phase 3 Trials", color='red', fontsize=14, fontweight='bold', alpha=0.4)

plot_path = 'docs/images/simulated_stress_curve.png'
plt.tight_layout()
plt.savefig(plot_path, dpi=150)
print(f"Saved plot to {plot_path}")

# Output dataset
df = pd.DataFrame({
    'timestamp': times,
    'ambient_temp_C': ambient_temp,
    'cap_control_pF': cap_control,
    'cap_stressed_pF': cap_underwater
})
df.to_csv('data_sandbox/synthetic_proxy_dataset.csv', index=False)
print("Saved 120 hourly proxy readings to data_sandbox/synthetic_proxy_dataset.csv")

