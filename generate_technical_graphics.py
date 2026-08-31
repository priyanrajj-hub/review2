import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('docs/images', exist_ok=True)

# -------------------------------------------------------------
# IMAGE 1: Diurnal Correction Concept
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
hours = np.linspace(0, 48, 200)

temp = 25 + 10 * np.sin(2 * np.pi * hours / 24 - np.pi/2)
raw_cap_healthy = 20 + 3 * np.sin(2 * np.pi * hours / 24 - np.pi/2) + np.random.normal(0, 0.2, 200)
raw_cap_stress = raw_cap_healthy.copy()
stress_start = 100
raw_cap_stress[stress_start:] -= np.linspace(0, 5, 100) # Divergence over time

ax1.plot(hours, raw_cap_healthy, label='Healthy (Control)', color='gray', alpha=0.7)
ax1.plot(hours, raw_cap_stress, label='Underwatered', color='red', linewidth=2)
ax1.set_ylabel('Raw Capacitance (pF)')
ax1.set_title('1. Raw Signal: Heavy Noise from Day/Night Temperature Cycles', fontweight='bold')
ax1.legend()
ax1.grid(alpha=0.3)

# Filtered/Corrected
ax2.plot(hours, raw_cap_healthy - (20 + 3 * np.sin(2 * np.pi * hours / 24 - np.pi/2)), label='Healthy (Corrected)', color='gray', alpha=0.7)
corrected_stress = raw_cap_stress - (20 + 3 * np.sin(2 * np.pi * hours / 24 - np.pi/2))
ax2.plot(hours, corrected_stress, label='Underwatered (Corrected)', color='red', linewidth=2)
ax2.set_xlabel('Time (Hours)')
ax2.set_ylabel('Δ Corrected Capacitance')
ax2.set_title('2. Diurnally Corrected: Isolated Physiological Stress Signal', fontweight='bold')
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('docs/images/diurnal_concept.png', dpi=150)
plt.close()

# -------------------------------------------------------------
# IMAGE 2: Cross-Morphology Cuticle Hypothesis
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

freqs = np.linspace(1, 100, 200) # MHz
# Tomato (thin cuticle)
tomato_resp = 80 - 0.5 * freqs + 5 * np.exp(-((freqs-20)**2)/100)
# Coconut (thick cuticle)
coconut_resp = 40 - 0.2 * freqs + 2 * np.exp(-((freqs-60)**2)/150)

plt.plot(freqs, tomato_resp, label='Tomato (Thin Cuticle, High VWC)', color='tomato', linewidth=3)
plt.plot(freqs, coconut_resp, label='Coconut (Thick Cuticle, Low VWC/High Fibre)', color='saddlebrown', linewidth=3)

plt.fill_between(freqs, tomato_resp-3, tomato_resp+3, color='tomato', alpha=0.2)
plt.fill_between(freqs, coconut_resp-2, coconut_resp+2, color='saddlebrown', alpha=0.2)

plt.axvline(x=25, color='gray', linestyle='--', label='Operating Frequency (25 MHz)')

plt.title('Theoretical Frequency Response: Cross-Morphology Calibration', fontsize=14, fontweight='bold')
plt.xlabel('Frequency (MHz)', fontsize=12)
plt.ylabel('Dielectric Permittivity (ε\')', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)

# Watermark
plt.text(45, 60, "PROJECT FRAMEWORK CONCEPT\nPending Physical Phase 3 Trials", color='black', fontsize=12, fontweight='bold', alpha=0.2)

plt.tight_layout()
plt.savefig('docs/images/cross_morphology.png', dpi=150)
plt.close()

# -------------------------------------------------------------
# IMAGE 3: System Pipeline Block Diagram
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 5))
ax.axis('off')

def add_box(ax, xy, width, height, text, bg_color):
    box = patches.FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.1", 
                                 edgecolor='black', facecolor=bg_color, lw=2)
    ax.add_patch(box)
    ax.text(xy[0] + width/2, xy[1] + height/2, text, ha='center', va='center', fontsize=11, fontweight='bold')

add_box(ax, (0.05, 0.4), 0.2, 0.3, "1. Edge Hardware\nFDC1004 + ESP32", 'lightblue')
add_box(ax, (0.35, 0.4), 0.2, 0.3, "2. Preprocessing\nDiurnal Drop & Filter", 'lightgreen')
add_box(ax, (0.65, 0.4), 0.25, 0.3, "3. ML Inference\nXGBoost + Conformal Bounds", 'lightcoral')

# Arrows
ax.annotate('', xy=(0.35, 0.55), xytext=(0.25, 0.55), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate('', xy=(0.65, 0.55), xytext=(0.55, 0.55), arrowprops=dict(arrowstyle="->", lw=2))

plt.title('End-to-End System Architecture Pipeline', fontsize=15, fontweight='bold', y=0.85)

plt.tight_layout()
plt.savefig('docs/images/architecture_flow.png', dpi=150)
plt.close()

print("Generated 3 technical infographics.")
