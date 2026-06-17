# -*- coding: utf-8 -*-
"""Matrice de criticité des risques (Probabilité x Gravite) - Projet GREMLIN."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"

BLEU = "#1F4E79"
fig, ax = plt.subplots(figsize=(9.2, 6.6), dpi=150)

# Fond : criticite P*G, de vert (faible) a rouge (fort)
for p in range(1, 5):
    for g in range(1, 5):
        c = p * g
        if c <= 3:
            col = "#C6E0B4"      # vert
        elif c <= 6:
            col = "#FFE699"      # jaune
        elif c <= 9:
            col = "#F8CBAD"      # orange
        else:
            col = "#F4827B"      # rouge
        ax.add_patch(Rectangle((g - 0.5, p - 0.5), 1, 1, facecolor=col,
                               edgecolor="white", linewidth=2, zorder=0))

# Risques : (code, P, G)
risques = [
    ("R1", 3, 4), ("R2", 3, 3), ("R3", 4, 2),
    ("R4", 2, 3), ("R5", 2, 3), ("R6", 2, 3), ("R7", 3, 3),
]
# Regroupe les points superposes pour decaler les etiquettes
from collections import defaultdict
groupes = defaultdict(list)
for code, p, g in risques:
    groupes[(p, g)].append(code)

for (p, g), codes in groupes.items():
    ax.plot(g, p, "o", markersize=20, color=BLEU, zorder=3,
            markeredgecolor="white", markeredgewidth=1.5)
    ax.text(g, p, str(len(codes)) if len(codes) > 1 else "", color="white",
            ha="center", va="center", fontsize=10, fontweight="bold", zorder=4)
    label = " / ".join(codes)
    ax.annotate(label, (g, p), xytext=(14, 14), textcoords="offset points",
                fontsize=10.5, fontweight="bold", color=BLEU, zorder=4)

ax.set_xlim(0.5, 4.5)
ax.set_ylim(0.5, 4.5)
ax.set_xticks([1, 2, 3, 4])
ax.set_yticks([1, 2, 3, 4])
ax.set_xticklabels(["1\nNégligeable", "2\nSérieuse", "3\nGrave", "4\nCritique"], fontsize=9.5)
ax.set_yticklabels(["1\nRare", "2\nPossible", "3\nProbable", "4\nTrès probable"], fontsize=9.5)
ax.set_xlabel("Gravité (G)", fontsize=12, fontweight="bold", color=BLEU)
ax.set_ylabel("Probabilité (P)", fontsize=12, fontweight="bold", color=BLEU)
ax.set_title("Matrice de criticité des risques  (Criticité = P × G)",
             fontsize=13.5, fontweight="bold", color=BLEU, pad=14)
ax.set_aspect("equal")
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)

# Legende des zones
from matplotlib.patches import Patch
leg = [Patch(facecolor="#C6E0B4", label="Faible (≤ 3)"),
       Patch(facecolor="#FFE699", label="Modérée (4–6)"),
       Patch(facecolor="#F8CBAD", label="Élevée (8–9)"),
       Patch(facecolor="#F4827B", label="Majeure (≥ 10)")]
ax.legend(handles=leg, loc="upper left", bbox_to_anchor=(1.01, 1.0),
          frameon=False, fontsize=9.5, title="Niveau de criticité",
          title_fontsize=10)

plt.tight_layout()
plt.savefig("/home/user/licence/gremlin/img/matrice_risques.png",
            bbox_inches="tight", facecolor="white")
print("matrice_risques.png OK")
