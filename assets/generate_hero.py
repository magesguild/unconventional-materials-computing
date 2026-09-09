import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# 1200x675 (16:9 Medium banner standard)
fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
fig.patch.set_facecolor('#0f141c')
ax.set_facecolor('#0f141c')

# Title and header
ax.text(0.5, 0.93, "COMPUTING BEYOND THE CIRCUIT BOARD", 
        fontsize=24, fontweight='bold', color='#f0f4f8', ha='center', va='center')
ax.text(0.5, 0.88, "Sub-Milliwatt Silicon, Unconventional Material Substrates & Stratospheric Mesh Networks", 
        fontsize=13, color='#88c0d0', ha='center', va='center')

# Central Metric Box
metric_box = patches.FancyBboxPatch((0.2, 0.76), 0.6, 0.08, boxstyle="round,pad=0.015", 
                                    facecolor="#1a2332", edgecolor="#4c566a", linewidth=1.5)
ax.add_patch(metric_box)
ax.text(0.5, 0.80, "THE 42-MICROWATT STILL POINT", fontsize=11, fontweight='bold', color='#e5c07b', ha='center', va='center')
ax.text(0.5, 0.775, r"$P_{\mathrm{total}} \approx 42\ \mu\mathrm{W}\quad \Longrightarrow \quad \Delta T < 0.001^{\circ}\mathrm{C}\quad (\mathrm{Bi} \approx 4.6 \times 10^{-5})$", 
        fontsize=13, color='#98c379', ha='center', va='center')

# 5 Material Substrates Cards
cards_data = [
    ("1. STRATOSPHERE", "#5e81ac", "1.46g Solar Pico-Balloon\n• 12 µm Mylar / GaAs\n• 500 km LoRa Horizon\n• +9.64 dB Fade Margin"),
    ("2. PLANT PAPER", "#d08770", "The Living Codex\n• 300 gsm Cotton Rag\n• Laser Graphene (LIG)\n• Tactile Yupana Touch"),
    ("3. E-TEXTILES", "#ebcb8b", "Andean Cumbi Weaving\n• Sinusoidal Silver Crimp\n• 25% Strain Decoupling\n• Waterproof Washable"),
    ("4. MYCO-SILICON", "#a3be8c", "Compostable Fungi\n• Reishi Mycelium Skin\n• PVD Zinc Metallization\n• 60-Day Soil Nutrient"),
    ("5. ARCH. GLASS", "#b48ead", "Inhabited Surfaces\n• Transparent ITO Mesh\n• Ultrasonic SAW Link\n• 100 kbps Building Wire")
]

x_starts = np.linspace(0.04, 0.82, 5)
card_width = 0.14
card_height = 0.38
y_top = 0.70

for i, (title, color, desc) in enumerate(cards_data):
    x = x_starts[i]
    # Card background
    card = patches.FancyBboxPatch((x, y_top - card_height), card_width, card_height, 
                                  boxstyle="round,pad=0.015", 
                                  facecolor="#151b24", edgecolor=color, linewidth=2.0)
    ax.add_patch(card)
    
    # Title pill
    title_pill = patches.FancyBboxPatch((x + 0.008, y_top - 0.05), card_width - 0.016, 0.038, 
                                        boxstyle="round,pad=0.008", 
                                        facecolor=color, edgecolor='none')
    ax.add_patch(title_pill)
    ax.text(x + card_width/2, y_top - 0.031, title, fontsize=9.5, fontweight='bold', color='#0f141c', ha='center', va='center')
    
    # Description text
    ax.text(x + 0.012, y_top - 0.08, desc, fontsize=9.2, color='#d8dee9', va='top', ha='left', linespacing=1.6)

# Bottom Unifying Protocol Banner
proto_box = patches.FancyBboxPatch((0.08, 0.12), 0.84, 0.12, boxstyle="round,pad=0.02", 
                                   facecolor="#1a212d", edgecolor="#88c0d0", linewidth=1.5)
ax.add_patch(proto_box)

ax.text(0.5, 0.19, "UNIFIED SOMATIC MEMBRANE: CORDLINK (CLP-64)", fontsize=13, fontweight='bold', color='#88c0d0', ha='center', va='center')
ax.text(0.5, 0.145, "Scale-Invariant 64-Byte Wire Invariant  ·  Hardware Gravity  ·  T-Stop Stasis  ·  Private Air-Gapped Field", 
        fontsize=10.5, color='#eceff4', ha='center', va='center')

# Footer
ax.text(0.5, 0.04, "Mage's Guild Research Laboratories & Basin Game Studios · Open Science (CC BY 4.0)", 
        fontsize=9, color='#4c566a', ha='center', va='center')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.tight_layout()
plt.savefig('/home/magesguild/research/02-regulus-and-hardware/paper-unconventional-materials/assets/hero_material_continuum.png', dpi=200, facecolor=fig.get_facecolor(), edgecolor='none')
print("Generated hero_material_continuum.png successfully!")
