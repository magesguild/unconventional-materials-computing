import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 7), dpi=150)
fig.patch.set_facecolor('#0f141c')
ax.set_facecolor('#0f141c')

# Title
ax.text(0.5, 0.93, "1.46g STRATOSPHERIC PICO-BALLOON ARCHITECTURE", 
        fontsize=16, fontweight='bold', color='#f0f4f8', ha='center', va='center')
ax.text(0.5, 0.88, "Lower Stratosphere Float (13 km / 42,000 ft) · 500 km Line-of-Sight LoRa Link", 
        fontsize=11, color='#88c0d0', ha='center', va='center')

# Balloon envelope
balloon = patches.Circle((0.5, 0.65), 0.16, facecolor='#2e3440', edgecolor='#88c0d0', linewidth=2, linestyle='--')
ax.add_patch(balloon)
ax.text(0.5, 0.66, "12 µm Aluminized Mylar\n(BoPET Balloon, r = 25 cm)", fontsize=10, color='#eceff4', ha='center', va='center')
ax.text(0.5, 0.58, "Gross Lift: 14.97 g | Net Payload: 1.87 g", fontsize=9, color='#a3be8c', ha='center', va='center')

# Tether
ax.plot([0.5, 0.5], [0.49, 0.40], color='#d8dee9', linewidth=1.5, linestyle=':')

# Solar Strip
solar = patches.FancyBboxPatch((0.36, 0.36), 0.28, 0.04, boxstyle="round,pad=0.008", facecolor='#434c5e', edgecolor='#ebcb8b', linewidth=1.5)
ax.add_patch(solar)
ax.text(0.5, 0.38, "Flexible GaAs Solar Ribbon (15 µm · 308 mW @ AM0)", fontsize=9, fontweight='bold', color='#ebcb8b', ha='center', va='center')

# Payload Pod
pod = patches.FancyBboxPatch((0.32, 0.20), 0.36, 0.14, boxstyle="round,pad=0.01", facecolor='#1a2332', edgecolor='#5e81ac', linewidth=2)
ax.add_patch(pod)

ax.text(0.5, 0.30, "INTEGRATED SOVEREIGN PAYLOAD (1.46 g)", fontsize=10.5, fontweight='bold', color='#88c0d0', ha='center', va='center')
ax.text(0.5, 0.25, "• Lattice iCE40UP5K K8 Core (4.8 mg · 42 µW)\n• Semtech SX1262 LoRa Radio (8.2 mg · +14 dBm)\n• 0.5F EDLC Supercapacitor (410 mg Buffer)", 
        fontsize=9, color='#e5e9f0', ha='center', va='center')

# Antenna
ax.plot([0.5, 0.5], [0.20, 0.06], color='#bf616a', linewidth=2)
ax.text(0.52, 0.12, "8.2 cm Enamel Copper Antenna (λ/4 @ 915 MHz)", fontsize=9, color='#bf616a', ha='left', va='center')

# Ray / Horizon text
ax.text(0.85, 0.15, "500 km Horizon\n+9.64 dB Fade Margin\nZero Terrestrial Infrastructure", 
        fontsize=9.5, fontweight='bold', color='#98c379', ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#151b24", edgecolor="#98c379"))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('/home/magesguild/research/02-regulus-and-hardware/paper-unconventional-materials/assets/stratospheric_balloon_diagram.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
print("Generated stratospheric_balloon_diagram.png successfully!")
