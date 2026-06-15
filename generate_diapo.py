# -*- coding: utf-8 -*-
"""
Diaporama oral - Étude de rénovation énergétique (Bloc 1 - Sujet A)
Maison individuelle à Saint-Jean-de-Chevelu (Savoie)
Guillaume Tardy - Chargé de projet énergie et bâtiment durables
Adapté au sujet d'école et à la grille d'évaluation officielle.
"""
import os, re
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION

ASSETS = "/home/user/licence/assets"
IMG = {
    "facade":     ASSETS + "/p05_x55_658x390.png",
    "facade2":    ASSETS + "/p05_x56_630x388.png",
    "facade3":    ASSETS + "/p05_x57_660x390.png",
    "poele":      ASSETS + "/p06_x61_450x596.png",
    "menuiserie": ASSETS + "/p06_x62_460x392.png",
    "ballon":     ASSETS + "/p06_x63_366x506.png",
    "chaudiere":  ASSETS + "/p06_x64_240x407.png",
    "carte":      ASSETS + "/p03_x47_914x528.png",
    "masque":     ASSETS + "/p04_x51_889x599.png",
    "plan_rdc":   ASSETS + "/p07_x68_1196x845.png",
    "plan_etage": ASSETS + "/p08_x72_1192x832.png",
    "coupe":      ASSETS + "/p08_x73_1188x641.png",
}

# ---------------- CHARTE ----------------
VERT      = RGBColor(0x1B, 0x5E, 0x20)
VERT_CLR  = RGBColor(0x2E, 0x7D, 0x32)
VERT_LIGHT= RGBColor(0xE8, 0xF5, 0xE9)
GRIS_TXT  = RGBColor(0x37, 0x47, 0x4F)
GRIS_CLR  = RGBColor(0x90, 0xA4, 0xAE)
BLANC     = RGBColor(0xFF, 0xFF, 0xFF)
ANTHRA    = RGBColor(0x26, 0x32, 0x38)
ORANGE    = RGBColor(0xE6, 0x51, 0x00)
BLEU      = RGBColor(0x15, 0x65, 0xC0)
ROUGE     = RGBColor(0xC6, 0x28, 0x28)
DPE_COLORS = {"A":RGBColor(0x00,0x83,0x36),"B":RGBColor(0x57,0xAA,0x27),
              "C":RGBColor(0xC3,0xD0,0x00),"D":RGBColor(0xFC,0xEA,0x10),
              "E":RGBColor(0xF7,0xB1,0x00),"F":RGBColor(0xEA,0x6C,0x16),
              "G":RGBColor(0xE2,0x00,0x1A)}

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

def add_slide(): return prs.slides.add_slide(BLANK)

def set_bg(slide, color):
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    rect.fill.solid(); rect.fill.fore_color.rgb = color
    rect.line.fill.background(); rect.shadow.inherit = False
    slide.shapes._spTree.remove(rect._element)
    slide.shapes._spTree.insert(2, rect._element)
    return rect

def box(slide, l, t, w, h, fill=None, line=None, line_w=None, shape=MSO_SHAPE.RECTANGLE):
    sp = slide.shapes.add_shape(shape, l, t, w, h)
    if fill is None: sp.fill.background()
    else: sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = line; sp.line.width = line_w or Pt(1)
    sp.shadow.inherit = False
    return sp

def text(slide, l, t, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         space_after=Pt(4), line_spacing=1.0, wrap=True):
    tb = slide.shapes.add_textbox(l, t, w, h); tf = tb.text_frame
    tf.word_wrap = wrap; tf.vertical_anchor = anchor
    tf.margin_left = Pt(2); tf.margin_right = Pt(2); tf.margin_top = Pt(2); tf.margin_bottom = Pt(2)
    first = True
    for para in runs:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.alignment = align; p.space_after = space_after; p.line_spacing = line_spacing
        for seg in para:
            txt, size, bold, color = seg[0], seg[1], seg[2], seg[3]
            italic = seg[4] if len(seg) > 4 else False
            r = p.add_run(); r.text = txt
            r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
            r.font.italic = italic; r.font.name = "Calibri"
    return tb

def notes(slide, txt): slide.notes_slide.notes_text_frame.text = txt

def header(slide, num, titre, sous=None):
    set_bg(slide, BLANC)
    box(slide, 0, 0, Inches(0.22), SH, fill=VERT)
    if num:
        box(slide, Inches(0.55), Inches(0.42), Inches(0.72), Inches(0.72), fill=VERT, shape=MSO_SHAPE.OVAL)
        text(slide, Inches(0.55), Inches(0.42), Inches(0.72), Inches(0.72),
             [[(num, 26, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        tl = Inches(1.45)
    else: tl = Inches(0.6)
    text(slide, tl, Inches(0.40), Inches(11.3), Inches(0.8),
         [[(titre, 29, True, VERT)]], anchor=MSO_ANCHOR.MIDDLE)
    if sous:
        text(slide, tl, Inches(1.16), Inches(11.3), Inches(0.4), [[(sous, 14, False, GRIS_CLR, True)]])
    box(slide, tl, Inches(1.28), Inches(11.0), Pt(2.2), fill=VERT_CLR)
    text(slide, Inches(0.55), Inches(7.08), Inches(9), Inches(0.32),
         [[("Rénovation énergétique – Saint-Jean-de-Chevelu (73) – Bloc 1", 9, False, GRIS_CLR)]])
    text(slide, Inches(10.3), Inches(7.08), Inches(2.5), Inches(0.32),
         [[("Guillaume Tardy", 9, False, GRIS_CLR)]], align=PP_ALIGN.RIGHT)

def make_table(slide, l, t, w, rows, col_widths, row_h=Inches(0.4),
               header_fill=VERT, header_size=13, body_size=12, first_col_bold=False):
    total = sum(col_widths, Emu(0)); nrows = len(rows)
    gtbl = slide.shapes.add_table(nrows, len(col_widths), l, t, total, row_h*nrows).table
    gtbl.first_row = False; gtbl.horz_banding = False
    for ci, cw in enumerate(col_widths): gtbl.columns[ci].width = cw
    for ri in range(nrows): gtbl.rows[ri].height = row_h
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = gtbl.cell(ri, ci)
            cell.margin_left = Pt(7); cell.margin_right = Pt(7)
            cell.margin_top = Pt(1); cell.margin_bottom = Pt(1)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            cell.fill.fore_color.rgb = header_fill if ri == 0 else (VERT_LIGHT if ri % 2 == 0 else BLANC)
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER
            r = p.add_run(); r.text = val; r.font.name = "Calibri"
            if ri == 0:
                r.font.size = Pt(header_size); r.font.bold = True; r.font.color.rgb = BLANC
            else:
                r.font.size = Pt(body_size); r.font.bold = (ci == 0 and first_col_bold); r.font.color.rgb = GRIS_TXT
    return gtbl

def bullets(slide, l, t, w, h, items, size=15, color=GRIS_TXT, gap=Pt(8),
            marker="●", marker_color=VERT_CLR, line_spacing=1.05):
    tb = slide.shapes.add_textbox(l, t, w, h); tf = tb.text_frame; tf.word_wrap = True
    first = True
    for it in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph(); first = False
        p.space_after = gap; p.line_spacing = line_spacing
        r0 = p.add_run(); r0.text = marker + "  "
        r0.font.size = Pt(size); r0.font.color.rgb = marker_color; r0.font.bold = True; r0.font.name = "Calibri"
        if isinstance(it, tuple):
            b, n = it
            r1 = p.add_run(); r1.text = b; r1.font.size = Pt(size); r1.font.bold = True
            r1.font.color.rgb = color; r1.font.name = "Calibri"
            r2 = p.add_run(); r2.text = n; r2.font.size = Pt(size); r2.font.color.rgb = color; r2.font.name = "Calibri"
        else:
            r1 = p.add_run(); r1.text = it; r1.font.size = Pt(size); r1.font.color.rgb = color; r1.font.name = "Calibri"
    return tb

def kpi(slide, l, t, w, h, value, label, accent=VERT, val_size=26):
    box(slide, l, t, w, h, fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    box(slide, l, t, w, Inches(0.12), fill=accent, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(slide, l, t + Inches(0.16), w, h - Inches(0.6),
         [[(value, val_size, True, accent)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(slide, l, t + h - Inches(0.52), w, Inches(0.48),
         [[(label, 11, False, GRIS_TXT)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

def picture(slide, path, bl, bt, bw, bh, caption=None, frame=True, cap_size=11):
    m = re.search(r'_(\d+)x(\d+)\.png$', path)
    iw, ih = int(m.group(1)), int(m.group(2))
    cap_h = Inches(0.34) if caption else Emu(0)
    avail_h = bh - cap_h
    scale = min(bw / iw, avail_h / ih)
    w = int(iw * scale); h = int(ih * scale)
    l = bl + (bw - w) // 2; t = bt + (avail_h - h) // 2
    if frame:
        box(slide, l - Emu(20000), t - Emu(20000), w + Emu(40000), h + Emu(40000),
            fill=BLANC, line=GRIS_CLR, line_w=Pt(1.2))
    slide.shapes.add_picture(path, l, t, width=w, height=h)
    if caption:
        text(slide, bl, bt + avail_h + Emu(20000), bw, cap_h,
             [[(caption, cap_size, False, GRIS_CLR, True)]], align=PP_ALIGN.CENTER)
    return l, t, w, h

def dpe_label(slide, cx, top, current, label_txt="Classe énergie", scale_h=Inches(0.42),
              base_w=Inches(1.0), step=Inches(0.34), letter_size=16, label_size=12):
    letters = ["A","B","C","D","E","F","G"]
    text(slide, cx, top, base_w + step*6, Inches(0.3),
         [[(label_txt, label_size, True, GRIS_TXT)]], align=PP_ALIGN.LEFT)
    y = top + Inches(0.36)
    for i, ltr in enumerate(letters):
        w = base_w + step*i; is_cur = (ltr == current)
        box(slide, cx, y, w, scale_h, fill=DPE_COLORS[ltr], shape=MSO_SHAPE.ROUNDED_RECTANGLE,
            line=(ANTHRA if is_cur else None), line_w=Pt(2.5))
        text(slide, cx + Inches(0.06), y, w - Inches(0.08), scale_h,
             [[(ltr, letter_size, True, BLANC)]], anchor=MSO_ANCHOR.MIDDLE)
        if is_cur:
            box(slide, cx - Inches(0.34), y, Inches(0.30), scale_h, fill=ANTHRA, shape=MSO_SHAPE.PENTAGON)
        y += scale_h + Inches(0.06)
    return y

# ===========================================================================
# 1 — TITRE
# ===========================================================================
s = add_slide(); set_bg(s, VERT)
box(s, 0, 0, Inches(6.4), SH, fill=VERT_CLR)
picture(s, IMG["facade"], Inches(0.0), Inches(0.0), Inches(6.4), SH, frame=False)
box(s, Inches(6.4), 0, Pt(6), SH, fill=RGBColor(0xA5,0xD6,0xA7))
text(s, Inches(6.85), Inches(0.7), Inches(6.2), Inches(0.5),
     [[("BLOC 1 — CHARGÉ DE PROJET ÉNERGIE ET BÂTIMENT DURABLES", 12, True, RGBColor(0xC8,0xE6,0xC9))]])
text(s, Inches(6.85), Inches(1.5), Inches(6.2), Inches(2.6),
     [[("Rénovation", 38, True, BLANC)],
      [("énergétique d’une", 38, True, BLANC)],
      [("ancienne ferme", 38, True, RGBColor(0xC8,0xE6,0xC9))],
      [("savoyarde", 38, True, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.0)
text(s, Inches(6.85), Inches(4.7), Inches(6.2), Inches(0.6),
     [[("Étude pour un maître d’ouvrage — Saint-Jean-de-Chevelu (73)", 15, False, BLANC)]])
box(s, Inches(6.85), Inches(5.5), Inches(5.9), Pt(2), fill=RGBColor(0xA5,0xD6,0xA7))
text(s, Inches(6.85), Inches(5.75), Inches(6.2), Inches(1.0),
     [[("Présenté par Guillaume Tardy", 17, True, BLANC)],
      [("Soutenance orale — Sujet A", 13, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.15)
notes(s, "Bonjour, je suis Guillaume Tardy. Je vous présente mon étude de rénovation énergétique réalisée "
         "pour le compte d'un maître d'ouvrage occupant. Il s'agit d'une ancienne ferme savoyarde de la fin du "
         "XIXe siècle, à Saint-Jean-de-Chevelu. Ma démarche : diagnostiquer l'existant, le comparer aux références, "
         "puis proposer deux scénarios de rénovation performante — un par étapes et un global — chiffrés et argumentés. "
         "Rappel du cadre : le photovoltaïque et la climatisation ne sont pas étudiés.")

# ===========================================================================
# 2 — SOMMAIRE
# ===========================================================================
s = add_slide(); header(s, None, "Sommaire")
items = [
    ("1","Analyse de la situation & objectifs","Contexte, maître d’ouvrage, confort visé"),
    ("2","Diagnostic technique de l’existant","Consommations, enveloppe, systèmes, éclairage"),
    ("3","Bilan des déperditions & DPE","Calculs thermiques, étiquette actuelle"),
    ("4","Deux scénarios de rénovation","Par étapes (B/B) et global (A/B)"),
    ("5","Dimensionnement & matériaux","Régulation, ECS, isolants biosourcés"),
    ("6","Analyse économique en coût global","Chiffrage, aides, reste à charge, ROI"),
    ("7","Plan de sobriété & conclusion","Conseils aux occupants, recommandation"),
]
y = Inches(1.7)
for num, t1, sub in items:
    box(s, Inches(0.9), y, Inches(0.52), Inches(0.52), fill=VERT, shape=MSO_SHAPE.OVAL)
    text(s, Inches(0.9), y, Inches(0.52), Inches(0.52), [[(num,17,True,BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(1.65), y - Inches(0.03), Inches(8), Inches(0.4), [[(t1,17,True,GRIS_TXT)]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(1.65), y + Inches(0.30), Inches(10.5), Inches(0.3), [[(sub,12,False,GRIS_CLR,True)]])
    y += Inches(0.70)
notes(s, "Voici mon plan. Je pars du contexte et des attentes du maître d'ouvrage, puis le diagnostic technique complet : "
         "consommations, enveloppe, systèmes, éclairage et ventilation. J'en tire le bilan des déperditions et le DPE. "
         "Je présente ensuite mes deux scénarios, leur dimensionnement, l'analyse économique en coût global, "
         "et je termine par le plan de sobriété et ma recommandation.")

# ===========================================================================
# 3 — CONTEXTE
# ===========================================================================
s = add_slide(); header(s, "1", "Analyse de la situation", "Nature du projet et contexte")
bullets(s, Inches(0.9), Inches(1.7), Inches(6.0), Inches(4.5), [
    ("Ancienne ferme ","fin XIXᵉ s., réhabilitée dans les années 1990"),
    ("Maison individuelle ","occupée par une famille (résidence principale)"),
    ("99 m² habitables chauffés ","sur 2 niveaux, sous combles perdus"),
    ("Partie non chauffée ","à l’Est : garage / débarras"),
    ("Murs en pierre calcaire 50 cm ","→ forte inertie, patrimoine local"),
    ("Étude pour le MOA : ","diagnostic + scénarios adaptés au bâti ancien"),
], size=14.5, gap=Pt(10))
picture(s, IMG["facade2"], Inches(7.3), Inches(1.7), Inches(5.1), Inches(2.9),
        caption="Façade de la maison — vue depuis l’accès")
box(s, Inches(7.3), Inches(4.85), Inches(5.1), Inches(1.5), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(7.55), Inches(4.95), Inches(4.6), Inches(1.3),
     [[("Saint-Jean-de-Chevelu (73170)", 13, True, VERT)],
      [("Altitude 498 m · versant Sud-Est · contexte rural", 12, False, GRIS_TXT)],
      [("Hors étude : photovoltaïque & climatisation", 11, False, GRIS_CLR, True)]], line_spacing=1.2)
notes(s, "Le bâtiment est une ancienne ferme savoyarde de la fin du XIXe, réhabilitée dans les années 90. "
         "99 m² chauffés sur deux niveaux, sous des combles perdus accessibles par une échelle. À l'Est, une partie non chauffée "
         "sert de garage. La signature du bâti : des murs en pierre calcaire de 50 cm — forte inertie mais aucune isolation. "
         "Tout l'enjeu sera d'isoler sans dénaturer la ferme et en respectant la perspirance des murs. "
         "Le sujet exclut le photovoltaïque et la climatisation.")

# ===========================================================================
# 4 — PLANS & COUPE (descriptif coef 3)
# ===========================================================================
s = add_slide(); header(s, "1", "Le bâtiment en plans", "Organisation des espaces et coupe")
picture(s, IMG["plan_rdc"], Inches(0.7), Inches(1.65), Inches(4.1), Inches(3.4), caption="Plan RDC — pièces de vie")
picture(s, IMG["plan_etage"], Inches(4.9), Inches(1.65), Inches(4.0), Inches(3.4), caption="Plan R+1 — espaces de nuit")
picture(s, IMG["coupe"], Inches(9.0), Inches(1.65), Inches(3.6), Inches(3.4), caption="Coupe sur la zone chauffée")
box(s, Inches(0.7), Inches(5.55), Inches(11.9), Inches(1.05), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(0.95), Inches(5.65), Inches(11.4), Inches(0.85),
     [[("Lecture : ", 13, True, VERT),
       ("RDC = pièces de vie, R+1 = chambres. Les combles perdus non chauffés surplombent l’étage : "
        "cette interface favorise les déperditions par la toiture, confirmées plus loin.", 13, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Je m'appuie sur les plans et la coupe fournis. Le rez-de-chaussée regroupe les pièces de vie — cuisine, salon, "
         "salle de bain — et l'étage les chambres. La coupe montre bien les combles perdus non chauffés au-dessus de l'étage, "
         "ce qui crée une interface déperditive importante. À noter : les plans portent encore les anciennes menuiseries de 1990, "
         "mais elles ont été remplacées en 2019 par du double vitrage bois posé en tunnel.")

# ===========================================================================
# 5 — OBJECTIFS & ATTENTES MOA
# ===========================================================================
s = add_slide(); header(s, "1", "Objectifs et attentes du maître d’ouvrage")
text(s, Inches(0.9), Inches(2.15), Inches(5.6), Inches(0.4), [[("Besoins & objectifs", 16, True, VERT)]])
bullets(s, Inches(0.9), Inches(2.65), Inches(5.6), Inches(4), [
    "Réduire les dépenses énergétiques",
    "Confort d’hiver (supprimer parois froides)",
    "Confort d’été (surchauffe sous toiture)",
    "Remplacer à terme la chaudière fioul",
    "Réduire les émissions de gaz à effet de serre",
    "Valoriser le patrimoine immobilier",
], size=14, gap=Pt(9))
text(s, Inches(6.9), Inches(2.15), Inches(5.6), Inches(0.4), [[("Moyens & contraintes", 16, True, VERT)]])
bullets(s, Inches(6.9), Inches(2.65), Inches(5.6), Inches(4), [
    "Budget pour des travaux importants…",
    "… investissements justifiés par les économies",
    "Conserver le caractère de la ferme",
    "Solutions compatibles avec les murs en pierre",
    "Limiter les risques liés à l’humidité",
    "Mobiliser les aides financières",
], size=14, gap=Pt(9), marker_color=ORANGE)
text(s, Inches(0.9), Inches(1.65), Inches(11.4), Inches(0.4),
     [[("Recueil réalisé lors de la rencontre avec le maître d’ouvrage occupant.", 14, False, GRIS_TXT, True)]])
notes(s, "J'ai recueilli les attentes lors de la rencontre avec le maître d'ouvrage. Ses objectifs : baisser ses factures, "
         "gagner en confort hiver comme été, sortir du fioul et réduire son empreinte carbone, tout en valorisant son bien. "
         "Côté moyens : il a un budget pour des travaux conséquents mais veut qu'ils soient justifiés par les économies. "
         "Ses contraintes orientent fortement le projet : préserver le cachet de la ferme, respecter les murs en pierre "
         "et gérer l'humidité — ce qui pointe vers une isolation par l'extérieur perspirante.")

# ===========================================================================
# 6 — OBJECTIFS DE CONFORT (tableau)
# ===========================================================================
s = add_slide(); header(s, "1", "Objectifs de confort à atteindre")
make_table(s, Inches(0.9), Inches(1.75), Inches(11.5), [
    ["Type de confort","Situation actuelle","Amélioration visée"],
    ["Confort d’hiver","Parois froides, écarts entre pièces","Températures homogènes (isolation + régulation)"],
    ["Confort d’été","Surchauffe sous toiture","Déphasage des isolants biosourcés"],
    ["Qualité de l’air","Ventilation naturelle non maîtrisée","Renouvellement d’air contrôlé (VMC hygro B)"],
    ["Confort visuel","Halogènes énergivores (25 %)","Éclairage 100 % LED, apports de lumière naturelle"],
    ["Confort acoustique","Isolation phonique limitée","Atténuation des bruits extérieurs (ITE)"],
    ["Confort / sanitaire","Chauffage peu régulé, condensation","Régulation fine, réduction de l’humidité"],
], [Inches(2.3), Inches(4.4), Inches(4.8)], row_h=Inches(0.62), header_size=13, body_size=12, first_col_bold=True)
text(s, Inches(0.9), Inches(6.55), Inches(11.4), Inches(0.5),
     [[("Aucun besoin d’accessibilité / PMR identifié dans cette étude.", 12, False, GRIS_CLR, True)]])
notes(s, "Au-delà des économies, j'ai formulé des objectifs de confort sur les quatre dimensions attendues : "
         "thermique d'hiver, thermique d'été, qualité de l'air et confort visuel. "
         "Hiver : fin des parois froides grâce à l'isolation et à une meilleure régulation. Été : déphasage des isolants biosourcés. "
         "Air : VMC hygroréglable. Visuel : passage en tout LED et valorisation de la lumière naturelle. "
         "J'ajoute l'acoustique, améliorée par l'isolation extérieure. Enfin, aucun besoin d'accessibilité PMR n'a été identifié, "
         "mais je l'ai bien vérifié comme le demande la méthode.")

# ===========================================================================
# 7 — ANALYSE BIOCLIMATIQUE
# ===========================================================================
s = add_slide(); header(s, "2", "Analyse bioclimatique du site", "Implantation, orientation et masque solaire")
picture(s, IMG["carte"], Inches(0.8), Inches(1.7), Inches(4.0), Inches(2.7), caption="Localisation — versant Sud-Est")
picture(s, IMG["masque"], Inches(5.0), Inches(1.7), Inches(4.2), Inches(2.7), caption="Diagramme de masque solaire lointain")
make_table(s, Inches(9.5), Inches(1.7), Inches(3.0), [
    ["Caractéristique","Valeur"],
    ["Altitude","498 m"],
    ["Orientation","Sud-Est"],
    ["Environnement","Rural"],
    ["Masque","Lointain présent"],
    ["Potentiel solaire","Hivernal favorable"],
], [Inches(1.7), Inches(1.3)], row_h=Inches(0.45), header_size=11, body_size=11)
box(s, Inches(0.8), Inches(4.9), Inches(11.7), Inches(1.4), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.05), Inches(5.0), Inches(11.2), Inches(1.2),
     [[("Atout : ", 13, True, VERT),
       ("l’orientation Sud-Est favorise les apports solaires d’hiver (gains gratuits, confort). ", 13, False, GRIS_TXT)],
      [("Vigilance : ", 13, True, ORANGE),
       ("ces mêmes apports peuvent provoquer des surchauffes l’été → d’où le choix d’isolants déphasants et la fermeture des volets.", 13, False, GRIS_TXT)]],
     line_spacing=1.2)
notes(s, "L'analyse bioclimatique étudie comment le bâtiment tire parti de son environnement. "
         "Il est implanté sur un versant orienté Sud-Est à 498 m d'altitude, en contexte rural. "
         "Le diagramme de masque solaire montre un masque lointain — le relief — qui limite un peu les apports à certaines heures, "
         "mais l'exposition reste globalement bonne. L'orientation Sud-Est est un vrai atout : apports solaires gratuits en hiver. "
         "Le revers : un risque de surchauffe estivale, que je traite par des isolants déphasants et la gestion des volets.")

# ===========================================================================
# 8 — CONSOMMATIONS RELEVÉES
# ===========================================================================
s = add_slide(); header(s, "2", "Analyse des consommations", "Relevés des factures sur 5 ans")
kpi(s, Inches(0.9), Inches(1.7), Inches(3.6), Inches(1.45), "1 560 L/an", "Fioul (moy.) — chauffage principal", accent=ORANGE)
kpi(s, Inches(4.7), Inches(1.7), Inches(3.6), Inches(1.45), "6 stères/an", "Bois bûche — poêle d’appoint", accent=VERT_CLR)
kpi(s, Inches(8.5), Inches(1.7), Inches(3.6), Inches(1.45), "5 447 kWh/an", "Électricité — ECS, éclairage, usages", accent=BLEU)
cd = CategoryChartData()
cd.categories = ["19-20","20-21","21-22","22-23","23-24"]
cd.add_series("Fioul (L)", (1500,1800,1700,1400,1400))
cd.add_series("Électricité (kWh)", (5552,5679,5334,5207,5461))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.9), Inches(3.45), Inches(7.0), Inches(3.15), cd)
ch = gf.chart; ch.has_title = True; ch.chart_title.text_frame.text = "Évolution des consommations facturées"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12)
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(9)
ch.plots[0].series[0].format.fill.solid(); ch.plots[0].series[0].format.fill.fore_color.rgb = ORANGE
ch.plots[0].series[1].format.fill.solid(); ch.plots[0].series[1].format.fill.fore_color.rgb = BLEU
box(s, Inches(8.3), Inches(3.45), Inches(4.0), Inches(3.15), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(8.55), Inches(3.55), Inches(3.5), Inches(0.4), [[("Lecture", 14, True, VERT)]])
bullets(s, Inches(8.55), Inches(4.0), Inches(3.6), Inches(2.5), [
    "Forte dépendance au fioul (chaudière 1991)",
    "Conso stable malgré la météo",
    "Cause : enveloppe peu performante",
    "ECS électrique = poste élec majeur",
], size=12, gap=Pt(7))
notes(s, "J'ai analysé les factures sur 5 ans, soit bien plus que les 3 ans minimum attendus. "
         "Chauffage : chaudière fioul de 1991 + poêle à bois en appoint. Moyennes : 1 560 L de fioul, 6 stères de bois, "
         "5 447 kWh d'électricité dont l'eau chaude par ballon électrique. Les consommations sont stables d'une année sur l'autre, "
         "signe d'un usage régulier ; le niveau élevé pour 99 m² trahit une enveloppe défaillante. "
         "C'est ce constat qui m'amène à comparer ces consommations aux références.")

# ===========================================================================
# 9 — COMPARAISON / RIGUEUR CLIMATIQUE / RÉPARTITION (coef 2-3)
# ===========================================================================
s = add_slide(); header(s, "2", "Postes de dépense & mise en perspective")
# camembert répartition des postes (final energy approx)
cd = CategoryChartData()
cd.categories = ["Chauffage (fioul+bois)","ECS (ballon élec.)","Électricité spécifique"]
cd.add_series("Postes", (78, 9, 13))
gf = s.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(0.6), Inches(1.7), Inches(5.6), Inches(4.6), cd)
ch = gf.chart; ch.has_title = True; ch.chart_title.text_frame.text = "Répartition des postes de dépense"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12)
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(10)
pl = ch.plots[0]; pl.has_data_labels = True
pl.data_labels.show_value = True; pl.data_labels.number_format = '0"%"'; pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(12); pl.data_labels.font.bold = True; pl.data_labels.font.color.rgb = BLANC
pl.data_labels.position = XL_LABEL_POSITION.INSIDE_END
for i, c in enumerate([ORANGE, BLEU, GRIS_CLR]):
    pl.series[0].points[i].format.fill.solid(); pl.series[0].points[i].format.fill.fore_color.rgb = c
# right column
text(s, Inches(6.7), Inches(1.7), Inches(5.8), Inches(0.4), [[("Mise en perspective", 16, True, VERT)]])
bullets(s, Inches(6.7), Inches(2.2), Inches(5.9), Inches(2.4), [
    ("Rigueur climatique intégrée : ","Savoie, 498 m, zone H1 (climat froid → besoins élevés)"),
    ("Cohérence factures / DPE : ","conso facturée en ligne avec l’estimation théorique du DPE"),
    ("Chauffage = poste dominant : ","près de 80 % de la dépense énergétique"),
], size=13.5, gap=Pt(11))
box(s, Inches(6.7), Inches(4.75), Inches(5.9), Inches(1.5), fill=RGBColor(0xFF,0xF3,0xE0), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(6.95), Inches(4.9), Inches(5.4), Inches(1.3),
     [[("Comparaison à la moyenne nationale", 13, True, ORANGE)],
      [("535 kWhEP/m².an  vs  ≈ 250 kWhEP/m².an", 16, True, GRIS_TXT)],
      [("→ plus du double d’une habitation moyenne", 12, False, GRIS_TXT)]], line_spacing=1.15)
notes(s, "Je mets ces consommations en perspective, comme l'attend la méthode. D'abord la répartition par poste : "
         "le chauffage pèse près de 80 % de la dépense, l'ECS électrique environ 10 %, le reste en électricité spécifique. "
         "J'ai intégré la rigueur climatique : nous sommes en Savoie, à 498 m, en zone climatique H1, donc des besoins de chauffage "
         "structurellement élevés. J'ai vérifié la cohérence entre les factures et l'estimation théorique du DPE. "
         "Enfin, la comparaison nationale est parlante : 535 contre environ 250 kWh d'énergie primaire au m² en moyenne, "
         "soit plus du double. Le diagnostic confirme une vraie passoire thermique.")

# ===========================================================================
# 10 — ENVELOPPE THERMIQUE
# ===========================================================================
s = add_slide(); header(s, "2", "Diagnostic de l’enveloppe thermique")
make_table(s, Inches(0.9), Inches(1.7), Inches(8.0), [
    ["Élément","Composition","Observation"],
    ["Murs extérieurs","Pierre calcaire 50 cm","Forte inertie, faible isolation"],
    ["Toiture / combles","8 cm laine minérale ancienne","Isolation insuffisante"],
    ["Menuiseries","Double vitrage bois 4/16/4 Argon (2019)","Bon état, performantes"],
    ["Plancher bas","Dalle béton sur terre-plein","Non isolé → déperditions"],
    ["Ponts thermiques","Jonctions des parois","Pertes importantes"],
    ["Étanchéité à l’air","Non maîtrisée (entrées d’air)","Infiltrations parasites"],
], [Inches(2.2), Inches(3.4), Inches(2.4)], row_h=Inches(0.55), header_size=12, body_size=11.5, first_col_bold=True)
picture(s, IMG["menuiserie"], Inches(9.2), Inches(1.7), Inches(3.2), Inches(2.7),
        caption="Pose des menuiseries bois en tunnel (2019)")
box(s, Inches(9.2), Inches(4.75), Inches(3.2), Inches(1.55), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(9.4), Inches(4.85), Inches(2.85), Inches(1.4),
     [[("À retenir", 13, True, VERT)],
      [("Fenêtres déjà rénovées →", 12, False, GRIS_TXT)],
      [("priorité : murs + toiture", 13, True, VERT)]], line_spacing=1.15)
notes(s, "L'enveloppe maintenant, poste par poste. Murs en pierre 50 cm : forte inertie mais pas d'isolation. "
         "Combles : seulement 8 cm de laine minérale ancienne, très insuffisant. Menuiseries : double vitrage bois argon posé en 2019, "
         "donc récentes et performantes, avec des grilles d'entrée d'air. Plancher sur terre-plein non isolé. "
         "Et une étanchéité à l'air non maîtrisée, source d'infiltrations. Conclusion : comme les fenêtres sont déjà bonnes, "
         "je concentre l'isolation sur les murs et la toiture.")

# ===========================================================================
# 11 — SYSTÈMES EXISTANTS
# ===========================================================================
s = add_slide(); header(s, "2", "Diagnostic des systèmes existants", "Chauffage, ECS et ventilation")
make_table(s, Inches(0.9), Inches(1.7), Inches(8.2), [
    ["Équipement","Description","Limite principale"],
    ["Chaudière fioul","Basse température, 1991","Ancienne, fossile, sans sonde extérieure"],
    ["Radiateurs fonte","Haute T°, sans robinet thermo.","Régulation pièce par pièce absente"],
    ["Poêle à bois","Bûches 6 kW (2010)","Pas de label Flamme Verte, non étanche"],
    ["Ballon ECS","Électrique 200 L, hors volume chauffé","Pertes thermiques, conso élec."],
    ["Ventilation","Naturelle (pas de VMC)","Débits non maîtrisés, pertes"],
], [Inches(2.2), Inches(3.5), Inches(2.5)], row_h=Inches(0.58), header_size=12, body_size=11.5, first_col_bold=True)
picture(s, IMG["chaudiere"], Inches(9.4), Inches(1.7), Inches(1.45), Inches(2.55), caption="Chaudière fioul (1991)")
picture(s, IMG["ballon"], Inches(11.0), Inches(1.7), Inches(1.45), Inches(2.55), caption="Ballon ECS")
box(s, Inches(0.9), Inches(5.45), Inches(11.5), Inches(0.95), fill=RGBColor(0xFF,0xF3,0xE0), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.55), Inches(11.0), Inches(0.75),
     [[("Constat : ", 13, True, ORANGE),
       ("équipements vieillissants, régulation rudimentaire et absence de VMC → leviers majeurs d’économies.", 13, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Les systèmes : chaudière fioul de 1991, sans sonde extérieure ni régulation climatique, alimentant des radiateurs fonte "
         "haute température dépourvus de robinets thermostatiques — donc impossible d'ajuster pièce par pièce. "
         "Le poêle à bois de 6 kW aide en appoint mais n'est ni labellisé ni étanche. L'eau chaude vient d'un vieux ballon électrique "
         "de 200 L placé hors volume chauffé, ce qui génère des pertes. Et toujours aucune VMC. "
         "Ces trois points — chauffage, régulation, ventilation — sont mes principaux leviers d'économies.")

# ===========================================================================
# 12 — ÉCLAIRAGE, QAI & ACOUSTIQUE (coef 1+1+1)
# ===========================================================================
s = add_slide(); header(s, "2", "Éclairage, qualité de l’air & acoustique")
# trois cartes
def carte(s, l, t, titre, lignes, accent):
    box(s, l, t, Inches(3.7), Inches(4.2), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    box(s, l, t, Inches(3.7), Inches(0.6), fill=accent, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, l, t, Inches(3.7), Inches(0.6), [[(titre, 15, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    bullets(s, l + Inches(0.2), t + Inches(0.8), Inches(3.35), Inches(3.3), lignes, size=12.5, gap=Pt(8))
carte(s, Inches(0.9), Inches(1.75), "Éclairage / confort visuel", [
    ("Existant : ","25 % halogènes + 75 % LED, 200 W installés"),
    ("Proposé : ","passage 100 % LED basse conso"),
    ("Valoriser ","la lumière naturelle (orientation SE)"),
], ORANGE)
carte(s, Inches(4.8), Inches(1.75), "Qualité de l’air (QAI)", [
    ("Existant : ","ventilation naturelle, débits non maîtrisés"),
    ("Risques : ","humidité, condensation, polluants"),
    ("Proposé : ","VMC hygroréglable de type B"),
], VERT_CLR)
carte(s, Inches(8.7), Inches(1.75), "Confort acoustique", [
    ("Sources : ","bruits extérieurs (route, voisinage)"),
    ("Existant : ","isolation phonique limitée"),
    ("Proposé : ","l’ITE améliore aussi l’affaiblissement acoustique"),
], BLEU)
notes(s, "Trois confforts souvent oubliés mais notés. L'éclairage : aujourd'hui 25 % d'halogènes énergivores et 75 % de LED, "
         "200 W installés ; je préconise le passage en 100 % LED et la valorisation de la lumière naturelle grâce à l'orientation Sud-Est. "
         "La qualité de l'air : la ventilation naturelle ne maîtrise pas les débits et favorise l'humidité ; je propose une VMC hygro B. "
         "L'acoustique : les bruits extérieurs sont mal filtrés ; or l'isolation par l'extérieur améliore aussi l'affaiblissement acoustique — "
         "un bénéfice complémentaire des travaux d'enveloppe.")

# ===========================================================================
# 13 — BILAN DES DÉPERDITIONS
# ===========================================================================
s = add_slide(); header(s, "3", "Bilan des déperditions thermiques", "Calcul thermique de l’existant")
cd = CategoryChartData()
cd.categories = ["Murs extérieurs","Toiture","Ventilation","Ponts thermiques","Fenêtres","Plancher bas"]
cd.add_series("Déperditions", (42,20,20,10,4,4))
gf = s.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(0.7), Inches(1.7), Inches(6.3), Inches(4.85), cd)
ch = gf.chart; ch.has_title = False
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.RIGHT; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(11)
pl = ch.plots[0]; pl.has_data_labels = True
pl.data_labels.show_value = True; pl.data_labels.number_format = '0"%"'; pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(11); pl.data_labels.font.bold = True; pl.data_labels.font.color.rgb = BLANC
pl.data_labels.position = XL_LABEL_POSITION.INSIDE_END
for i, c in enumerate([ROUGE, ORANGE, BLEU, RGBColor(0x8E,0x24,0xAA), VERT_CLR, GRIS_CLR]):
    pl.series[0].points[i].format.fill.solid(); pl.series[0].points[i].format.fill.fore_color.rgb = c
text(s, Inches(7.5), Inches(1.7), Inches(5), Inches(0.4), [[("Indicateurs techniques", 15, True, VERT)]])
make_table(s, Inches(7.5), Inches(2.2), Inches(4.9), [
    ["Indicateur","Valeur"],
    ["Surface déperditive","232,91 m²"],
    ["Coefficient Ubât","2,03 W/(m².K)"],
    ["Ubât de référence","0,47 W/(m².K)"],
    ["Coefficient GV","722 W/K"],
    ["Puissance de chauffage","21,3 kW"],
], [Inches(2.9), Inches(2.0)], row_h=Inches(0.47), header_size=12, body_size=12)
text(s, Inches(7.5), Inches(5.5), Inches(4.9), Inches(1.0),
     [[("Ubât ≈ 4× la référence : l’enveloppe est le vrai problème.", 13, True, ROUGE)]])
notes(s, "Voici le cœur du diagnostic : le calcul des déperditions. 42 % partent par les murs, 20 % par la toiture, "
         "20 % par la ventilation, 10 % par les ponts thermiques, et seulement 4 % chacun pour fenêtres et plancher. "
         "L'indicateur clé : un Ubât de 2,03 contre une référence de 0,47, soit près de quatre fois trop. "
         "La puissance de chauffage nécessaire est de 21,3 kW. Ce calcul justifie directement mes priorités : "
         "murs, toiture et ventilation, qui cumulent plus de 80 % des pertes.")

# ===========================================================================
# 14 — DPE EXISTANT
# ===========================================================================
s = add_slide(); header(s, "3", "Étiquette DPE de l’existant", "Un logement très énergivore")
dpe_label(s, Inches(1.0), Inches(1.7), "G", "Classe énergie")
dpe_label(s, Inches(4.6), Inches(1.7), "G", "Classe climat (GES)")
kpi(s, Inches(8.2), Inches(1.85), Inches(4.1), Inches(1.15), "535 kWhEP/m².an", "Consommation énergétique", accent=ROUGE, val_size=21)
kpi(s, Inches(8.2), Inches(3.12), Inches(4.1), Inches(1.15), "156 kgCO₂/m².an", "Émissions de GES", accent=ROUGE, val_size=21)
kpi(s, Inches(8.2), Inches(4.39), Inches(4.1), Inches(1.15), "7 100 – 9 610 €/an", "Coût énergétique annuel", accent=ROUGE, val_size=21)
text(s, Inches(0.9), Inches(6.45), Inches(11.4), Inches(0.6),
     [[("→ Classe G sur les deux étiquettes : la rénovation performante est pleinement justifiée.", 15, True, VERT)]])
notes(s, "Tout converge vers le DPE. Le logement est classé G — la pire classe — en énergie comme en climat. "
         "535 kWh d'énergie primaire par m², 156 kg de CO2 par m², et une facture de 7 100 à 9 610 € par an. "
         "C'est cohérent avec ce qu'on a vu : murs non isolés et chaudière fioul. Cet état des lieux justifie une rénovation ambitieuse, "
         "ce qui m'amène à mes scénarios.")

# ===========================================================================
# 15 — RÉGLEMENTATION
# ===========================================================================
s = add_slide(); header(s, "4", "Réglementation et urbanisme")
text(s, Inches(0.9), Inches(1.65), Inches(11.4), Inches(0.5),
     [[("Les travaux respectent le cadre réglementaire et préservent le caractère de la ferme.", 15, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.25), Inches(11.5), [
    ["Élément réglementaire","Impact sur le projet"],
    ["Plan Local d’Urbanisme (PLU)","Vérification des règles applicables"],
    ["Isolation par l’extérieur (ITE)","Déclaration préalable de travaux"],
    ["Modification des façades","Respect de l’aspect architectural existant"],
    ["Rénovation performante (L.111-1 CCH)","Cadre du « bâtiment basse consommation »"],
    ["Aides à la rénovation","Respect des critères techniques exigés"],
    ["Normes & DTU","Mise en œuvre conforme"],
], [Inches(5.0), Inches(6.5)], row_h=Inches(0.55), header_size=14, body_size=13, first_col_bold=True)
notes(s, "Avant les travaux, le cadre réglementaire. L'ITE modifie l'aspect des façades : déclaration préalable en mairie et respect du PLU. "
         "Mes scénarios s'inscrivent dans la rénovation performante au sens du code de la construction, c'est-à-dire viser le niveau BBC. "
         "Les matériaux doivent respecter les critères techniques pour ouvrir droit aux aides, et tout est posé selon les DTU, "
         "en préservant le caractère de la ferme.")

# ===========================================================================
# 16 — SCÉNARIO 1 : PAR ÉTAPES (B/B)
# ===========================================================================
s = add_slide(); header(s, "4", "Scénario 1 — Rénovation performante par étapes", "Étape 1 : l’enveloppe")
text(s, Inches(0.9), Inches(1.6), Inches(11.4), Inches(0.4),
     [[("1ʳᵉ étape ciblée sur l’enveloppe : elle traite 2 postes d’isolation et fait gagner plusieurs classes (G → B).", 13.5, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.1), Inches(7.1), [
    ["Poste","Solution — étape 1"],
    ["Murs","ITE laine de bois 200 mm"],
    ["Combles","Ouate de cellulose 400 mm"],
    ["Ventilation","VMC hygroréglable type B"],
    ["Chauffage","Fioul conservé (étape ultérieure)"],
    ["ECS","Ballon conservé (étape ultérieure)"],
], [Inches(1.9), Inches(5.2)], row_h=Inches(0.5), header_size=13, body_size=12, first_col_bold=True)
dpe_label(s, Inches(8.7), Inches(1.95), "B", "Énergie", scale_h=Inches(0.30), base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
dpe_label(s, Inches(10.9), Inches(1.95), "B", "Climat", scale_h=Inches(0.30), base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
box(s, Inches(0.9), Inches(5.05), Inches(11.5), Inches(1.55), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.15), Inches(11), Inches(0.4), [[("Avantages & cohérence des étapes", 14, True, VERT)]])
bullets(s, Inches(1.15), Inches(5.6), Inches(5.5), Inches(1.0), [
    "Traite les 2 premiers postes de pertes (murs + toiture)",
    "Ne compromet pas le futur changement de chauffage",
    "Investissement maîtrisé : ≈ 24 000 €",
], size=12, gap=Pt(5))
bullets(s, Inches(6.9), Inches(5.6), Inches(5.3), Inches(1.0), [
    "Confort d’hiver et d’été améliorés",
    "Inertie des murs en pierre conservée",
    "Étiquette DPE : G → B / B",
], size=12, gap=Pt(5))
notes(s, "Mon premier scénario est une rénovation performante PAR ÉTAPES. L'étape 1 cible l'enveloppe : "
         "isolation des murs par l'extérieur en laine de bois 200 mm, isolation des combles en ouate de cellulose 400 mm, et VMC hygro B. "
         "C'est cohérent avec l'attendu : cette première étape traite les DEUX premiers postes d'isolation — murs et toiture — "
         "et fait gagner plusieurs classes, de G à B. Point important : en commençant par l'isolation, on réduit les besoins, "
         "ce qui ne compromet pas mais au contraire prépare le changement de chauffage à l'étape suivante — on pourra alors dimensionner plus petit. "
         "Le chauffage et l'ECS sont conservés à ce stade. Investissement : environ 24 000 €.")

# ===========================================================================
# 17 — SCÉNARIO 2 : GLOBAL (A/B)
# ===========================================================================
s = add_slide(); header(s, "4", "Scénario 2 — Rénovation performante globale", "Enveloppe + remplacement du chauffage")
text(s, Inches(0.9), Inches(1.55), Inches(11.4), Inches(0.4),
     [[("Toute l’isolation du scénario 1 + sortie du fioul. Deux solutions de chauffage comparées :", 13.5, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.05), Inches(7.5), [
    ["Critère","PAC Air/Eau","Chaudière granulés"],
    ["Rendement","COP > 3","> 90 %"],
    ["Émissions CO₂","Très faibles","Très faibles"],
    ["Stockage","Aucun","Silo nécessaire"],
    ["Radiateurs fonte (haute T°)","Moins adaptée","Très adaptée"],
    ["Bâti ancien savoyard","Bonne","Très adaptée"],
], [Inches(2.9), Inches(2.3), Inches(2.3)], row_h=Inches(0.5), header_size=12, body_size=11.5, first_col_bold=True)
dpe_label(s, Inches(9.0), Inches(1.95), "A", "Énergie", scale_h=Inches(0.28), base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
dpe_label(s, Inches(11.1), Inches(1.95), "B", "Climat", scale_h=Inches(0.28), base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=11)
box(s, Inches(0.9), Inches(5.35), Inches(7.5), Inches(1.3), fill=VERT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.45), Inches(7.0), Inches(1.1),
     [[("✔ Solution retenue : chaudière à granulés 12 kW + silo", 14, True, BLANC)],
      [("Conserve les radiateurs fonte existants · énergie renouvelable locale · approvisionnement facile en Savoie.", 11.5, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.05)
box(s, Inches(8.7), Inches(5.35), Inches(3.7), Inches(1.3), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(8.9), Inches(5.45), Inches(3.3), Inches(1.1),
     [[("Étiquette DPE", 12, True, VERT)],
      [("G → A / B", 22, True, DPE_COLORS["A"])],
      [("Investissement ≈ 40 000 €", 12, False, GRIS_TXT)]], line_spacing=1.0)
notes(s, "Mon second scénario est une rénovation performante GLOBALE : toute l'isolation du scénario 1 en une fois, "
         "plus le remplacement du chauffage. J'ai étudié deux solutions bas carbone : la PAC air/eau et la chaudière à granulés. "
         "Les deux ont d'excellents rendements et de faibles émissions. Je retiens la chaudière à granulés pour deux raisons décisives : "
         "elle est compatible avec les radiateurs en fonte HAUTE température déjà en place — la PAC serait moins efficace sur de la haute température — "
         "et le granulé est une énergie renouvelable locale, facile à approvisionner en Savoie. Résultat : étiquette A/B, pour environ 40 000 €.")

# ===========================================================================
# 18 — OPTIMISATION DES SYSTÈMES (régulation + ECS) coef 5
# ===========================================================================
s = add_slide(); header(s, "5", "Optimisation des systèmes", "Régulation du chauffage & production d’ECS")
box(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(4.6), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(0.6), fill=VERT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(0.6), [[("Régulation du chauffage", 16, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
bullets(s, Inches(1.15), Inches(2.55), Inches(5.25), Inches(3.6), [
    ("Sonde de température extérieure ","→ pilotage par loi d’eau"),
    ("Robinets thermostatiques ","sur les radiateurs fonte (régulation pièce par pièce)"),
    ("Thermostat programmable ","(réduit en absence / nuit)"),
    ("Rendement global ","amélioré : générateur récent + émetteurs régulés",),
], size=13.5, gap=Pt(11))
box(s, Inches(6.9), Inches(1.75), Inches(5.5), Inches(4.6), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, Inches(6.9), Inches(1.75), Inches(5.5), Inches(0.6), fill=BLEU, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(6.9), Inches(1.75), Inches(5.5), Inches(0.6), [[("Production d’eau chaude (ECS)", 16, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
bullets(s, Inches(7.15), Inches(2.55), Inches(5.05), Inches(3.6), [
    ("Existant : ","vieux ballon élec. 200 L hors volume chauffé (pertes)"),
    ("Sc. 1 : ","chauffe-eau thermodynamique (÷3 sur la conso ECS)"),
    ("Sc. 2 : ","ECS couplée à la chaudière granulés (ballon tampon)"),
    ("Ballon repositionné ","dans le volume chauffé",),
], size=13.5, gap=Pt(11))
notes(s, "Cette diapo répond à un attendu fortement coefficienté : l'adaptation et l'optimisation des équipements. "
         "Côté régulation, le diagnostic a montré l'absence de sonde extérieure et de robinets thermostatiques. Je préconise donc : "
         "une sonde extérieure pour piloter la chaudière par loi d'eau, des robinets thermostatiques sur les radiateurs fonte pour réguler "
         "pièce par pièce, et un thermostat programmable. On améliore ainsi le rendement global de l'installation. "
         "Côté eau chaude : le vieux ballon électrique hors volume chauffé est un gouffre. Dans le scénario 1, je propose un chauffe-eau "
         "thermodynamique qui divise la conso ECS par trois ; dans le scénario 2, l'ECS est couplée à la chaudière granulés via un ballon tampon. "
         "Dans les deux cas, on replace le ballon dans le volume chauffé.")

# ===========================================================================
# 19 — MATÉRIAUX BIOSOURCÉS
# ===========================================================================
s = add_slide(); header(s, "5", "Solutions à faible impact carbone", "Le choix des matériaux biosourcés")
make_table(s, Inches(0.9), Inches(1.85), Inches(8.0), [
    ["Critère","Laine de bois","Ouate de cellulose"],
    ["Origine","Fibres de bois","Papier recyclé"],
    ["Type","Biosourcé","Biosourcé"],
    ["Performance thermique","Très bonne","Très bonne"],
    ["Impact environnemental","Faible","Très faible"],
    ["Utilisation retenue","ITE des murs","Isolation des combles"],
], [Inches(3.0), Inches(2.5), Inches(2.5)], row_h=Inches(0.55), header_size=12, body_size=12, first_col_bold=True)
box(s, Inches(9.2), Inches(1.85), Inches(3.2), Inches(3.3), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(9.4), Inches(2.0), Inches(2.8), Inches(3.1),
     [[("Pourquoi le biosourcé ?", 13, True, VERT)],
      [("",6,False,VERT)],
      [("• Faible impact carbone", 12, False, GRIS_TXT)],
      [("• Excellent déphasage", 12, False, GRIS_TXT)],
      [("  → confort d’été", 11, False, GRIS_CLR, True)],
      [("• Murs perspirants", 12, False, GRIS_TXT)],
      [("  → gestion de l’humidité", 11, False, GRIS_CLR, True)]], line_spacing=1.15)
notes(s, "Comme le demande la grille, j'ai privilégié des solutions bas carbone : des matériaux biosourcés. "
         "Laine de bois pour l'ITE des murs, ouate de cellulose — du papier recyclé — pour les combles. "
         "Trois raisons : un faible impact carbone, un excellent déphasage thermique qui apporte le confort d'été recherché, "
         "et surtout la perspirance, essentielle sur des murs en pierre anciens qui doivent laisser passer la vapeur d'eau pour éviter les pathologies d'humidité.")

# ===========================================================================
# 20 — DIMENSIONNEMENT
# ===========================================================================
s = add_slide(); header(s, "5", "Dimensionnement des installations", "Du calcul au choix des équipements")
box(s, Inches(0.9), Inches(1.7), Inches(5.7), Inches(2.35), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.1), Inches(1.8), Inches(5.3), Inches(2.25),
     [[("Résistance des isolants  (R = e / λ)", 13, True, VERT)],
      [("",5,False,VERT)],
      [("Murs — laine de bois 200 mm (λ=0,038) :", 12, True, GRIS_TXT)],
      [("R = 0,20 / 0,038 = 5,26 m².K/W", 13, False, BLEU)],
      [("",4,False,VERT)],
      [("Combles — ouate 400 mm (λ=0,039) :", 12, True, GRIS_TXT)],
      [("R = 0,40 / 0,039 = 10,26 m².K/W", 13, False, BLEU)]], line_spacing=1.1)
box(s, Inches(6.8), Inches(1.7), Inches(5.6), Inches(2.35), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(7.0), Inches(1.8), Inches(5.2), Inches(2.25),
     [[("Puissance de chauffage après travaux", 13, True, VERT)],
      [("",5,False,VERT)],
      [("Réduction des besoins estimée : 55 %", 12, True, GRIS_TXT)],
      [("P = 21,3 × (1 − 0,55) = 9,6 kW ≈ 10 kW", 13, False, BLEU)],
      [("",4,False,VERT)],
      [("Avec marge de sécurité :", 12, True, GRIS_TXT)],
      [("→ Chaudière à granulés de 12 kW", 14, True, VERT)]], line_spacing=1.1)
make_table(s, Inches(0.9), Inches(4.4), Inches(5.7), [
    ["Combustible granulés","Valeur"],
    ["Besoin après travaux","7 020 kWh/an"],
    ["PCI granulés","4,8 kWh/kg"],
    ["Conso annuelle","≈ 1,5 t/an"],
    ["Silo retenu","2 tonnes"],
], [Inches(3.2), Inches(2.5)], row_h=Inches(0.42), header_size=12, body_size=11)
make_table(s, Inches(6.8), Inches(4.4), Inches(5.6), [
    ["VMC Hygro B — débits","m³/h"],
    ["Cuisine","45 à 135"],
    ["Salle de bain","30"],
    ["WC","15"],
    ["Total maximal","180"],
], [Inches(3.3), Inches(2.3)], row_h=Inches(0.42), header_size=12, body_size=11)
notes(s, "Le dimensionnement. Pour l'isolation, R = épaisseur / lambda : R = 5,26 pour les murs, R = 10,26 pour les combles — "
         "des valeurs conformes à une rénovation performante. Pour le chauffage : la puissance initiale est de 21,3 kW ; "
         "avec une réduction des besoins estimée à 55 % grâce à l'isolation et la VMC, on tombe à environ 10 kW. "
         "Avec une marge de sécurité pour les jours les plus froids, je retiens 12 kW. "
         "Le besoin annuel revient à environ 1,5 tonne de granulés, d'où un silo de 2 tonnes. La VMC hygro B est dimensionnée à 180 m³/h maxi.")

# ===========================================================================
# 21 — CHIFFRAGE
# ===========================================================================
s = add_slide(); header(s, "6", "Chiffrage des travaux", "Estimation HT par poste")
text(s, Inches(0.9), Inches(1.7), Inches(5.5), Inches(0.4), [[("Scénario 1 — 24 000 €", 16, True, BLEU)]])
make_table(s, Inches(0.9), Inches(2.15), Inches(5.5), [
    ["Poste","Coût HT"],
    ["ITE laine de bois 200 mm","18 000 €"],
    ["Isolation combles ouate 400 mm","2 500 €"],
    ["VMC Hygro B","2 000 €"],
    ["Divers et raccordements","1 500 €"],
    ["Total","24 000 €"],
], [Inches(3.7), Inches(1.8)], row_h=Inches(0.5), header_size=12, body_size=12)
text(s, Inches(6.8), Inches(1.7), Inches(5.5), Inches(0.4), [[("Scénario 2 — 40 000 €", 16, True, VERT)]])
make_table(s, Inches(6.8), Inches(2.15), Inches(5.6), [
    ["Poste","Coût HT"],
    ["ITE laine de bois 200 mm","18 000 €"],
    ["Isolation combles ouate 400 mm","2 500 €"],
    ["VMC Hygro B","2 000 €"],
    ["Chaudière à granulés 12 kW","13 000 €"],
    ["Silo de stockage","2 500 €"],
    ["Divers et raccordements","2 000 €"],
    ["Total","40 000 €"],
], [Inches(3.8), Inches(1.8)], row_h=Inches(0.47), header_size=12, body_size=11.5)
notes(s, "Le chiffrage s'appuie sur les prix moyens du marché par type de travaux. "
         "Scénario 1 : 24 000 € HT, dont 18 000 € pour l'isolation des murs — logique, c'est le premier poste de pertes. "
         "Scénario 2 : on ajoute la chaudière à granulés et le silo, soit 40 000 € au total. "
         "L'écart de 16 000 € correspond donc au remplacement du chauffage.")

# ===========================================================================
# 22 — FINANCEMENT
# ===========================================================================
s = add_slide(); header(s, "6", "Plan de financement", "Aides mobilisables & reste à charge")
make_table(s, Inches(0.9), Inches(1.9), Inches(5.5), [
    ["Scénario 1","Montant"],
    ["Coût total des travaux","24 000 €"],
    ["MaPrimeRénov’","− 5 000 €"],
    ["CEE","− 2 000 €"],
    ["Reste à charge","17 000 €"],
], [Inches(3.5), Inches(2.0)], row_h=Inches(0.55), header_size=13, body_size=12)
make_table(s, Inches(6.8), Inches(1.9), Inches(5.5), [
    ["Scénario 2","Montant"],
    ["Coût total des travaux","40 000 €"],
    ["MaPrimeRénov’","− 8 000 €"],
    ["CEE","− 4 000 €"],
    ["Aides locales","− 1 000 €"],
    ["Reste à charge","27 000 €"],
], [Inches(3.5), Inches(2.0)], row_h=Inches(0.5), header_size=13, body_size=12)
box(s, Inches(0.9), Inches(5.5), Inches(11.5), Inches(1.0), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.6), Inches(11.0), Inches(0.8),
     [[("MaPrimeRénov’, CEE et aides locales réduisent fortement le reste à charge — "
        "sous réserve du respect des critères techniques des travaux et selon les revenus du ménage.", 14, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Les travaux sont éligibles à plusieurs aides, ce qui permet de calculer le reste à charge — un attendu important. "
         "Scénario 1 : 5 000 € de MaPrimeRénov' et 2 000 € de CEE, reste à charge 17 000 €. "
         "Scénario 2, plus ambitieux donc mieux aidé : 8 000 € de MaPrimeRénov', 4 000 € de CEE, 1 000 € d'aides locales, reste à charge 27 000 €. "
         "Ce sont des estimations : les montants réels dépendent des revenus du ménage et des barèmes en vigueur.")

# ===========================================================================
# 23 — COÛT GLOBAL & ROI
# ===========================================================================
s = add_slide(); header(s, "6", "Analyse en coût global & rentabilité")
cd = CategoryChartData()
cd.categories = ["État initial","Scénario 1","Scénario 2"]
cd.add_series("Coût global sur 30 ans (€)", (250650, 159000, 130000))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.9), Inches(1.75), Inches(6.6), Inches(3.4), cd)
ch = gf.chart; ch.has_title = True; ch.chart_title.text_frame.text = "Coût global sur 30 ans"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12); ch.has_legend = False
pl = ch.plots[0]; pl.has_data_labels = True
pl.data_labels.number_format = '# ##0 "€"'; pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(10); pl.data_labels.font.bold = True
for i, c in enumerate([ROUGE, BLEU, VERT]):
    pl.series[0].points[i].format.fill.solid(); pl.series[0].points[i].format.fill.fore_color.rgb = c
text(s, Inches(7.9), Inches(1.7), Inches(4.5), Inches(0.4), [[("Coûts mensuels & ROI", 13, True, VERT)]])
make_table(s, Inches(7.9), Inches(2.2), Inches(4.5), [
    ["Situation","€/an","€/mois"],
    ["Avant travaux","8 355","696"],
    ["Scénario 1","4 500","375"],
    ["Scénario 2","3 000","250"],
], [Inches(1.9), Inches(1.3), Inches(1.3)], row_h=Inches(0.47), header_size=11.5, body_size=11)
make_table(s, Inches(7.9), Inches(4.55), Inches(4.5), [
    ["ROI","Sc. 1","Sc. 2"],
    ["Reste à charge","17 000 €","27 000 €"],
    ["Économies/an","3 000 €","5 000 €"],
    ["Amortissement","5,7 ans","5,4 ans"],
], [Inches(1.9), Inches(1.3), Inches(1.3)], row_h=Inches(0.47), header_size=11.5, body_size=11)
notes(s, "C'est l'analyse en coût global qui tranche entre les scénarios. Sans rien faire, on dépense 250 000 € sur 30 ans ; "
         "le scénario 1 ramène à 159 000 €, le scénario 2 à 130 000 €. Donc malgré un investissement initial plus élevé, "
         "le scénario 2 coûte MOINS cher au final. Les coûts mensuels passent de 696 € à 250 €. "
         "Et le ROI est rapide : 5,7 ans pour le scénario 1, 5,4 ans pour le scénario 2. "
         "Question possible du jury : j'ai retenu 30 ans ; en intégrant une hausse du prix de l'énergie, l'écart se creuserait encore en faveur du scénario 2.")

# ===========================================================================
# 24 — PLAN DE SOBRIÉTÉ
# ===========================================================================
s = add_slide(); header(s, "7", "Plan de sobriété", "Conseils aux occupants")
bullets(s, Inches(0.9), Inches(1.85), Inches(5.7), Inches(4.5), [
    "Chauffer entre 19 °C et 20 °C dans les pièces de vie",
    "Réduire la température durant les absences",
    "Entretien régulier de la chaudière et de la VMC",
    "Limiter les consommations d’eau chaude sanitaire",
], size=15, gap=Pt(12))
bullets(s, Inches(6.9), Inches(1.85), Inches(5.5), Inches(4.5), [
    "Fermer les volets la nuit en hiver",
    "Privilégier l’électroménager performant",
    "Éteindre les appareils en veille",
    "Suivre régulièrement ses consommations",
], size=15, gap=Pt(12))
box(s, Inches(0.9), Inches(5.85), Inches(11.5), Inches(0.85), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.95), Inches(11), Inches(0.65),
     [[("Des conseils simples, accessibles à des non-spécialistes, qui amplifient les économies des travaux.", 14, True, VERT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "En complément des travaux, un mode opératoire de sobriété destiné aux occupants — un attendu de la grille. "
         "Des gestes simples et gratuits, formulés pour des non-spécialistes : maintenir 19-20 °C, baisser en cas d'absence, "
         "entretenir les équipements, fermer les volets la nuit, traquer les veilles, suivre ses consommations. "
         "Ces gestes amplifient les économies obtenues par la rénovation.")

# ===========================================================================
# 25 — SYNTHÈSE COMPARATIVE
# ===========================================================================
s = add_slide(); header(s, "7", "Synthèse comparative des scénarios")
make_table(s, Inches(0.9), Inches(1.85), Inches(11.5), [
    ["Critère","État initial","Scénario 1 (par étapes)","Scénario 2 (global)"],
    ["Étiquette DPE","G / G","B / B","A / B"],
    ["Chauffage","Fioul (1991)","Fioul conservé (étape 1)","Granulés 12 kW"],
    ["Coût des travaux","—","24 000 €","40 000 €"],
    ["Reste à charge","—","17 000 €","27 000 €"],
    ["Coût annuel","8 355 €","4 500 €","3 000 €"],
    ["Coût global 30 ans","250 650 €","159 000 €","130 000 €"],
    ["Retour sur investissement","—","5,7 ans","5,4 ans"],
], [Inches(3.0), Inches(2.4), Inches(3.05), Inches(3.05)], row_h=Inches(0.52), header_size=12.5, body_size=12, first_col_bold=True)
notes(s, "Cette synthèse récapitule tout. On lit la progression : de G/G à B/B avec le scénario par étapes, "
         "jusqu'à A/B avec le scénario global. Le scénario 2 coûte plus cher à l'achat mais affiche le coût annuel le plus bas, "
         "le coût global le plus faible et même le ROI le plus court. C'est la base de ma recommandation.")

# ===========================================================================
# 26 — CONCLUSION
# ===========================================================================
s = add_slide(); set_bg(s, VERT)
box(s, 0, 0, SW, Inches(1.5), fill=VERT_CLR)
text(s, Inches(0.9), Inches(0.4), Inches(11.5), Inches(0.9), [[("Conclusion & recommandation", 32, True, BLANC)]], anchor=MSO_ANCHOR.MIDDLE)
box(s, Inches(0.9), Inches(1.9), Inches(11.5), Inches(2.5), fill=BLANC, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.2), Inches(2.05), Inches(11), Inches(0.5), [[("→ Je recommande le Scénario 2 (rénovation globale)", 22, True, VERT)]])
bullets(s, Inches(1.2), Inches(2.7), Inches(11), Inches(1.6), [
    ("Performance maximale : ","de G à A / B (énergie / climat)"),
    ("Sortie du fioul : ","énergie renouvelable et locale (granulés savoyards)"),
    ("Meilleure rentabilité long terme : ","coût global le plus bas, ROI 5,4 ans"),
    ("Compatible avec le bâti : ","ITE biosourcée + radiateurs fonte conservés"),
], size=14, gap=Pt(7))
box(s, 0, Inches(4.7), SW, Inches(2.8), fill=VERT)
text(s, Inches(0.9), Inches(5.0), Inches(11.5), Inches(0.6),
     [[("Budget contraint ? Le Scénario 1 reste une excellente 1ʳᵉ étape (G → B/B), complétée plus tard par le chauffage.", 15, False, RGBColor(0xC8,0xE6,0xC9), True)]])
text(s, Inches(0.9), Inches(5.9), Inches(11.5), Inches(1.4),
     [[("Merci de votre attention.", 30, True, BLANC)],
      [("Je suis à votre disposition pour vos questions.", 16, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.1)
notes(s, "Pour conclure : au regard de la performance, du confort, de la sortie du fioul et de la rentabilité long terme, "
         "je recommande le scénario 2, la rénovation globale, qui fait passer le logement de G à A/B et qui coûte le moins cher sur 30 ans. "
         "Si le budget initial est un frein, le scénario 1 par étapes est une excellente première étape, "
         "qu'on complétera plus tard par le changement de chauffage — les deux scénarios sont d'ailleurs cohérents entre eux. "
         "Je vous remercie de votre attention et je suis prêt à répondre à vos questions.")

out = "/home/user/licence/Soutenance_Renovation_Saint-Jean-de-Chevelu.pptx"
prs.save(out)
print("OK - slides:", len(prs.slides._sldIdLst))
