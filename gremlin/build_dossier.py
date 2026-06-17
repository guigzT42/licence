# -*- coding: utf-8 -*-
"""
Génère le dossier de conduite de projet GREMLIN (.docx).
Phase de préparation de la maquette - essai en soufflerie.
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement, parse_xml

IMG = "/home/user/licence/gremlin/img"
OUT = "/home/user/licence/Projet_GREMLIN_Dossier.docx"

# ---------- Charte graphique ----------
NAVY   = RGBColor(0x1F, 0x4E, 0x79)   # bleu marine titres
NAVY2  = RGBColor(0x2E, 0x6B, 0xA8)   # bleu moyen
GREY   = RGBColor(0x40, 0x40, 0x40)   # texte
LGREY  = RGBColor(0x7F, 0x7F, 0x7F)
RED    = RGBColor(0xC0, 0x39, 0x2B)
GREEN  = RGBColor(0x2E, 0x7D, 0x32)
HDR_BG = "1F4E79"   # fond entête de tableau
BAND   = "EAF1F8"   # bandes claires
WARN_BG= "FDECEA"
OK_BG  = "E8F5E9"

# ---------- Typographie française (espaces insécables) ----------
NBSP = " "      # espace insécable
NNBSP = " "     # espace fine insécable

def fr(t):
    """Applique les espaces insécables avant la ponctuation double (usage FR)."""
    if t is None:
        return t
    t = t.replace(" :", NBSP + ":")
    t = t.replace(" ;", NNBSP + ";")
    t = t.replace(" !", NNBSP + "!")
    t = t.replace(" ?", NNBSP + "?")
    t = t.replace(" %", NNBSP + "%")
    t = t.replace("« ", "«" + NBSP)
    t = t.replace(" »", NBSP + "»")
    return t

# =====================================================================
doc = Document()

# ---------- Styles de base ----------
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)
normal.font.color.rgb = GREY
pf = normal.paragraph_format
pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
pf.line_spacing = 1.15
pf.space_after = Pt(8)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

for lvl, sz in [("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)]:
    st = doc.styles[lvl]
    st.font.name = "Calibri"
    st.font.size = Pt(sz)
    st.font.bold = True
    st.font.color.rgb = NAVY
    st.paragraph_format.space_before = Pt(14 if lvl == "Heading 1" else 10)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = True

# Marges
sec = doc.sections[0]
sec.top_margin = Cm(2.2)
sec.bottom_margin = Cm(2.0)
sec.left_margin = Cm(2.3)
sec.right_margin = Cm(2.3)

# =====================================================================
# Helpers
# =====================================================================
def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)

def set_cell_margins(cell, top=40, bottom=40, left=90, right=90):
    tcPr = cell._tc.get_or_add_tcPr()
    m = OxmlElement("w:tcMar")
    for tag, val in (("top", top), ("bottom", bottom), ("start", left), ("end", right)):
        e = OxmlElement("w:" + tag)
        e.set(qn("w:w"), str(val))
        e.set(qn("w:type"), "dxa")
        m.append(e)
    tcPr.append(m)

def cell_text(cell, text, bold=False, color=None, size=10, align="left", italic=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    p.alignment = {"left": WD_ALIGN_PARAGRAPH.LEFT, "center": WD_ALIGN_PARAGRAPH.CENTER,
                   "right": WD_ALIGN_PARAGRAPH.RIGHT}[align]
    r = p.add_run(fr(str(text)))
    r.bold = bold
    r.italic = italic
    r.font.size = Pt(size)
    r.font.name = "Calibri"
    if color is not None:
        r.font.color.rgb = color
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    return p

def make_table(rows, headers, widths=None, aligns=None, fontsize=10,
               band=True, caption=None, highlight=None):
    """highlight: fonction(row_index, row_values) -> hexcolor ou None."""
    n = len(headers)
    table = doc.add_table(rows=1, cols=n)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    table.autofit = False
    # En-tête
    hdr = table.rows[0].cells
    for j, h in enumerate(headers):
        cell_text(hdr[j], h, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
                  size=fontsize, align="center")
        shade(hdr[j], HDR_BG)
        set_cell_margins(hdr[j])
    # Lignes
    for i, row in enumerate(rows):
        cells = table.add_row().cells
        hl = highlight(i, row) if highlight else None
        for j, val in enumerate(row):
            a = aligns[j] if aligns else "left"
            cell_text(cells[j], val, size=fontsize, align=a)
            set_cell_margins(cells[j])
            if hl:
                shade(cells[j], hl)
            elif band and i % 2 == 1:
                shade(cells[j], BAND)
    # Largeurs
    if widths:
        for row in table.rows:
            for j, w in enumerate(widths):
                row.cells[j].width = Cm(w)
    # Répète l'en-tête sur chaque page
    trPr = table.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    trPr.append(th)
    if caption:
        add_caption(caption)
    return table

FIG_N = [0]
TAB_N = [0]

def add_caption(text, kind="Figure"):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(fr(text))
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = LGREY

def add_image(path, width_cm, caption=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(width_cm))
    if caption:
        add_caption(caption)

def para(text, bold=False, italic=False, color=None, size=11, align="justify",
         space_after=8, space_before=0):
    p = doc.add_paragraph()
    p.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY, "left": WD_ALIGN_PARAGRAPH.LEFT,
                   "center": WD_ALIGN_PARAGRAPH.CENTER}[align]
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    r = p.add_run(fr(text))
    r.bold = bold
    r.italic = italic
    r.font.size = Pt(size)
    if color is not None:
        r.font.color.rgb = color
    return p

def bullet(text, bold_lead=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(4)
    if bold_lead:
        r = p.add_run(fr(bold_lead))
        r.bold = True
        r.font.size = Pt(11)
        r2 = p.add_run(fr(text))
        r2.font.size = Pt(11)
    else:
        r = p.add_run(fr(text))
        r.font.size = Pt(11)
    return p

def h1(text):
    return doc.add_heading(fr(text), level=1)

def h2(text):
    return doc.add_heading(fr(text), level=2)

def callout(title, lines, bg=OK_BG, border=GREEN):
    """Encadré type 'verdict / point clé'."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    shade(cell, bg)
    set_cell_margins(cell, top=120, bottom=120, left=200, right=200)
    cell.width = Cm(16.4)
    p0 = cell.paragraphs[0]
    p0.paragraph_format.space_after = Pt(4)
    r = p0.add_run(fr(title))
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = NAVY
    for ln in lines:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        rr = p.add_run(fr(ln))
        rr.font.size = Pt(10.5)
        rr.font.color.rgb = GREY
    # bordure colorée
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "bottom", "start", "end"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "18")
        e.set(qn("w:color"), "%02X%02X%02X" % (border[0], border[1], border[2]))
        borders.append(e)
    tcPr.append(borders)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

# =====================================================================
# PAGE DE GARDE
# =====================================================================
def hrule(color="1F4E79", size="24", space_before=0, space_after=10):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pbdr.append(bottom)
    pPr.append(pbdr)
    return p

for _ in range(2):
    doc.add_paragraph()

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("CONDUITE DE PROJET"); r.font.size = Pt(13); r.font.color.rgb = LGREY
r.font.bold = True
p.paragraph_format.space_after = Pt(2)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Dossier de projet"); r.font.size = Pt(15); r.font.color.rgb = GREY
p.paragraph_format.space_after = Pt(18)

hrule(space_after=14)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("PROJET GREMLIN")
r.font.size = Pt(40); r.font.bold = True; r.font.color.rgb = NAVY
p.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(fr("Essai en soufflerie d’une maquette"))
r.font.size = Pt(16); r.font.color.rgb = NAVY2
p.paragraph_format.space_after = Pt(2)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(fr("Programme de développement d’un nouvel avion"))
r.font.size = Pt(13); r.font.italic = True; r.font.color.rgb = LGREY
p.paragraph_format.space_after = Pt(14)

hrule(space_after=18)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(fr("Phase étudiée : préparation de la maquette"))
r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = GREY
p.paragraph_format.space_after = Pt(2)

p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(fr("Scénario · organigramme des tâches · planning · budget · risques · pilotage"))
r.font.size = Pt(10.5); r.font.italic = True; r.font.color.rgb = LGREY
p.paragraph_format.space_after = Pt(40)

# Bloc identité (tableau discret)
info = doc.add_table(rows=4, cols=2)
info.alignment = WD_TABLE_ALIGNMENT.CENTER
data_info = [
    ("Rôle", "Chargé de projet"),
    ("Destinataires", "Direction de la soufflerie — Client (avionneur)"),
    ("Version", "1.0"),
    ("Date", "17 juin 2026"),
]
for i, (k, v) in enumerate(data_info):
    cell_text(info.cell(i, 0), k, bold=True, color=NAVY, size=10.5, align="right")
    cell_text(info.cell(i, 1), v, size=10.5, align="left")
    info.cell(i, 0).width = Cm(4.5)
    info.cell(i, 1).width = Cm(9.5)
# pas de bordures sur ce tableau
tblPr = info._tbl.tblPr
borders = OxmlElement("w:tblBorders")
for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
    e = OxmlElement("w:" + edge); e.set(qn("w:val"), "none")
    borders.append(e)
tblPr.append(borders)

doc.add_page_break()

# =====================================================================
# SOMMAIRE (champ TOC + cache visible)
# =====================================================================
# Titre "Sommaire" volontairement hors styles Heading -> n'apparaît pas dans le TOC
_pt = doc.add_paragraph()
_pt.paragraph_format.space_before = Pt(6)
_pt.paragraph_format.space_after = Pt(6)
_r = _pt.add_run("Sommaire")
_r.font.size = Pt(16); _r.bold = True; _r.font.color.rgb = NAVY
para("Sommaire généré automatiquement. Pour le mettre à jour dans Word : clic droit "
     "dessus puis « Mettre à jour les champs » (ou touche F9). Les numéros de page "
     "s’affichent après cette mise à jour.", italic=True, color=LGREY, size=9.5,
     space_after=10)

# Entrées affichées tant que le champ n'a pas été recalculé
TOC_ENTRIES = [
    (1, "1. Présentation et cadrage du projet"),
    (2, "1.1 Contexte et enjeu commercial"),
    (2, "1.2 Périmètre du présent dossier"),
    (2, "1.3 Objectifs et contraintes à respecter"),
    (2, "1.4 Hypothèses de travail"),
    (2, "1.5 Livrables attendus"),
    (1, "2. Scénario du projet"),
    (2, "2.1 Les cinq grandes étapes"),
    (2, "2.2 Communication et livrables de fin de projet"),
    (2, "2.3 Schéma du scénario"),
    (1, "3. Organigramme des tâches (WBS)"),
    (2, "3.1 Découpage en lots"),
    (2, "3.2 Représentation hiérarchique"),
    (2, "3.3 Liste détaillée des 22 tâches"),
    (1, "4. Planning de réalisation"),
    (2, "4.1 Tableau des antériorités"),
    (2, "4.2 Réseau d’antériorités (graphe PERT)"),
    (2, "4.3 Calcul des dates et des marges"),
    (2, "4.4 Chemin critique et durée totale"),
    (2, "4.5 Diagramme de Gantt"),
    (2, "4.6 Plan de charge des ressources"),
    (1, "5. Budget de la phase de préparation"),
    (2, "5.1 Bases de calcul"),
    (2, "5.2 Coût par tâche"),
    (2, "5.3 Synthèse budgétaire"),
    (2, "5.4 Courbe en « S »"),
    (1, "6. Analyse des risques"),
    (1, "7. Pilotage de la réalisation"),
    (2, "7.1 Dispositif de suivi"),
    (2, "7.2 Jalons de la phase"),
    (2, "7.3 Indicateurs de pilotage"),
    (2, "7.4 Conclusion du chargé de projet"),
    (1, "Annexe — Glossaire"),
]

def _fldchar(kind, dirty=False):
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), kind)
    if dirty:
        e.set(qn("w:dirty"), "true")
    return e

def add_toc(entries):
    last_p = None
    for idx, (lvl, text) in enumerate(entries):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.0 if lvl == 1 else 0.7)
        p.paragraph_format.space_after = Pt(2 if lvl == 1 else 1)
        p.paragraph_format.space_before = Pt(4 if lvl == 1 else 0)
        if idx == 0:
            # ouverture du champ dans le 1er paragraphe (pas de ligne vide)
            r0 = p.add_run()
            instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
            instr.text = ' TOC \\o "1-3" \\h \\z \\u '
            r0._r.append(_fldchar("begin", dirty=True))
            r0._r.append(instr)
            r0._r.append(_fldchar("separate"))
        r = p.add_run(fr(text))
        r.font.size = Pt(11 if lvl == 1 else 10)
        r.bold = (lvl == 1)
        r.font.color.rgb = NAVY if lvl == 1 else GREY
        last_p = p
    # fermeture du champ après la dernière entrée
    rend = last_p.add_run()
    rend._r.append(_fldchar("end"))

add_toc(TOC_ENTRIES)
doc.add_page_break()

# =====================================================================
# 1. PRÉSENTATION ET CADRAGE
# =====================================================================
h1("1. Présentation et cadrage du projet")

h2("1.1 Contexte et enjeu commercial")
para("La Direction de la soufflerie a été sollicitée par un avionneur étranger, "
     "de notoriété internationale, pour réaliser l’essai en soufflerie d’une maquette "
     "dans le cadre du développement d’un nouvel avion (nom de code : GREMLIN). "
     "L’opération n’est pas de grande ampleur en elle-même, mais l’enjeu dépasse "
     "largement le seul chiffre d’affaires de l’essai : il s’agit d’un nouveau client, "
     "et la Direction insiste pour décrocher la commande car les débouchés possibles "
     "sont importants. Autant dire que la qualité de la proposition et le respect des "
     "engagements pèseront lourd.")
para("Le devis initial s’élevait à 297 K€. Le client l’a jugé élevé, en s’appuyant "
     "sur une offre concurrente à 259 K€. Il s’est toutefois montré sensible au sérieux "
     "des interlocuteurs et à l’engagement ferme de tenir les délais. Après négociation, "
     "la commande a finalement été passée sur les bases suivantes :")
bullet("272 000 € pour l’ensemble de l’opération ;")
bullet("85 jours ouvrables, délai contractuel ferme.")
para("Nous partons donc d’un projet sous double pression : un prix revu à la baisse "
     "par rapport au devis, et un délai sur lequel l’entreprise s’est explicitement "
     "engagée pour emporter l’affaire.")

h2("1.2 Périmètre du présent dossier")
para("Le projet complet se découpe en plusieurs grandes phases (préparation, "
     "installation, mesures, dépouillement, restitution). Ce dossier porte uniquement "
     "sur la première d’entre elles : la préparation de la maquette. Concrètement, "
     "cette phase consiste à fixer la maquette sur un support qui permet de la "
     "positionner dans la soufflerie, puis à l’équiper des capteurs et de "
     "l’instrumentation nécessaires aux mesures. Elle se termine par une revue avec "
     "le client et par les contrôles de bon fonctionnement, avant de remettre une "
     "maquette « prête à l’expérimentation » à l’équipe de mesures.")
para("Cette phase est le point de départ de tout le reste : si elle dérape, c’est "
     "l’engagement global des 85 jours qui est menacé. C’est pourquoi on lui consacre "
     "une étude détaillée (scénario, tâches, planning, budget, risques et pilotage).")

h2("1.3 Objectifs et contraintes à respecter")
para("Trois contraintes encadrent la phase de préparation. Elles servent de référence "
     "tout au long du dossier : chaque livrable est ensuite confronté à la cible "
     "correspondante.")
make_table(
    rows=[
        ["Délai", "≤ 45 jours ouvrables", "Borne fixée par le scénario pour tenir l’engagement global de 85 jours"],
        ["Budget", "≤ 48 500 €", "Au-delà, la phase devient déficitaire"],
        ["Qualité / image", "Essai réussi + support de communication (DVD)", "Exigence du client et de la Direction"],
    ],
    headers=["Contrainte", "Cible", "Origine"],
    widths=[3.2, 5.0, 8.2],
    aligns=["left", "left", "left"],
    fontsize=10,
    caption="Tableau 1 — Les trois contraintes de la phase de préparation.",
)

h2("1.4 Hypothèses de travail")
para("Le scénario fournit un certain nombre d’hypothèses qui cadrent la répartition "
     "des rôles. Je les reprends ici telles qu’elles m’ont été communiquées, car elles "
     "déterminent qui fait quoi et ce qui entre, ou non, dans le périmètre chiffré :")
bullet("le client fournit toutes les précisions utiles via son cahier des charges ;")
bullet("la maquette à tester est livrée par l’avionneur ;")
bullet("les pièces de fixation sont conçues et fabriquées par l’atelier d’usinage interne ;")
bullet("l’équipement spécifique (capteurs, instrumentation), défini et acheté sous notre "
       "responsabilité, reste la propriété de l’entreprise ;")
bullet("la préparation, l’installation puis le démontage en fin d’essai sont assurés "
       "par les techniciens et ouvriers de l’entreprise ;")
bullet("l’équipe de préparation, déjà très chargée, ne participe pas aux essais : "
       "elle rédige un mode opératoire à l’intention de l’équipe de mesures ;")
bullet("les modifications des logiciels de calcul sont prises en charge par les "
       "informaticiens, à partir des indications du client ;")
bullet("des revues de projet sont organisées régulièrement avec le client, qui "
       "assistera par ailleurs aux mesures en soufflerie.")

h2("1.5 Livrables attendus")
para("Pour cette phase, les productions à fournir sont les suivantes — elles "
     "structurent d’ailleurs le plan de ce dossier :")
make_table(
    rows=[
        ["Scénario du projet", "Vue d’ensemble des opérations et de leur enchaînement", "§ 2"],
        ["Organigramme des tâches", "Décomposition structurée du travail (WBS)", "§ 3"],
        ["Planning de réalisation", "Ordonnancement, chemin critique, Gantt, durée", "§ 4"],
        ["Budget", "Coût par tâche, coût total, courbe en S", "§ 5"],
        ["Analyse des risques", "Identification, cotation et parades", "§ 6"],
        ["Pilotage de la réalisation", "Dispositif de suivi et indicateurs", "§ 7"],
    ],
    headers=["Livrable", "Contenu", "Renvoi"],
    widths=[4.6, 8.6, 2.2],
    aligns=["left", "left", "center"],
    fontsize=10,
    caption="Tableau 2 — Livrables de la phase et renvois vers le dossier.",
)

doc.add_page_break()

# =====================================================================
# 2. SCÉNARIO
# =====================================================================
h1("2. Scénario du projet")
para("Le scénario donne la vision d’ensemble : quelles grandes opérations on réalise, "
     "et comment elles s’articulent dans le temps. Il ne descend pas encore au niveau "
     "des tâches élémentaires (c’est l’objet du § 3), il pose le déroulement général "
     "du projet.")

h2("2.1 Les cinq grandes étapes")
para("Vu de loin, le projet GREMLIN s’enchaîne en cinq étapes successives :")
bullet("préparation de la maquette : fixation sur le support et équipement en "
       "instrumentation. C’est la phase étudiée dans ce dossier ;", bold_lead="Étape 1 — ")
bullet("installation en soufflerie : mise en place de la maquette équipée dans la "
       "veine d’essai ;", bold_lead="Étape 2 — ")
bullet("réalisation des mesures : exécution des essais et acquisition des données "
       "prévues au cahier des charges ;", bold_lead="Étape 3 — ")
bullet("dépouillement et rapport : exploitation des résultats et rédaction du "
       "rapport final ;", bold_lead="Étape 4 — ")
bullet("restitution et démontage : remise au client du rapport, de la maquette et "
       "du DVD, puis démontage de l’installation.", bold_lead="Étape 5 — ")

h2("2.2 Communication et livrables de fin de projet")
para("La Direction a choisi d’adosser à cette opération une action de communication "
     "destinée à valoriser l’image de l’entreprise. Trois séquences sont filmées par "
     "un prestataire extérieur — la préparation de la maquette, son installation en "
     "soufflerie et la réalisation des mesures — pour produire un DVD financé sur le "
     "budget publicité. Le tournage se fait dans le respect des consignes de "
     "confidentialité : c’est un point auquel il faudra veiller, car on filme un "
     "produit client encore confidentiel.")
para("À la clôture du projet, trois éléments sont remis au client : un rapport sur "
     "les résultats obtenus, la maquette, et un exemplaire du DVD.")

h2("2.3 Schéma du scénario")
para("Le schéma ci-dessous place les cinq étapes sur l’axe du temps et rappelle, en "
     "partie basse, les grands ensembles de travail de la phase de préparation "
     "(détaillés au § 3). Le bandeau orange figure l’opération de communication, qui "
     "court sur les trois premières étapes.")
add_image(IMG + "/scenario.png", 16.0,
          "Figure 1 — Scénario du projet : articulation des opérations dans le temps.")

callout("Ce qu’il faut retenir du scénario",
        ["La phase de préparation conditionne tout le reste : c’est le maillon de "
         "départ de la chaîne des 85 jours.",
         "Trois ensembles peuvent avancer en parallèle (support, pièces de fixation, "
         "approvisionnement des équipements), ce qui sera la clé pour tenir le délai."],
        bg=BAND, border=NAVY2)

doc.add_page_break()

# =====================================================================
# 3. ORGANIGRAMME DES TÂCHES (WBS)
# =====================================================================
h1("3. Organigramme des tâches (WBS)")
para("L’organigramme des tâches décompose la phase de préparation en opérations "
     "élémentaires. La méthode suivie est celle conseillée pour ce type de cas : on "
     "part du produit final attendu — une maquette prête à l’expérimentation — puis "
     "on le décompose en sous-ensembles. Pour chaque sous-ensemble, on liste les "
     "tâches qui permettent de l’obtenir ; on ajoute enfin les tâches d’assemblage "
     "entre sous-ensembles.")

h2("3.1 Découpage en lots")
para("Cette logique aboutit à six lots de travail :")
bullet("l’étude d’ensemble, qui alimente tous les autres lots (tâche A) ;",
       bold_lead="Lot 0 — Études générales : ")
bullet("spécification, choix et préparation du support (D, E, F) ;",
       bold_lead="Lot 1 — Support : ")
bullet("réception de la maquette, fabrication et ajustement des pièces, puis "
       "fixation (B, G, H, I, J) ;", bold_lead="Lot 2 — Pièces de fixation et maquette : ")
bullet("tout le processus achat des équipements spécifiques (C, K, L, M, N, O, P, Q) ;",
       bold_lead="Lot 3 — Approvisionnement des équipements : ")
bullet("spécification du montage, équipement de la maquette, revue client et "
       "vérification (R, S, T, U) ;", bold_lead="Lot 4 — Montage et validation : ")
bullet("rédaction du mode opératoire (V).", bold_lead="Lot 5 — Documentation : ")

h2("3.2 Représentation hiérarchique")
para("L’arbre ci-dessous présente la décomposition complète. Les tâches surlignées en "
     "rouge sont celles qui se révéleront critiques à l’issue du planning (§ 4) : on "
     "les met en évidence dès maintenant pour faire le lien entre la structure du "
     "travail et les points de vigilance.")
add_image(IMG + "/wbs.png", 16.0,
          "Figure 2 — Organigramme des tâches de la phase de préparation.")

h2("3.3 Liste détaillée des 22 tâches")
para("Les données du cas (exécutant, charge de travail et durée) sont reprises "
     "intégralement dans le tableau ci-dessous. L’effort est exprimé en heures de "
     "travail, la durée en jours ouvrables. Les tâches H (fabrication) et P (livraison) "
     "sont confiées à des intervenants externes au projet (atelier d’usinage et "
     "fournisseur) : elles n’ont pas d’effort interne, seulement une durée.")
tasks = [
    ("A", "Étude d’ensemble", "Ingénieur", "80", "10"),
    ("B", "Réception de la maquette", "Technicien", "20", "5"),
    ("C", "Étude de l’équipement", "Technicien", "16", "2"),
    ("D", "Spécification du support", "Ingénieur", "12", "3"),
    ("E", "Choix du support", "Technicien", "8", "2"),
    ("F", "Préparation du support", "Ouvrier", "140", "7"),
    ("G", "Spécification des pièces", "Technicien", "12", "3"),
    ("H", "Fabrication des pièces", "Atelier", "—", "14"),
    ("I", "Contrôle et ajustement des pièces", "Technicien", "12", "3"),
    ("J", "Fixation de la maquette", "Ouvrier", "110", "4"),
    ("K", "Spécification des équipements", "Ingénieur", "8", "2"),
    ("L", "Consultation pour les équipements", "Ingénieur", "16", "4"),
    ("M", "Négociation pour les équipements", "Acheteur", "24", "3"),
    ("N", "Choix du fournisseur", "Ingénieur", "12", "2"),
    ("O", "Passation de la commande", "Acheteur", "8", "2"),
    ("P", "Livraison des équipements", "Fournisseur", "—", "5"),
    ("Q", "Contrôle des équipements", "Ingénieur", "4", "1"),
    ("R", "Spécification du montage", "Ingénieur", "24", "6"),
    ("S", "Équipement de la maquette", "Ouvrier", "160", "4"),
    ("T", "Revue avec le client", "Ingénieur", "8", "1"),
    ("U", "Vérification du fonctionnement", "Ingénieur", "32", "4"),
    ("V", "Rédaction du mode opératoire", "Ingénieur", "8", "2"),
]
make_table(
    rows=[list(t) for t in tasks],
    headers=["Code", "Tâche", "Exécutant", "Effort (h)", "Durée (j)"],
    widths=[1.4, 7.4, 3.0, 2.2, 2.0],
    aligns=["center", "left", "left", "center", "center"],
    fontsize=9.5,
    caption="Tableau 3 — Les 22 tâches de la phase de préparation (données du cas).",
)

doc.add_page_break()

# =====================================================================
# 4. PLANNING
# =====================================================================
h1("4. Planning de réalisation")
para("Le planning a un objectif précis : vérifier que la phase tient dans les "
     "45 jours ouvrables. Pour cela, je commence par établir les liens d’antériorité "
     "entre tâches, j’en déduis un réseau, puis je calcule les dates au plus tôt et "
     "au plus tard pour faire ressortir le chemin critique et les marges.")

h2("4.1 Tableau des antériorités")
para("Les antériorités traduisent la logique du déroulement : on ne peut pas fixer la "
     "maquette (J) tant que le support, les pièces et la maquette elle-même ne sont "
     "pas prêts ; on ne l’équipe (S) qu’une fois fixée et les équipements reçus, etc. "
     "Le tableau ci-dessous fixe ces liens. Ils s’appuient sur le découpage en lots et "
     "sur le fait que les trois branches — support, pièces et approvisionnement — "
     "peuvent progresser en parallèle après l’étude d’ensemble.")
ant = [
    ("A", "Étude d’ensemble", "—"),
    ("B", "Réception de la maquette", "A"),
    ("C", "Étude de l’équipement", "A"),
    ("D", "Spécification du support", "A"),
    ("E", "Choix du support", "D"),
    ("F", "Préparation du support", "E"),
    ("G", "Spécification des pièces", "A"),
    ("H", "Fabrication des pièces", "G"),
    ("I", "Contrôle et ajustement des pièces", "H"),
    ("J", "Fixation de la maquette", "B, F, I"),
    ("K", "Spécification des équipements", "C"),
    ("L", "Consultation pour les équipements", "K"),
    ("M", "Négociation pour les équipements", "L"),
    ("N", "Choix du fournisseur", "M"),
    ("O", "Passation de la commande", "N"),
    ("P", "Livraison des équipements", "O"),
    ("Q", "Contrôle des équipements", "P"),
    ("R", "Spécification du montage", "A"),
    ("S", "Équipement de la maquette", "J, Q, R"),
    ("T", "Revue avec le client", "S"),
    ("U", "Vérification du fonctionnement", "T"),
    ("V", "Rédaction du mode opératoire", "U"),
]
make_table(
    rows=[list(a) for a in ant],
    headers=["Tâche", "Libellé", "Antériorités"],
    widths=[1.6, 8.4, 4.0],
    aligns=["center", "left", "center"],
    fontsize=9.5,
    caption="Tableau 4 — Liens d’antériorité entre tâches.",
)

h2("4.2 Réseau d’antériorités (graphe PERT)")
para("Le réseau ci-dessous met en image ces enchaînements. On distingue nettement les "
     "trois branches parallèles. Le chemin critique — la plus longue chaîne, celle qui "
     "ne tolère aucun retard — apparaît en rouge.")
add_image(IMG + "/pert.png", 16.0,
          "Figure 3 — Réseau d’antériorités. Chemin critique en rouge : A-G-H-I-J-S-T-U-V (45 j).")

h2("4.3 Calcul des dates et des marges")
para("Le calcul est mené par la méthode des potentiels (dates au plus tôt en parcours "
     "avant, dates au plus tard en parcours arrière), en jours ouvrables, le projet "
     "démarrant au jour 0. La marge totale d’une tâche mesure le retard qu’elle peut "
     "absorber sans repousser la fin de la phase. Une marge nulle signale une tâche "
     "critique (lignes surlignées).")
dates = [
    ("A", "0", "10", "0", "10", "0", "Oui"),
    ("B", "10", "15", "25", "30", "15", ""),
    ("C", "10", "12", "13", "15", "3", ""),
    ("D", "10", "13", "18", "21", "8", ""),
    ("E", "13", "15", "21", "23", "8", ""),
    ("F", "15", "22", "23", "30", "8", ""),
    ("G", "10", "13", "10", "13", "0", "Oui"),
    ("H", "13", "27", "13", "27", "0", "Oui"),
    ("I", "27", "30", "27", "30", "0", "Oui"),
    ("J", "30", "34", "30", "34", "0", "Oui"),
    ("K", "12", "14", "15", "17", "3", ""),
    ("L", "14", "18", "17", "21", "3", ""),
    ("M", "18", "21", "21", "24", "3", ""),
    ("N", "21", "23", "24", "26", "3", ""),
    ("O", "23", "25", "26", "28", "3", ""),
    ("P", "25", "30", "28", "33", "3", ""),
    ("Q", "30", "31", "33", "34", "3", ""),
    ("R", "10", "16", "28", "34", "18", ""),
    ("S", "34", "38", "34", "38", "0", "Oui"),
    ("T", "38", "39", "38", "39", "0", "Oui"),
    ("U", "39", "43", "39", "43", "0", "Oui"),
    ("V", "43", "45", "43", "45", "0", "Oui"),
]
make_table(
    rows=[list(d) for d in dates],
    headers=["Tâche", "Début +tôt", "Fin +tôt", "Début +tard", "Fin +tard", "Marge", "Critique"],
    widths=[1.5, 2.3, 2.1, 2.4, 2.2, 1.7, 1.8],
    aligns=["center"] * 7,
    fontsize=9,
    caption="Tableau 5 — Dates au plus tôt / au plus tard et marges (jours ouvrables).",
    highlight=lambda i, r: OK_BG if r[6] == "Oui" else None,
)

h2("4.4 Chemin critique et durée totale")
para("Le chemin critique relie les tâches A, G, H, I, J, S, T, U et V. La somme de "
     "leurs durées donne la durée de la phase :")
para("A (10) + G (3) + H (14) + I (3) + J (4) + S (4) + T (1) + U (4) + V (2) "
     "= 45 jours ouvrables.", bold=True, align="center", color=NAVY)
callout("Vérification de la contrainte de délai",
        ["Durée de la phase = 45 jours ouvrables, pour une cible de 45 jours.",
         "La contrainte est respectée… mais tout juste : il n’existe aucune marge sur "
         "le chemin critique. Le moindre retard sur une tâche critique repousse la fin "
         "de phase d’autant."],
        bg=OK_BG, border=GREEN)
para("Le point le plus sensible est la tâche H, « fabrication des pièces » : 14 jours, "
     "soit de loin la plus longue, et elle est critique. À l’inverse, deux branches "
     "respirent : le support dispose de 8 jours de marge, l’approvisionnement de "
     "3 jours. Ce sont elles qui pourront servir d’amortisseur en cas d’aléa.")

h2("4.5 Diagramme de Gantt")
para("Le Gantt reprend le planning calé au plus tôt. Les barres rouges marquent les "
     "tâches critiques, les barres bleues les autres tâches, et les segments gris leur "
     "marge. La ligne verticale verte rappelle la butée des 45 jours.")
add_image(IMG + "/gantt.png", 16.0,
          "Figure 4 — Diagramme de Gantt (planning au plus tôt).")

h2("4.6 Plan de charge des ressources")
para("Au-delà des dates, il faut s’assurer que les équipes peuvent réellement absorber "
     "la charge. Le plan ci-dessous cumule, jour par jour, les heures demandées à "
     "chaque catégorie de personnel selon le planning au plus tôt. Il fait apparaître "
     "des pics : la charge Ouvrier dépasse 30 h/jour sur la fin de phase (tâche S), ce "
     "qui suppose de mobiliser plusieurs ouvriers en parallèle. C’est cohérent avec "
     "les 5 ouvriers qualifiés alloués, mais cela mérite d’être anticipé.")
add_image(IMG + "/plan_charge.png", 16.0,
          "Figure 5 — Plan de charge des ressources (planning au plus tôt).")
para("Hors prestations externes (atelier et fournisseur), le volume total se répartit "
     "ainsi : 204 h d’ingénieur, 68 h de technicien, 32 h d’acheteur et 410 h "
     "d’ouvrier. La main-d’œuvre ouvrière représente à elle seule plus de la moitié "
     "de la charge interne — un point que l’on retrouvera dans le budget.")

doc.add_page_break()

# =====================================================================
# 5. BUDGET
# =====================================================================
h1("5. Budget de la phase de préparation")
para("L’objectif est ici de chiffrer la phase et de la comparer à l’enveloppe de "
     "48 500 €. Je calcule d’abord le coût de chaque tâche (c’est plus fin que de "
     "raisonner par intervenant, et cela permet de raccrocher le budget au planning "
     "pour la courbe en S), puis je consolide.")

h2("5.1 Bases de calcul")
para("La Comptabilité a transmis les taux horaires de main-d’œuvre, ainsi que les "
     "montants des prestations externes :")
bullet("ingénieur : 82 €/h  •  technicien : 64 €/h  •  acheteur : 58 €/h  •  ouvrier : 46 €/h ;")
bullet("fabrication des pièces de fixation par l’atelier : 2 940 € (imputés en fin de "
       "tâche H) ;")
bullet("équipements approvisionnés à l’extérieur : 5 200 €, réglés à 50 % à la "
       "commande et 50 % à la livraison ;")
bullet("enveloppe budgétaire allouée à la phase : 48 500 € (au-delà, la phase est "
       "déficitaire).")

h2("5.2 Coût par tâche")
para("Pour chaque tâche interne, le coût est le produit de la charge par le taux "
     "horaire de l’exécutant. Les tâches H et P portent les montants des prestations "
     "externes.")
costs = [
    ("A", "Étude d’ensemble", "Ingénieur", "80 h × 82 €", "6 560 €"),
    ("B", "Réception de la maquette", "Technicien", "20 h × 64 €", "1 280 €"),
    ("C", "Étude de l’équipement", "Technicien", "16 h × 64 €", "1 024 €"),
    ("D", "Spécification du support", "Ingénieur", "12 h × 82 €", "984 €"),
    ("E", "Choix du support", "Technicien", "8 h × 64 €", "512 €"),
    ("F", "Préparation du support", "Ouvrier", "140 h × 46 €", "6 440 €"),
    ("G", "Spécification des pièces", "Technicien", "12 h × 64 €", "768 €"),
    ("H", "Fabrication des pièces", "Atelier", "forfait", "2 940 €"),
    ("I", "Contrôle et ajustement des pièces", "Technicien", "12 h × 64 €", "768 €"),
    ("J", "Fixation de la maquette", "Ouvrier", "110 h × 46 €", "5 060 €"),
    ("K", "Spécification des équipements", "Ingénieur", "8 h × 82 €", "656 €"),
    ("L", "Consultation pour les équipements", "Ingénieur", "16 h × 82 €", "1 312 €"),
    ("M", "Négociation pour les équipements", "Acheteur", "24 h × 58 €", "1 392 €"),
    ("N", "Choix du fournisseur", "Ingénieur", "12 h × 82 €", "984 €"),
    ("O", "Passation de la commande", "Acheteur", "8 h × 58 €", "464 €"),
    ("P", "Livraison des équipements", "Fournisseur", "achat", "5 200 €"),
    ("Q", "Contrôle des équipements", "Ingénieur", "4 h × 82 €", "328 €"),
    ("R", "Spécification du montage", "Ingénieur", "24 h × 82 €", "1 968 €"),
    ("S", "Équipement de la maquette", "Ouvrier", "160 h × 46 €", "7 360 €"),
    ("T", "Revue avec le client", "Ingénieur", "8 h × 82 €", "656 €"),
    ("U", "Vérification du fonctionnement", "Ingénieur", "32 h × 82 €", "2 624 €"),
    ("V", "Rédaction du mode opératoire", "Ingénieur", "8 h × 82 €", "656 €"),
]
make_table(
    rows=[list(c) for c in costs],
    headers=["Code", "Tâche", "Exécutant", "Détail", "Coût"],
    widths=[1.3, 6.7, 2.7, 3.0, 2.6],
    aligns=["center", "left", "left", "left", "right"],
    fontsize=9,
    caption="Tableau 6 — Coût détaillé par tâche.",
)

h2("5.3 Synthèse budgétaire")
synth = [
    ("Main-d’œuvre Ingénieur (204 h × 82 €)", "16 728 €"),
    ("Main-d’œuvre Technicien (68 h × 64 €)", "4 352 €"),
    ("Main-d’œuvre Acheteur (32 h × 58 €)", "1 856 €"),
    ("Main-d’œuvre Ouvrier (410 h × 46 €)", "18 860 €"),
    ("Sous-total main-d’œuvre", "41 796 €"),
    ("Fabrication des pièces de fixation (atelier)", "2 940 €"),
    ("Équipements approvisionnés à l’extérieur", "5 200 €"),
    ("COÛT TOTAL DE LA PHASE", "49 936 €"),
    ("Enveloppe budgétaire allouée", "48 500 €"),
    ("ÉCART", "+ 1 436 € (dépassement)"),
]
def synth_hl(i, r):
    if r[0].startswith("COÛT TOTAL"):
        return WARN_BG
    if r[0] == "ÉCART":
        return WARN_BG
    if r[0].startswith("Sous-total"):
        return BAND
    return None
make_table(
    rows=[list(s) for s in synth],
    headers=["Poste", "Montant"],
    widths=[11.0, 5.0],
    aligns=["left", "right"],
    fontsize=10,
    band=False,
    caption="Tableau 7 — Synthèse budgétaire de la phase.",
    highlight=synth_hl,
)
callout("Vérification de la contrainte de budget",
        ["Coût estimé = 49 936 €, pour une enveloppe de 48 500 €.",
         "La contrainte n’est PAS respectée : dépassement de 1 436 €, soit environ 3 %. "
         "En l’état, la phase de préparation est donc légèrement déficitaire."],
        bg=WARN_BG, border=RED)

para("Le constat appelle des mesures correctives. Les postes les plus lourds sont la "
     "main-d’œuvre ouvrière — surtout la tâche S, « équipement de la maquette », à elle "
     "seule 160 h — ainsi que l’étude d’ensemble A. Plusieurs pistes de retour à "
     "l’équilibre sont envisageables, à arbitrer avec la Direction :")
bullet("réexaminer le contenu et la charge des grosses tâches ouvrier (S, F, J) : "
       "méthodes de travail, préparation en amont, standardisation des opérations ;")
bullet("renégocier le prix des équipements externes (5 200 €) ou le devis de "
       "l’atelier (2 940 €) ;")
bullet("réaffecter, quand c’est possible, une partie des heures d’ingénieur (82 €/h) "
       "vers des techniciens (64 €/h) ;")
bullet("s’assurer que le coût de la communication (DVD) reste bien porté par le budget "
       "publicité, et non imputé à la phase.")
para("À titre d’ordre de grandeur, économiser une trentaine d’heures d’ouvrier ou "
     "renégocier de 25 % les équipements suffirait à repasser sous l’enveloppe. "
     "L’écart est faible : il est rattrapable, à condition de le traiter avant le "
     "lancement.")

h2("5.4 Courbe en « S »")
para("La courbe en S représente les dépenses cumulées au fil du planning : la "
     "main-d’œuvre est étalée sur la durée de chaque tâche, le devis de l’atelier est "
     "imputé en fin de fabrication (H) et les équipements sont payés pour moitié à la "
     "commande, pour moitié à la livraison. Elle servira de référence en phase de "
     "réalisation pour comparer le réalisé au prévu.")
add_image(IMG + "/courbe_s.png", 16.0,
          "Figure 6 — Courbe en S des dépenses cumulées. Le coût final dépasse "
          "l’enveloppe (trait rouge).")
para("On voit bien la courbe franchir la ligne de l’enveloppe en toute fin de phase : "
     "c’est la traduction visuelle du dépassement de 1 436 €.")

doc.add_page_break()

# =====================================================================
# 6. RISQUES
# =====================================================================
h1("6. Analyse des risques")
para("Tenir 45 jours sans marge et un budget déjà juste : le projet comporte de vrais "
     "points de fragilité. Je les recense ci-dessous, en les cotant selon deux axes — "
     "la probabilité (P) qu’ils surviennent et la gravité (G) de leurs conséquences — "
     "sur une échelle de 1 (faible) à 4 (fort). La criticité est le produit P × G ; "
     "plus elle est élevée, plus le risque doit être suivi de près.")
risks = [
    ("R1", "Retard de la fabrication des pièces (tâche H, 14 j, critique)", "3", "4", "12",
     "Lancer H au plus tôt, suivi rapproché de l’atelier, jalon intermédiaire"),
    ("R2", "Modifications des logiciels de calcul dans un temps restreint", "3", "3", "9",
     "Cadrer tôt les spécifications avec le client, ressource informatique dédiée"),
    ("R3", "Dépassement budgétaire (+ 1 436 € constaté)", "4", "2", "8",
     "Plan d’économies du § 5.3, validation Direction, contrôle des heures"),
    ("R4", "Retard de livraison des équipements externes (P, 5 j)", "2", "3", "6",
     "Marge de 3 j sur la branche, clause de délai au contrat fournisseur"),
    ("R5", "Maquette livrée non conforme par le client (tâche B)", "2", "3", "6",
     "Contrôle à réception, procès-verbal contradictoire avec le client"),
    ("R6", "Non-respect de la confidentialité lors du tournage du DVD", "2", "3", "6",
     "Engagement de confidentialité du prestataire, validation des rushes"),
    ("R7", "Absence de marge sur le chemin critique (45/45 j)", "3", "3", "9",
     "Surveillance des tâches critiques, plan de rattrapage anticipé"),
]
make_table(
    rows=[list(r) for r in risks],
    headers=["#", "Risque", "P", "G", "Crit.", "Parade / action de maîtrise"],
    widths=[1.0, 5.6, 0.9, 0.9, 1.2, 6.8],
    aligns=["center", "left", "center", "center", "center", "left"],
    fontsize=9,
    caption="Tableau 8 — Identification, cotation et maîtrise des risques.",
    highlight=lambda i, r: WARN_BG if int(r[4]) >= 9 else None,
)
para("Trois risques ressortent comme prioritaires (criticité ≥ 9) : le retard de "
     "fabrication des pièces (R1), les modifications logicielles dans un délai serré "
     "(R2) et l’absence totale de marge sur le chemin critique (R7). Ce sont eux qui "
     "feront l’objet du suivi le plus rapproché en revue de projet.")
add_image(IMG + "/matrice_risques.png", 13.5,
          "Figure 7 — Matrice de criticité : positionnement des risques.")
para("La matrice confirme la hiérarchie : R1 se loge dans la zone rouge (majeure), "
     "tandis que R2 et R7 sont en zone orange haute. Les risques R4 à R6, de criticité "
     "modérée, restent à surveiller sans mobiliser de moyens lourds.")

doc.add_page_break()

# =====================================================================
# 7. PILOTAGE
# =====================================================================
h1("7. Pilotage de la réalisation")
para("Une fois la phase lancée, l’enjeu n’est plus de planifier mais de tenir le cap. "
     "Compte tenu de l’absence de marge sur le délai et du budget déjà tendu, le "
     "pilotage doit être à la fois simple et réactif.")

h2("7.1 Dispositif de suivi")
bullet("revues de projet régulières avec le client, calées sur les jalons clés "
       "(fin de l’étude A, maquette fixée en J, maquette équipée et revue en S/T) ;")
bullet("suivi de l’avancement physique tâche par tâche et mise à jour hebdomadaire "
       "du Gantt ;")
bullet("surveillance prioritaire des tâches du chemin critique (A, G, H, I, J, S, T, "
       "U, V), qui n’ont aucune marge ;")
bullet("suivi des marges des branches « support » (8 j) et « approvisionnement » (3 j), "
       "qui constituent la seule réserve pour absorber les aléas ;")
bullet("contrôle des dépenses engagées par rapport à la courbe en S, et tenue à jour "
       "du plan d’économies.")

h2("7.2 Jalons de la phase")
para("Les points de contrôle suivants jalonnent la phase. Ce sont les moments où l’on "
     "fait le point sur l’avancement, le budget et les risques.")
jalons = [
    ("J0", "Lancement de la phase", "Jour 0", "Étude d’ensemble engagée"),
    ("J1", "Fin de l’étude d’ensemble", "Jour 10", "Spécifications validées (A)"),
    ("J2", "Pièces fabriquées et contrôlées", "Jour 30", "Fin de I (point dur H levé)"),
    ("J3", "Maquette fixée sur le support", "Jour 34", "Fin de J"),
    ("J4", "Maquette équipée — revue client", "Jour 39", "Fin de S et T"),
    ("J5", "Maquette prête à l’expérimentation", "Jour 45", "Fin de V, mode opératoire remis"),
]
make_table(
    rows=[list(j) for j in jalons],
    headers=["Jalon", "Évènement", "Échéance", "Critère de franchissement"],
    widths=[1.5, 5.6, 2.4, 6.5],
    aligns=["center", "left", "center", "left"],
    fontsize=9.5,
    caption="Tableau 9 — Jalons de la phase de préparation.",
)

h2("7.3 Indicateurs de pilotage")
para("Le tableau de bord s’appuie sur quelques indicateurs simples, suivis en revue. "
     "Les indicateurs de coût et de délai reposent sur la méthode de la valeur "
     "acquise, qui compare ce qui était prévu, ce qui a été réalisé et ce qui a été "
     "réellement dépensé.")
inds = [
    ("Avancement délai (jours consommés vs planning)", "Alerte si glissement > 0 j sur une tâche critique"),
    ("Coût réel cumulé vs courbe en S", "Alerte si écart > 5 %"),
    ("Indices de performance délai (SPI) et coût (CPI)", "Objectif : SPI et CPI ≥ 1"),
    ("Jalons clients tenus", "100 %"),
    ("Risques prioritaires (R1, R2, R7)", "Revue à chaque jalon, parades à jour"),
]
make_table(
    rows=[list(x) for x in inds],
    headers=["Indicateur", "Cible / seuil d’alerte"],
    widths=[8.4, 7.6],
    aligns=["left", "left"],
    fontsize=9.5,
    caption="Tableau 10 — Tableau de bord du pilotage.",
)

h2("7.4 Conclusion du chargé de projet")
para("La phase de préparation est réalisable en 45 jours ouvrables : la contrainte de "
     "délai est respectée, mais sans la moindre marge sur le chemin critique. Le "
     "pilotage devra donc être particulièrement vigilant sur la tâche H (fabrication "
     "des pièces) et, plus largement, sur toute la chaîne critique. Côté budget, le "
     "coût estimé à 49 936 € dépasse l’enveloppe de 1 436 €. Ce dépassement reste "
     "modeste et un plan d’économies est proposé ; il devra être validé par la "
     "Direction avant le lancement.")
para("En synthèse, le projet est tenable, mais il ne laisse aucune place à "
     "l’improvisation. Sécuriser la fabrication des pièces, valider le plan "
     "d’économies et tenir les revues avec le client sont les trois conditions pour "
     "honorer l’engagement global des 85 jours — et, au-delà, pour transformer ce "
     "premier essai en relation durable avec un client à fort potentiel.")

doc.add_page_break()

# =====================================================================
# ANNEXES
# =====================================================================
h1("Annexe — Glossaire")
gloss = [
    ("Organigramme des tâches (WBS)", "Décomposition hiérarchique du projet en lots puis en tâches élémentaires."),
    ("Antériorité", "Lien logique imposant qu’une tâche soit terminée avant qu’une autre puisse commencer."),
    ("Réseau PERT", "Représentation graphique des tâches et de leurs antériorités, utilisée pour calculer les dates."),
    ("Date au plus tôt / au plus tard", "Dates extrêmes de début (ou de fin) d’une tâche sans retarder le projet."),
    ("Marge totale", "Retard maximal admissible sur une tâche sans repousser la fin du projet."),
    ("Chemin critique", "Suite de tâches à marge nulle qui fixe la durée minimale du projet."),
    ("Diagramme de Gantt", "Représentation des tâches sous forme de barres positionnées dans le temps."),
    ("Plan de charge", "Cumul, par ressource et par période, des heures de travail demandées."),
    ("Courbe en S", "Cumul des dépenses au fil du temps, en forme de S, servant de référence de suivi."),
    ("Valeur acquise (SPI/CPI)", "Méthode comparant prévu, réalisé et dépensé pour piloter délais et coûts."),
]
make_table(
    rows=[list(g) for g in gloss],
    headers=["Terme", "Définition"],
    widths=[4.6, 11.4],
    aligns=["left", "left"],
    fontsize=9.5,
)

# =====================================================================
# EN-TÊTE ET PIED DE PAGE
# =====================================================================
def add_field(paragraph, field):
    # Run 1 : begin + code + separate
    r1 = paragraph.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    i = OxmlElement("w:instrText"); i.set(qn("xml:space"), "preserve"); i.text = field
    s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate")
    r1._r.append(b); r1._r.append(i); r1._r.append(s)
    # Run 2 : valeur de cache, ENTRE separate et end (sinon le "1" reste collé)
    rc = paragraph.add_run("1")
    rc.font.size = Pt(8.5); rc.font.color.rgb = LGREY
    # Run 3 : end
    r3 = paragraph.add_run()
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    r3._r.append(e)

section = doc.sections[0]
section.different_first_page_header_footer = True

# En-tête (hors 1re page)
hdr = section.header
hdr.is_linked_to_previous = False
hp = hdr.paragraphs[0]
hp.text = ""
hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = hp.add_run(fr("Projet GREMLIN — Dossier de conduite de projet"))
r.font.size = Pt(8.5); r.font.color.rgb = LGREY; r.italic = True
hr_p = hdr.add_paragraph()
hrp_pPr = hr_p._p.get_or_add_pPr()
pbdr = OxmlElement("w:pBdr"); bottom = OxmlElement("w:bottom")
bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "6")
bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), "BBBBBB")
pbdr.append(bottom); hrp_pPr.append(pbdr)

# Pied de page (hors 1re page)
ftr = section.footer
ftr.is_linked_to_previous = False
fp = ftr.paragraphs[0]
fp.text = ""
tabs = fp.paragraph_format.tab_stops
tabs.add_tab_stop(Cm(8.0), WD_TAB_ALIGNMENT.CENTER)
tabs.add_tab_stop(Cm(16.0), WD_TAB_ALIGNMENT.RIGHT)
r = fp.add_run("Diffusion restreinte"); r.font.size = Pt(8.5); r.font.color.rgb = LGREY
fp.add_run("\t")
rmid = fp.add_run("Page "); rmid.font.size = Pt(8.5); rmid.font.color.rgb = LGREY
add_field(fp, " PAGE ")
rmid2 = fp.add_run(" / "); rmid2.font.size = Pt(8.5); rmid2.font.color.rgb = LGREY
add_field(fp, " NUMPAGES ")
fp.add_run("\t")
rr = fp.add_run("Projet GREMLIN"); rr.font.size = Pt(8.5); rr.font.color.rgb = LGREY

# Pied de 1re page (page de garde) : discret
ffp = section.first_page_footer
ffp.is_linked_to_previous = False
ffp_p = ffp.paragraphs[0]
ffp_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
rg = ffp_p.add_run("Cas n° 1 — Conduite de projet")
rg.font.size = Pt(8.5); rg.font.color.rgb = LGREY; rg.italic = True

# =====================================================================
# Forcer la mise à jour des champs (sommaire) à l'ouverture
# =====================================================================
settings = doc.settings.element
upd = OxmlElement("w:updateFields"); upd.set(qn("w:val"), "true")
settings.append(upd)

doc.save(OUT)
print("Dossier généré :", OUT)

