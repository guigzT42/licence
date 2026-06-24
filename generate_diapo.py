# -*- coding: utf-8 -*-
"""
Diaporama oral - Etude de renovation energetique (Bloc 1 - Sujet A)
Maison individuelle a Saint-Jean-de-Chevelu (Savoie) - Guillaume Tardy
v3 : DPE calcules (G->D->B), prix realistes avec marques, foyer modeste, 22 diapos.
"""
import re
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
              "C":RGBColor(0xC3,0xD0,0x00),"D":RGBColor(0xF7,0xCB,0x00),
              "E":RGBColor(0xF7,0xB1,0x00),"F":RGBColor(0xEA,0x6C,0x16),
              "G":RGBColor(0xE2,0x00,0x1A)}
DPE_TXT = {"A":BLANC,"B":BLANC,"C":ANTHRA,"D":ANTHRA,"E":BLANC,"F":BLANC,"G":BLANC}

prs = Presentation()
prs.slide_width  = Inches(13.333); prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

def add_slide(): return prs.slides.add_slide(BLANK)

def set_bg(slide, color):
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SW, SH)
    rect.fill.solid(); rect.fill.fore_color.rgb = color
    rect.line.fill.background(); rect.shadow.inherit = False
    slide.shapes._spTree.remove(rect._element); slide.shapes._spTree.insert(2, rect._element)
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
    text(slide, tl, Inches(0.40), Inches(11.3), Inches(0.8), [[(titre, 28, True, VERT)]], anchor=MSO_ANCHOR.MIDDLE)
    if sous:
        text(slide, tl, Inches(1.14), Inches(11.3), Inches(0.4), [[(sous, 14, False, GRIS_CLR, True)]])
    box(slide, tl, Inches(1.26), Inches(11.0), Pt(2.2), fill=VERT_CLR)
    text(slide, Inches(0.55), Inches(7.08), Inches(9), Inches(0.32),
         [[("Renovation energetique - Saint-Jean-de-Chevelu (73) - Bloc 1", 9, False, GRIS_CLR)]])
    text(slide, Inches(10.3), Inches(7.08), Inches(2.5), Inches(0.32),
         [[("Guillaume Tardy", 9, False, GRIS_CLR)]], align=PP_ALIGN.RIGHT)

def make_table(slide, l, t, rows, col_widths, row_h=Inches(0.4),
               header_fill=VERT, header_size=13, body_size=12, first_col_bold=False,
               highlight_rows=None, highlight_fill=None):
    highlight_rows = highlight_rows or []
    nrows = len(rows)
    gtbl = slide.shapes.add_table(nrows, len(col_widths), l, t, sum(col_widths, Emu(0)), row_h*nrows).table
    gtbl.first_row = False; gtbl.horz_banding = False
    for ci, cw in enumerate(col_widths): gtbl.columns[ci].width = cw
    for ri in range(nrows): gtbl.rows[ri].height = row_h
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = gtbl.cell(ri, ci)
            cell.margin_left = Pt(6); cell.margin_right = Pt(6)
            cell.margin_top = Pt(1); cell.margin_bottom = Pt(1)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if ri == 0: cell.fill.fore_color.rgb = header_fill
            elif ri in highlight_rows: cell.fill.fore_color.rgb = highlight_fill or VERT_LIGHT
            else: cell.fill.fore_color.rgb = VERT_LIGHT if ri % 2 == 0 else BLANC
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER
            r = p.add_run(); r.text = val; r.font.name = "Calibri"
            if ri == 0:
                r.font.size = Pt(header_size); r.font.bold = True; r.font.color.rgb = BLANC
            else:
                r.font.size = Pt(body_size)
                r.font.bold = (ci == 0 and first_col_bold) or (ri in highlight_rows)
                r.font.color.rgb = GRIS_TXT
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
    text(slide, l, t + Inches(0.16), w, h - Inches(0.6), [[(value, val_size, True, accent)]],
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(slide, l, t + h - Inches(0.52), w, Inches(0.48), [[(label, 11, False, GRIS_TXT)]],
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

def picture(slide, path, bl, bt, bw, bh, caption=None, frame=True, cap_size=11):
    m = re.search(r'_(\d+)x(\d+)\.png$', path); iw, ih = int(m.group(1)), int(m.group(2))
    cap_h = Inches(0.34) if caption else Emu(0)
    avail_h = bh - cap_h
    scale = min(bw / iw, avail_h / ih)
    w = int(iw * scale); h = int(ih * scale)
    l = bl + (bw - w) // 2; t = bt + (avail_h - h) // 2
    if frame:
        box(slide, l - Emu(20000), t - Emu(20000), w + Emu(40000), h + Emu(40000), fill=BLANC, line=GRIS_CLR, line_w=Pt(1.2))
    slide.shapes.add_picture(path, l, t, width=w, height=h)
    if caption:
        text(slide, bl, bt + avail_h + Emu(20000), bw, cap_h, [[(caption, cap_size, False, GRIS_CLR, True)]], align=PP_ALIGN.CENTER)
    return l, t, w, h

def dpe_label(slide, cx, top, current, label_txt="Classe energie", scale_h=Inches(0.42),
              base_w=Inches(1.0), step=Inches(0.34), letter_size=16, label_size=12):
    letters = ["A","B","C","D","E","F","G"]
    text(slide, cx, top, base_w + step*6, Inches(0.3), [[(label_txt, label_size, True, GRIS_TXT)]], align=PP_ALIGN.LEFT)
    y = top + Inches(0.36)
    for i, ltr in enumerate(letters):
        w = base_w + step*i; is_cur = (ltr == current)
        box(slide, cx, y, w, scale_h, fill=DPE_COLORS[ltr], shape=MSO_SHAPE.ROUNDED_RECTANGLE,
            line=(ANTHRA if is_cur else None), line_w=Pt(2.5))
        text(slide, cx + Inches(0.06), y, w - Inches(0.08), scale_h, [[(ltr, letter_size, True, DPE_TXT[ltr])]], anchor=MSO_ANCHOR.MIDDLE)
        if is_cur:
            box(slide, cx - Inches(0.34), y, Inches(0.30), scale_h, fill=ANTHRA, shape=MSO_SHAPE.PENTAGON)
        y += scale_h + Inches(0.06)
    return y

def dpe_badge(slide, l, t, letter, w=Inches(0.95), h=Inches(0.95), sub=None):
    box(slide, l, t, w, h, fill=DPE_COLORS[letter], shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(slide, l, t, w, h, [[(letter, 34, True, DPE_TXT[letter])]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    if sub:
        text(slide, l - Inches(0.4), t + h + Inches(0.02), w + Inches(0.8), Inches(0.3),
             [[(sub, 11, True, GRIS_TXT)]], align=PP_ALIGN.CENTER)

# ===========================================================================
# 1 - TITRE
# ===========================================================================
s = add_slide(); set_bg(s, VERT)
box(s, 0, 0, Inches(6.4), SH, fill=VERT_CLR)
picture(s, IMG["facade"], Inches(0.0), Inches(0.0), Inches(6.4), SH, frame=False)
box(s, Inches(6.4), 0, Pt(6), SH, fill=RGBColor(0xA5,0xD6,0xA7))
text(s, Inches(6.85), Inches(0.7), Inches(6.2), Inches(0.5),
     [[("BLOC 1 - CHARGE DE PROJET ENERGIE ET BATIMENT DURABLES", 12, True, RGBColor(0xC8,0xE6,0xC9))]])
text(s, Inches(6.85), Inches(1.5), Inches(6.2), Inches(2.6),
     [[("Renovation", 38, True, BLANC)], [("energetique d'une", 38, True, BLANC)],
      [("ancienne ferme", 38, True, RGBColor(0xC8,0xE6,0xC9))], [("savoyarde", 38, True, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.0)
text(s, Inches(6.85), Inches(4.7), Inches(6.2), Inches(0.6),
     [[("Etude pour un maitre d'ouvrage - Saint-Jean-de-Chevelu (73)", 15, False, BLANC)]])
box(s, Inches(6.85), Inches(5.5), Inches(5.9), Pt(2), fill=RGBColor(0xA5,0xD6,0xA7))
text(s, Inches(6.85), Inches(5.75), Inches(6.2), Inches(1.0),
     [[("Presente par Guillaume Tardy", 17, True, BLANC)], [("Soutenance orale - Sujet A", 13, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.15)
notes(s, "Bonjour, je suis Guillaume Tardy. Je vous presente mon etude de renovation energetique realisee pour un maitre "
         "d'ouvrage occupant : une ancienne ferme savoyarde de la fin du XIXe siecle a Saint-Jean-de-Chevelu. Ma demarche : "
         "diagnostiquer l'existant, le comparer aux references, puis proposer deux scenarios de renovation performante - "
         "un par etapes et un global - chiffres et argumentes. Le photovoltaique et la climatisation sont hors etude.")

# ===========================================================================
# 2 - SOMMAIRE
# ===========================================================================
s = add_slide(); header(s, None, "Sommaire")
items = [
    ("1","Situation, foyer & objectifs","Contexte, moyens du MOA, confort vise"),
    ("2","Diagnostic technique de l'existant","Consommations, enveloppe, systemes, eclairage"),
    ("3","Deperditions & DPE de l'existant","Calcul thermique, etiquette G"),
    ("4","Deux scenarios de renovation","Par etapes (D) et global (B)"),
    ("5","DPE des scenarios & dimensionnement","Calculs DPE, regulation, ECS, materiaux"),
    ("6","Analyse economique en cout global","Chiffrage, aides, reste a charge, ROI"),
    ("7","Sobriete & conclusion","Conseils occupants, recommandation"),
]
y = Inches(1.7)
for num, t1, sub in items:
    box(s, Inches(0.9), y, Inches(0.52), Inches(0.52), fill=VERT, shape=MSO_SHAPE.OVAL)
    text(s, Inches(0.9), y, Inches(0.52), Inches(0.52), [[(num,17,True,BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(1.65), y - Inches(0.03), Inches(8), Inches(0.4), [[(t1,17,True,GRIS_TXT)]], anchor=MSO_ANCHOR.MIDDLE)
    text(s, Inches(1.65), y + Inches(0.30), Inches(10.5), Inches(0.3), [[(sub,12,False,GRIS_CLR,True)]])
    y += Inches(0.70)
notes(s, "Voici mon plan : contexte et moyens du maitre d'ouvrage, puis le diagnostic technique complet. "
         "J'en tire les deperditions et le DPE actuel. Je presente ensuite mes deux scenarios, le calcul de leur DPE, "
         "leur dimensionnement, l'analyse economique en cout global, et je termine par la sobriete et ma recommandation.")

# ===========================================================================
# 3 - CONTEXTE + PROFIL FOYER
# ===========================================================================
s = add_slide(); header(s, "1", "Analyse de la situation", "Le batiment et le foyer")
bullets(s, Inches(0.9), Inches(1.7), Inches(6.0), Inches(3.0), [
    ("Ancienne ferme ","fin XIXe s., rehabilitee dans les annees 1990"),
    ("99 m2 habitables chauffes ","sur 2 niveaux, sous combles perdus"),
    ("Partie non chauffee ","a l'Est : garage / debarras"),
    ("Murs en pierre calcaire 50 cm ","-> forte inertie, patrimoine local"),
    ("Versant Sud-Est, 498 m, rural ","-> apports solaires d'hiver favorables"),
], size=14, gap=Pt(9))
picture(s, IMG["facade2"], Inches(7.3), Inches(1.7), Inches(5.1), Inches(2.6),
        caption="Facade de la maison")
# profil foyer (moyens du MOA - grille coef 1)
box(s, Inches(0.9), Inches(4.95), Inches(11.5), Inches(1.5), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.05), Inches(11), Inches(0.4), [[("Profil et moyens du maitre d'ouvrage", 14, True, VERT)]])
text(s, Inches(1.15), Inches(5.5), Inches(11), Inches(0.9),
     [[("Famille de 4 personnes  -  revenu ~40 000 €/an (categorie « revenus modestes »)  -  "
        "apport personnel de 10 000 €.", 13.5, False, GRIS_TXT)],
      [("Budget pour des travaux importants, a condition qu'ils soient justifies par les economies et soutenus par les aides.", 12.5, False, GRIS_CLR, True)]],
     line_spacing=1.15)
notes(s, "Le batiment est une ancienne ferme savoyarde de la fin du XIXe, 99 m2 chauffes sur deux niveaux sous combles perdus, "
         "avec des murs en pierre de 50 cm - forte inertie mais aucune isolation. Cote foyer, element essentiel pour les aides : "
         "une famille de 4 personnes, un revenu d'environ 40 000 euros par an - ce qui les place en categorie 'revenus modestes' "
         "au sens de l'Anah - et un apport personnel de 10 000 euros. Ils ont un budget pour des travaux importants, "
         "mais veulent qu'ils soient justifies par les economies et bien aides. Orientation Sud-Est : un atout pour les apports solaires d'hiver.")

# ===========================================================================
# 4 - PLANS & COUPE
# ===========================================================================
s = add_slide(); header(s, "1", "Le batiment en plans", "Organisation des espaces et coupe")
picture(s, IMG["plan_rdc"], Inches(0.7), Inches(1.65), Inches(4.1), Inches(3.4), caption="Plan RDC - pieces de vie")
picture(s, IMG["plan_etage"], Inches(4.9), Inches(1.65), Inches(4.0), Inches(3.4), caption="Plan R+1 - espaces de nuit")
picture(s, IMG["coupe"], Inches(9.0), Inches(1.65), Inches(3.6), Inches(3.4), caption="Coupe sur la zone chauffee")
box(s, Inches(0.7), Inches(5.55), Inches(11.9), Inches(1.05), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(0.95), Inches(5.65), Inches(11.4), Inches(0.85),
     [[("Lecture : ", 13, True, VERT),
       ("RDC = pieces de vie, R+1 = chambres. Les combles perdus non chauffes surplombent l'etage : "
        "cette interface favorise les deperditions par la toiture, confirmees plus loin.", 13, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Je m'appuie sur les plans et la coupe fournis. Le RDC regroupe les pieces de vie, l'etage les chambres. "
         "La coupe montre les combles perdus non chauffes au-dessus de l'etage, une interface tres deperditive. "
         "A noter : les plans portent encore les anciennes menuiseries de 1990, mais elles ont ete remplacees en 2019 "
         "par du double vitrage bois pose en tunnel.")

# ===========================================================================
# 5 - BIOCLIMATIQUE
# ===========================================================================
s = add_slide(); header(s, "1", "Analyse bioclimatique du site")
picture(s, IMG["carte"], Inches(0.9), Inches(1.8), Inches(4.6), Inches(3.1), caption="Localisation - versant Sud-Est")
picture(s, IMG["masque"], Inches(5.8), Inches(1.8), Inches(4.6), Inches(3.1), caption="Diagramme de masque solaire lointain")
bullets(s, Inches(10.6), Inches(1.9), Inches(2.3), Inches(3.0), [
    "Altitude 498 m",
    "Orientation Sud-Est",
    "Contexte rural",
    "Masque lointain (relief)",
    "Solaire d'hiver favorable",
], size=12, gap=Pt(9))
box(s, Inches(0.9), Inches(5.3), Inches(11.5), Inches(1.3), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.4), Inches(11.1), Inches(1.1),
     [[("Atout : ", 13, True, VERT), ("l'orientation Sud-Est favorise les apports solaires gratuits en hiver. ", 13, False, GRIS_TXT)],
      [("Vigilance : ", 13, True, ORANGE), ("ces apports peuvent provoquer des surchauffes l'ete -> isolants dephasants + gestion des volets.", 13, False, GRIS_TXT)]],
     line_spacing=1.2)
notes(s, "L'analyse bioclimatique : le batiment est sur un versant Sud-Est a 498 m, en milieu rural. "
         "Le diagramme de masque montre un masque lointain - le relief - qui limite un peu les apports a certaines heures, "
         "mais l'exposition reste bonne. L'orientation Sud-Est est un atout : apports solaires gratuits en hiver. "
         "Le revers : un risque de surchauffe estivale, que je traite par des isolants dephasants et la gestion des volets.")

# ===========================================================================
# 6 - OBJECTIFS & ATTENTES
# ===========================================================================
s = add_slide(); header(s, "1", "Objectifs et attentes du maitre d'ouvrage")
text(s, Inches(0.9), Inches(2.1), Inches(5.6), Inches(0.4), [[("Besoins & objectifs", 16, True, VERT)]])
bullets(s, Inches(0.9), Inches(2.6), Inches(5.6), Inches(4), [
    "Reduire les depenses energetiques",
    "Confort d'hiver (supprimer parois froides)",
    "Confort d'ete (surchauffe sous toiture)",
    "Remplacer a terme la chaudiere fioul",
    "Reduire les emissions de CO2",
    "Valoriser le patrimoine immobilier",
], size=14, gap=Pt(9))
text(s, Inches(6.9), Inches(2.1), Inches(5.6), Inches(0.4), [[("Moyens & contraintes", 16, True, VERT)]])
bullets(s, Inches(6.9), Inches(2.6), Inches(5.6), Inches(4), [
    "Budget + apport 10 000 €, foyer modeste",
    "Investissements justifies par les economies",
    "Conserver le caractere de la ferme",
    "Solutions compatibles avec les murs en pierre",
    "Limiter les risques lies a l'humidite",
    "Mobiliser un maximum d'aides",
], size=14, gap=Pt(9), marker_color=ORANGE)
text(s, Inches(0.9), Inches(1.6), Inches(11.4), Inches(0.4),
     [[("Recueil realise lors de la rencontre avec le maitre d'ouvrage occupant.", 14, False, GRIS_TXT, True)]])
notes(s, "Lors de la rencontre, j'ai recueilli ses objectifs : baisser ses factures, gagner en confort hiver comme ete, "
         "sortir du fioul, reduire son empreinte carbone et valoriser son bien. Cote moyens : un budget complete par un apport "
         "de 10 000 euros, mais un foyer modeste qui veut des investissements justifies par les economies et bien aides. "
         "Ses contraintes orientent le projet : preserver le cachet de la ferme, respecter les murs en pierre et gerer l'humidite - "
         "d'ou une isolation par l'exterieur perspirante.")

# ===========================================================================
# 7 - CONFORT
# ===========================================================================
s = add_slide(); header(s, "1", "Objectifs de confort a atteindre")
make_table(s, Inches(0.9), Inches(1.75), [
    ["Type de confort","Situation actuelle","Amelioration visee"],
    ["Confort d'hiver","Parois froides, ecarts entre pieces","Temperatures homogenes (isolation + regulation)"],
    ["Confort d'ete","Surchauffe sous toiture","Dephasage des isolants biosources"],
    ["Qualite de l'air","Ventilation naturelle non maitrisee","Renouvellement d'air controle (VMC hygro B)"],
    ["Confort visuel","Halogenes energivores (25 %)","Eclairage 100 % LED + lumiere naturelle"],
    ["Confort acoustique","Isolation phonique limitee","Attenuation des bruits exterieurs (ITE)"],
    ["Confort sanitaire","Risque de condensation","Regulation fine, reduction de l'humidite"],
], [Inches(2.3), Inches(4.4), Inches(4.8)], row_h=Inches(0.62), header_size=13, body_size=12, first_col_bold=True)
text(s, Inches(0.9), Inches(6.55), Inches(11.4), Inches(0.5),
     [[("Aucun besoin d'accessibilite / PMR identifie dans cette etude.", 12, False, GRIS_CLR, True)]])
notes(s, "J'ai formule des objectifs de confort sur les quatre dimensions attendues : thermique d'hiver, thermique d'ete, "
         "qualite de l'air et confort visuel. Hiver : fin des parois froides via isolation et regulation. Ete : dephasage des isolants. "
         "Air : VMC hygro B. Visuel : tout LED et valorisation de la lumiere naturelle. J'ajoute l'acoustique, amelioree par l'ITE. "
         "Enfin, j'ai verifie qu'aucun besoin d'accessibilite PMR n'etait a prevoir.")

# ===========================================================================
# 8 - CONSOMMATIONS
# ===========================================================================
s = add_slide(); header(s, "2", "Analyse des consommations", "Factures sur 5 ans")
kpi(s, Inches(0.9), Inches(1.65), Inches(3.6), Inches(1.35), "1 560 L/an", "Fioul (moy.) - chauffage", accent=ORANGE)
kpi(s, Inches(4.7), Inches(1.65), Inches(3.6), Inches(1.35), "6 steres/an", "Bois - poele d'appoint", accent=VERT_CLR)
kpi(s, Inches(8.5), Inches(1.65), Inches(3.6), Inches(1.35), "5 447 kWh/an", "Electricite - ECS, usages", accent=BLEU)
cd = CategoryChartData()
cd.categories = ["19-20","20-21","21-22","22-23","23-24"]
cd.add_series("Fioul (L)", (1500,1800,1700,1400,1400))
cd.add_series("Electricite (kWh)", (5552,5679,5334,5207,5461))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.9), Inches(3.25), Inches(7.0), Inches(2.7), cd)
ch = gf.chart; ch.has_title = True; ch.chart_title.text_frame.text = "Evolution des consommations facturees"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12)
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.BOTTOM; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(9)
ch.plots[0].series[0].format.fill.solid(); ch.plots[0].series[0].format.fill.fore_color.rgb = ORANGE
ch.plots[0].series[1].format.fill.solid(); ch.plots[0].series[1].format.fill.fore_color.rgb = BLEU
box(s, Inches(8.3), Inches(3.25), Inches(4.1), Inches(2.7), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(8.55), Inches(3.35), Inches(3.6), Inches(0.4), [[("Lecture", 13, True, VERT)]])
bullets(s, Inches(8.55), Inches(3.8), Inches(3.6), Inches(2.1), [
    "Chauffage ~80 % de la depense",
    "Forte dependance au fioul (1991)",
    "ECS electrique = poste elec majeur",
], size=12, gap=Pt(7))
# bande perspective
box(s, Inches(0.9), Inches(6.05), Inches(11.5), Inches(0.95), fill=RGBColor(0xFF,0xF3,0xE0), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(6.12), Inches(11.0), Inches(0.8),
     [[("Mise en perspective : ", 12.5, True, ORANGE),
       ("rigueur climatique integree (Savoie, 498 m, zone H1) ; facture reelle ~3 800 €/an (chauffage partiel + appoint bois), "
        "sous l'estimation conventionnelle du DPE ; 535 vs ~250 kWhEP/m2.an en moyenne nationale.", 12.5, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "J'ai analyse les factures sur 5 ans, au-dela des 3 ans minimum attendus. Chauffage : chaudiere fioul de 1991 + poele bois. "
         "Moyennes : 1 560 L de fioul, 6 steres, 5 447 kWh d'electricite dont l'ECS. Le chauffage pese environ 80 % de la depense. "
         "J'ai integre la rigueur climatique - zone H1, 498 m, donc des besoins eleves - verifie la coherence entre factures et DPE, "
         "et compare a la moyenne nationale : 535 contre environ 250 kWh primaire au m2, soit plus du double. Une vraie passoire thermique.")

# ===========================================================================
# 9 - ENVELOPPE
# ===========================================================================
s = add_slide(); header(s, "2", "Diagnostic de l'enveloppe thermique")
make_table(s, Inches(0.9), Inches(1.7), [
    ["Element","Composition","Observation"],
    ["Murs exterieurs","Pierre calcaire 50 cm","Forte inertie, faible isolation"],
    ["Toiture / combles","8 cm laine minerale ancienne","Isolation insuffisante"],
    ["Menuiseries","Double vitrage bois 4/16/4 Argon (2019)","Bon etat, performantes"],
    ["Plancher bas","Dalle beton sur terre-plein","Non isole -> deperditions"],
    ["Ponts thermiques","Jonctions des parois","Pertes importantes"],
    ["Etancheite a l'air","Non maitrisee (entrees d'air)","Infiltrations parasites"],
], [Inches(2.2), Inches(3.4), Inches(2.4)], row_h=Inches(0.55), header_size=12, body_size=11.5, first_col_bold=True)
picture(s, IMG["menuiserie"], Inches(9.2), Inches(1.7), Inches(3.2), Inches(2.7), caption="Menuiseries bois posees en 2019")
box(s, Inches(9.2), Inches(4.75), Inches(3.2), Inches(1.55), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(9.4), Inches(4.85), Inches(2.85), Inches(1.4),
     [[("A retenir", 13, True, VERT)], [("Fenetres deja renovees ->", 12, False, GRIS_TXT)], [("priorite : murs + toiture", 13, True, VERT)]], line_spacing=1.15)
notes(s, "L'enveloppe poste par poste. Murs pierre 50 cm : inertie mais pas d'isolation. Combles : seulement 8 cm de laine ancienne. "
         "Menuiseries : double vitrage bois argon de 2019, performantes. Plancher sur terre-plein non isole. Etancheite a l'air non maitrisee. "
         "Conclusion : comme les fenetres sont deja bonnes, je concentre l'isolation sur les murs et la toiture.")

# ===========================================================================
# 10 - SYSTEMES
# ===========================================================================
s = add_slide(); header(s, "2", "Diagnostic des systemes existants", "Chauffage, ECS, ventilation")
make_table(s, Inches(0.9), Inches(1.7), [
    ["Equipement","Description","Limite principale"],
    ["Chaudiere fioul","Basse temperature, 1991","Ancienne, fossile, sans sonde exterieure"],
    ["Radiateurs fonte","Haute T, sans robinet thermo.","Pas de regulation piece par piece"],
    ["Poele a bois","Buches 6 kW (2010)","Pas de label Flamme Verte, non etanche"],
    ["Ballon ECS","Electrique 200 L, hors volume chauffe","Pertes thermiques, conso elec."],
    ["Ventilation","Naturelle (pas de VMC)","Debits non maitrises, pertes"],
], [Inches(2.2), Inches(3.5), Inches(2.5)], row_h=Inches(0.58), header_size=12, body_size=11.5, first_col_bold=True)
picture(s, IMG["chaudiere"], Inches(9.4), Inches(1.7), Inches(1.45), Inches(2.55), caption="Chaudiere fioul (1991)")
picture(s, IMG["ballon"], Inches(11.0), Inches(1.7), Inches(1.45), Inches(2.55), caption="Ballon ECS")
box(s, Inches(0.9), Inches(5.45), Inches(11.5), Inches(0.95), fill=RGBColor(0xFF,0xF3,0xE0), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.55), Inches(11.0), Inches(0.75),
     [[("Constat : ", 13, True, ORANGE), ("equipements vieillissants, regulation rudimentaire, absence de VMC -> leviers majeurs d'economies.", 13, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Les systemes : chaudiere fioul de 1991 sans sonde exterieure, alimentant des radiateurs fonte haute temperature sans robinets "
         "thermostatiques - donc pas de reglage piece par piece. Poele bois 6 kW non labellise. ECS par vieux ballon electrique hors volume "
         "chauffe, source de pertes. Aucune VMC. Ces trois points - chauffage, regulation, ventilation - sont mes principaux leviers.")

# ===========================================================================
# 11 - ECLAIRAGE / QAI / ACOUSTIQUE
# ===========================================================================
s = add_slide(); header(s, "2", "Eclairage, qualite de l'air & acoustique")
def carte(s, l, t, titre, lignes, accent):
    box(s, l, t, Inches(3.7), Inches(4.3), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    box(s, l, t, Inches(3.7), Inches(0.6), fill=accent, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, l, t, Inches(3.7), Inches(0.6), [[(titre, 15, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    bullets(s, l + Inches(0.2), t + Inches(0.8), Inches(3.35), Inches(3.4), lignes, size=12.5, gap=Pt(8))
carte(s, Inches(0.9), Inches(1.7), "Eclairage / confort visuel", [
    ("Existant : ","25 % halogenes + 75 % LED, 200 W"),
    ("Propose : ","passage 100 % LED basse conso"),
    ("Valoriser ","la lumiere naturelle (Sud-Est)"),
], ORANGE)
carte(s, Inches(4.8), Inches(1.7), "Qualite de l'air (QAI)", [
    ("Existant : ","ventilation naturelle, debits non maitrises"),
    ("Risques : ","humidite, condensation, polluants"),
    ("Propose : ","VMC hygroreglable de type B"),
], VERT_CLR)
carte(s, Inches(8.7), Inches(1.7), "Confort acoustique", [
    ("Sources : ","bruits exterieurs (route, voisinage)"),
    ("Existant : ","isolation phonique limitee"),
    ("Propose : ","l'ITE ameliore aussi l'acoustique"),
], BLEU)
notes(s, "Trois conforts souvent oublies mais notes. Eclairage : 25 % d'halogenes energivores, 75 % de LED, 200 W ; je preconise le tout LED "
         "et la lumiere naturelle. QAI : la ventilation naturelle ne maitrise pas les debits et favorise l'humidite ; je propose une VMC hygro B. "
         "Acoustique : les bruits exterieurs sont mal filtres, or l'isolation par l'exterieur ameliore aussi l'affaiblissement acoustique.")

# ===========================================================================
# 12 - DEPERDITIONS + DPE EXISTANT (merged)
# ===========================================================================
s = add_slide(); header(s, "3", "Deperditions & DPE de l'existant", "Calcul thermique : ou part la chaleur")
cd = CategoryChartData()
cd.categories = ["Murs","Toiture","Ventilation","Ponts therm.","Fenetres","Plancher"]
cd.add_series("Deperditions", (42,20,20,10,4,4))
gf = s.shapes.add_chart(XL_CHART_TYPE.PIE, Inches(0.5), Inches(1.7), Inches(5.6), Inches(4.6), cd)
ch = gf.chart; ch.has_title = False
ch.has_legend = True; ch.legend.position = XL_LEGEND_POSITION.RIGHT; ch.legend.include_in_layout = False; ch.legend.font.size = Pt(10)
pl = ch.plots[0]; pl.has_data_labels = True
pl.data_labels.show_value = True; pl.data_labels.number_format = '0"%"'; pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(11); pl.data_labels.font.bold = True; pl.data_labels.font.color.rgb = BLANC
pl.data_labels.position = XL_LABEL_POSITION.INSIDE_END
for i, c in enumerate([ROUGE, ORANGE, BLEU, RGBColor(0x8E,0x24,0xAA), VERT_CLR, GRIS_CLR]):
    pl.series[0].points[i].format.fill.solid(); pl.series[0].points[i].format.fill.fore_color.rgb = c
# DPE existant a droite
dpe_label(s, Inches(6.7), Inches(1.7), "G", "Energie", scale_h=Inches(0.32), base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=12)
dpe_label(s, Inches(8.9), Inches(1.7), "G", "Climat", scale_h=Inches(0.32), base_w=Inches(0.55), step=Inches(0.16), letter_size=12, label_size=12)
make_table(s, Inches(10.6), Inches(1.95), [
    ["Indicateur","Valeur"],
    ["Conso","535 kWhEP/m2"],
    ["CO2","156 kg/m2"],
    ["Cout/an","7 100-9 610 €"],
    ["Ubat","2,03 W/m2K"],
    ["P. chauff.","21,3 kW"],
], [Inches(1.0), Inches(1.6)], row_h=Inches(0.42), header_size=10.5, body_size=10.5)
box(s, Inches(6.7), Inches(4.5), Inches(5.9), Inches(1.8), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(6.95), Inches(4.62), Inches(5.5), Inches(1.6),
     [[("Diagnostic : classe G / G", 15, True, ROUGE)],
      [("Murs + toiture + ventilation = plus de 80 % des pertes.", 12.5, False, GRIS_TXT)],
      [("Ubat ~4x la reference (0,47) : l'enveloppe est le 1er probleme.", 12.5, False, GRIS_TXT)],
      [("-> renovation performante pleinement justifiee.", 12.5, True, VERT)]], line_spacing=1.12)
notes(s, "Le coeur du diagnostic. A gauche, le calcul des deperditions : 42 % par les murs, 20 % toiture, 20 % ventilation, "
         "10 % ponts thermiques, 4 % fenetres et plancher. A droite, le DPE : classe G sur les deux axes - 535 kWh primaire au m2, "
         "156 kg de CO2, facture de 7 100 a 9 610 euros par an. Le Ubat de 2,03 vaut environ quatre fois la reference. "
         "Murs, toiture et ventilation cumulent plus de 80 % des pertes : c'est ce qui guide mes priorites de travaux.")

# ===========================================================================
# 13 - SCENARIO 1 (D)
# ===========================================================================
s = add_slide(); header(s, "4", "Scenario 1 - Renovation performante par etapes", "Etape 1 : l'enveloppe (chauffage conserve)")
text(s, Inches(0.9), Inches(1.55), Inches(11.4), Inches(0.4),
     [[("1re etape ciblee enveloppe : traite 2 postes d'isolation (murs + toiture) et fait gagner 3 classes (G -> D).", 13, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.05), [
    ["Poste","Solution - etape 1"],
    ["Murs","ITE laine de bois 200 mm"],
    ["Combles","Ouate de cellulose 400 mm"],
    ["Ventilation","VMC hygroreglable type B"],
    ["ECS","Chauffe-eau thermodynamique"],
    ["Chauffage","Fioul conserve (etape ulterieure)"],
], [Inches(1.9), Inches(5.2)], row_h=Inches(0.5), header_size=13, body_size=12, first_col_bold=True)
dpe_label(s, Inches(8.8), Inches(1.9), "C", "Energie", scale_h=Inches(0.27), base_w=Inches(0.5), step=Inches(0.15), letter_size=11, label_size=11)
dpe_label(s, Inches(10.8), Inches(1.9), "D", "Climat", scale_h=Inches(0.27), base_w=Inches(0.5), step=Inches(0.15), letter_size=11, label_size=11)
dpe_badge(s, Inches(11.3), Inches(4.35), "D", w=Inches(0.9), h=Inches(0.9))
text(s, Inches(10.5), Inches(5.3), Inches(2.5), Inches(0.3), [[("DPE resultant", 11, True, GRIS_TXT)]], align=PP_ALIGN.CENTER)
box(s, Inches(0.9), Inches(5.0), Inches(9.3), Inches(1.6), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.1), Inches(9), Inches(0.4), [[("Avantages & coherence des etapes", 14, True, VERT)]])
bullets(s, Inches(1.15), Inches(5.55), Inches(4.5), Inches(1.0), [
    "Traite d'abord les 2 postes de pertes majeurs",
    "Prepare et facilite le futur changement de chauffage",
    "Investissement maitrise : ~42 500 €",
], size=11.5, gap=Pt(4))
bullets(s, Inches(5.8), Inches(5.55), Inches(4.3), Inches(1.0), [
    "Confort d'hiver et d'ete ameliores",
    "Inertie des murs en pierre conservee",
    "Limite : le fioul plafonne le DPE a D",
], size=11.5, gap=Pt(4))
notes(s, "Mon premier scenario est une renovation performante PAR ETAPES. L'etape 1 cible l'enveloppe : ITE laine de bois 200 mm, "
         "combles ouate 400 mm, VMC hygro B, et je remplace le vieux ballon par un chauffe-eau thermodynamique. La chaudiere fioul est conservee a ce stade. "
         "C'est coherent avec l'attendu : cette etape traite les DEUX premiers postes d'isolation - murs et toiture - et fait gagner 3 classes, de G a D. "
         "En reduisant d'abord les besoins, on prepare le changement de chauffage a l'etape suivante, qu'on pourra dimensionner plus petit. "
         "Sa limite, et c'est important : meme bien isole, le fioul plafonne le DPE a D a cause de ses emissions de CO2. "
         "Reglementation : l'ITE necessite une declaration prealable en mairie. Investissement : environ 42 500 euros.")

# ===========================================================================
# 14 - SCENARIO 2 (B)
# ===========================================================================
s = add_slide(); header(s, "4", "Scenario 2 - Renovation performante globale", "Enveloppe + sortie du fioul")
text(s, Inches(0.9), Inches(1.5), Inches(11.4), Inches(0.4),
     [[("Toute l'isolation du scenario 1 + remplacement du fioul. Deux solutions bas carbone comparees :", 13, False, GRIS_TXT, True)]])
make_table(s, Inches(0.9), Inches(2.0), [
    ["Critere","PAC Air/Eau","Chaudiere granules"],
    ["Energie primaire","Plus faible (elec/COP)","Coef. 1 (biomasse)"],
    ["Emissions CO2","Faibles","Tres faibles"],
    ["Radiateurs fonte haute T","Moins adaptee","Tres adaptee"],
    ["Bati ancien savoyard","Bonne","Tres adaptee"],
], [Inches(2.7), Inches(2.4), Inches(2.4)], row_h=Inches(0.5), header_size=12, body_size=11.5, first_col_bold=True)
dpe_label(s, Inches(8.9), Inches(1.9), "B", "Energie", scale_h=Inches(0.27), base_w=Inches(0.5), step=Inches(0.15), letter_size=11, label_size=11)
dpe_label(s, Inches(10.9), Inches(1.9), "A", "Climat", scale_h=Inches(0.27), base_w=Inches(0.5), step=Inches(0.15), letter_size=11, label_size=11)
dpe_badge(s, Inches(11.4), Inches(4.3), "B", w=Inches(0.9), h=Inches(0.9))
text(s, Inches(10.6), Inches(5.25), Inches(2.5), Inches(0.3), [[("DPE resultant", 11, True, GRIS_TXT)]], align=PP_ALIGN.CENTER)
box(s, Inches(0.9), Inches(5.0), Inches(7.6), Inches(1.5), fill=VERT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(5.1), Inches(7.1), Inches(1.3),
     [[("Solution retenue : chaudiere a granules 12 kW (sans silo)", 14, True, BLANC)],
      [("Tremie integree, conserve les radiateurs fonte, energie renouvelable locale, approvisionnement facile en Savoie.", 11.5, False, RGBColor(0xC8,0xE6,0xC9))]], line_spacing=1.05)
text(s, Inches(0.9), Inches(6.55), Inches(11), Inches(0.4),
     [[("Reglementation : declaration prealable (ITE), conformite DTU et criteres d'aides respectes.", 11, False, GRIS_CLR, True)]])
notes(s, "Mon second scenario est une renovation GLOBALE : toute l'isolation du scenario 1 en une fois, plus le remplacement du chauffage. "
         "J'ai compare deux solutions bas carbone. La PAC air/eau donne la meilleure energie primaire, mais elle est moins efficace sur les radiateurs "
         "fonte HAUTE temperature deja en place. La chaudiere a granules, elle, est tres adaptee a ces radiateurs et au bati ancien, avec une energie "
         "renouvelable locale. Je la retiens, AVEC tremie integree pour eviter le silo. Resultat DPE : energie B, climat A - le granule fait basculer "
         "l'etiquette en B. C'est tout l'interet de sortir du fioul. Investissement : environ 63 000 euros.")

# ===========================================================================
# 15 - OPTIMISATION SYSTEMES
# ===========================================================================
s = add_slide(); header(s, "5", "Optimisation des systemes", "Regulation du chauffage & production d'ECS")
box(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(4.55), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(0.6), fill=VERT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(0.9), Inches(1.75), Inches(5.7), Inches(0.6), [[("Regulation du chauffage", 16, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
bullets(s, Inches(1.15), Inches(2.55), Inches(5.25), Inches(3.6), [
    ("Sonde de temperature exterieure ","-> pilotage par loi d'eau"),
    ("Robinets thermostatiques ","sur les radiateurs fonte (regulation piece par piece)"),
    ("Thermostat programmable ","(reduit en absence / nuit)"),
    ("Rendement global ","ameliore : generateur recent + emetteurs regules"),
], size=13.5, gap=Pt(11))
box(s, Inches(6.9), Inches(1.75), Inches(5.5), Inches(4.55), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
box(s, Inches(6.9), Inches(1.75), Inches(5.5), Inches(0.6), fill=BLEU, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(6.9), Inches(1.75), Inches(5.5), Inches(0.6), [[("Production d'eau chaude (ECS)", 16, True, BLANC)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
bullets(s, Inches(7.15), Inches(2.55), Inches(5.05), Inches(3.6), [
    ("Existant : ","vieux ballon elec. 200 L hors volume chauffe (pertes)"),
    ("Solution : ","chauffe-eau thermodynamique (COP ~3, conso /3)"),
    ("Ballon repositionne ","dans le volume chauffe"),
    ("Resultat : ","poste ECS fortement reduit dans les 2 scenarios"),
], size=13.5, gap=Pt(11))
notes(s, "Cette diapo repond a un attendu fortement coefficiente : adapter et optimiser les equipements. Cote regulation, le diagnostic a montre "
         "l'absence de sonde exterieure et de robinets thermostatiques. Je preconise : une sonde exterieure pour piloter par loi d'eau, des robinets "
         "thermostatiques sur les radiateurs fonte, et un thermostat programmable - on ameliore le rendement global. Cote eau chaude : le vieux ballon "
         "electrique hors volume chauffe est un gouffre ; je propose un chauffe-eau thermodynamique, COP environ 3, qui divise la conso par trois, "
         "et je le replace dans le volume chauffe. Ce poste ECS optimise est integre dans les deux scenarios.")

# ===========================================================================
# 16 - DPE DES SCENARIOS - LE CALCUL
# ===========================================================================
s = add_slide(); header(s, "5", "DPE des scenarios - le calcul", "Methode 3CL : energie primaire + CO2")
# hypotheses
box(s, Inches(0.9), Inches(1.7), Inches(3.5), Inches(4.6), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.1), Inches(1.8), Inches(3.2), Inches(0.4), [[("Hypotheses", 13, True, VERT)]])
text(s, Inches(1.1), Inches(2.25), Inches(3.2), Inches(4.0),
     [[("Besoin chauffage apres travaux : 7 020 kWh/an (-55 %)", 10.5, False, GRIS_TXT)],
      [("", 4, False, VERT)],
      [("Rendements : fioul 1991 ~72 %, granules ~90 %", 10.5, False, GRIS_TXT)],
      [("", 4, False, VERT)],
      [("ECS thermodynamique (COP 3), VMC + LED", 10.5, False, GRIS_TXT)],
      [("", 4, False, VERT)],
      [("Energie primaire : elec x2,3 ; fioul/granules x1", 10.5, False, GRIS_TXT)],
      [("", 4, False, VERT)],
      [("CO2 (kg/kWh) : fioul 0,324 ; granules 0,030 ; elec 0,064", 10.5, False, GRIS_TXT)]], line_spacing=1.1)
# table energie
text(s, Inches(4.7), Inches(1.65), Inches(7.7), Inches(0.35), [[("Energie primaire (kWhEP/m2.an)", 12.5, True, VERT)]])
make_table(s, Inches(4.7), Inches(2.05), [
    ["Poste","Existant","Sc. 1","Sc. 2"],
    ["Chauffage","405","98","79"],
    ["ECS","95","19","19"],
    ["Auxiliaires + eclairage","35","11","11"],
    ["Total","535","128","109"],
    ["Classe energie","G","C","B"],
], [Inches(3.1), Inches(1.55), Inches(1.55), Inches(1.55)], row_h=Inches(0.36), header_size=11.5, body_size=11,
   first_col_bold=True, highlight_rows=[4,5], highlight_fill=RGBColor(0xD7,0xE9,0xD0))
# table CO2
text(s, Inches(4.7), Inches(4.45), Inches(7.7), Inches(0.35), [[("Emissions de CO2 (kgCO2/m2.an)", 12.5, True, VERT)]])
make_table(s, Inches(4.7), Inches(4.85), [
    ["Poste","Existant","Sc. 1","Sc. 2"],
    ["Chauffage","150","32","2"],
    ["ECS + auxiliaires","6","1","1"],
    ["Total","156","33","3"],
    ["Classe climat","G","D","A"],
], [Inches(3.1), Inches(1.55), Inches(1.55), Inches(1.55)], row_h=Inches(0.36), header_size=11.5, body_size=11,
   first_col_bold=True, highlight_rows=[3,4], highlight_fill=RGBColor(0xD7,0xE9,0xD0))
# resultat band
box(s, Inches(0.9), Inches(6.5), Inches(11.5), Inches(0.55), fill=ANTHRA, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(6.5), Inches(11), Inches(0.55),
     [[("Classe DPE (la moins bonne des 2 axes) :   Existant G   ->   Scenario 1 D   ->   Scenario 2 B", 14, True, BLANC)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "C'est la diapo sur laquelle j'insiste. Je calcule le DPE selon la logique 3CL : energie primaire d'un cote, emissions de CO2 de l'autre, "
         "et la classe finale est la MOINS bonne des deux. J'ancre tout sur mon etude thermique : un besoin de chauffage ramene a 7 020 kWh par an apres isolation. "
         "En energie primaire, les deux scenarios sont proches : le scenario 1 atteint C (128), le scenario 2 B (109) grace au meilleur rendement de la chaudiere granules. "
         "Mais c'est le CO2 qui fait la difference : avec le fioul conserve, le scenario 1 reste a 33 kg, soit classe D - le fioul plafonne. "
         "Avec le granule, le scenario 2 tombe a 3 kg, classe A. Resultat : on passe de G a D avec le scenario par etapes, et a B avec le scenario global. "
         "Le message cle : a isolation egale, c'est le choix de l'energie de chauffage qui determine l'etiquette finale.")

# ===========================================================================
# 17 - DIMENSIONNEMENT + MATERIAUX
# ===========================================================================
s = add_slide(); header(s, "5", "Dimensionnement & materiaux", "Calculs et choix techniques")
box(s, Inches(0.9), Inches(1.7), Inches(5.7), Inches(2.3), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.1), Inches(1.8), Inches(5.3), Inches(2.2),
     [[("Isolants  (R = e / lambda)", 13, True, VERT)], [("",4,False,VERT)],
      [("Murs - laine de bois 200 mm (l=0,038) :", 11.5, True, GRIS_TXT)],
      [("R = 0,20 / 0,038 = 5,26 m2.K/W", 12.5, False, BLEU)], [("",3,False,VERT)],
      [("Combles - ouate 400 mm (l=0,039) :", 11.5, True, GRIS_TXT)],
      [("R = 0,40 / 0,039 = 10,26 m2.K/W", 12.5, False, BLEU)]], line_spacing=1.05)
box(s, Inches(6.8), Inches(1.7), Inches(5.6), Inches(2.3), fill=BLANC, line=GRIS_CLR, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(7.0), Inches(1.8), Inches(5.2), Inches(2.2),
     [[("Puissance de chauffage", 13, True, VERT)], [("",4,False,VERT)],
      [("Reduction des besoins : -55 % (isolation + VMC)", 11.5, True, GRIS_TXT)],
      [("P = 21,3 x (1 - 0,55) = 9,6 kW", 12.5, False, BLEU)], [("",3,False,VERT)],
      [("Avec marge de securite :", 11.5, True, GRIS_TXT)],
      [("-> chaudiere a granules de 12 kW", 13, True, VERT)]], line_spacing=1.05)
make_table(s, Inches(0.9), Inches(4.25), [
    ["Granules / VMC","Valeur"],
    ["Conso granules estimee","~1,5 t/an"],
    ["Stockage","Tremie integree (sans silo)"],
    ["VMC hygro B - debit max","180 m3/h"],
], [Inches(3.0), Inches(2.7)], row_h=Inches(0.44), header_size=12, body_size=11)
box(s, Inches(6.8), Inches(4.25), Inches(5.6), Inches(2.05), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(7.0), Inches(4.35), Inches(5.2), Inches(0.4), [[("Materiaux biosources", 13, True, VERT)]])
bullets(s, Inches(7.0), Inches(4.8), Inches(5.2), Inches(1.4), [
    ("Laine de bois (murs) & ouate de cellulose (combles)", ""),
    ("Faible impact carbone, excellent dephasage (confort d'ete)", ""),
    ("Murs perspirants -> gestion de l'humidite du bati ancien", ""),
], size=11.5, gap=Pt(5))
notes(s, "Le dimensionnement. Pour l'isolation : R = epaisseur / lambda donne R = 5,26 pour les murs et 10,26 pour les combles, "
         "conformes a une renovation performante. Pour le chauffage : 21,3 kW initiaux, reduits de 55 % par l'isolation et la VMC -> environ 10 kW, "
         "donc une chaudiere de 12 kW avec marge. La conso est d'environ 1,5 tonne de granules par an ; j'ai SUPPRIME le silo au profit d'une tremie integree. "
         "La VMC hygro B est dimensionnee a 180 m3/h. Cote materiaux, j'ai choisi des biosources - laine de bois et ouate - pour le faible carbone, "
         "le dephasage qui apporte le confort d'ete, et la perspirance indispensable sur des murs en pierre.")

# ===========================================================================
# 18 - CHIFFRAGE
# ===========================================================================
s = add_slide(); header(s, "6", "Chiffrage des travaux", "Prix fourni-pose TTC (marques reelles, main d'oeuvre comprise)")
text(s, Inches(0.9), Inches(1.7), Inches(5.6), Inches(0.4), [[("Scenario 1 - 42 500 €", 15, True, BLEU)]])
make_table(s, Inches(0.9), Inches(2.15), [
    ["Poste / marque","TTC"],
    ["ITE laine de bois 200 mm (Steico + enduit)","30 000 €"],
    ["Combles ouate 400 mm (Ouateco)","3 500 €"],
    ["Etancheite a l'air + ponts thermiques","2 000 €"],
    ["VMC hygro B (Aldes / Atlantic)","3 500 €"],
    ["ECS thermodynamique (Atlantic Calypso)","3 500 €"],
    ["Total","42 500 €"],
], [Inches(4.4), Inches(1.5)], row_h=Inches(0.5), header_size=12, body_size=11, highlight_rows=[6], highlight_fill=RGBColor(0xDC,0xE9,0xF7))
text(s, Inches(6.9), Inches(1.7), Inches(5.6), Inches(0.4), [[("Scenario 2 - 63 000 €", 15, True, VERT)]])
make_table(s, Inches(6.9), Inches(2.15), [
    ["Poste / marque","TTC"],
    ["Travaux du scenario 1 (enveloppe + VMC + ECS)","42 500 €"],
    ["Chaudiere granules 12 kW (OkoFEN / Hargassner)","15 000 €"],
    ["Ballon tampon + hydraulique + tubage fumees","4 000 €"],
    ["Depose chaudiere fioul + cuve","1 500 €"],
    ["Total","63 000 €"],
], [Inches(4.4), Inches(1.5)], row_h=Inches(0.5), header_size=12, body_size=11, highlight_rows=[5], highlight_fill=RGBColor(0xD7,0xE9,0xD0))
box(s, Inches(0.9), Inches(6.0), Inches(11.5), Inches(0.85), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(6.08), Inches(11.0), Inches(0.7),
     [[("Prix fourni-pose TTC (TVA 5,5 %), main d'oeuvre et echafaudage compris. La pose represente ~40 % du cout de l'ITE.", 12.5, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Le chiffrage, sur la base de prix de marche par type de travaux et de marques reelles, en fourni-pose TTC main d'oeuvre comprise. "
         "Scenario 1, 42 500 euros : le gros poste est l'ITE laine de bois - type Steico avec enduit - a 30 000 euros, dont environ 40 % de main d'oeuvre "
         "et l'echafaudage ; puis les combles en ouate Ouateco, l'etancheite a l'air, la VMC Aldes ou Atlantic, et le chauffe-eau thermodynamique Atlantic Calypso. "
         "Scenario 2 : on ajoute la chaudiere granules ÖkoFEN ou Hargassner a 15 000 euros, le ballon tampon et le tubage, et la depose de la cuve fioul - "
         "soit 63 000 euros au total. Plus de silo. L'ecart de 20 500 euros correspond au changement de chauffage.")

# ===========================================================================
# 19 - FINANCEMENT
# ===========================================================================
s = add_slide(); header(s, "6", "Plan de financement", "Foyer modeste : aides, apport et reste a charge")
make_table(s, Inches(0.9), Inches(1.85), [
    ["Element financier","Scenario 1","Scenario 2"],
    ["Cout total des travaux TTC","42 500 €","63 000 €"],
    ["MaPrimeRenov' (estimation prudente)","- 15 000 €","- 24 000 €"],
    ["Certificats d'economies d'energie (CEE)","- 2 500 €","- 4 000 €"],
    ["Aides locales eventuelles","- 2 500 €","- 2 000 €"],
    ["Reste a charge","22 500 €","33 000 €"],
    ["- Apport personnel","- 10 000 €","- 10 000 €"],
    ["A financer (eco-PTZ a 0 %)","12 500 €","23 000 €"],
], [Inches(5.3), Inches(3.1), Inches(3.1)], row_h=Inches(0.46), header_size=13, body_size=12,
   first_col_bold=True, highlight_rows=[5,7], highlight_fill=RGBColor(0xD7,0xE9,0xD0))
box(s, Inches(0.9), Inches(5.95), Inches(11.5), Inches(0.95), fill=VERT_LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(6.02), Inches(11.0), Inches(0.8),
     [[("Estimation prudente des aides (~20 000 € et ~30 000 €). Apres apport, le solde (12 500 a 23 000 €) est finance par un "
        "eco-PTZ a 0 % -> projet dans le budget de la famille.", 12.5, False, GRIS_TXT)]],
     anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Le financement, avec une estimation PRUDENTE des aides - plus realiste que les taux maximaux. Pour ce foyer de 4 personnes, "
         "MaPrimeRenov' et les CEE couvrent environ 20 000 euros au scenario 1 et 30 000 euros au scenario 2. Le reste a charge s'eleve donc a "
         "22 500 euros pour le scenario 1 et 33 000 euros pour le scenario 2 - des montants coherents avec ce qu'observent des projets comparables. "
         "On deduit l'apport de 10 000 euros, et le solde - 12 500 a 23 000 euros - est finance par un eco-PTZ a taux zero. "
         "Le projet reste dans le budget : la mensualite de l'eco-PTZ est largement couverte par les economies d'energie.")

# ===========================================================================
# 20 - COUT GLOBAL & ROI
# ===========================================================================
s = add_slide(); header(s, "6", "Analyse en cout global & rentabilite")
cd = CategoryChartData()
cd.categories = ["Etat initial","Scenario 1","Scenario 2"]
cd.add_series("Cout global sur 30 ans (€)", (252000, 188500, 169000))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.9), Inches(1.75), Inches(6.6), Inches(3.4), cd)
ch = gf.chart; ch.has_title = True; ch.chart_title.text_frame.text = "Cout global 30 ans (travaux + energie, +5 %/an)"
ch.chart_title.text_frame.paragraphs[0].font.size = Pt(12); ch.has_legend = False
pl = ch.plots[0]; pl.has_data_labels = True
pl.data_labels.number_format = '# ##0 "€"'; pl.data_labels.number_format_is_linked = False
pl.data_labels.font.size = Pt(10); pl.data_labels.font.bold = True
for i, c in enumerate([ROUGE, BLEU, VERT]):
    pl.series[0].points[i].format.fill.solid(); pl.series[0].points[i].format.fill.fore_color.rgb = c
text(s, Inches(7.9), Inches(1.7), Inches(4.5), Inches(0.4), [[("Factures reelles & ROI", 13, True, VERT)]])
make_table(s, Inches(7.9), Inches(2.2), [
    ["Situation","€/an","€/mois"],
    ["Avant travaux","3 800","317"],
    ["Scenario 1","2 200","183"],
    ["Scenario 2","1 600","133"],
], [Inches(1.9), Inches(1.3), Inches(1.3)], row_h=Inches(0.47), header_size=11.5, body_size=11)
make_table(s, Inches(7.9), Inches(4.55), [
    ["ROI (sur reste a charge)","Sc. 1","Sc. 2"],
    ["Reste a charge","22 500 €","33 000 €"],
    ["Economies/an","1 600 €","2 200 €"],
    ["Amortissement","~14 ans","~15 ans"],
], [Inches(2.3), Inches(1.1), Inches(1.1)], row_h=Inches(0.47), header_size=11, body_size=11)
notes(s, "L'analyse economique se base sur la facture REELLE du foyer - environ 3 800 euros par an - et non sur le cout conventionnel du DPE, "
         "qui le surestime. Apres travaux, la facture tombe a 2 200 euros au scenario 1 et 1 600 euros au scenario 2, soit des economies de "
         "1 600 a 2 200 euros par an. Sur le reste a charge, le retour sur investissement est d'environ 14 ans pour le scenario 1 et 15 ans pour le scenario 2 - "
         "coherent avec des projets comparables. Pour le cout global, j'integre une hausse du prix de l'energie de 5 % par an, comme attendu : "
         "sur 30 ans, ne rien faire coute 252 000 euros, le scenario 1 188 500, et le scenario 2 169 000. Malgre un investissement plus eleve, "
         "le scenario 2 reste le plus avantageux sur la duree.")

# ===========================================================================
# 21 - SYNTHESE
# ===========================================================================
s = add_slide(); header(s, "7", "Synthese comparative des scenarios")
make_table(s, Inches(0.9), Inches(1.8), [
    ["Critere","Etat initial","Scenario 1 (par etapes)","Scenario 2 (global)"],
    ["Classe DPE","G","D","B"],
    ["Energie / Climat","G / G","C / D","B / A"],
    ["Chauffage","Fioul (1991)","Fioul conserve","Granules (sans silo)"],
    ["Travaux TTC","-","42 500 €","63 000 €"],
    ["Aides estimees","-","~20 000 €","~30 000 €"],
    ["Reste a charge","-","22 500 €","33 000 €"],
    ["Cout energie / an (reel)","3 800 €","2 200 €","1 600 €"],
    ["Cout global 30 ans","252 000 €","188 500 €","169 000 €"],
    ["Amortissement","-","~14 ans","~15 ans"],
], [Inches(2.9), Inches(2.4), Inches(3.1), Inches(3.1)], row_h=Inches(0.44), header_size=12.5, body_size=11.5,
   first_col_bold=True, highlight_rows=[1], highlight_fill=RGBColor(0xD7,0xE9,0xD0))
notes(s, "Cette synthese recapitule tout. On lit la progression du DPE : de G a D avec le scenario par etapes, jusqu'a B avec le scenario global. "
         "Le scenario 2 coute plus cher a l'achat mais affiche le cout annuel le plus bas, le cout global le plus faible et l'amortissement le plus court. "
         "C'est la base de ma recommandation.")

# ===========================================================================
# 22 - CONCLUSION + SOBRIETE
# ===========================================================================
s = add_slide(); set_bg(s, VERT)
box(s, 0, 0, SW, Inches(1.3), fill=VERT_CLR)
text(s, Inches(0.9), Inches(0.3), Inches(11.5), Inches(0.8), [[("Conclusion & recommandation", 30, True, BLANC)]], anchor=MSO_ANCHOR.MIDDLE)
# reco
box(s, Inches(0.9), Inches(1.6), Inches(7.4), Inches(4.0), fill=BLANC, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(1.15), Inches(1.75), Inches(7.0), Inches(0.5), [[("-> Je recommande le Scenario 2 (global)", 19, True, VERT)]])
bullets(s, Inches(1.15), Inches(2.45), Inches(7.0), Inches(3.0), [
    ("Performance maximale : ","DPE de G a B (energie B / climat A)"),
    ("Sortie du fioul : ","energie renouvelable et locale (granules)"),
    ("Meilleure rentabilite : ","cout global le plus bas, ROI ~15 ans"),
    ("Compatible avec le bati : ","ITE biosourcee + radiateurs fonte conserves"),
    ("Dans le budget : ","reste a charge ~33 000 €, aides ~30 000 € + apport"),
], size=13, gap=Pt(8))
# sobriete
box(s, Inches(8.5), Inches(1.6), Inches(3.9), Inches(4.0), fill=ANTHRA, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, Inches(8.7), Inches(1.72), Inches(3.5), Inches(0.4), [[("Conseils de sobriete", 14, True, BLANC)]])
bullets(s, Inches(8.7), Inches(2.2), Inches(3.5), Inches(3.3), [
    "Chauffer 19-20 °C, reduire en absence",
    "Fermer les volets la nuit en hiver",
    "Entretien chaudiere & VMC",
    "Eteindre les veilles, suivi des consos",
], size=11.5, gap=Pt(7), marker_color=RGBColor(0xA5,0xD6,0xA7))
text(s, Inches(0.9), Inches(5.85), Inches(11.5), Inches(0.5),
     [[("Budget contraint ? Le Scenario 1 reste une excellente 1re etape (G -> D), completee plus tard par le chauffage.", 13, False, RGBColor(0xC8,0xE6,0xC9), True)]])
text(s, Inches(0.9), Inches(6.5), Inches(11.5), Inches(0.7),
     [[("Merci de votre attention - je suis a votre disposition pour vos questions.", 18, True, BLANC)]])
notes(s, "Pour conclure : au regard de la performance, de la sortie du fioul, de la rentabilite et du respect du bati, je recommande le scenario 2, "
         "qui fait passer le logement de G a B et reste le moins cher sur 30 ans (avec hausse de l'energie), tout en restant dans le budget grace aux aides et a l'apport. "
         "Si le budget initial est un frein, le scenario 1 par etapes est une excellente premiere etape, completee plus tard par le chauffage. "
         "J'ai aussi remis au maitre d'ouvrage des conseils de sobriete simples qui amplifient les economies. Je vous remercie et je suis pret pour vos questions.")

out = "/home/user/licence/Soutenance_Renovation_Saint-Jean-de-Chevelu.pptx"
prs.save(out)
print("OK - slides:", len(prs.slides._sldIdLst))
