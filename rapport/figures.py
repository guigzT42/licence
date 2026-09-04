# -*- coding: utf-8 -*-
"""
Génère les figures du rapport d'étude tutorée — Sujet 2026-C
Rénovation énergétique d'une ancienne ferme à Saint-Jean-de-Chevelu (73)
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch
import numpy as np

plt.rcParams["font.family"] = "Liberation Sans"
plt.rcParams["axes.edgecolor"] = "#B0BEC5"
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["axes.unicode_minus"] = False

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

VERT = "#2E7D32"
VERT_CLAIR = "#66BB6A"
ORANGE = "#EF6C00"
BLEU = "#1565C0"
ROUGE = "#C62828"
GRIS = "#78909C"
ANTHRA = "#37474F"

DPE_COLORS = {
    "A": "#319834", "B": "#33CC31", "C": "#CBFC34", "D": "#FFFA01",
    "E": "#FEE100", "F": "#FEB92E", "G": "#FE0000",
}


def eur(v, dec=0):
    """Formatage monétaire à la française : 12 345 €"""
    s = f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")
    return s


def save(fig, name, dpi=200):
    path = os.path.join(OUT, name + ".png")
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ->", name + ".png")
    return path


def style_axes(ax, grid_axis="y"):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis=grid_axis, color="#E0E0E0", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)


# ===========================================================================
# 1 — Consommations relevées sur 5 ans (propane + DJU)
# ===========================================================================
def fig_consommations():
    annees = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    propane = [2522, 2252, 1456, 1473, 1653]
    dju = [2397.2, 2422.8, 2121.9, 2069.8, 2142.4]

    fig, ax = plt.subplots(figsize=(8.6, 4.0))
    x = np.arange(len(annees))
    bars = ax.bar(x, propane, width=0.55, color=ORANGE, zorder=3,
                  label="Propane (kg)")
    for b, v in zip(bars, propane):
        ax.text(b.get_x() + b.get_width() / 2, v + 45, f"{v}", ha="center",
                va="bottom", fontsize=10, fontweight="bold", color=ANTHRA)
    ax.set_ylabel("Propane consommé (kg/an)", fontsize=10, color=ORANGE)
    ax.set_ylim(0, 3100)
    ax.set_xticks(x)
    ax.set_xticklabels(annees, fontsize=10)
    style_axes(ax)

    ax2 = ax.twinx()
    ax2.plot(x, dju, marker="o", color=BLEU, linewidth=2.2, markersize=7,
             zorder=4, label="DJU18 station (°C.j)")
    for xi, v in zip(x, dju):
        ax2.annotate(f"{v:.0f}".replace(".", ","), (xi, v),
                     textcoords="offset points", xytext=(0, 11),
                     ha="center", fontsize=9, color=BLEU)
    ax2.set_ylabel("DJU18 Chambéry-Aix (°C.j)", fontsize=10, color=BLEU)
    ax2.set_ylim(1700, 2800)
    ax2.spines["top"].set_visible(False)

    ax.axvspan(1.5, 4.5, color=ROUGE, alpha=0.05, zorder=1)
    ax.annotate("Rupture 2022 : le foyer réduit\nsa consigne de chauffage",
                xy=(2.30, 1500), xytext=(2.55, 2560), fontsize=9.5, color=ROUGE,
                ha="left",
                arrowprops=dict(arrowstyle="->", color=ROUGE, linewidth=1.3))

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper center", fontsize=9.5,
              frameon=False, ncol=2, bbox_to_anchor=(0.5, -0.11))
    ax.set_title("Consommations de propane et rigueur climatique "
                 "(5 saisons de chauffe)",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=12)
    return save(fig, "01_consommations")


# ===========================================================================
# 2 — Consommations corrigées du climat
# ===========================================================================
def fig_correction_climat():
    annees = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    brut = [2522, 2252, 1456, 1473, 1653]
    dju = [2397.2, 2422.8, 2121.9, 2069.8, 2142.4]
    ref = float(np.mean(dju))
    corrige = [b * ref / d for b, d in zip(brut, dju)]

    fig, ax = plt.subplots(figsize=(8.6, 3.9))
    x = np.arange(len(annees))
    w = 0.38
    b1 = ax.bar(x - w / 2, brut, w, color="#FFCC80", zorder=3,
                label="Consommation brute (kg)")
    b2 = ax.bar(x + w / 2, corrige, w, color=ORANGE, zorder=3,
                label="Consommation corrigée du climat (kg)")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 40,
                    f"{b.get_height():.0f}", ha="center", va="bottom",
                    fontsize=8.6, color=ANTHRA)
    ax.plot(x + w / 2, corrige, color=ROUGE, linewidth=1.6, linestyle="--",
            marker="o", markersize=5, zorder=4)
    ax.set_ylabel("Propane (kg/an)", fontsize=10)
    ax.set_ylim(0, 3000)
    ax.set_xticks(x)
    ax.set_xticklabels(annees, fontsize=10)
    style_axes(ax)
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    ax.set_title("Climat neutralisé, la baisse de −27 % persiste : "
                 "elle est comportementale",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=12)
    return save(fig, "02_correction_climat")


# ===========================================================================
# 3 — Répartition de la facture énergétique
# ===========================================================================
def fig_postes():
    labels = ["Chauffage\n(propane + bois)",
              "Eau chaude sanitaire\n(ballon électrique)",
              "Électricité spécifique\net cuisson"]
    vals = [74, 13, 13]
    colors = [ORANGE, BLEU, GRIS]

    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    wedges, _, _ = ax.pie(
        vals, colors=colors, autopct="%1.0f %%", startangle=90,
        counterclock=False, pctdistance=0.73,
        wedgeprops=dict(width=0.52, edgecolor="white", linewidth=2.5),
        textprops=dict(fontsize=13, fontweight="bold", color="white"))
    ax.text(0, 0.08, "5 739 €", ha="center", va="center", fontsize=18,
            fontweight="bold", color=ANTHRA)
    ax.text(0, -0.16, "de facture annuelle", ha="center", va="center",
            fontsize=10, color=GRIS)
    ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(0.97, 0.5),
              fontsize=9.5, frameon=False)
    ax.set_title("Répartition de la dépense énergétique réelle",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=8)
    return save(fig, "03_postes_depense")


# ===========================================================================
# 4 — Répartition des déperditions
# ===========================================================================
def fig_deperditions():
    postes = ["Murs extérieurs", "Mur mitoyen du garage", "Renouvellement d'air",
              "Menuiseries", "Plancher bas", "Ponts thermiques",
              "Plafond / combles"]
    vals = [256.3, 80.9, 76.5, 73.9, 31.6, 27.7, 5.8]
    pct = [v / sum(vals) * 100 for v in vals]
    colors = [ROUGE, "#E57373", BLEU, ORANGE, "#8E24AA", GRIS, VERT_CLAIR]

    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    y = np.arange(len(postes))[::-1]
    bars = ax.barh(y, vals, color=colors, height=0.62, zorder=3)
    for b, v, p in zip(bars, vals, pct):
        ax.text(v + 6, b.get_y() + b.get_height() / 2,
                f"{v:.0f} W/K   ({p:.0f} %)".replace(".", ","), va="center",
                fontsize=10, fontweight="bold", color=ANTHRA)
    ax.set_yticks(y)
    ax.set_yticklabels(postes, fontsize=10.5)
    ax.set_xlabel("Déperditions (W/K)", fontsize=10)
    ax.set_xlim(0, 345)
    style_axes(ax, grid_axis="x")
    ax.set_title("Bilan des déperditions de l'existant — GV = 553 W/K",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    ax.text(150, y[0] - 1.3, "Les murs concentrent 61 % des pertes",
            fontsize=10.5, color=ROUGE, fontweight="bold")
    return save(fig, "04_deperditions")


# ===========================================================================
# 5 — Étiquettes DPE
# ===========================================================================
def _dpe_scale(ax, classe, seuils, unite, titre, x0=0.0):
    lettres = list("ABCDEFG")
    n = len(lettres)
    for i, L in enumerate(lettres):
        y = n - 1 - i
        w = 0.30 + 0.085 * i
        poly = Polygon([[x0, y], [x0 + w, y], [x0 + w + 0.07, y + 0.42],
                        [x0 + w, y + 0.84], [x0, y + 0.84]],
                       closed=True, facecolor=DPE_COLORS[L],
                       edgecolor="white", linewidth=1.4, zorder=3)
        ax.add_patch(poly)
        ax.text(x0 + 0.05, y + 0.42, L, fontsize=13, fontweight="bold",
                va="center", ha="left", color="black", zorder=4)
        ax.text(x0 + w + 0.14, y + 0.42, seuils[i], fontsize=8.2,
                va="center", ha="left", color="#546E7A", zorder=4)
        if L == classe:
            ax.add_patch(FancyBboxPatch(
                (x0 - 0.035, y - 0.045), w + 0.11, 0.93,
                boxstyle="round,pad=0.015", linewidth=2.4,
                edgecolor=ANTHRA, facecolor="none", zorder=5))
    ax.text(x0 + 0.5, n + 0.28, titre, fontsize=10.5, fontweight="bold",
            ha="center", color=ANTHRA)
    ax.text(x0 + 0.5, -0.58, unite, fontsize=9.5, ha="center",
            color=ANTHRA, fontweight="bold")


def fig_dpe(nom, classe_e, classe_c, val_e, val_c, titre):
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.set_xlim(-0.15, 2.6)
    ax.set_ylim(-0.95, 8.15)
    ax.axis("off")
    _dpe_scale(ax, classe_e,
               ["≤ 70", "71 - 110", "111 - 180", "181 - 250", "251 - 330",
                "331 - 420", "> 420"],
               f"{val_e} kWh EP/m².an", "ÉNERGIE", x0=0.0)
    _dpe_scale(ax, classe_c,
               ["≤ 6", "7 - 11", "12 - 30", "31 - 50", "51 - 70", "71 - 100",
                "> 100"],
               f"{val_c} kg CO₂/m².an", "CLIMAT", x0=1.35)
    fig.suptitle(titre, fontsize=12, fontweight="bold", color=ANTHRA, y=1.01)
    return save(fig, nom)


# ===========================================================================
# 6 — Comparaison des déperditions avant / après
# ===========================================================================
def fig_gv():
    postes = ["Murs\nextérieurs", "Mur mitoyen\ngarage", "Menuiseries",
              "Renouvellement\nd'air", "Plancher\nbas", "Ponts\nthermiques",
              "Combles"]
    avant = [256.3, 80.9, 73.9, 76.5, 31.6, 27.7, 5.8]
    apres = [23.8, 9.8, 20.5, 38.3, 25.9, 8.1, 5.8]

    fig, ax = plt.subplots(figsize=(9.0, 4.1))
    x = np.arange(len(postes))
    w = 0.38
    b1 = ax.bar(x - w / 2, avant, w, color=ROUGE, zorder=3,
                label="Existant  —  GV = 553 W/K")
    b2 = ax.bar(x + w / 2, apres, w, color=VERT, zorder=3,
                label="Après travaux  —  GV = 132 W/K")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 4,
                    f"{b.get_height():.0f}", ha="center", va="bottom",
                    fontsize=8.6, color=ANTHRA)
    ax.set_ylabel("Déperditions (W/K)", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(postes, fontsize=9.2)
    ax.set_ylim(0, 300)
    style_axes(ax)
    ax.legend(fontsize=9.5, frameon=False)
    ax.set_title("Effet des travaux poste par poste : −76 % de déperditions",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "06_gv_avant_apres")


# ===========================================================================
# 7 — Puissance des radiateurs fonte selon le régime de température
# ===========================================================================
def fig_emetteurs():
    regimes = ["75/65/20\nΔθ = 50 K", "65/55/20\nΔθ = 40 K", "55/45/20\nΔθ = 30 K",
               "50/40/20\nΔθ = 25 K", "45/35/20\nΔθ = 20 K"]
    dt = [50, 40, 30, 25, 20]
    p_nom = 16.25
    puiss = [p_nom * (d / 50.0) ** 1.3 for d in dt]

    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    x = np.arange(len(regimes))
    colors = [BLEU if p >= 4.1 else GRIS for p in puiss]
    bars = ax.bar(x, puiss, width=0.5, color=colors, zorder=3)
    for b, p in zip(bars, puiss):
        ax.text(b.get_x() + b.get_width() / 2, p + 0.45,
                f"{p:.1f} kW".replace(".", ","), ha="center", va="bottom",
                fontsize=10.5, fontweight="bold", color=ANTHRA)
    ax.axhline(17.1, color=ROUGE, linewidth=1.8, linestyle="--", zorder=2)
    ax.text(4.62, 17.1, "Besoin AVANT\ntravaux : 17,1 kW", fontsize=9.3,
            color=ROUGE, va="center", fontweight="bold")
    ax.axhline(4.1, color=VERT, linewidth=1.8, linestyle="--", zorder=2)
    ax.text(4.62, 4.1, "Besoin APRÈS\ntravaux : 4,1 kW", fontsize=9.3,
            color=VERT, va="center", fontweight="bold")
    ax.set_ylabel("Puissance émise par les 7 radiateurs fonte (kW)", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(regimes, fontsize=9)
    ax.set_ylim(0, 21.5)
    ax.set_xlim(-0.55, 6.5)
    style_axes(ax)
    ax.set_title("Après isolation, les radiateurs fonte existants deviennent\n"
                 "compatibles avec un régime basse température",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "07_emetteurs")


# ===========================================================================
# 8 — Facture annuelle comparée
# ===========================================================================
def fig_facture():
    cats = ["Situation actuelle\n(≈ 16 °C réels)",
            "Situation actuelle\nramenée à 19 °C",
            "Scénario B\nétape 1", "Scénario A\n(global)"]
    vals = [6009, 8653, 2963, 1833]
    colors = [ORANGE, ROUGE, BLEU, VERT]

    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    x = np.arange(len(cats))
    bars = ax.bar(x, vals, width=0.55, color=colors, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 150, eur(v) + " €",
                ha="center", va="bottom", fontsize=11.5, fontweight="bold",
                color=ANTHRA)
        ax.text(b.get_x() + b.get_width() / 2, v / 2, f"{v/12:.0f} €/mois",
                ha="center", va="center", fontsize=9.5, color="white",
                fontweight="bold")
    ax.set_ylabel("Coût annuel énergie + entretien (€ TTC)", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=9.5)
    ax.set_ylim(0, 10400)
    style_axes(ax)
    ax.set_title("Coût annuel d'exploitation : état initial et scénarios",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "08_facture")


# ===========================================================================
# 9 — Coût global sur 30 ans
# ===========================================================================
def fig_cout_global():
    cats = ["Ne rien faire", "Scénario B\n(par étapes)", "Scénario A\n(global)"]
    invest = [0, 45800, 44600]
    energie = [170907, 47515, 42377]
    entretien = [6561, 9633, 9963]
    renouv = [14500, 3000, 3000]

    fig, ax = plt.subplots(figsize=(8.4, 4.5))
    x = np.arange(len(cats))
    w = 0.5
    ax.bar(x, invest, w, color=ANTHRA, zorder=3,
           label="Investissement (reste à charge)")
    ax.bar(x, energie, w, bottom=invest, color=ORANGE, zorder=3,
           label="Énergie (20 ans, +4 %/an)")
    bot2 = [a + b for a, b in zip(invest, energie)]
    ax.bar(x, entretien, w, bottom=bot2, color=BLEU, zorder=3,
           label="Entretien et maintenance")
    bot3 = [a + b for a, b in zip(bot2, entretien)]
    ax.bar(x, renouv, w, bottom=bot3, color=GRIS, zorder=3,
           label="Renouvellement des équipements")

    totaux = [i + e + m + r for i, e, m, r in zip(invest, energie, entretien, renouv)]
    for xi, t in zip(x, totaux):
        ax.text(xi, t + 5500, eur(t) + " €", ha="center", va="bottom",
                fontsize=12.5, fontweight="bold", color=ANTHRA)
    ax.set_ylabel("Coût global cumulé sur 20 ans (€)", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10.5, fontweight="bold")
    ax.set_ylim(0, 225000)
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda v, p: eur(v)))
    style_axes(ax)
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    ax.set_title("Analyse en coût global sur 20 ans "
                 "(énergie indexée à +4 %/an)",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "09_cout_global")


# ===========================================================================
# 10 — Trajectoire du DPE
# ===========================================================================
def fig_trajectoire():
    etapes = ["Existant", "Scénario B\nétape 1", "Scénario A\n(global)"]
    conso = [622, 157, 75]
    co2 = [122, 19.5, 2.5]
    classes = ["G", "C", "B"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.0))
    for ax, vals, lab, title in [
            (ax1, conso, "kWh EP/m².an", "Consommation d'énergie primaire"),
            (ax2, co2, "kg CO₂/m².an", "Émissions de gaz à effet de serre")]:
        x = np.arange(len(etapes))
        cols = [DPE_COLORS[c] for c in classes]
        bars = ax.bar(x, vals, width=0.52, color=cols, edgecolor="#90A4AE",
                      linewidth=0.8, zorder=3)
        for b, v, c in zip(bars, vals, classes):
            txt = f"{v}".replace(".", ",")
            ax.text(b.get_x() + b.get_width() / 2, v + max(vals) * 0.035,
                    f"{txt}\nclasse {c}", ha="center", va="bottom",
                    fontsize=9.5, fontweight="bold", color=ANTHRA)
        ax.set_xticks(x)
        ax.set_xticklabels(etapes, fontsize=9)
        ax.set_ylabel(lab, fontsize=9.5)
        ax.set_ylim(0, max(vals) * 1.36)
        style_axes(ax)
        ax.set_title(title, fontsize=10.5, fontweight="bold", color=ANTHRA)
    fig.suptitle("Trajectoire de performance : de la classe G à la classe C puis B",
                 fontsize=12, fontweight="bold", color=ANTHRA, y=1.04)
    fig.tight_layout()
    return save(fig, "10_trajectoire")


# ===========================================================================
# 11 — Plan de financement
# ===========================================================================
def fig_financement():
    fig, ax = plt.subplots(figsize=(8.8, 4.3))
    scen = ["Scénario A — global\n85 100 € TTC",
            "Scénario B — étape 1\n65 600 € TTC",
            "Scénario B — étape 2\n22 500 € TTC"]
    series = [("MaPrimeRénov'", [38500, 34200, 3400], VERT),
              ("CEE et aides locales", [2000, 2000, 2700], VERT_CLAIR),
              ("Apport personnel", [10000, 10000, 0], BLEU),
              ("Éco-PTZ à taux zéro", [34600, 19400, 16400], ORANGE)]
    y = np.arange(len(scen))[::-1]
    h = 0.46
    left = np.zeros(3)
    for lab, vals, col in series:
        ax.barh(y, vals, h, left=left, color=col, zorder=3, label=lab)
        for yi, v, l in zip(y, vals, left):
            if v > 3500:
                ax.text(l + v / 2, yi, eur(v), ha="center", va="center",
                        fontsize=9, fontweight="bold", color="white")
        left = left + np.array(vals, dtype=float)
    ax.set_yticks(y)
    ax.set_yticklabels(scen, fontsize=10, fontweight="bold")
    ax.set_xlabel("€ TTC", fontsize=10)
    ax.set_xlim(0, 95000)
    ax.get_xaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda v, p: eur(v)))
    style_axes(ax, grid_axis="x")
    ax.legend(fontsize=9, frameon=False, ncol=4, loc="upper center",
              bbox_to_anchor=(0.5, -0.20))
    ax.set_title("Plan de financement : comment chaque opération est couverte",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "11_financement")


# ===========================================================================
# 12 — Autofinancement mensuel
# ===========================================================================
def fig_autofinancement():
    fig, ax = plt.subplots(figsize=(8.4, 4.1))
    cats = ["Scénario A — global", "Scénario B — étape 1"]
    eco = [4176 / 12, 3046 / 12]
    mens = [144, 81]
    x = np.arange(len(cats))
    w = 0.30
    b1 = ax.bar(x - w / 2 - 0.03, eco, w, color=VERT, zorder=3,
                label="Économie mensuelle sur les factures")
    b2 = ax.bar(x + w / 2 + 0.03, mens, w, color=ORANGE, zorder=3,
                label="Mensualité de l'éco-PTZ (20 ans)")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 6,
                    f"{b.get_height():.0f} €", ha="center", va="bottom",
                    fontsize=10.5, fontweight="bold", color=ANTHRA)
    for xi, e, m in zip(x, eco, mens):
        ax.annotate("", xy=(xi + 0.30, e), xytext=(xi + 0.30, m),
                    arrowprops=dict(arrowstyle="<->", color=VERT, linewidth=1.6))
        ax.text(xi + 0.36, (e + m) / 2, f"+ {e-m:.0f} €/mois\nde gain net",
                fontsize=9.5, color=VERT, fontweight="bold", va="center")
    ax.set_ylabel("€ par mois", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=10.5, fontweight="bold")
    ax.set_ylim(0, 430)
    ax.set_xlim(-0.6, 1.95)
    style_axes(ax)
    ax.legend(fontsize=9.5, frameon=False, loc="upper left")
    ax.set_title("Les deux scénarios s'autofinancent dès la première année",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "12_autofinancement")


# ===========================================================================
# 13 — Comparaison à la moyenne nationale
# ===========================================================================
def fig_comparaison_nationale():
    fig, ax = plt.subplots(figsize=(8.4, 3.5))
    labels = ["Ce logement\n(état existant)", "Moyenne du parc\nrésidentiel français",
              "Objectif BBC\nrénovation", "Ce logement\naprès scénario 2"]
    vals = [622, 250, 110, 75]
    colors = [ROUGE, GRIS, VERT_CLAIR, VERT]
    y = np.arange(len(labels))[::-1]
    bars = ax.barh(y, vals, height=0.55, color=colors, zorder=3)
    for b, v in zip(bars, vals):
        ax.text(v + 10, b.get_y() + b.get_height() / 2, f"{v} kWh EP/m².an",
                va="center", fontsize=10.5, fontweight="bold", color=ANTHRA)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlim(0, 800)
    ax.set_xlabel("Consommation d'énergie primaire (kWh EP/m².an)", fontsize=9.5)
    style_axes(ax, grid_axis="x")
    ax.set_title("Le logement consomme 2,5 fois la moyenne nationale",
                 fontsize=11.5, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "13_comparaison_nationale")


# ===========================================================================
# 14 — Sensibilité au prix des énergies
# ===========================================================================
def fig_sensibilite():
    fig, ax = plt.subplots(figsize=(8.4, 4.0))
    scenarios = ["Prix bas\npropane 1,50 €/kg\nélec. 0,22 €/kWh",
                 "Hypothèse retenue\npropane 1,80 €/kg\nélec. 0,25 €/kWh",
                 "Prix haut\npropane 2,20 €/kg\nélec. 0,30 €/kWh"]
    ecoB = [2616, 3046, 3619]
    ecoA = [3522, 4176, 5007]
    x = np.arange(len(scenarios))
    w = 0.35
    b1 = ax.bar(x - w / 2, ecoB, w, color=BLEU, zorder=3,
                label="Scénario B — étape 1")
    b2 = ax.bar(x + w / 2, ecoA, w, color=VERT, zorder=3,
                label="Scénario A — global")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 80,
                    eur(b.get_height()) + " €", ha="center", va="bottom",
                    fontsize=9.5, fontweight="bold", color=ANTHRA)
    ax.set_ylabel("Économie annuelle (€/an)", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=8.8)
    ax.set_ylim(0, 6100)
    style_axes(ax)
    ax.legend(fontsize=9.5, frameon=False)
    ax.set_title("Analyse de sensibilité : la rentabilité résiste "
                 "à toutes les hypothèses de prix",
                 fontsize=11, fontweight="bold", color=ANTHRA, pad=10)
    return save(fig, "14_sensibilite")


if __name__ == "__main__":
    print("Génération des figures :")
    fig_consommations()
    fig_correction_climat()
    fig_postes()
    fig_deperditions()
    fig_dpe("05_dpe_existant", "G", "G", "622", "122",
            "DPE de l'existant : classe G / G — passoire thermique")
    fig_gv()
    fig_emetteurs()
    fig_facture()
    fig_cout_global()
    fig_trajectoire()
    fig_financement()
    fig_autofinancement()
    fig_comparaison_nationale()
    fig_sensibilite()
    fig_dpe("15_dpe_etape1", "C", "C", "157", "19,5",
            "DPE après l'étape 1 du scénario B : classe C (énergie C / climat C)")
    fig_dpe("16_dpe_global", "B", "A", "75", "2,5",
            "DPE après le scénario A global : classe B (énergie B / climat A)")
    print("Terminé.")
