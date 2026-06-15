# -*- coding: utf-8 -*-
"""
Génération du diaporama oral - Rénovation énergétique
Maison à Saint-Jean-de-Chevelu (Savoie)
Guillaume Tardy - Bloc 1 - Chargé de projet énergie et bâtiment durables
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION

# ---------------------------------------------------------------------------
# CHARTE GRAPHIQUE
# ---------------------------------------------------------------------------
VERT      = RGBColor(0x1B, 0x5E, 0x20)   # vert foncé principal
VERT_CLR  = RGBColor(0x2E, 0x7D, 0x32)   # vert moyen
VERT_LIGHT= RGBColor(0xE8, 0xF5, 0xE9)   # vert très clair (fonds)
GRIS_TXT  = RGBColor(0x37, 0x47, 0x4F)   # texte gris foncé
GRIS_CLR  = RGBColor(0x90, 0xA4, 0xAE)   # gris clair
BLANC     = RGBColor(0xFF, 0xFF, 0xFF)
ANTHRA    = RGBColor(0x26, 0x32, 0x38)
ORANGE    = RGBColor(0xE6, 0x51, 0x00)
BLEU      = RGBColor(0x15, 0x65, 0xC0)
ROUGE     = RGBColor(0xC6, 0x28, 0x28)

# Couleurs étiquettes DPE A -> G
DPE_COLORS = {
    "A": RGBColor(0x00, 0x83, 0x36),
    "B": RGBColor(0x57, 0xAA, 0x27),
    "C": RGBColor(0xC3, 0xD0, 0x00),
    "D": RGBColor(0xFC, 0xEA, 0x10),
    "E": RGBColor(0xF7, 0xB1, 0x00),
    "F": RGBColor(0xEA, 0x6C, 0x16),
    "G": RGBColor(0xE2, 0x00, 0x1A),
}

prs = Presentation()
prs.slide_width  = Inches(13.333)   # format 16:9
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

# ---------------------------------------------------------------------------
# FONCTIONS UTILITAIRES
# ---------------------------------------------------------------------------
def add_slide():
    return prs.slides.add_slide(BLANK)

def set_bg(slide, color):
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    rect.fill.solid(); rect.fill.fore_color.rgb = color
    rect.line.fill.background()
    rect.shadow.inherit = False
    slide.shapes._spTree.remove(rect._element)
    slide.shapes._spTree.insert(2, rect._element)
    return rect

def box(slide, l, t, w, h, fill=None, line=None, line_w=None, shape=MSO_SHAPE.RECTANGLE, shadow=False):
    sp = slide.shapes.add_shape(shape, l, t, w, h)
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line
        sp.line.width = line_w or Pt(1)
    sp.shadow.inherit = False
    return sp

def text(slide, l, t, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         space_after=Pt(4), line_spacing=1.0, wrap=True):
    """runs: liste de paragraphes ; chaque paragraphe = liste de tuples (txt, size, bold, color, italic)"""
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = Pt(2); tf.margin_right = Pt(2)
    tf.margin_top = Pt(2); tf.margin_bottom = Pt(2)
    first = True
    for para in runs:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align
        p.space_after = space_after
        p.line_spacing = line_spacing
        for seg in para:
            txt, size, bold, color = seg[0], seg[1], seg[2], seg[3]
            italic = seg[4] if len(seg) > 4 else False
            r = p.add_run(); r.text = txt
            r.font.size = Pt(size); r.font.bold = bold
            r.font.color.rgb = color; r.font.italic = italic
            r.font.name = "Calibri"
    return tb

def notes(slide, txt):
    slide.notes_slide.notes_text_frame.text = txt

def header(slide, num_section, titre, sous_titre=None):
    """Bandeau de titre standard pour les slides de contenu."""
    set_bg(slide, BLANC)
    # bande latérale verte
    box(slide, 0, 0, Inches(0.22), SH, fill=VERT)
    # pastille numéro
    if num_section:
        c = box(slide, Inches(0.55), Inches(0.42), Inches(0.72), Inches(0.72),
                fill=VERT, shape=MSO_SHAPE.OVAL)
        text(slide, Inches(0.55), Inches(0.42), Inches(0.72), Inches(0.72),
             [[(num_section, 26, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        tl = Inches(1.45)
    else:
        tl = Inches(0.6)
    text(slide, tl, Inches(0.40), Inches(11.3), Inches(0.85),
         [[(titre, 30, True, VERT)]], anchor=MSO_ANCHOR.MIDDLE)
    if sous_titre:
        text(slide, tl, Inches(1.18), Inches(11.3), Inches(0.4),
             [[(sous_titre, 15, False, GRIS_CLR, True)]])
    # filet sous le titre
    box(slide, tl, Inches(1.30), Inches(11.0), Pt(2.2), fill=VERT_CLR)
    # pied de page
    text(slide, Inches(0.55), Inches(7.05), Inches(9), Inches(0.35),
         [[("Rénovation énergétique – Saint-Jean-de-Chevelu (73)", 9, False, GRIS_CLR)]])
    text(slide, Inches(10.3), Inches(7.05), Inches(2.5), Inches(0.35),
         [[("Guillaume Tardy", 9, False, GRIS_CLR)]], align=PP_ALIGN.RIGHT)

def make_table(slide, l, t, w, rows, col_widths, row_h=Inches(0.4),
               header_fill=VERT, body_fill=BLANC, alt_fill=VERT_LIGHT,
               header_size=13, body_size=12, first_col_bold=False):
    """rows : liste de listes de chaînes. La 1ère ligne = en-tête."""
    total = sum(col_widths, Emu(0))
    nrows = len(rows)
    tbl_h = row_h * nrows
    gtbl = slide.shapes.add_table(nrows, len(col_widths), l, t, total, tbl_h).table
    gtbl.first_row = False; gtbl.horz_banding = False
    for ci, cw in enumerate(col_widths):
        gtbl.columns[ci].width = cw
    for ri in range(nrows):
        gtbl.rows[ri].height = row_h
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = gtbl.cell(ri, ci)
            cell.margin_left = Pt(7); cell.margin_right = Pt(7)
            cell.margin_top = Pt(2); cell.margin_bottom = Pt(2)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            if ri == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = header_fill
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = alt_fill if ri % 2 == 0 else body_fill
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER
            r = p.add_run(); r.text = val
            r.font.name = "Calibri"
            if ri == 0:
                r.font.size = Pt(header_size); r.font.bold = True; r.font.color.rgb = BLANC
            else:
                r.font.size = Pt(body_size)
                r.font.bold = (ci == 0 and first_col_bold)
                r.font.color.rgb = GRIS_TXT
    return gtbl

def dpe_label(slide, cx, top, current, label_txt="Classe énergie", scale_h=Inches(0.42),
              base_w=Inches(1.0), step=Inches(0.34), letter_size=16, label_size=12):
    """Dessine une échelle DPE verticale A->G avec la classe courante mise en avant.
    Le marqueur de la classe courante est placé à GAUCHE de l'échelle (ne déborde pas)."""
    letters = ["A", "B", "C", "D", "E", "F", "G"]
    text(slide, cx, top, base_w + step * 6, Inches(0.3),
         [[(label_txt, label_size, True, GRIS_TXT)]], align=PP_ALIGN.LEFT)
    y = top + Inches(0.36)
    for i, ltr in enumerate(letters):
        w = base_w + step * i
        is_cur = (ltr == current)
        bar = box(slide, cx, y, w, scale_h, fill=DPE_COLORS[ltr],
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE,
                  line=(ANTHRA if is_cur else None), line_w=Pt(2.5))
        text(slide, cx + Inches(0.06), y, w - Inches(0.08), scale_h,
             [[(ltr, letter_size, True, BLANC)]], anchor=MSO_ANCHOR.MIDDLE)
        if is_cur:
            # flèche-marqueur à gauche
            mk = box(slide, cx - Inches(0.34), y, Inches(0.30), scale_h,
                     fill=ANTHRA, shape=MSO_SHAPE.PENTAGON)
        y += scale_h + Inches(0.06)
    return y

def bullet_block(slide, l, t, w, h, items, size=15, color=GRIS_TXT, gap=Pt(8),
                 marker="●", marker_color=VERT_CLR, line_spacing=1.05):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame; tf.word_wrap = True
    first = True
    for it in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = gap; p.line_spacing = line_spacing
        r0 = p.add_run(); r0.text = marker + "  "
        r0.font.size = Pt(size); r0.font.color.rgb = marker_color; r0.font.bold = True
        r0.font.name = "Calibri"
        # texte (support gras via tuple)
        if isinstance(it, tuple):
            bold_part, normal_part = it
            r1 = p.add_run(); r1.text = bold_part
            r1.font.size = Pt(size); r1.font.bold = True; r1.font.color.rgb = color; r1.font.name="Calibri"
            r2 = p.add_run(); r2.text = normal_part
            r2.font.size = Pt(size); r2.font.color.rgb = color; r2.font.name="Calibri"
        else:
            r1 = p.add_run(); r1.text = it
            r1.font.size = Pt(size); r1.font.color.rgb = color; r1.font.name="Calibri"
    return tb

def kpi_card(slide, l, t, w, h, value, label, accent=VERT, val_size=30):
    card = box(slide, l, t, w, h, fill=BLANC, line=GRIS_CLR, line_w=Pt(1),
               shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    box(slide, l, t, w, Inches(0.12), fill=accent, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(slide, l, t + Inches(0.18), w, h - Inches(0.6),
         [[(value, val_size, True, accent)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(slide, l, t + h - Inches(0.55), w, Inches(0.5),
         [[(label, 11, False, GRIS_TXT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

# ===========================================================================
# DIAPO 1 — TITRE
# ===========================================================================
s = add_slide()
set_bg(s, VERT)
box(s, 0, 0, SW, Inches(2.4), fill=VERT_CLR)
box(s, 0, Inches(2.4), SW, Pt(4), fill=RGBColor(0xA5,0xD6,0xA7))
# eyebrow
text(s, Inches(1.0), Inches(0.7), Inches(11), Inches(0.5),
     [[("FORMATION CHARGÉ DE PROJET ÉNERGIE ET BÂTIMENT DURABLES — BLOC 1", 13, True, VERT)]])
text(s, Inches(1.0), Inches(1.25), Inches(11), Inches(1.0),
     [[("Soutenance d’étude énergétique", 20, False, VERT)]])
# titre principal
text(s, Inches(1.0), Inches(2.95), Inches(11.3), Inches(1.8),
     [[("Rénovation énergétique d’une", 40, True, BLANC)],
      [("ancienne ferme savoyarde", 40, True, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.05)
text(s, Inches(1.0), Inches(4.7), Inches(11), Inches(0.6),
     [[("Maison individuelle — Saint-Jean-de-Chevelu (73), Savoie", 18, False, RGBColor(0xE8,0xF5,0xE9))]])
# bandeau bas
box(s, 0, Inches(6.4), SW, Inches(1.1), fill=ANTHRA)
text(s, Inches(1.0), Inches(6.55), Inches(8), Inches(0.85),
     [[("Présenté par Guillaume Tardy", 16, True, BLANC)],
      [("Diagnostic · Scénarios de rénovation · Analyse économique", 12, False, GRIS_CLR)]])
text(s, Inches(9.3), Inches(6.55), Inches(3), Inches(0.85),
     [[("Année 2026", 14, True, BLANC)]], align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Bonjour, je suis Guillaume Tardy. Je vais vous présenter mon étude énergétique "
         "portant sur la rénovation d'une maison individuelle, une ancienne ferme du XIXe siècle "
         "située à Saint-Jean-de-Chevelu en Savoie. Mon objectif : diagnostiquer la performance "
         "actuelle, identifier les faiblesses, puis proposer et comparer deux scénarios de rénovation. "
         "La présentation dure une vingtaine de minutes.")

# ===========================================================================
# DIAPO 2 — SOMMAIRE
# ===========================================================================
s = add_slide()
header(s, None, "Sommaire de la présentation")
items = [
    ("1", "Analyse de la situation et objectifs", "Contexte, maître d’ouvrage, objectifs"),
    ("2", "Analyse technique de l’existant", "Consommations, enveloppe, systèmes"),
    ("3", "Bilan des déperditions & DPE", "Où part la chaleur ? Étiquette actuelle"),
    ("4", "Les deux scénarios de rénovation", "Scénario 1 et Scénario 2"),
    ("5", "Dimensionnement & matériaux", "Calculs, isolants biosourcés"),
    ("6", "Analyse économique", "Coûts, aides, ROI, coût global 30 ans"),
    ("7", "Plan de sobriété & conclusion", "Recommandation finale"),
]
y = Inches(1.75)
for num, titre, sub in items:
    box(s, Inches(0.9), y, Inches(0.55), Inches(0.55), fill=VERT, shape=MSO_SHAPE.OVAL)
    text(s, Inches(0.9), y, Inches(0.55), Inches(0.55),
         [[(num, 18, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(1.7), y - Inches(0.02), Inches(7.5), Inches(0.4),
         [[(titre, 17, True, GRIS_TXT)]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(1.7), y + Inches(0.32), Inches(10), Inches(0.3),
         [[(sub, 12, False, GRIS_CLR, True)]])
    y += Inches(0.72)
notes(s, "Voici le déroulé : je commence par le contexte et les attentes du maître d'ouvrage, "
         "puis le diagnostic technique de l'existant. J'aborde ensuite les déperditions et le DPE, "
         "qui justifient les travaux. Je présente les deux scénarios de rénovation, leur dimensionnement, "
         "et enfin l'analyse économique qui guide ma recommandation finale.")

# ===========================================================================
# DIAPO 3 — CONTEXTE / NATURE DU PROJET
# ===========================================================================
s = add_slide()
header(s, "1", "Analyse de la situation", "Nature du projet et contexte")
# colonne gauche : description
bullet_block(s, Inches(0.9), Inches(1.7), Inches(6.4), Inches(4.5), [
    ("Ancienne ferme ", "de la fin du XIXᵉ siècle, réhabilitée dans les années 1990"),
    ("Maison individuelle ", "occupée par une famille (résidence principale)"),
    ("Surface habitable chauffée : ", "≈ 99 m² sur 2 niveaux"),
    ("Zones non chauffées : ", "garage, appentis, combles perdus"),
    ("Murs en pierre calcaire ", "de 50 cm — forte inertie, patrimoine local"),
    ("Objectif de l’étude : ", "évaluer la performance, cibler les déperditions et proposer des solutions adaptées au bâti ancien"),
], size=15, gap=Pt(11))
# colonne droite : carte d'identité
box(s, Inches(7.7), Inches(1.7), Inches(4.6), Inches(4.4), fill=VERT_LIGHT,
    shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(7.95), Inches(1.85), Inches(4.1), Inches(0.4),
     [[("Carte d’identité du bâtiment", 14, True, VERT)]])
make_table(s, Inches(7.95), Inches(2.4), Inches(4.1), [
    ["Caractéristique", "Valeur"],
    ["Localisation", "Saint-Jean-de-Chevelu (73)"],
    ["Altitude", "498 m"],
    ["Environnement", "Rural"],
    ["Orientation", "Sud-Est"],
    ["Surface chauffée", "99 m²"],
    ["Niveaux", "2"],
], [Inches(2.0), Inches(2.1)], row_h=Inches(0.43), header_size=12, body_size=11)
notes(s, "Le bâtiment étudié est une ancienne ferme savoyarde de la fin du XIXe siècle, "
         "réhabilitée dans les années 90. La surface habitable chauffée est d'environ 99 m² sur deux niveaux. "
         "Particularité importante : des murs en pierre calcaire de 50 cm, qui offrent une forte inertie mais "
         "très peu d'isolation. Tout l'enjeu sera de l'isoler SANS dénaturer le bâti et en gérant l'humidité. "
         "L'étude porte sur l'enveloppe, le chauffage, l'ECS et la ventilation.")

# ===========================================================================
# DIAPO 4 — OBJECTIFS & BESOINS DU MAÎTRE D'OUVRAGE
# ===========================================================================
s = add_slide()
header(s, "1", "Objectifs et attentes du maître d’ouvrage")
text(s, Inches(0.9), Inches(1.65), Inches(11), Inches(0.4),
     [[("Le maître d’ouvrage souhaite engager une rénovation durable, compatible avec son bâti ancien.", 15, False, GRIS_TXT, True)]])
# deux colonnes
text(s, Inches(0.9), Inches(2.2), Inches(5.6), Inches(0.4), [[("Besoins exprimés", 16, True, VERT)]])
bullet_block(s, Inches(0.9), Inches(2.7), Inches(5.6), Inches(4), [
    "Réduire les dépenses énergétiques",
    "Améliorer le confort d’hiver (parois froides)",
    "Améliorer le confort d’été (surchauffe sous toiture)",
    "Remplacer à terme la chaudière fioul",
    "Réduire les émissions de gaz à effet de serre",
    "Valoriser le patrimoine immobilier",
], size=14, gap=Pt(9))
text(s, Inches(6.9), Inches(2.2), Inches(5.6), Inches(0.4), [[("Moyens & contraintes", 16, True, VERT)]])
bullet_block(s, Inches(6.9), Inches(2.7), Inches(5.6), Inches(4), [
    "Budget permettant des travaux importants…",
    "… mais investissements à justifier par les économies",
    "Conserver le caractère architectural de la ferme",
    "Solutions compatibles avec les murs en pierre épais",
    "Limiter les risques liés à l’humidité",
    "Mobiliser les aides financières disponibles",
], size=14, gap=Pt(9), marker_color=ORANGE)
notes(s, "Le maître d'ouvrage occupant a des besoins clairs : réduire ses factures, gagner en confort "
         "hiver comme été, remplacer la vieille chaudière fioul et baisser son empreinte carbone. "
         "Côté contraintes : il a un budget mais veut des investissements justifiés par les économies. "
         "Surtout, il tient à conserver le cachet de la ferme et à respecter les murs en pierre, "
         "ce qui oriente fortement vers une isolation par l'extérieur et des matériaux adaptés à l'humidité.")

# ===========================================================================
# DIAPO 5 — OBJECTIFS À ATTEINDRE (confort)
# ===========================================================================
s = add_slide()
header(s, "2", "Objectifs à atteindre", "Performance énergétique & confort des habitants")
make_table(s, Inches(0.9), Inches(1.8), Inches(11.5), [
    ["Type de confort", "Situation actuelle", "Amélioration attendue"],
    ["Confort d’hiver", "Parois froides, écarts de T° entre pièces", "Températures homogènes, fin des parois froides"],
    ["Confort d’été", "Surchauffe des pièces sous toiture", "Température plus stable (isolants déphasants)"],
    ["Qualité de l’air", "Ventilation naturelle non maîtrisée", "Renouvellement d’air contrôlé (VMC)"],
    ["Confort acoustique", "Isolation phonique limitée", "Atténuation des bruits extérieurs (ITE)"],
    ["Confort d’utilisation", "Chauffage peu régulé, équipts vieillissants", "Régulation précise, équipement fiable"],
    ["Confort sanitaire", "Risque de condensation", "Réduction de l’humidité"],
], [Inches(2.3), Inches(4.5), Inches(4.7)], row_h=Inches(0.62), header_size=13, body_size=12, first_col_bold=True)
notes(s, "Au-delà des économies, l'objectif est le confort sur toute l'année. "
         "Ce tableau confronte la situation actuelle aux gains attendus, poste par poste : "
         "confort d'hiver avec la fin des parois froides, confort d'été grâce au déphasage des isolants biosourcés, "
         "qualité de l'air avec la VMC, et confort acoustique apporté par l'isolation extérieure. "
         "Remarque : aucun besoin d'accessibilité PMR n'a été identifié dans cette étude.")

# ===========================================================================
# DIAPO 6 — CONSOMMATIONS D'ÉNERGIE
# ===========================================================================
s = add_slide()
header(s, "2", "Analyse des consommations d’énergie", "Relevés sur 5 ans")
# 3 cartes KPI
kpi_card(s, Inches(0.9), Inches(1.75), Inches(3.6), Inches(1.5), "1 560 L/an", "Fioul (moyenne) — chauffage principal", accent=ORANGE, val_size=26)
kpi_card(s, Inches(4.7), Inches(1.75), Inches(3.6), Inches(1.5), "6 stères/an", "Bois bûche — poêle d’appoint", accent=VERT_CLR, val_size=26)
kpi_card(s, Inches(8.5), Inches(1.75), Inches(3.6), Inches(1.5), "5 447 kWh/an", "Électricité — ECS, éclairage, usages", accent=BLEU, val_size=26)
# graphique évolution fioul + élec
chart_data = CategoryChartData()
chart_data.categories = ["19-20", "20-21", "21-22", "22-23", "23-24"]
chart_data.add_series("Fioul (L)", (1500, 1800, 1700, 1400, 1400))
chart_data.add_series("Électricité (kWh)", (5552, 5679, 5334, 5207, 5461))
gframe = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,
                            Inches(0.9), Inches(3.5), Inches(7.0), Inches(3.1), chart_data)
chart = gframe.chart
chart.has_title = True; chart.chart_title.text_frame.text = "Évolution des consommations"
chart.chart_title.text_frame.paragraphs[0].font.size = Pt(12)
chart.has_legend = True; chart.legend.position = XL_LEGEND_POSITION.BOTTOM; chart.legend.include_in_layout = False
chart.legend.font.size = Pt(9)
chart.plots[0].series[0].format.fill.solid(); chart.plots[0].series[0].format.fill.fore_color.rgb = ORANGE
chart.plots[0].series[1].format.fill.solid(); chart.plots[0].series[1].format.fill.fore_color.rgb = BLEU
# commentaire à droite
box(s, Inches(8.3), Inches(3.5), Inches(4.0), Inches(3.1), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(8.55), Inches(3.65), Inches(3.5), Inches(0.4), [[("Ce que cela révèle", 14, True, VERT)]])
bullet_block(s, Inches(8.55), Inches(4.15), Inches(3.6), Inches(2.4), [
    "Forte dépendance au fioul (chaudière de 1991)",
    "Consommation élevée pour 99 m²",
    "Cause : enveloppe peu performante (murs + combles)",
    "ECS électrique = poste électrique majeur",
], size=12, gap=Pt(7))
notes(s, "J'ai analysé les relevés sur 5 ans. Le chauffage repose sur une chaudière fioul de 1991, "
         "complétée par un poêle à bois en appoint. La moyenne est de 1 560 litres de fioul par an, "
         "6 stères de bois, et 5 447 kWh d'électricité (dont l'eau chaude sanitaire par ballon électrique). "
         "1 560 L pour 99 m², c'est beaucoup : le signe d'une enveloppe thermique défaillante. "
         "C'est ce diagnostic des consommations qui justifie d'aller regarder l'enveloppe en détail.")

# ===========================================================================
# DIAPO 7 — ENVELOPPE THERMIQUE
# ===========================================================================
s = add_slide()
header(s, "2", "Analyse de l’enveloppe thermique")
make_table(s, Inches(0.9), Inches(1.75), Inches(11.5), [
    ["Élément", "Composition", "Observation"],
    ["Murs extérieurs", "Pierre calcaire 50 cm", "Forte inertie mais faible isolation"],
    ["Toiture / combles", "8 cm laine minérale ancienne", "Isolation insuffisante"],
    ["Menuiseries", "Double vitrage bois 4/16/4 Argon", "Bon état, performances satisfaisantes"],
    ["Plancher bas", "Dalle béton sur terre-plein", "Non isolé → déperditions"],
    ["Ponts thermiques", "Jonctions des parois", "Pertes importantes"],
], [Inches(2.6), Inches(4.0), Inches(4.9)], row_h=Inches(0.6), header_size=13, body_size=12, first_col_bold=True)
box(s, Inches(0.9), Inches(5.5), Inches(11.5), Inches(1.1), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.62), Inches(11.0), Inches(0.9),
     [[("À retenir : ", 14, True, VERT), ("les fenêtres ont déjà été rénovées (peu de pertes). "
        "Les axes prioritaires sont donc l’isolation des murs et de la toiture.", 14, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "L'enveloppe, c'est l'interface entre le chauffé et l'extérieur. Point par point : "
         "les murs en pierre de 50 cm ont une forte inertie mais ne sont pas isolés ; les combles n'ont que "
         "8 cm de laine minérale ancienne, c'est très insuffisant ; les menuiseries en double vitrage bois argon "
         "sont récentes et performantes ; le plancher sur terre-plein n'est pas isolé. "
         "Conclusion clé : comme les fenêtres sont déjà bonnes, je concentre les travaux sur les murs et la toiture.")

# ===========================================================================
# DIAPO 8 — SYSTÈMES & VENTILATION
# ===========================================================================
s = add_slide()
header(s, "2", "Analyse des systèmes existants", "Chauffage, ECS et ventilation")
make_table(s, Inches(0.9), Inches(1.75), Inches(11.5), [
    ["Équipement", "Description", "Limite principale"],
    ["Chaudière fioul", "Basse température, installée en 1991", "Ancienne, énergie fossile émettrice de CO₂"],
    ["Poêle à bois", "Bûches, installé en 2010 (appoint)", "Pas de label Flamme Verte, non étanche"],
    ["Ballon ECS", "Électrique 200 L, hors volume chauffé", "Pertes thermiques, conso électrique"],
    ["Régulation", "Thermostat non programmable", "Gestion peu optimisée"],
    ["Ventilation", "Naturelle (pas de VMC)", "Débits non maîtrisés, pertes importantes"],
], [Inches(2.4), Inches(4.4), Inches(4.7)], row_h=Inches(0.6), header_size=13, body_size=12, first_col_bold=True)
box(s, Inches(0.9), Inches(5.55), Inches(11.5), Inches(1.0), fill=RGBColor(0xFF,0xF3,0xE0), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.65), Inches(11.0), Inches(0.8),
     [[("Constat : ", 14, True, ORANGE), ("des équipements vieillissants et énergivores, "
        "et surtout l’absence totale de ventilation mécanique → un poste de pertes majeur.", 14, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Côté systèmes : la chaudière fioul de 1991 fonctionne encore mais a un rendement limité et émet beaucoup de CO2. "
         "Le poêle à bois aide en appoint mais n'est ni labellisé ni étanche. L'eau chaude est produite par un ballon "
         "électrique de 200 L placé dans un local non chauffé, ce qui génère des pertes. "
         "Et surtout : aucune VMC. Le renouvellement d'air se fait par les défauts d'étanchéité, "
         "ce qui est à la fois mauvais pour la qualité de l'air et très coûteux en énergie.")

# ===========================================================================
# DIAPO 9 — BILAN DES DÉPERDITIONS (camembert)
# ===========================================================================
s = add_slide()
header(s, "3", "Bilan des déperditions thermiques", "Où part la chaleur ?")
# camembert
cdata = CategoryChartData()
cdata.categories = ["Murs extérieurs", "Toiture", "Ventilation", "Ponts thermiques", "Fenêtres", "Plancher bas"]
cdata.add_series("Déperditions", (42, 20, 20, 10, 4, 4))
gf = s.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(0.7), Inches(1.7), Inches(6.3), Inches(4.9), cdata)
ch = gf.chart
ch.has_title = False
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.RIGHT; ch.legend.include_in_layout = False
ch.legend.font.size = Pt(11)
plot = ch.plots[0]
plot.has_data_labels = True
dl = plot.data_labels
dl.show_percentage = False; dl.show_value = True
dl.number_format = '0"%"'; dl.number_format_is_linked = False
dl.font.size = Pt(11); dl.font.bold = True; dl.font.color.rgb = BLANC
dl.position = XL_LABEL_POSITION.INSIDE_END
pie_colors = [ROUGE, ORANGE, BLEU, RGBColor(0x8E,0x24,0xAA), VERT_CLR, GRIS_CLR]
for i, pt in enumerate(plot.series[0].points):
    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = pie_colors[i]
# indicateurs techniques à droite
text(s, Inches(7.5), Inches(1.7), Inches(5), Inches(0.4), [[("Indicateurs techniques", 15, True, VERT)]])
make_table(s, Inches(7.5), Inches(2.2), Inches(4.9), [
    ["Indicateur", "Valeur"],
    ["Surface déperditive", "232,91 m²"],
    ["Coefficient Ubât", "2,03 W/(m².K)"],
    ["Ubât de référence", "0,47 W/(m².K)"],
    ["Coefficient GV", "722 W/K"],
    ["Puissance de chauffage", "21,3 kW"],
], [Inches(2.9), Inches(2.0)], row_h=Inches(0.48), header_size=12, body_size=12)
text(s, Inches(7.5), Inches(5.55), Inches(4.9), Inches(1.0),
     [[("Ubât 4× supérieur à la référence : l’enveloppe est le vrai problème.", 13, True, ROUGE)]])
notes(s, "Ce camembert est central dans mon étude. Il montre où part la chaleur : "
         "42 % par les murs, 20 % par la toiture, 20 % par la ventilation, 10 % par les ponts thermiques, "
         "et seulement 4 % chacun pour fenêtres et plancher. "
         "À droite, l'indicateur clé : le Ubât du bâtiment est de 2,03, soit plus de 4 fois la référence de 0,47. "
         "La puissance de chauffage nécessaire est de 21,3 kW. Ce graphique justifie directement mes priorités de travaux : "
         "murs, toiture et ventilation représentent à eux seuls plus de 80 % des pertes.")

# ===========================================================================
# DIAPO 10 — DPE EXISTANT (G)
# ===========================================================================
s = add_slide()
header(s, "3", "Étiquette DPE de l’existant", "Un logement très énergivore")
dpe_label(s, Inches(1.0), Inches(1.7), "G", "Classe énergie")
dpe_label(s, Inches(4.6), Inches(1.7), "G", "Classe climat (GES)")
# KPI à droite
kpi_card(s, Inches(8.2), Inches(1.9), Inches(4.1), Inches(1.15), "535 kWhEP/m².an", "Consommation énergétique", accent=ROUGE, val_size=22)
kpi_card(s, Inches(8.2), Inches(3.2), Inches(4.1), Inches(1.15), "156 kgCO₂/m².an", "Émissions de gaz à effet de serre", accent=ROUGE, val_size=22)
kpi_card(s, Inches(8.2), Inches(4.5), Inches(4.1), Inches(1.15), "7 100 – 9 610 €/an", "Coût énergétique annuel", accent=ROUGE, val_size=22)
text(s, Inches(0.9), Inches(6.45), Inches(11.4), Inches(0.7),
     [[("→ Classe G sur les deux étiquettes : la rénovation est pleinement justifiée.", 15, True, VERT)]])
notes(s, "Tout converge vers le DPE. Le logement est classé G — la pire classe — à la fois en énergie et en climat. "
         "Concrètement : 535 kWh d'énergie primaire par m² et par an, 156 kg de CO2 par m², "
         "et une facture énergétique comprise entre 7 100 et 9 610 € par an. "
         "C'est une passoire thermique, principalement à cause des murs non isolés et de la chaudière fioul. "
         "Cet état des lieux justifie pleinement d'engager des travaux ambitieux, ce qui m'amène aux scénarios.")

# ===========================================================================
# DIAPO 11 — RÉGLEMENTATION
# ===========================================================================
s = add_slide()
header(s, "4", "Réglementation et urbanisme")
text(s, Inches(0.9), Inches(1.65), Inches(11.4), Inches(0.5),
     [[("Les travaux doivent respecter le cadre réglementaire et préserver le caractère de la ferme.", 15, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.25), Inches(11.5), [
    ["Élément réglementaire", "Impact sur le projet"],
    ["Plan Local d’Urbanisme (PLU)", "Vérification des règles applicables"],
    ["Isolation thermique par l’extérieur", "Déclaration préalable de travaux possible"],
    ["Modification des façades", "Respect de l’aspect architectural existant"],
    ["Aides à la rénovation énergétique", "Respect des critères techniques exigés"],
    ["Normes et DTU", "Mise en œuvre conforme des travaux"],
], [Inches(5.0), Inches(6.5)], row_h=Inches(0.62), header_size=14, body_size=13, first_col_bold=True)
notes(s, "Avant les travaux, un point réglementaire. L'isolation par l'extérieur modifie l'aspect des façades : "
         "elle nécessite donc probablement une déclaration préalable en mairie, et le respect du PLU. "
         "Les matériaux doivent répondre aux critères techniques pour ouvrir droit aux aides, "
         "et tout doit être posé selon les DTU. Une attention particulière est portée à la conservation "
         "du caractère architectural de cette ancienne ferme.")

# ===========================================================================
# DIAPO 12 — SCÉNARIO 1 (B / B)
# ===========================================================================
s = add_slide()
header(s, "4", "Scénario 1 — Améliorer l’enveloppe", "Isolation + ventilation, sans toucher au chauffage")
make_table(s, Inches(0.9), Inches(1.75), Inches(7.1), [
    ["Poste", "Solution retenue"],
    ["Murs", "ITE laine de bois 200 mm"],
    ["Combles", "Ouate de cellulose 400 mm (soufflage)"],
    ["Ventilation", "VMC hygroréglable type B"],
    ["Chauffage", "Chaudière fioul conservée"],
    ["ECS", "Ballon électrique conservé"],
], [Inches(1.9), Inches(5.2)], row_h=Inches(0.55), header_size=13, body_size=12, first_col_bold=True)
# étiquette DPE B/B (version compacte)
dpe_label(s, Inches(8.7), Inches(1.65), "B", "Énergie", scale_h=Inches(0.30),
          base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
dpe_label(s, Inches(10.9), Inches(1.65), "B", "Climat", scale_h=Inches(0.30),
          base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
# avantages
box(s, Inches(0.9), Inches(5.0), Inches(11.5), Inches(1.7), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.1), Inches(11), Inches(0.4), [[("Avantages du scénario 1", 14, True, VERT)]])
bullet_block(s, Inches(1.15), Inches(5.55), Inches(5.5), Inches(1.1), [
    "Réduction importante des déperditions",
    "Confort d’hiver et d’été amélioré",
    "Conservation de l’inertie des murs en pierre",
], size=12, gap=Pt(5))
bullet_block(s, Inches(6.9), Inches(5.55), Inches(5.3), Inches(1.1), [
    "Meilleure qualité de l’air intérieur",
    "Investissement plus limité (≈ 24 000 €)",
    "Étiquette DPE : passage de G à B / B",
], size=12, gap=Pt(5))
notes(s, "Premier scénario : je traite uniquement l'enveloppe, sans toucher au chauffage. "
         "Isolation des murs par l'extérieur en laine de bois 200 mm, isolation des combles en ouate de cellulose 400 mm, "
         "et installation d'une VMC hygro B. La chaudière fioul et le ballon électrique sont conservés. "
         "Résultat : on passe de la classe G à une étiquette B / B, pour un investissement limité d'environ 24 000 €. "
         "C'est une première étape pertinente car elle attaque les causes principales des pertes. "
         "Sa limite : on garde le fioul, donc une énergie fossile.")

# ===========================================================================
# DIAPO 13 — SCÉNARIO 2 (A / B) + comparaison PAC / granulés
# ===========================================================================
s = add_slide()
header(s, "4", "Scénario 2 — Rénovation globale", "Enveloppe du scénario 1 + remplacement du chauffage")
text(s, Inches(0.9), Inches(1.6), Inches(11.4), Inches(0.45),
     [[("On reprend toute l’isolation du scénario 1, puis on remplace la chaudière fioul. Deux solutions étudiées :", 14, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.1), Inches(7.5), [
    ["Critère", "PAC Air/Eau", "Chaudière granulés"],
    ["Rendement", "COP > 3", "> 90 %"],
    ["Émissions CO₂", "Très faibles", "Très faibles"],
    ["Stockage combustible", "Aucun", "Nécessaire (silo)"],
    ["Compatibilité radiateurs fonte", "Moyenne", "Très bonne (haute T°)"],
    ["Adaptation au bâti ancien", "Bonne", "Très adaptée"],
], [Inches(2.9), Inches(2.3), Inches(2.3)], row_h=Inches(0.55), header_size=12, body_size=11.5, first_col_bold=True)
# étiquette A/B (version compacte)
dpe_label(s, Inches(9.0), Inches(1.95), "A", "Énergie", scale_h=Inches(0.28),
          base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
dpe_label(s, Inches(11.1), Inches(1.95), "B", "Climat", scale_h=Inches(0.28),
          base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
# solution retenue
box(s, Inches(0.9), Inches(5.4), Inches(7.5), Inches(1.3), fill=VERT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.5), Inches(7.0), Inches(1.1),
     [[("✔ Solution retenue : chaudière à granulés 12 kW + silo", 14, True, BLANC)],
      [("Conserve les radiateurs fonte existants, énergie renouvelable locale, "
        "approvisionnement facile en Savoie.", 12, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.05)
box(s, Inches(8.7), Inches(5.4), Inches(3.7), Inches(1.3), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(8.9), Inches(5.5), Inches(3.3), Inches(1.1),
     [[("Étiquette DPE", 12, True, VERT)],
      [("G → A / B", 22, True, DPE_COLORS["A"])],
      [("Investissement ≈ 40 000 €", 12, False, GRIS_TXT)]], line_spacing=1.0)
notes(s, "Le scénario 2 reprend toute l'isolation du scénario 1 et y ajoute le remplacement du chauffage. "
         "J'ai comparé deux solutions : la pompe à chaleur air/eau et la chaudière à granulés. "
         "Les deux ont d'excellents rendements et de faibles émissions. Mais je retiens la chaudière à granulés "
         "pour deux raisons décisives : elle est compatible avec les radiateurs en fonte haute température déjà en place, "
         "et le granulé est une énergie renouvelable abondante et locale en Savoie. "
         "Résultat : étiquette A / B, pour environ 40 000 €. La PAC reste une alternative valable si on était parti "
         "sur de la basse température.")

# ===========================================================================
# DIAPO 14 — MATÉRIAUX BIOSOURCÉS
# ===========================================================================
s = add_slide()
header(s, "5", "Analyse environnementale des matériaux", "Le choix du biosourcé")
make_table(s, Inches(0.9), Inches(1.8), Inches(8.0), [
    ["Critère", "Laine de bois", "Ouate de cellulose"],
    ["Origine", "Fibres de bois", "Papier recyclé"],
    ["Type", "Biosourcé", "Biosourcé"],
    ["Performance thermique", "Très bonne", "Très bonne"],
    ["Impact environnemental", "Faible", "Très faible"],
    ["Utilisation retenue", "ITE des murs", "Isolation des combles"],
], [Inches(3.0), Inches(2.5), Inches(2.5)], row_h=Inches(0.55), header_size=12, body_size=12, first_col_bold=True)
box(s, Inches(9.2), Inches(1.8), Inches(3.2), Inches(3.3), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(9.4), Inches(1.95), Inches(2.8), Inches(3.1),
     [[("Pourquoi le biosourcé ?", 13, True, VERT)],
      [("", 6, False, VERT)],
      [("• Faible impact carbone", 12, False, GRIS_TXT)],
      [("• Excellent déphasage", 12, False, GRIS_TXT)],
      [("  → confort d’été", 11, False, GRIS_CLR, True)],
      [("• Gestion de l’humidité", 12, False, GRIS_TXT)],
      [("  adaptée au bâti ancien", 11, False, GRIS_CLR, True)]], line_spacing=1.15)
notes(s, "J'ai volontairement choisi des matériaux biosourcés. La laine de bois pour l'isolation des murs par l'extérieur, "
         "la ouate de cellulose (du papier recyclé) pour les combles. "
         "Trois raisons : un faible impact environnemental, un excellent déphasage thermique qui apporte le confort d'été "
         "que recherche le maître d'ouvrage, et une bonne gestion de l'humidité — essentielle sur des murs en pierre anciens "
         "qui doivent rester perspirants.")

# ===========================================================================
# DIAPO 15 — DIMENSIONNEMENT (calculs)
# ===========================================================================
s = add_slide()
header(s, "5", "Dimensionnement des installations", "Du calcul thermique au choix des équipements")
# colonne gauche : isolation R
box(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(2.4), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.1), Inches(1.85), Inches(5.3), Inches(2.3),
     [[("Résistance thermique des isolants  (R = e / λ)", 13, True, VERT)],
      [("", 5, False, VERT)],
      [("Murs — laine de bois 200 mm (λ=0,038) :", 12, True, GRIS_TXT)],
      [("R = 0,20 / 0,038 = 5,26 m².K/W", 13, False, BLEU)],
      [("", 4, False, VERT)],
      [("Combles — ouate 400 mm (λ=0,039) :", 12, True, GRIS_TXT)],
      [("R = 0,40 / 0,039 = 10,26 m².K/W", 13, False, BLEU)]], line_spacing=1.12)
# colonne droite : puissance chaudière
box(s, Inches(6.8), Inches(1.75), Inches(5.6), Inches(2.4), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(7.0), Inches(1.85), Inches(5.2), Inches(2.3),
     [[("Puissance de chauffage après travaux", 13, True, VERT)],
      [("", 5, False, VERT)],
      [("Réduction des besoins estimée : 55 %", 12, True, GRIS_TXT)],
      [("P = 21,3 × (1 − 0,55) = 9,6 kW ≈ 10 kW", 13, False, BLEU)],
      [("", 4, False, VERT)],
      [("Avec marge de sécurité :", 12, True, GRIS_TXT)],
      [("→ Chaudière à granulés de 12 kW", 14, True, VERT)]], line_spacing=1.12)
# bandeau bas : conso granulés + VMC
make_table(s, Inches(0.9), Inches(4.45), Inches(5.7), [
    ["Combustible granulés", "Valeur"],
    ["Besoin après travaux", "7 020 kWh/an"],
    ["PCI granulés", "4,8 kWh/kg"],
    ["Conso annuelle", "≈ 1,5 t/an"],
    ["Silo retenu", "2 tonnes"],
], [Inches(3.2), Inches(2.5)], row_h=Inches(0.42), header_size=12, body_size=11)
make_table(s, Inches(6.8), Inches(4.45), Inches(5.6), [
    ["VMC Hygro B — débits", "m³/h"],
    ["Cuisine", "45 à 135"],
    ["Salle de bain", "30"],
    ["WC", "15"],
    ["Total maximal", "180"],
], [Inches(3.3), Inches(2.3)], row_h=Inches(0.42), header_size=12, body_size=11)
notes(s, "Voici comment j'ai dimensionné. Pour l'isolation, j'applique R = épaisseur / lambda : "
         "les murs atteignent R = 5,26 et les combles R = 10,26, des valeurs conformes à une rénovation performante. "
         "Pour le chauffage : la puissance initiale est de 21,3 kW ; avec une réduction des besoins estimée à 55 % grâce à l'isolation et la VMC, "
         "on tombe à environ 10 kW. Avec une marge de sécurité, je retiens une chaudière de 12 kW. "
         "Côté combustible, le besoin annuel revient à environ 1,5 tonne de granulés, d'où un silo de 2 tonnes pour l'autonomie. "
         "La VMC hygro B est dimensionnée à 180 m³/h maxi.")

# ===========================================================================
# DIAPO 16 — CHIFFRAGE DES TRAVAUX
# ===========================================================================
s = add_slide()
header(s, "6", "Chiffrage des travaux", "Estimation HT par poste")
text(s, Inches(0.9), Inches(1.7), Inches(5.5), Inches(0.4), [[("Scénario 1 — 24 000 €", 16, True, BLEU)]])
make_table(s, Inches(0.9), Inches(2.15), Inches(5.5), [
    ["Poste", "Coût HT"],
    ["ITE laine de bois 200 mm", "18 000 €"],
    ["Isolation combles ouate 400 mm", "2 500 €"],
    ["VMC Hygro B", "2 000 €"],
    ["Divers et raccordements", "1 500 €"],
    ["Total", "24 000 €"],
], [Inches(3.7), Inches(1.8)], row_h=Inches(0.5), header_size=12, body_size=12, first_col_bold=False)
text(s, Inches(6.8), Inches(1.7), Inches(5.5), Inches(0.4), [[("Scénario 2 — 40 000 €", 16, True, VERT)]])
make_table(s, Inches(6.8), Inches(2.15), Inches(5.6), [
    ["Poste", "Coût HT"],
    ["ITE laine de bois 200 mm", "18 000 €"],
    ["Isolation combles ouate 400 mm", "2 500 €"],
    ["VMC Hygro B", "2 000 €"],
    ["Chaudière à granulés 12 kW", "13 000 €"],
    ["Silo de stockage", "2 500 €"],
    ["Divers et raccordements", "2 000 €"],
    ["Total", "40 000 €"],
], [Inches(3.8), Inches(1.8)], row_h=Inches(0.47), header_size=12, body_size=11.5)
notes(s, "Le chiffrage repose sur des prix moyens de marché. "
         "Pour le scénario 1, on est à 24 000 € HT, dont 18 000 € rien que pour l'isolation des murs — "
         "ce qui est logique puisque c'est le premier poste de déperdition. "
         "Le scénario 2 reprend ces postes et ajoute la chaudière à granulés (13 000 €) et le silo (2 500 €), "
         "pour un total de 40 000 €. L'écart entre les deux, environ 16 000 €, correspond donc au remplacement du chauffage.")

# ===========================================================================
# DIAPO 17 — PLAN DE FINANCEMENT
# ===========================================================================
s = add_slide()
header(s, "6", "Plan de financement", "Reste à charge après aides")
make_table(s, Inches(0.9), Inches(1.9), Inches(5.5), [
    ["Scénario 1", "Montant"],
    ["Coût total des travaux", "24 000 €"],
    ["MaPrimeRénov’", "− 5 000 €"],
    ["CEE", "− 2 000 €"],
    ["Reste à charge", "17 000 €"],
], [Inches(3.5), Inches(2.0)], row_h=Inches(0.55), header_size=13, body_size=12)
make_table(s, Inches(6.8), Inches(1.9), Inches(5.5), [
    ["Scénario 2", "Montant"],
    ["Coût total des travaux", "40 000 €"],
    ["MaPrimeRénov’", "− 8 000 €"],
    ["CEE", "− 4 000 €"],
    ["Aides locales", "− 1 000 €"],
    ["Reste à charge", "27 000 €"],
], [Inches(3.5), Inches(2.0)], row_h=Inches(0.5), header_size=13, body_size=12)
box(s, Inches(0.9), Inches(5.5), Inches(11.5), Inches(1.0), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.6), Inches(11.0), Inches(0.8),
     [[("Les aides (MaPrimeRénov’, CEE, aides locales) réduisent fortement le reste à charge — "
        "et sont conditionnées au respect des critères techniques des travaux.", 14, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Les travaux sont éligibles à plusieurs aides. Pour le scénario 1 : MaPrimeRénov' à 5 000 € et CEE à 2 000 €, "
         "ramenant le reste à charge à 17 000 €. Pour le scénario 2, plus ambitieux, les aides sont aussi plus élevées : "
         "8 000 € de MaPrimeRénov', 4 000 € de CEE et 1 000 € d'aides locales, pour un reste à charge de 27 000 €. "
         "Ce sont des estimations : les montants réels dépendent des revenus du ménage et des barèmes en vigueur.")

# ===========================================================================
# DIAPO 18 — COÛTS, COÛT GLOBAL, ROI
# ===========================================================================
s = add_slide()
header(s, "6", "Rentabilité : coût global sur 30 ans & ROI")
# graphique coût global
cg = CategoryChartData()
cg.categories = ["État initial", "Scénario 1", "Scénario 2"]
cg.add_series("Coût global sur 30 ans (€)", (250650, 159000, 130000))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.9), Inches(1.75), Inches(6.6), Inches(3.4), cg)
ch = gf.chart
ch.has_title = True; ch.chart_title.text_frame.text = "Coût global sur 30 ans"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12)
ch.has_legend = False
plot = ch.plots[0]; plot.has_data_labels = True
plot.data_labels.number_format = '# ##0 "€"'; plot.data_labels.number_format_is_linked = False
plot.data_labels.font.size = Pt(10); plot.data_labels.font.bold = True
ser = plot.series[0]
for i, c in enumerate([ROUGE, BLEU, VERT]):
    ser.points[i].format.fill.solid(); ser.points[i].format.fill.fore_color.rgb = c
# tableau coûts mensuels + ROI
text(s, Inches(7.9), Inches(1.7), Inches(4.5), Inches(0.4), [[("Coûts & retour sur investissement", 13, True, VERT)]])
make_table(s, Inches(7.9), Inches(2.2), Inches(4.5), [
    ["Situation", "€/an", "€/mois"],
    ["Avant travaux", "8 355", "696"],
    ["Scénario 1", "4 500", "375"],
    ["Scénario 2", "3 000", "250"],
], [Inches(1.9), Inches(1.3), Inches(1.3)], row_h=Inches(0.47), header_size=11.5, body_size=11)
make_table(s, Inches(7.9), Inches(4.55), Inches(4.5), [
    ["ROI", "Sc. 1", "Sc. 2"],
    ["Reste à charge", "17 000 €", "27 000 €"],
    ["Économies/an", "3 000 €", "5 000 €"],
    ["Amortissement", "5,7 ans", "5,4 ans"],
], [Inches(1.9), Inches(1.3), Inches(1.3)], row_h=Inches(0.47), header_size=11.5, body_size=11)
notes(s, "C'est l'analyse qui tranche entre les deux scénarios. "
         "À gauche, le coût global sur 30 ans : sans rien faire, on dépense 250 000 € ; le scénario 1 ramène à 159 000 €, "
         "et le scénario 2 à 130 000 €. Donc malgré un investissement de départ plus élevé, le scénario 2 coûte MOINS cher au final. "
         "Les coûts mensuels passent de 696 € avant travaux à 250 € avec le scénario 2. "
         "Et côté ROI, les deux s'amortissent vite : 5,7 ans pour le scénario 1, 5,4 ans pour le scénario 2. "
         "Le scénario 2 est donc le meilleur compromis performance / rentabilité.")

# ===========================================================================
# DIAPO 19 — PLAN DE SOBRIÉTÉ
# ===========================================================================
s = add_slide()
header(s, "7", "Plan de sobriété", "Des gestes complémentaires aux travaux")
bullet_block(s, Inches(0.9), Inches(1.85), Inches(5.7), Inches(4.5), [
    "Chauffer entre 19 °C et 20 °C dans les pièces de vie",
    "Réduire la température durant les absences",
    "Entretien régulier de la chaudière et de la VMC",
    "Limiter les consommations d’eau chaude sanitaire",
], size=15, gap=Pt(13))
bullet_block(s, Inches(6.9), Inches(1.85), Inches(5.5), Inches(4.5), [
    "Fermer les volets la nuit en hiver",
    "Privilégier l’électroménager performant",
    "Éteindre les appareils en veille",
    "Suivre régulièrement ses consommations",
], size=15, gap=Pt(13))
box(s, Inches(0.9), Inches(5.9), Inches(11.5), Inches(0.85), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(6.0), Inches(11), Inches(0.65),
     [[("La sobriété ne coûte rien et amplifie les économies générées par les travaux.", 14, True, VERT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "En complément des travaux, je propose un plan de sobriété : des gestes simples et gratuits. "
         "Maintenir 19-20 °C dans les pièces de vie, baisser en cas d'absence, entretenir les équipements, "
         "fermer les volets la nuit en hiver, traquer les veilles, et suivre ses consommations. "
         "Ces actions n'engagent aucun coût mais amplifient les économies obtenues par la rénovation.")

# ===========================================================================
# DIAPO 20 — SYNTHÈSE COMPARATIVE
# ===========================================================================
s = add_slide()
header(s, "7", "Synthèse comparative des scénarios")
make_table(s, Inches(0.9), Inches(1.85), Inches(11.5), [
    ["Critère", "État initial", "Scénario 1", "Scénario 2"],
    ["Étiquette DPE", "G / G", "B / B", "A / B"],
    ["Chauffage", "Fioul (1991)", "Fioul conservé", "Granulés 12 kW"],
    ["Coût des travaux", "—", "24 000 €", "40 000 €"],
    ["Reste à charge", "—", "17 000 €", "27 000 €"],
    ["Coût annuel", "8 355 €", "4 500 €", "3 000 €"],
    ["Coût global 30 ans", "250 650 €", "159 000 €", "130 000 €"],
    ["Retour sur investissement", "—", "5,7 ans", "5,4 ans"],
], [Inches(3.2), Inches(2.6), Inches(2.85), Inches(2.85)], row_h=Inches(0.52), header_size=13, body_size=12, first_col_bold=True)
notes(s, "Cette diapo récapitule tout en un coup d'œil. On lit la progression : de G/G à B/B avec le scénario 1, "
         "et jusqu'à A/B avec le scénario 2. Le scénario 2 coûte plus cher à l'achat mais affiche le coût annuel le plus bas, "
         "le coût global sur 30 ans le plus faible, et même le ROI le plus court. "
         "C'est sur cette base que je formule ma recommandation.")

# ===========================================================================
# DIAPO 21 — CONCLUSION / RECOMMANDATION
# ===========================================================================
s = add_slide()
set_bg(s, VERT)
box(s, 0, 0, SW, Inches(1.5), fill=VERT_CLR)
text(s, Inches(0.9), Inches(0.4), Inches(11.5), Inches(0.9),
     [[("Conclusion & recommandation", 32, True, BLANC)]], anchor=MSO_ANCHOR.MIDDLE)
# carte recommandation
box(s, Inches(0.9), Inches(1.9), Inches(11.5), Inches(2.5), fill=BLANC, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.2), Inches(2.05), Inches(11), Inches(0.5),
     [[("→ Je recommande le Scénario 2 (rénovation globale)", 22, True, VERT)]])
bullet_block(s, Inches(1.2), Inches(2.7), Inches(11), Inches(1.6), [
    ("Performance maximale : ", "passage de G à A / B (énergie / climat)"),
    ("Sortie du fioul : ", "énergie renouvelable et locale (granulés savoyards)"),
    ("Meilleure rentabilité long terme : ", "coût global le plus bas et ROI de 5,4 ans"),
    ("Compatible avec le bâti : ", "ITE biosourcée + radiateurs fonte conservés"),
], size=14, gap=Pt(7))
# bandeau bas
box(s, 0, Inches(4.7), SW, Inches(2.8), fill=VERT)
text(s, Inches(0.9), Inches(5.0), Inches(11.5), Inches(0.6),
     [[("Si le budget initial est contraint, le Scénario 1 reste une excellente première étape (G → B / B).", 15, False, RGBColor(0xC8,0xE6,0xC9), True)]])
text(s, Inches(0.9), Inches(5.9), Inches(11.5), Inches(1.4),
     [[("Merci de votre attention.", 30, True, BLANC)],
      [("Je suis à votre disposition pour vos questions.", 16, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.1)
notes(s, "Pour conclure : au regard de la performance, du confort, de la sortie du fioul et de la rentabilité long terme, "
         "je recommande le scénario 2, la rénovation globale, qui fait passer le logement de G à A/B. "
         "C'est aussi celui qui coûte le moins cher sur 30 ans et qui s'amortit le plus vite. "
         "Si le budget de départ est un frein, le scénario 1 reste une excellente première étape, "
         "que l'on peut compléter plus tard par le changement de chauffage. "
         "Je vous remercie de votre attention et je suis prêt à répondre à vos questions.")

prs.save("/home/user/licence/Soutenance_Renovation_Saint-Jean-de-Chevelu.pptx")
print("OK - slides:", len(prs.slides._sldIdLst))
