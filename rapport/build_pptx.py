# -*- coding: utf-8 -*-
"""Diaporama de soutenance - Bloc 4 - Guillaume TARDY (IRUP, licence CPEBD)."""
from pptx import Presentation
from pptx.util import Cm, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

# --- Logos : déposer les fichiers dans rapport/logos/ pour qu'ils soient insérés
#     automatiquement au prochain lancement du script (PNG ou JPG, fond transparent
#     de préférence ; le SVG n'est pas supporté par PowerPoint via ce script).
LOGO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logos')

def logo_path(*names):
    for n in names:
        for ext in ('.png', '.PNG', '.jpg', '.jpeg', '.JPG'):
            f = os.path.join(LOGO_DIR, n + ext)
            if os.path.exists(f):
                return f
    return None

LOGO_SANTERNE = logo_path('santerne', 'santerne_surfaces_commerciales', 'logo_santerne')
LOGO_VINCI    = logo_path('vinci', 'vinci_energies', 'logo_vinci')
LOGO_ECOLE    = logo_path('irup', 'asder', 'ecole', 'logo_ecole')

def put_logo(slide, path, right, top, height_cm):
    """Place un logo en respectant son rapport d'aspect, calé à droite."""
    if not path:
        return None
    from PIL import Image
    with Image.open(path) as im:
        ratio = im.size[0] / float(im.size[1])
    h = Cm(height_cm)
    w = Emu(int(h * ratio))
    return slide.shapes.add_picture(path, right - w, top, width=w, height=h)

BLUE   = RGBColor(0x00, 0x3A, 0x70)
BLUE_L = RGBColor(0xE8, 0xEF, 0xF7)
RED    = RGBColor(0xD3, 0x1B, 0x2E)
GREEN  = RGBColor(0x0B, 0x8A, 0x5B)
GREY   = RGBColor(0x55, 0x5F, 0x6B)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
DARK   = RGBColor(0x1E, 0x28, 0x32)

prs = Presentation()
prs.slide_width, prs.slide_height = Cm(33.87), Cm(19.05)   # 16:9
W, H = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

def txbox(slide, x, y, w, h, text, size=14, bold=False, color=DARK,
          align=PP_ALIGN.LEFT, font='Calibri', space_after=4, line=1.0, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Cm(0)
    tf.margin_top = tf.margin_bottom = Cm(0)
    lines = text.split('\n')
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        p.line_spacing = line
        # segments **bold**
        parts = ln.split('**')
        for j, seg in enumerate(parts):
            if not seg:
                continue
            r = p.add_run(); r.text = seg
            r.font.size = Pt(size); r.font.name = font
            r.font.bold = bold or (j % 2 == 1)
            r.font.color.rgb = color
    return tb

def rect(slide, x, y, w, h, fill, line=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=0.06):
    sh = slide.shapes.add_shape(shape, x, y, w, h)
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line; sh.line.width = Pt(1)
    sh.shadow.inherit = False
    try:
        sh.adjustments[0] = adj
    except Exception:
        pass
    sh.text_frame.text = ''
    return sh

def header(slide, part, title):
    rect(slide, Cm(0), Cm(0), W, Cm(2.35), BLUE, shape=MSO_SHAPE.RECTANGLE)
    txbox(slide, Cm(1.2), Cm(0.28), Cm(24), Cm(0.6), part, size=11, bold=True, color=RGBColor(0x9C,0xC2,0xE8))
    txbox(slide, Cm(1.2), Cm(0.85), Cm(26), Cm(1.2), title, size=21, bold=True, color=WHITE)
    if LOGO_SANTERNE:
        put_logo(slide, LOGO_SANTERNE, W - Cm(1.2), Cm(0.55), 1.15)

def footer(slide, idx, timing=None):
    txbox(slide, Cm(1.2), H - Cm(1.15), Cm(22), Cm(0.6),
          "Guillaume TARDY — Licence CPEBD, IRUP Saint-Étienne — Bloc 4", size=9, color=GREY)
    if timing:
        txbox(slide, W - Cm(9.4), H - Cm(1.15), Cm(6), Cm(0.6), timing, size=9, color=GREY, align=PP_ALIGN.RIGHT)
    txbox(slide, W - Cm(2.6), H - Cm(1.15), Cm(1.4), Cm(0.6), str(idx), size=9, bold=True, color=BLUE, align=PP_ALIGN.RIGHT)

COUNT = {'n': 0}
def new(part=None, title=None, timing=None):
    s = prs.slides.add_slide(BLANK)
    COUNT['n'] += 1
    if title:
        header(s, part, title)
        footer(s, COUNT['n'], timing)
    return s

def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text

def bullets(slide, x, y, w, items, size=14, gap=0.92):
    for i, it in enumerate(items):
        yy = y + Cm(gap * i)
        d = rect(slide, x, yy + Cm(0.17), Cm(0.22), Cm(0.22), BLUE, shape=MSO_SHAPE.OVAL)
        txbox(slide, x + Cm(0.6), yy, w - Cm(0.6), Cm(0.8), it, size=size)

def kpi(slide, x, y, w, h, value, label, color=BLUE, vsize=30, lsize=11):
    rect(slide, x, y, w, h, BLUE_L)
    txbox(slide, x, y + Cm(0.45), w, Cm(1.4), value, size=vsize, bold=True, color=color, align=PP_ALIGN.CENTER)
    txbox(slide, x + Cm(0.3), y + h - Cm(1.5), w - Cm(0.6), Cm(1.2), label, size=lsize, color=GREY, align=PP_ALIGN.CENTER)

def table(slide, x, y, w, headers, rows, colw=None, fs=12, hfs=12, rh=Cm(0.95)):
    r, c = len(rows) + 1, len(headers)
    shp = slide.shapes.add_table(r, c, x, y, w, rh * r)
    t = shp.table
    if colw:
        tot = sum(colw)
        for i, cw in enumerate(colw):
            t.columns[i].width = Emu(int(w * cw / tot))
    for i, htxt in enumerate(headers):
        cell = t.cell(0, i)
        cell.text = ''
        cell.fill.solid(); cell.fill.fore_color.rgb = BLUE
        cell.margin_left = cell.margin_right = Cm(0.2)
        p = cell.text_frame.paragraphs[0]
        run = p.add_run(); run.text = htxt
        run.font.size = Pt(hfs); run.font.bold = True; run.font.color.rgb = WHITE; run.font.name = 'Calibri'
    for ri, row in enumerate(rows, start=1):
        for ci, val in enumerate(row):
            cell = t.cell(ri, ci)
            cell.text = ''
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE if ri % 2 else BLUE_L
            cell.margin_left = cell.margin_right = Cm(0.2)
            p = cell.text_frame.paragraphs[0]
            for j, seg in enumerate(str(val).split('**')):
                if not seg:
                    continue
                run = p.add_run(); run.text = seg
                run.font.size = Pt(fs); run.font.name = 'Calibri'
                run.font.bold = (j % 2 == 1)
                run.font.color.rgb = DARK
    return t

# =====================================================================
# 1 — TITRE
# =====================================================================
s = new()
rect(s, Cm(0), Cm(0), W, Cm(19.05), BLUE, shape=MSO_SHAPE.RECTANGLE)
rect(s, Cm(0), Cm(11.4), W, Cm(0.12), RED, shape=MSO_SHAPE.RECTANGLE)
txbox(s, Cm(2.5), Cm(3.2), Cm(29), Cm(1), "SOUTENANCE — BLOC 4", size=14, bold=True, color=RGBColor(0x9C,0xC2,0xE8))
txbox(s, Cm(2.5), Cm(4.2), Cm(29), Cm(1), "Initiation et coordination de projets de transition énergétique", size=15, color=RGBColor(0xC9,0xDC,0xEF))
txbox(s, Cm(2.5), Cm(5.7), Cm(29.2), Cm(4.2),
      "Remplacement d'une chaudière gaz de 1987\npar une pompe à chaleur réversible DRV", size=30, bold=True, color=WHITE, line=1.15)
txbox(s, Cm(2.5), Cm(9.7), Cm(29.2), Cm(1.2),
      "Surface de vente de l'INTERMARCHÉ de Rive-de-Gier (42)", size=18, color=RGBColor(0xC9,0xDC,0xEF))
txbox(s, Cm(2.5), Cm(12.2), Cm(20), Cm(3),
      "**Guillaume TARDY**\nTechnicien CVC — Chargé de maintenance\nSANTERNE SURFACES COMMERCIALES — VINCI Energies",
      size=14, color=WHITE, space_after=3)
txbox(s, Cm(22), Cm(12.2), Cm(10), Cm(3),
      "Licence professionnelle CPEBD\nIRUP — Saint-Étienne\n2025 – 2026", size=14, color=RGBColor(0xC9,0xDC,0xEF),
      align=PP_ALIGN.RIGHT, space_after=3)
if LOGO_SANTERNE or LOGO_VINCI or LOGO_ECOLE:
    rect(s, Cm(2.5), Cm(15.6), Cm(28.9), Cm(2.4), WHITE)
    xr = Cm(30.9)
    for lg in (LOGO_ECOLE, LOGO_VINCI, LOGO_SANTERNE):
        if lg:
            pic = put_logo(s, lg, xr, Cm(16.0), 1.6)
            xr = pic.left - Cm(1.2)
notes(s, "0:00 — Bonjour, je suis Guillaume Tardy, technicien CVC et chargé de maintenance chez Santerne Surfaces Commerciales, entreprise de VINCI Energies. Je vais vous présenter le projet que j'ai suivi : le remplacement d'une chaudière gaz de 1987 par une pompe à chaleur réversible sur l'Intermarché de Rive-de-Gier.")

# =====================================================================
# 2 — SOMMAIRE
# =====================================================================
s = new("SOMMAIRE", "Le déroulé de ma présentation", "20 minutes")
items = [
    ("1", "L'ENTREPRISE", "Le groupe VINCI Energies · Santerne Surfaces Commerciales · la cellule CVC · mon poste", "3 min"),
    ("2", "MES MISSIONS", "Entretiens · dépannages · devis · la naissance du projet", "2 min"),
    ("3", "LE PROJET", "Le site et l'existant · l'audit énergétique · la réglementation · la solution · le budget · le chantier de nuit · les résultats", "11 min"),
    ("4", "ANALYSE ET CONCLUSION", "Ce qui a marché · ce que je referais autrement · l'équipe · les perspectives", "4 min"),
]
y = Cm(3.3)
for num, titre, sous, dur in items:
    rect(s, Cm(1.6), y, Cm(30.6), Cm(3.1), BLUE_L)
    rect(s, Cm(1.6), y, Cm(1.7), Cm(3.1), BLUE)
    txbox(s, Cm(1.6), y + Cm(0.85), Cm(1.7), Cm(1.4), num, size=28, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txbox(s, Cm(3.9), y + Cm(0.5), Cm(22), Cm(0.9), titre, size=18, bold=True, color=BLUE)
    txbox(s, Cm(3.9), y + Cm(1.6), Cm(24.5), Cm(1.2), sous, size=12.5, color=GREY)
    txbox(s, Cm(28.6), y + Cm(1.1), Cm(3), Cm(0.9), dur, size=14, bold=True, color=RED, align=PP_ALIGN.RIGHT)
    y += Cm(3.5)
notes(s, "0:40 — Je vais suivre quatre temps : l'entreprise, mes missions, le projet lui-même qui occupera l'essentiel de la présentation, puis mon analyse. Annoncer clairement le plan : c'est noté sur la clarté des explications.")

# =====================================================================
# PARTIE 1
# =====================================================================
def divider(num, titre, sous_items, timing):
    s = new()
    rect(s, Cm(0), Cm(0), W, H, BLUE, shape=MSO_SHAPE.RECTANGLE)
    txbox(s, Cm(2.5), Cm(4.4), Cm(6), Cm(3), "PARTIE " + num, size=15, bold=True, color=RGBColor(0x9C,0xC2,0xE8))
    txbox(s, Cm(2.5), Cm(5.4), Cm(28), Cm(2.2), titre, size=36, bold=True, color=WHITE)
    rect(s, Cm(2.5), Cm(8.6), Cm(5), Cm(0.1), RED, shape=MSO_SHAPE.RECTANGLE)
    y = Cm(9.6)
    for it in sous_items:
        txbox(s, Cm(2.5), y, Cm(1), Cm(0.8), "—", size=15, bold=True, color=RED)
        txbox(s, Cm(3.6), y, Cm(26), Cm(0.8), it, size=15, color=RGBColor(0xDC,0xE7,0xF3))
        y += Cm(1.1)
    txbox(s, W - Cm(8.5), Cm(4.6), Cm(6), Cm(0.8), timing, size=13, bold=True, color=RGBColor(0x9C,0xC2,0xE8), align=PP_ALIGN.RIGHT)
    return s

s = divider("1", "L'entreprise",
            ["Du groupe VINCI à mon entreprise",
             "Santerne Surfaces Commerciales : qui, quoi, où",
             "La cellule Climatisation et mon poste"], "≈ 3 minutes")
notes(s, "1:00 — Première partie, courte : d'où je viens.")

s = new("PARTIE 1 — L'ENTREPRISE", "Du groupe VINCI à mon entreprise", "1 min")
chain = [("GROUPE VINCI", "61,6 Md€ · 219 300 collaborateurs"),
         ("VINCI ENERGIES", "16,7 Md€ · 1 800 entreprises · 57 pays"),
         ("POLE VEF TERTIAIRE CENTRE-EST SUD", "277 M€ · 1 690 collaborateurs · 38 entreprises"),
         ("SANTERNE SURFACES COMMERCIALES", "20 M€ · 82 collaborateurs dont 13 alternants")]
y = Cm(3.2)
for i, (t, d) in enumerate(chain):
    col = BLUE if i < 3 else RED
    rect(s, Cm(1.6) + Cm(1.1 * i), y, Cm(29) - Cm(2.2 * i), Cm(2.0), BLUE_L if i < 3 else RGBColor(0xFB,0xE7,0xE9))
    txbox(s, Cm(2.2) + Cm(1.1 * i), y + Cm(0.32), Cm(20), Cm(0.8), t, size=15, bold=True, color=col)
    txbox(s, Cm(2.2) + Cm(1.1 * i), y + Cm(1.12), Cm(20), Cm(0.7), d, size=11.5, color=GREY)
    y += Cm(2.35)
txbox(s, Cm(1.6), Cm(13.1), Cm(30.6), Cm(3),
      "**Le modèle VINCI Energies : des entreprises autonomes, mises en réseau.**\n"
      "C'est ce « maillage » qui m'a permis de mobiliser un **ingénieur énergéticien du groupe** pour auditer le magasin :\n"
      "une PME de 82 personnes n'aurait pas eu cette compétence en interne.", size=14, line=1.15)
notes(s, "1:10 — Une PME de 82 personnes, mais adossée à un groupe international. Insister sur le maillage : c'est ce qui rend le projet possible. La Talaudière, près de Saint-Étienne, spécialité surfaces commerciales : électricité et génie climatique.")

s = new("PARTIE 1 — L'ENTREPRISE", "La cellule Climatisation et mon poste", "1 min 30")
rect(s, Cm(1.6), Cm(3.1), Cm(15), Cm(11.6), BLUE_L)
txbox(s, Cm(2.2), Cm(3.5), Cm(14), Cm(0.8), "LA CELLULE CLIMATISATION", size=14, bold=True, color=BLUE)
org = ["**Jean-Michel BERJAUD** — Responsable d'affaires",
       "**A. BESSARD · S. HAMDOUCHE** — Responsables chantiers",
       "**M. NEGGAZ · R. PAUWELS · G. VACHER** — Techniciens",
       "**Guillaume TARDY** + 3 alternants"]
yy = Cm(4.7)
for i, o in enumerate(org):
    rect(s, Cm(2.2) + Cm(0.5 * i), yy, Cm(13.8) - Cm(1.0 * i), Cm(1.5), WHITE)
    txbox(s, Cm(2.6) + Cm(0.5 * i), yy + Cm(0.42), Cm(13) - Cm(1.0 * i), Cm(0.8), o, size=12)
    yy += Cm(1.75)
txbox(s, Cm(2.2), Cm(11.9), Cm(14), Cm(2.4),
      "Travaux neufs · maintenance préventive et corrective ·\nconseil en amélioration énergétique.\nClients : grande distribution, retail, tertiaire, collectivités.",
      size=12, color=GREY, line=1.15)
rect(s, Cm(17.6), Cm(3.1), Cm(14.6), Cm(11.6), WHITE, line=BLUE)
txbox(s, Cm(18.2), Cm(3.5), Cm(13.4), Cm(0.8), "MON POSTE : CHARGÉ DE MAINTENANCE", size=14, bold=True, color=RED)
txbox(s, Cm(18.2), Cm(4.5), Cm(13.4), Cm(1.4),
      "**3 ans** technicien CVC · **1 an et demi** chargé de maintenance", size=13, color=GREY)
bullets(s, Cm(18.2), Cm(6.0), Cm(13.4),
        ["**Les entretiens** — visites de maintenance préventive",
         "**Les dépannages** — maintenance corrective",
         "**Les devis** — dépannages et remplacement de petites installations"], size=13, gap=1.55)
rect(s, Cm(18.2), Cm(11.3), Cm(13.4), Cm(3.0), BLUE_L)
txbox(s, Cm(18.7), Cm(11.75), Cm(12.4), Cm(2.3),
      "Un projet à **90 000 €** ne relève donc **pas** de mon périmètre habituel.\nJ'y suis venu en cherchant un projet support pour ma licence.",
      size=12, line=1.2)
notes(s, "2:10 — Mon métier, très concrètement : entretiens, dépannages, devis. Dire honnêtement que le projet dépasse mon périmètre habituel : c'est plus crédible, et le jury le vérifiera en questions.")

# =====================================================================
# PARTIE 2
# =====================================================================
s = divider("2", "Mes missions", ["Ce que je fais au quotidien",
                                  "Comment le projet est né"], "≈ 2 minutes")
notes(s, "2:40 —")

s = new("PARTIE 2 — MES MISSIONS", "Du quotidien de maintenance au projet", "2 min")
cols = [("ENTRETENIR", "Visites préventives, contrôles de fonctionnement, nettoyages,\n**contrôles d'étanchéité** réglementaires des circuits frigorifiques"),
        ("DÉPANNER", "Diagnostic, recherche de la **cause racine**, réparation\nou mise en sécurité, remise en service"),
        ("CHIFFRER", "Devis de dépannage et de **remplacement de petites installations** :\nrelevé, consultation fournisseurs, prix de vente, relance")]
for i, (t, d) in enumerate(cols):
    x = Cm(1.6) + Cm(10.4) * i
    rect(s, x, Cm(3.2), Cm(9.6), Cm(5.4), BLUE_L)
    txbox(s, x + Cm(0.5), Cm(3.7), Cm(8.6), Cm(0.8), t, size=15, bold=True, color=BLUE)
    txbox(s, x + Cm(0.5), Cm(4.9), Cm(8.6), Cm(3.2), d, size=12, line=1.15)
rect(s, Cm(1.6), Cm(9.4), Cm(30.6), Cm(5.0), WHITE, line=RED)
txbox(s, Cm(2.3), Cm(9.9), Cm(29), Cm(0.8), "COMMENT LE PROJET EST NÉ", size=15, bold=True, color=RED)
steps = ["Je cherche un **projet support** pour ma licence CPEBD",
         "J'en parle à **J.-M. BERJAUD**, responsable d'affaires",
         "Il me met en relation avec l'**ingénieur énergéticien VINCI**",
         "**Participation à l'audit**, puis **réalisation d'une partie du chantier**"]
for i, st in enumerate(steps):
    x = Cm(2.3) + Cm(7.4) * i
    txbox(s, x, Cm(11.1), Cm(1.2), Cm(0.8), str(i + 1), size=20, bold=True, color=RED)
    txbox(s, x, Cm(12.0), Cm(6.8), Cm(2.2), st, size=12, line=1.15)
    if i < 3:
        txbox(s, x + Cm(6.6), Cm(11.9), Cm(1), Cm(0.8), "▶", size=14, color=GREY)
notes(s, "2:50 — Trois missions, et surtout : c'est la maintenance qui fait remonter le besoin. Le lien avec l'ingénieur est le point de bascule du projet.")

# =====================================================================
# PARTIE 3
# =====================================================================
s = divider("3", "Le projet",
            ["Le site et la situation de départ",
             "L'audit énergétique et la problématique",
             "Les obligations réglementaires : l'argument décisif",
             "La solution retenue et son dimensionnement",
             "Le budget, les CEE et le retour sur investissement",
             "Le chantier de nuit en ERP : sécurité et planning",
             "Les résultats et les indicateurs d'impact"], "≈ 11 minutes")
notes(s, "4:40 — Cœur de la présentation.")

s = new("3.1 — LE SITE", "La situation de départ", "1 min")
for i, (v, l) in enumerate([("3 690 m²", "surface totale\ndont 2 596 m² de vente"),
                            ("452 kW", "chaudière gaz\nFERROLI de 1987"),
                            ("4 h 45 – 19 h 45", "amplitude d'ouverture\n6,5 jours / 7"),
                            ("165 340 €", "facture énergétique\nannuelle HT")]):
    kpi(s, Cm(1.6) + Cm(7.8) * i, Cm(3.1), Cm(7.0), Cm(4.6), v, l, vsize=24 if i != 2 else 19)
rect(s, Cm(1.6), Cm(8.6), Cm(15.1), Cm(5.9), WHITE, line=BLUE)
txbox(s, Cm(2.2), Cm(9.0), Cm(14), Cm(0.8), "CE QUI POSAIT PROBLÈME", size=14, bold=True, color=BLUE)
bullets(s, Cm(2.2), Cm(10.0), Cm(14),
        ["Chaudière gaz de **1987**, en fin de vie", "Émission par **aérothermes**, régulation sommaire",
         "**Aucune climatisation** hors zone frais", "Pas de GTB : régulation de **classe D**"], size=12.5, gap=1.05)
rect(s, Cm(17.6), Cm(8.6), Cm(14.6), Cm(5.9), RGBColor(0xFB,0xE7,0xE9))
txbox(s, Cm(18.2), Cm(9.0), Cm(13.4), Cm(0.8), "LE RISQUE POUR LE CLIENT", size=14, bold=True, color=RED)
txbox(s, Cm(18.2), Cm(10.0), Cm(13.4), Cm(4),
      "Une panne de chaudière **en pleine saison**, un remplacement en urgence au prix fort,\n"
      "un inconfort d'été subi par les clients et les salariés,\n"
      "et une facture qui ne fait qu'augmenter.", size=13, line=1.25)
notes(s, "4:50 — Poser le décor en 4 chiffres. La chaudière de 1987 est l'élément déclencheur : ce n'est pas un projet de confort, c'est un équipement en fin de vie.")

s = new("3.2 — L'AUDIT ÉNERGÉTIQUE", "Méthode et état des lieux", "1 min 30")
rect(s, Cm(1.6), Cm(3.1), Cm(15.1), Cm(5.2), BLUE_L)
txbox(s, Cm(2.2), Cm(3.5), Cm(14), Cm(0.8), "LA MÉTHODE", size=14, bold=True, color=BLUE)
txbox(s, Cm(2.2), Cm(4.5), Cm(14), Cm(3.4),
      "Visite du site le **17/04/2025**, rapport du **30/07/2025**\n"
      "Données **ENEDIS / GRDF** et factures sur 3 ans\n"
      "Modélisation **IPMVP** (outil Flash Energy)\n"
      "Suivi via la plateforme **ENERGISME**", size=13, line=1.3)
rect(s, Cm(17.6), Cm(3.1), Cm(14.6), Cm(5.2), WHITE, line=BLUE)
txbox(s, Cm(18.2), Cm(3.5), Cm(13.4), Cm(0.8), "MA CONTRIBUTION", size=14, bold=True, color=RED)
txbox(s, Cm(18.2), Cm(4.5), Cm(13.4), Cm(3.4),
      "Visite et **relevé de l'existant CVC**\nHistorique d'exploitation et des pannes\nÉchanges sur les scénarios CVC\n"
      "→ l'ingénieur modélise, chiffre et rédige", size=13, line=1.3)
txbox(s, Cm(1.6), Cm(8.9), Cm(30.6), Cm(0.8), "LA RÉPARTITION DES CONSOMMATIONS — 1 219 000 kWh/an, soit 330,6 kWh/m²/an", size=15, bold=True, color=BLUE)
data = [("Froid alimentaire", 37, RED), ("Éclairage", 27, BLUE), ("Autres", 18, GREY),
        ("Chauffage", 13, GREEN), ("Climatisation", 4, GREY), ("ECS", 1, GREY)]
x = Cm(1.6)
for name, pct, col in data:
    w = Cm(30.6) * pct / 100.0
    rect(s, x, Cm(10.0), w, Cm(1.5), col, shape=MSO_SHAPE.RECTANGLE)
    if pct >= 10:
        txbox(s, x, Cm(10.35), w, Cm(0.8), "%d %%" % pct, size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
        txbox(s, x, Cm(11.8), w, Cm(0.8), name, size=11.5, color=DARK, align=PP_ALIGN.CENTER)
    x += w
txbox(s, Cm(25.5), Cm(12.45), Cm(6.7), Cm(0.8), "Climatisation 4 % · ECS 1 %", size=10.5, color=GREY, align=PP_ALIGN.RIGHT)
txbox(s, Cm(1.6), Cm(13.2), Cm(30.6), Cm(1.6),
      "**Le chauffage ne pèse que 13 %** des consommations du site. Ce n'est donc pas le plus gros gisement —\n"
      "mais c'est celui qui cumule un équipement en fin de vie, un besoin de confort et une contribution réglementaire.",
      size=13.5, line=1.2)
notes(s, "5:50 — Montrer que je sais lire une répartition par usage. Le froid alimentaire est le premier poste d'un supermarché, pas le chauffage. Le dire avant que le jury ne le demande : c'est de la prise de recul.")

s = new("3.3 — LA RÉGLEMENTATION", "L'argument qui a déclenché la décision", "2 min")
rows = [["**Décret tertiaire**", "Surface > 1 000 m²\n**3 690 m²**", "− 40 % en **2030**", "**369,2 → 221,5 kWh/m²**"],
        ["**Décret BACS**", "Puissance > 70 kW\n**chaudière de 452 kW**", "**1ᵉʳ janvier 2025**\n(déjà dépassé)", "GTB de classe C minimum"],
        ["**Loi APER**", "Parking > 1 500 m²\n**3 179 m²**", "**2028**", "≈ 1 480 m² d'ombrières PV"],
        ["**Loi LOM**", "> 20 places\n**120 places**", "**1ᵉʳ janvier 2025**", "6 bornes dont 1 PMR"]]
table(s, Cm(1.6), Cm(3.1), Cm(30.6), ["Obligation", "Pourquoi le site est concerné", "Échéance", "Ce que cela impose"],
      rows, colw=[20, 27, 20, 33], fs=12, rh=Cm(1.45))
rect(s, Cm(1.6), Cm(11.0), Cm(30.6), Cm(3.6), RGBColor(0xFB,0xE7,0xE9))
txbox(s, Cm(2.3), Cm(11.4), Cm(29), Cm(3),
      "**En cas de manquement au décret tertiaire :** mise en demeure du préfet, puis **publication du manquement**\n"
      "sur un site public de l'État — le « name and shame » — et amende administrative jusqu'à **7 500 €**.\n"
      "**L'argument qui porte n'est pas l'amende, c'est l'image et le report de la facture :** ne rien faire aujourd'hui,\n"
      "c'est devoir faire deux fois plus, deux fois plus vite, en 2029.", size=13.5, line=1.25)
notes(s, "7:20 — Slide clé pour le critère « argumenter la pertinence / convaincre de passer à l'action ». Le client ignorait trois de ces quatre obligations. Prendre le temps ici.")

s = new("3.4 — LA SOLUTION", "Ce qui a été installé", "1 min 30")
rect(s, Cm(1.6), Cm(3.1), Cm(15.1), Cm(7.0), BLUE_L)
txbox(s, Cm(2.2), Cm(3.5), Cm(14), Cm(0.8), "UNITÉS EXTÉRIEURES — cour arrière, sur dalle", size=13, bold=True, color=BLUE)
txbox(s, Cm(2.2), Cm(4.6), Cm(14), Cm(4.8),
      "**DAIKIN VRV IV — RXYQ36U**\n(RXYQ20U 20 CV + RXYQ16U 16 CV)\n\n"
      "**70,4 kW** en chaud à − 10 °C · **89,5 kW** en froid\n"
      "ETAS **162,4 %** chaud · **250,8 %** froid\nFluide **R-410A — 38 kg**", size=12.5, line=1.3)
rect(s, Cm(17.6), Cm(3.1), Cm(14.6), Cm(7.0), WHITE, line=BLUE)
txbox(s, Cm(18.2), Cm(3.5), Cm(13.4), Cm(0.8), "UNITÉS INTÉRIEURES — surface de vente", size=13, bold=True, color=BLUE)
txbox(s, Cm(18.2), Cm(4.6), Cm(13.4), Cm(4.8),
      "**1 gainable FXMQ-250A** — 28 kW, 4 440 m³/h\n"
      "→ **59 ml de gaine perforée Ø 550** sur la ligne\n    de caisses et le fond de magasin\n\n"
      "**4 cassettes 900 × 900** Roundflow — 16 kW\n5 télécommandes MADOKA", size=12.5, line=1.3)
rect(s, Cm(1.6), Cm(10.5), Cm(30.6), Cm(4.0), BLUE_L)
txbox(s, Cm(2.3), Cm(10.8), Cm(29), Cm(0.8), "POURQUOI UN DRV PLUTÔT QU'AUTRE CHOSE ?", size=13.5, bold=True, color=BLUE)
why = [("Chaudière\nà condensation", "47 800 € pour 2 250 €/an\n**et aucune climatisation**", RED),
       ("Rooftops", "Rendement inférieur en charge partielle,\ncharge en toiture", RED),
       ("PAC air/eau", "Aérothermes conservés,\npas de climatisation", RED),
       ("**DRV réversible**", "Chauffage **et** froid, zonage,\npose en site occupé, pas d'eau en magasin", GREEN)]
for i, (t, d, c) in enumerate(why):
    x = Cm(2.3) + Cm(7.4) * i
    txbox(s, x, Cm(11.8), Cm(6.8), Cm(1.0), t, size=12.5, bold=True, color=c, line=1.05)
    txbox(s, x, Cm(12.95), Cm(6.8), Cm(1.4), d, size=10.5, color=GREY, line=1.12)
notes(s, "9:20 — Décrire l'installation puis justifier le choix. Si on me demande pourquoi le R-410A : assumer, c'est la limite du projet, j'y reviens en partie 4.")

s = new("3.5 — LE DIMENSIONNEMENT", "452 kW remplacés par 70,4 kW", "1 min")
rect(s, Cm(2.5), Cm(3.6), Cm(12), Cm(4.0), RGBColor(0xFB,0xE7,0xE9))
txbox(s, Cm(2.5), Cm(4.1), Cm(12), Cm(1.6), "452 kW", size=40, bold=True, color=RED, align=PP_ALIGN.CENTER)
txbox(s, Cm(2.5), Cm(6.1), Cm(12), Cm(1), "chaudière gaz de 1987", size=13, color=GREY, align=PP_ALIGN.CENTER)
txbox(s, Cm(15.2), Cm(4.4), Cm(3.4), Cm(1.5), "➜", size=34, bold=True, color=BLUE, align=PP_ALIGN.CENTER)
rect(s, Cm(19.2), Cm(3.6), Cm(12), Cm(4.0), RGBColor(0xE4,0xF3,0xEC))
txbox(s, Cm(19.2), Cm(4.1), Cm(12), Cm(1.6), "70,4 kW", size=40, bold=True, color=GREEN, align=PP_ALIGN.CENTER)
txbox(s, Cm(19.2), Cm(6.1), Cm(12), Cm(1), "PAC réversible DRV", size=13, color=GREY, align=PP_ALIGN.CENTER)
txbox(s, Cm(1.6), Cm(8.4), Cm(30.6), Cm(0.9), "SOIT UNE PUISSANCE DIVISÉE PAR 6,4 — POURQUOI ?", size=15, bold=True, color=BLUE, align=PP_ALIGN.CENTER)
reasons = ["Chaudière de 1987 **très largement surdimensionnée**, comme la plupart des installations de cette époque",
           "Bâtiment **isolé et modifié** depuis : toiture, doublages, extension récente",
           "**Apports internes considérables** : éclairage, occupants, et surtout les rejets des groupes de froid alimentaire (37 % des consommations)",
           "Rendement d'émission d'un **DRV à détente directe** sans commune mesure avec des aérothermes pilotés en loi d'eau"]
bullets(s, Cm(2.5), Cm(9.9), Cm(28.5), reasons, size=13.5, gap=1.15)
rect(s, Cm(2.5), Cm(14.3), Cm(28.5), Cm(0.06), BLUE, shape=MSO_SHAPE.RECTANGLE)
notes(s, "10:20 — C'est mon meilleur argument technique : remplacer à l'identique aurait fait réinstaller six fois trop de puissance. Montre que j'ai redimensionné, pas recopié.")

s = new("3.6 — LE BUDGET", "Devis, financement et retour sur investissement", "1 min 30")
for i, (v, l, c) in enumerate([("90 000 €", "montant HT du devis", BLUE),
                               ("11 000 €", "prime CEE\nTotalEnergies / GreenFlex", GREEN),
                               ("79 000 €", "investissement net", BLUE),
                               ("≈ 15 ans", "temps de retour\naprès CEE", RED)]):
    kpi(s, Cm(1.6) + Cm(7.8) * i, Cm(3.1), Cm(7.0), Cm(4.3), v, l, color=c, vsize=25)
rect(s, Cm(1.6), Cm(8.2), Cm(15.1), Cm(6.3), WHITE, line=BLUE)
txbox(s, Cm(2.2), Cm(8.6), Cm(14), Cm(0.8), "LES POSTES DU DEVIS", size=14, bold=True, color=BLUE)
posts = [("Unités extérieures", "32 %"), ("Liaisons frigorifiques", "22 %"), ("Unités intérieures", "12 %"),
         ("**Travail en horaire décalé**", "**10,5 %**"), ("Gaine de diffusion", "10 %"), ("Électricité, condensats, divers", "13,5 %")]
yy = Cm(9.6)
for n, p in posts:
    txbox(s, Cm(2.2), yy, Cm(11), Cm(0.7), n, size=12)
    txbox(s, Cm(13.2), yy, Cm(3), Cm(0.7), p, size=12, bold=True, color=BLUE, align=PP_ALIGN.RIGHT)
    yy += Cm(0.78)
rect(s, Cm(17.6), Cm(8.2), Cm(14.6), Cm(6.3), BLUE_L)
txbox(s, Cm(18.2), Cm(8.6), Cm(13.4), Cm(0.8), "POURQUOI 15 ANS — ET POURQUOI LE FAIRE", size=13, bold=True, color=RED)
txbox(s, Cm(18.2), Cm(9.6), Cm(13.4), Cm(4.6),
      "On remplace une énergie **bon marché** (gaz) par une énergie **chère** (électricité), et on **ajoute** un usage : + 102 MWh de climatisation.\n\n"
      "Ce qui justifie le projet : **chaudière de 1987**, **confort d'été** sur 2 596 m², **décret tertiaire** et **décret BACS**.\n"
      "Le bouquet complet, lui, revient à **9,3 ans**.", size=12, line=1.25)
notes(s, "11:20 — Ne pas cacher les 15 ans : l'assumer et expliquer. C'est ce qui distingue une présentation honnête d'un argumentaire commercial.")

s = new("3.7 — LE CHANTIER", "Deux mois de nuit dans un ERP en exploitation", "2 min")
for i, (v, l) in enumerate([("mi-avril\n→ mi-juin 2026", "période de réalisation"),
                            ("19 h 45 → 4 h 45", "soit 8 h de fenêtre utile"),
                            ("2", "compagnons"),
                            ("70 %", "des tâches en nacelle")]):
    kpi(s, Cm(1.6) + Cm(7.8) * i, Cm(3.1), Cm(7.0), Cm(4.0), v, l, vsize=17 if i < 2 else 30)
cards = [("TRAVAIL DE NUIT", "Code du travail **L. 3122-1 et s.**\nPériode 21 h – 6 h · 8 h max/jour\n40 h en moyenne sur 12 semaines\nContreparties en repos · suivi médical renforcé\n**Interdit aux mineurs** : apprentis exclus"),
         ("ERP EN EXPLOITATION", "Arrêté du 25 juin 1980, **article GN 13**\nDégagements et issues **jamais obstrués**\n**Permis de feu** pour les brasages\nDétection remise en service **avant 4 h 45**\nMagasin propre et exploitable chaque matin"),
         ("TRAVAIL EN HAUTEUR", "**PEMP** : nacelle, pas d'échelle (R. 4323-58)\n**CACES R486** + autorisation de conduite\nVGP tous les 6 mois · harnais + longe courte\n**Personne au sol formée aux manœuvres de secours**\nZone au sol balisée et interdite")]
for i, (t, d) in enumerate(cards):
    x = Cm(1.6) + Cm(10.4) * i
    rect(s, x, Cm(7.9), Cm(9.6), Cm(6.6), WHITE, line=BLUE)
    rect(s, x, Cm(7.9), Cm(9.6), Cm(0.9), BLUE, shape=MSO_SHAPE.RECTANGLE)
    txbox(s, x + Cm(0.4), Cm(8.1), Cm(8.8), Cm(0.6), t, size=12.5, bold=True, color=WHITE)
    txbox(s, x + Cm(0.4), Cm(9.1), Cm(8.8), Cm(5.2), d, size=11.5, line=1.25)
txbox(s, Cm(1.6), Cm(14.8), Cm(30.6), Cm(0.8),
      "**Plan de prévention écrit obligatoire** (> 400 h et travaux dangereux) + inspection commune préalable avec le magasin.",
      size=12.5, color=GREY)
notes(s, "12:50 — Point fort du projet. Insister sur la hiérarchie : protection collective avant protection individuelle, et sur la personne au sol formée au secours, souvent oubliée.")

s = new("3.8 — L'ALÉA", "Un temps de nuit multiplié par deux", "1 min 30")
rect(s, Cm(1.6), Cm(3.1), Cm(30.6), Cm(2.3), RGBColor(0xFB,0xE7,0xE9))
txbox(s, Cm(2.3), Cm(3.6), Cm(29), Cm(1.4),
      "**Le fait :** la période a été tenue — mi-avril à mi-juin 2026 — mais le **volume d'heures de nuit a doublé**\n"
      "par rapport au chiffrage. Ce n'est pas un incident : c'est un **écart de productivité structurel**.", size=14, line=1.2)
txbox(s, Cm(1.6), Cm(5.9), Cm(15.1), Cm(0.8), "LES CAUSES", size=14, bold=True, color=BLUE)
bullets(s, Cm(1.6), Cm(6.9), Cm(15.1),
        ["Fenêtre utile de 8 h, dont installation et repli quotidiens",
         "Tout est monté puis redescendu **chaque nuit**",
         "70 % en nacelle : réinstallation à chaque zone",
         "59 ml de gaine à aligner en hauteur",
         "Vigilance nocturne et fatigue cumulée"], size=12.5, gap=1.0)
txbox(s, Cm(17.6), Cm(5.9), Cm(14.6), Cm(0.8), "LES CONSÉQUENCES ET LE BILAN", size=14, bold=True, color=RED)
rect(s, Cm(17.6), Cm(6.9), Cm(14.6), Cm(4.0), BLUE_L)
txbox(s, Cm(18.1), Cm(7.25), Cm(13.6), Cm(3.5),
      "Marge prévue **consommée** par les heures supplémentaires.\n"
      "**Zéro heure de fermeture** du magasin : l'écart a été absorbé par l'entreprise, **pas par le client**.\n"
      "Affaire finalement **très légèrement bénéficiaire**, grâce aux **économies d'achat et à la négociation**.",
      size=12.5, line=1.2)
rect(s, Cm(17.6), Cm(11.2), Cm(14.6), Cm(3.3), WHITE, line=RED)
txbox(s, Cm(18.1), Cm(11.55), Cm(13.6), Cm(2.8),
      "**Ce que j'en retiens**\nUn bon résultat **ne valide pas** une mauvaise estimation : la compensation est venue d'un levier ponctuel, pas de la méthode.", size=12.5, line=1.25)
rect(s, Cm(1.6), Cm(12.1), Cm(15.1), Cm(2.4), WHITE, line=BLUE)
txbox(s, Cm(2.1), Cm(12.45), Cm(14.1), Cm(2.0),
      "**La correction :** distinguer au devis le **temps de production** du **temps de mise en place et de repli**, et appliquer un coefficient de productivité nocturne.", size=11.5, line=1.2)
notes(s, "14:20 — Slide très noté : « proposer des modifications pour s'adapter aux aléas ». Assumer l'erreur de chiffrage et donner la correction concrète.")

s = new("3.9 — LES RÉSULTATS", "Indicateurs d'impact pour la transition énergétique", "1 min 30")
rows = [["Consommation du site", "**1 219 000 kWh/an**\n330,6 kWh/m²", "objectif bouquet :\n779 000 kWh — 211,2 kWh/m²", "**− 36 %**"],
        ["Objectif décret tertiaire 2030", "369,2 kWh/m²", "**221,5 kWh/m²** exigés", "**conforme**"],
        ["Émissions évitées — action PAC", "—", "**16 679 kgCO₂e/an**", "76 650 km en voiture"],
        ["Émissions évitées — bouquet", "—", "**64 830 kgCO₂e/an**", "**− 70 %**"],
        ["Fermeture du magasin", "—", "**0 heure**", "objectif tenu"],
        ["Décret BACS", "aucune GTB", "**liaisons Modbus/BACnet posées**", "anticipé"]]
table(s, Cm(1.6), Cm(3.1), Cm(30.6), ["Indicateur", "Avant", "Après / objectif", "Impact"],
      rows, colw=[30, 22, 30, 18], fs=12, rh=Cm(1.35))
rect(s, Cm(1.6), Cm(12.2), Cm(30.6), Cm(2.4), BLUE_L)
txbox(s, Cm(2.3), Cm(12.6), Cm(29), Cm(1.8),
      "**Comment je vérifierai réellement le gain :** correction des consommations par les **degrés-jours (DJU)**,\n"
      "raisonnement en **kWh avant les euros**, suivi via **ENERGISME** et déclaration **OPERAT** — sur une année pleine minimum.",
      size=13, line=1.25)
notes(s, "15:50 — Donner les indicateurs, puis montrer que je sais qu'une comparaison brute de factures ne prouve rien. Reconnaître l'absence de sous-comptage avant travaux si on me le demande.")

# =====================================================================
# PARTIE 4
# =====================================================================
s = divider("4", "Analyse et conclusion",
            ["Ce qui a fonctionné", "Ce que je referais autrement",
             "L'équipe : organisation et axes d'amélioration", "Les perspectives pour le site"], "≈ 4 minutes")
notes(s, "17:20 —")

s = new("PARTIE 4 — ANALYSE", "Ce qui a marché, ce que je referais autrement", "1 min 30")
rect(s, Cm(1.6), Cm(3.1), Cm(15.1), Cm(11.4), RGBColor(0xE4,0xF3,0xEC))
txbox(s, Cm(2.2), Cm(3.5), Cm(14), Cm(0.8), "CE QUI A FONCTIONNÉ", size=15, bold=True, color=GREEN)
bullets(s, Cm(2.2), Cm(4.6), Cm(14),
        ["Partir d'un **audit**, pas d'une envie de vendre une machine",
         "Le **maillage VINCI** : une expertise inaccessible à une PME seule",
         "**Séquencement intelligent** : liaisons GTB posées, GTC plus tard",
         "**Dimensionnement repris à la source** : 452 → 70,4 kW",
         "**Zéro heure de fermeture**, zéro accident"], size=12.5, gap=1.85)
rect(s, Cm(17.6), Cm(3.1), Cm(14.6), Cm(11.4), RGBColor(0xFB,0xE7,0xE9))
txbox(s, Cm(18.2), Cm(3.5), Cm(13.4), Cm(0.8), "CE QUE JE REFERAIS AUTREMENT", size=15, bold=True, color=RED)
bullets(s, Cm(18.2), Cm(4.6), Cm(13.4),
        ["**Le fluide** : 38 kg de R-410A = **79,3 tCO₂e**, soit 4,8 années de gain. Au R-32 : 25,7 t, et contrôle annuel au lieu de semestriel",
         "**Le chiffrage du travail de nuit**, sous-évalué d'un facteur 2",
         "**Un sous-comptage** du poste chauffage avant travaux",
         "**Exploiter l'écart** budget audit / devis réel (− 27 %) auprès du client"], size=12.5, gap=2.3)
notes(s, "17:30 — Critère à coefficient 3. Être franc : le R-410A est la vraie faiblesse, et je sais la chiffrer. C'est ce qui fera la différence.")

s = new("PARTIE 4 — L'ÉQUIPE", "Organisation, limites et axes d'amélioration", "1 min")
rows = [["**Mon rôle**", "Participation à l'audit · réalisation d'une partie du chantier · exploitation en maintenance"],
        ["**Points forts**", "Chaîne de décision très courte · binôme polyvalent · l'installation est posée par celui qui la maintient"],
        ["**Points faibles**", "Effectif de 2 sans marge · transmission nuit/jour décalée de 24 h · isolement de l'équipe de nuit · fatigue"],
        ["**Axes d'amélioration**", "Compte rendu photo standardisé en fin de poste · recouvrement hebdomadaire jour/nuit · 3ᵉ compagnon en renfort sur les phases lourdes · rotation des tâches physiques"],
        ["**Situation de handicap**", "Aménagement de poste avec le médecin du travail et le référent handicap : tâches de **préfabrication au sol** plutôt qu'en nacelle, adaptation des horaires, accessibilité des zones"]]
table(s, Cm(1.6), Cm(3.3), Cm(30.6), ["Thème", "Organisation de l'équipe projet"], rows, colw=[24, 76], fs=12.5, rh=Cm(1.95))
notes(s, "19:00 — Slide qui coche un critère entier de la grille, souvent oublié par les candidats. Ne pas le sauter même si le temps presse.")

s = new("PARTIE 4 — PERSPECTIVES", "La suite pour le magasin", "45 s")
road = [("1", "Récupération de chaleur\nsur les groupes froids", "34 200 € — **4,3 ans**"),
        ("2", "GTC classe A / C", "39 000 € — **5,3 ans**\nconformité BACS"),
        ("3", "Ballons thermodynamiques\npour les labos", "8 840 € — **6,3 ans**"),
        ("4", "Ombrières photovoltaïques\n271,9 kWc", "368 000 € — **8,4 ans**\nconformité APER"),
        ("5", "Fermeture des meubles\nfrigorifiques", "le **premier gisement**\nrestant : 58 % des consos")]
for i, (n, t, d) in enumerate(road):
    x = Cm(1.6) + Cm(6.25) * i
    rect(s, x, Cm(3.4), Cm(5.8), Cm(6.6), BLUE_L)
    txbox(s, x, Cm(3.8), Cm(5.8), Cm(1), n, size=26, bold=True, color=BLUE, align=PP_ALIGN.CENTER)
    txbox(s, x + Cm(0.35), Cm(5.2), Cm(5.1), Cm(2.4), t, size=12, bold=True, align=PP_ALIGN.CENTER, line=1.15)
    txbox(s, x + Cm(0.35), Cm(7.8), Cm(5.1), Cm(1.8), d, size=11, color=GREY, align=PP_ALIGN.CENTER, line=1.15)
rect(s, Cm(1.6), Cm(10.6), Cm(30.6), Cm(3.9), WHITE, line=BLUE)
txbox(s, Cm(2.3), Cm(11.1), Cm(29), Cm(3.2),
      "**Le bouquet complet : 572 940 € HT · 58 590 € d'économies par an · 9,3 ans de retour · − 70 % d'émissions.**\n"
      "Mon projet est la **première brique** de cette trajectoire : sans PAC réversible, pas de sortie du gaz,\n"
      "pas de confort d'été, et un objectif 2030 hors d'atteinte. L'action la moins rentable isolément\n"
      "était indispensable à l'ensemble.", size=13.5, line=1.25)
notes(s, "20:00 — Terminer sur la trajectoire : le projet n'est pas un coup isolé, il ouvre une feuille de route.")

s = new()
rect(s, Cm(0), Cm(0), W, H, BLUE, shape=MSO_SHAPE.RECTANGLE)
rect(s, Cm(2.5), Cm(6.4), Cm(5), Cm(0.1), RED, shape=MSO_SHAPE.RECTANGLE)
txbox(s, Cm(2.5), Cm(4.4), Cm(28), Cm(2), "Conclusion", size=34, bold=True, color=WHITE)
txbox(s, Cm(2.5), Cm(7.4), Cm(28.5), Cm(5),
      "D'une chaudière gaz de 1987 à une **pompe à chaleur réversible de 70,4 kW**,\n"
      "installée **de nuit, en deux mois, sans un seul jour de fermeture**,\n"
      "pour **90 000 € HT dont 11 000 € financés par les CEE**.\n\n"
      "Le rôle d'un chargé de projet en transition énergétique n'est pas de proposer\n"
      "**la meilleure solution technique**, mais de **rendre une solution possible** :\n"
      "acceptable économiquement, réalisable pour l'équipe, sûre pour les compagnons\n"
      "et conforme pour le bâtiment.", size=17, color=WHITE, line=1.35)
txbox(s, Cm(2.5), Cm(15.3), Cm(20), Cm(1.2), "Merci de votre attention — je suis à votre disposition pour vos questions.",
      size=15, bold=True, color=RGBColor(0x9C,0xC2,0xE8))
if LOGO_SANTERNE or LOGO_VINCI:
    xr = Cm(31.4)
    for lg in (LOGO_VINCI, LOGO_SANTERNE):
        if lg:
            pic = put_logo(s, lg, xr, Cm(15.1), 1.5)
            xr = pic.left - Cm(1.0)
notes(s, "20:00 — Conclure net, ne pas déborder. Enchaîner sur les questions.")

# =====================================================================
# ANNEXES (backup, non présentées)
# =====================================================================
s = new("ANNEXE", "Détail du devis — 92 939,39 € HT ramenés à 90 000 €")
rows = [["A.1 Unités intérieures", "1 gainable FXMQ-250A + 4 cassettes Roundflow 125", "11 055,30 €"],
        ["A.2 Plénums", "Acier galvanisé, isolation 25 mm", "552,63 €"],
        ["A.3 Gaine de diffusion", "SIONAIR GMD perforée Ø 550 — 59 ml", "8 991,82 €"],
        ["A.4 Régulation", "5 télécommandes MADOKA BRC1H52", "774,00 €"],
        ["A.5 Unités extérieures", "RXYQ20U + RXYQ16U, supports, mise en service constructeur", "30 036,98 €"],
        ["A.6 Liaisons frigorifiques", "Cuivre 2 tubes, Refnet, charge R-410A, chemins de câbles", "20 307,90 €"],
        ["A.7 Condensats", "65 m PVC DN 40, 5 siphons", "1 471,59 €"],
        ["A.8 Électricité", "Bus LIYCY, sondes, coffret CVC, **liaisons Modbus/BACnet**", "8 388,75 €"],
        ["A.9 Divers", "**Travail en horaire décalé 9 715,85 €**, dossier DESP, percements", "11 360,42 €"]]
table(s, Cm(1.6), Cm(3.1), Cm(30.6), ["Poste", "Contenu", "Montant HT"], rows, colw=[25, 55, 20], fs=11.5, rh=Cm(1.1))
txbox(s, Cm(1.6), Cm(14.0), Cm(30.6), Cm(1),
      "Remise − 2 939,39 € → **90 000 € HT** · TVA 20 % → 108 000 € TTC · **CEE − 11 000 €** → **97 000 € TTC**", size=13.5)
notes(s, "ANNEXE — à ouvrir si le jury demande le détail du budget.")

s = new("ANNEXE", "Les 9 actions chiffrées par l'audit")
rows = [["Récupération de chaleur sur groupes froids", "34 200 €", "6 400 €", "**4,3 ans**", "✔ retenue"],
        ["GTC (classe A / C)", "39 000 €", "5 400 €", "**5,3 ans**", "✔ retenue"],
        ["Ballons thermodynamiques labos", "8 840 €", "1 410 €", "6,3 ans", "✔ retenue"],
        ["Calorifuge de la chaufferie", "1 680 €", "220 €", "6,5 ans", "✘ sans objet"],
        ["Ombrières photovoltaïques 271,9 kWc", "368 000 €", "43 830 €", "8,4 ans", "✔ retenue"],
        ["Solution Air Booster", "69 800 €", "6 300 €", "11,0 ans", "✘ arbres à abattre"],
        ["Chaudière gaz à condensation", "47 800 €", "2 250 €", "21,4 ans", "✘ pas de clim"],
        ["Destratificateurs (29 unités)", "44 100 €", "1 600 €", "21,4 ans", "✘"],
        ["**PAC réversible surface de vente**", "**122 800 €**", "**5 260 €**", "21,5 ans", "**✔ mon projet**"]]
table(s, Cm(1.6), Cm(3.1), Cm(30.6), ["Action de performance énergétique", "Coût HT", "Économie/an", "Retour", "Décision"],
      rows, colw=[42, 14, 15, 13, 16], fs=11.5, rh=Cm(1.1))
txbox(s, Cm(1.6), Cm(14.0), Cm(30.6), Cm(1),
      "Bouquet retenu : **572 940 € HT · 58 590 €/an · 26 700 € de subventions · 9,3 ans · − 70 % d'émissions**", size=13.5)
notes(s, "ANNEXE — à ouvrir si on me demande pourquoi cette action plutôt qu'une autre.")

s = new("ANNEXE", "Le fluide frigorigène : R-410A contre R-32")
rows = [["Charge de l'installation", "**38 kg**", "38 kg"],
        ["GWP du fluide", "**2 088**", "675"],
        ["Impact potentiel", "**79,3 t CO₂e**", "25,7 t CO₂e"],
        ["Équivalent en années de gain (16,7 t/an)", "**4,8 ans**", "1,5 an"],
        ["Seuil des 50 t CO₂e", "**dépassé**", "non dépassé"],
        ["Contrôle d'étanchéité réglementaire", "**tous les 6 mois**", "tous les 12 mois"]]
table(s, Cm(3.6), Cm(3.6), Cm(26.6), ["", "R-410A (installé)", "R-32 (alternative)"], rows, colw=[46, 27, 27], fs=13, rh=Cm(1.4))
txbox(s, Cm(3.6), Cm(12.6), Cm(26.6), Cm(2),
      "**Un choix de fluide a un effet chiffrable sur 20 ans** : sur le bilan carbone réel du projet,\n"
      "et sur le coût d'exploitation, via la périodicité des contrôles réglementaires.", size=14, line=1.25)
notes(s, "ANNEXE — la question du fluide viendra probablement. Cette slide y répond en 20 secondes.")

prs.save('Soutenance_Bloc4_VRV_Intermarche_Rive-de-Gier.pptx')
print("OK — %d diapositives" % len(prs.slides._sldIdLst))
