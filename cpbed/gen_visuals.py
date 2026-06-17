# -*- coding: utf-8 -*-
"""Visuels pour l'étude de cas BATIPROJET / DIGITECH : WBS, Gantt, matrice des risques."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from collections import defaultdict
import os

plt.rcParams["font.family"] = "DejaVu Sans"
NAVY = "#1F4E79"; BLUE = "#2E6BA8"; LBLUE = "#BDD3E9"; RED = "#C0392B"
GREEN = "#2E7D32"; GREY = "#5A5A5A"
OUT = "/home/user/licence/cpbed/img"
os.makedirs(OUT, exist_ok=True)

# =====================================================================
# 1. WBS
# =====================================================================
def wbs():
    fig, ax = plt.subplots(figsize=(15.5, 6.6), dpi=150)
    ax.set_xlim(0, 100); ax.set_ylim(37, 100); ax.axis("off")
    ax.set_title("WBS — Construction du siège social DIGITECH (bâtiment tertiaire BEPOS)",
                 fontsize=15, fontweight="bold", color=NAVY, pad=10)

    def box(x, y, w, h, text, fc, tc="white", fs=9.5, bold=True):
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3,rounding_size=1.2",
                           fc=fc, ec="white", lw=1.2, zorder=2)
        ax.add_patch(b)
        ax.text(x + w/2, y + h/2, text, ha="center", va="center",
                fontsize=fs, color=tc, fontweight="bold" if bold else "normal", zorder=3)

    # Racine
    box(30, 90, 40, 7, "PROJET — Siège social DIGITECH", NAVY, fs=12)
    # 6 phases
    phases = [
        ("1. Études &\nconception", ["1.1 Études détaillées", "1.2 Permis de construire", "1.3 Consultation entreprises"]),
        ("2. Préparation\ndu chantier", ["2.1 Installation de chantier", "2.2 Plan SPS & sécurité"]),
        ("3. Gros œuvre", ["3.1 Terrassement", "3.2 Fondations", "3.3 Structure béton", "3.4 Couverture / étanchéité"]),
        ("4. Second œuvre\n& techniques", ["4.1 Second œuvre", "4.2 Lots techniques (CVC, élec, plomb.)", "4.3 Photovoltaïque & bornes IRVE"]),
        ("5. Aménagements\nextérieurs", ["5.1 Parking (120 pl.)", "5.2 Espaces verts & détente"]),
        ("6. Réception\n& livraison", ["6.1 Essais & mise en service", "6.2 Levée des réserves", "6.3 Réception / livraison"]),
    ]
    n = len(phases); margin = 2.0; total_w = 100 - 2*margin
    cw = total_w / n; bw = cw - 2.0
    ytop = 78
    for i, (ph, subs) in enumerate(phases):
        x = margin + i*cw + 1.0
        # lien vers racine
        ax.plot([50, x + bw/2], [90, ytop + 7], color=GREY, lw=0.8, zorder=1)
        box(x, ytop, bw, 7, ph, BLUE, fs=9.5)
        yy = ytop - 7
        for s in subs:
            box(x, yy, bw, 5.0, s, "#DCE7F2", tc=NAVY, fs=7.6, bold=False)
            yy -= 5.8
    # Bande transverse
    box(8, 40, 84, 6, "Management de projet (transverse) : pilotage · qualité HQE / RE2020 · sécurité SPS · environnement · BIM",
        GREEN, fs=10)
    plt.tight_layout()
    plt.savefig(OUT + "/wbs.png", bbox_inches="tight", facecolor="white")
    print("wbs.png OK")

# =====================================================================
# 2. GANTT
# =====================================================================
def gantt():
    tasks = [
        ("Études détaillées",        0, 2, True,  0),
        ("Permis de construire",     2, 3, True,  0),
        ("Consultation entreprises", 2, 2, False, 1),
        ("Installation chantier",    5, 1, True,  0),
        ("Terrassement",             6, 1, True,  0),
        ("Fondations",               7, 2, True,  0),
        ("Structure béton",          9, 4, True,  0),
        ("Couverture / étanchéité", 13, 2, True,  0),
        ("Second œuvre",            15, 4, True,  0),
        ("Lots techniques",         15, 3, False, 1),
        ("Essais et mise en service",19,1, True,  0),
        ("Réception",               20, 1, True,  0),
    ]
    fig, ax = plt.subplots(figsize=(13.5, 7.0), dpi=150)
    y = len(tasks)
    for name, start, dur, crit, marge in tasks:
        y -= 1
        col = RED if crit else BLUE
        ax.barh(y, dur, left=start, height=0.55, color=col, zorder=3,
                edgecolor="white")
        if marge:
            ax.barh(y, marge, left=start+dur, height=0.2, color="#C9C9C9", zorder=2)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([t[0] for t in reversed(tasks)], fontsize=9.5)
    ax.set_xticks(range(0, 23, 2))
    ax.set_xlabel("Mois", fontsize=11, fontweight="bold")
    ax.set_xlim(0, 22)
    ax.set_title("Diagramme de Gantt — Rouge : chemin critique · Bleu : tâche · Gris : marge",
                 fontsize=13, fontweight="bold", color=NAVY, pad=12)
    ax.axvline(18, color=GREEN, ls="--", lw=2, zorder=5)
    ax.text(18, len(tasks)-0.3, " objectif 18 mois", color=GREEN, fontsize=10,
            fontweight="bold", va="top")
    ax.axvline(21, color=RED, ls=":", lw=2, zorder=5)
    ax.text(21, len(tasks)-0.3, " fin réelle\n 21 mois", color=RED, fontsize=10,
            fontweight="bold", va="top")
    ax.grid(axis="x", ls=":", color="#CCCCCC", zorder=0)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    plt.tight_layout()
    plt.savefig(OUT + "/gantt.png", bbox_inches="tight", facecolor="white")
    print("gantt.png OK")

# =====================================================================
# 3. MATRICE DES RISQUES
# =====================================================================
def risques():
    fig, ax = plt.subplots(figsize=(8.8, 6.4), dpi=150)
    for p in range(1, 5):
        for impact in range(1, 5):
            c = p*impact
            if c <= 4: col = "#C6E0B4"
            elif c <= 8: col = "#FFE699"
            elif c <= 12: col = "#F8CBAD"
            else: col = "#F4827B"
            ax.add_patch(Rectangle((impact-0.5, p-0.5), 1, 1, fc=col, ec="white", lw=2))
    # (code, P, I)
    R = [("R1",4,4),("R2",4,3),("R3",3,3),("R4",3,4),("R5",2,4),("R6",3,3),
         ("R7",2,4),("R8",2,4),("R9",3,3),("R10",3,2),("R11",2,3),("R12",2,3)]
    g = defaultdict(list)
    for c, p, i in R: g[(p, i)].append(c)
    for (p, i), codes in g.items():
        ax.plot(i, p, "o", ms=18, color=NAVY, mec="white", mew=1.5, zorder=3)
        if len(codes) > 1:
            ax.text(i, p, str(len(codes)), color="white", ha="center", va="center",
                    fontsize=9, fontweight="bold", zorder=4)
        ax.annotate(" ".join(codes), (i, p), xytext=(12, 12),
                    textcoords="offset points", fontsize=9.5, fontweight="bold",
                    color=NAVY, zorder=4)
    ax.set_xlim(0.5, 4.75); ax.set_ylim(0.5, 4.5)
    ax.set_xticks([1,2,3,4]); ax.set_yticks([1,2,3,4])
    ax.set_xticklabels(["1\nFaible","2\nModéré","3\nFort","4\nMajeur"], fontsize=9)
    ax.set_yticklabels(["1\nRare","2\nPossible","3\nProbable","4\nQuasi-certain"], fontsize=9)
    ax.set_xlabel("Impact (I)", fontsize=12, fontweight="bold", color=NAVY)
    ax.set_ylabel("Probabilité (P)", fontsize=12, fontweight="bold", color=NAVY)
    ax.set_title("Matrice des risques  (Criticité = P × I)", fontsize=13,
                 fontweight="bold", color=NAVY, pad=12)
    ax.set_aspect("equal"); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    plt.tight_layout()
    plt.savefig(OUT + "/risques.png", bbox_inches="tight", facecolor="white")
    print("risques.png OK")

wbs(); gantt(); risques()
