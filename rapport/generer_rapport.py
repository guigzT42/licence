# -*- coding: utf-8 -*-
"""
RAPPORT D'ÉTUDE TUTORÉE — SUJET 2026-C
Rénovation énergétique d'une ancienne ferme à Saint-Jean-de-Chevelu (73)
Bloc 1 — Chargé de projet énergie et bâtiment durables

Structure conforme à la trame officielle « B1 — Trame rapport pour apprenants ».
Corps du rapport resserré ; le détail est reporté en annexes.
"""
import os
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

from mise_en_page import (Rapport, IMG, FIG, VERT, VERT_CLAIR, ORANGE, BLEU,
                          ROUGE, GRIS, ANTHRA, NOIR, BLANC, par_border, H_VERT,
                          H_VERT_PALE, H_ORANGE_PALE, H_BLEU_PALE,
                          H_ROUGE_PALE, H_GRIS_PALE, add_field)

BASE = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(os.path.dirname(BASE),
                      "Rapport_etude_Sujet_C_Guillaume_Tardy.docx")

im = lambda n: os.path.join(IMG, n + ".jpg")
fg = lambda n: os.path.join(FIG, n + ".png")

R = Rapport("Étude de rénovation énergétique — Saint-Jean-de-Chevelu (73) — "
            "Sujet 2026-C")
D = R.doc


def titre_hors_numerotation(texte, dans_sommaire=False):
    """Titre de premier niveau non numéroté (Sommaire, Résumé de l'étude)."""
    p = D.add_paragraph(style="Heading 1" if dans_sommaire else None)
    pf = p.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(4)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(texte)
    r.font.name = "Calibri"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = VERT
    par_border(p, cotes=("bottom",), sz=12, couleur=H_VERT, space=5)
    if dans_sommaire:
        R.titres.append((1, texte))
    R.espace(6)


# ==========================================================================
#  PAGE DE GARDE
# ==========================================================================
def page_de_garde():
    R.espace(26)
    R.para("BLOC 1 — RÉALISATION D'ÉTUDES TECHNIQUES POUR DES BÂTIMENTS "
           "PERFORMANTS, CONFORTABLES ET À FAIBLE IMPACT ENVIRONNEMENTAL",
           size=9.5, couleur=VERT_CLAIR, align="center", gras=True,
           space_after=4)
    R.para("Formation Chargé de projet énergie et bâtiment durables — ASDER",
           size=10, couleur=GRIS, align="center", space_after=20)
    R.para("RÉNOVATION ÉNERGÉTIQUE", size=25, couleur=VERT, align="center",
           gras=True, space_after=2, interligne=1.0)
    R.para("D'UNE ANCIENNE FERME SAVOYARDE", size=25, couleur=VERT,
           align="center", gras=True, space_after=8, interligne=1.0)
    R.para("Étude technique, économique et environnementale réalisée pour le "
           "compte d'un maître d'ouvrage occupant",
           size=12, couleur=ANTHRA, align="center", italique=True,
           space_after=14)
    R.figure(im("vue_generale"), largeur_cm=10.1,
             legende="La ferme étudiée — Saint-Jean-de-Chevelu (Savoie), "
                     "versant sud-est, altitude 498 m", numerote=False)
    R.espace(8)
    R.tableau([
        ["NOM, Prénom", "TARDY, Guillaume"],
        ["Promotion", "Chargé de projet énergie et bâtiment durables — Bloc 1"],
        ["Sujet", "Projet d'étude tutoré 2026-C — version 1.1"],
        ["Objet de l'étude", "Maison individuelle de 100 m² habitables, "
                             "ancienne ferme de la fin du XIXᵉ siècle"],
        ["Localisation", "Saint-Jean-de-Chevelu (73170) — Savoie — "
                         "zone climatique H1c, altitude 498 m"],
        ["Maître d'ouvrage", "Propriétaire occupant — famille de 4 personnes"],
    ], largeurs=[0.24, 0.76], size=10, size_entete=10, zebra=True)
    R.espace(8)
    R.para("Les plans, photographies et données techniques reproduits dans ce "
           "rapport sont issus du sujet 2026-C, propriété de l'ASDER.",
           size=8, couleur=GRIS, align="center", italique=True)
    R.saut_page()


# ==========================================================================
#  SOMMAIRE
# ==========================================================================
def sommaire():
    titre_hors_numerotation("Sommaire")
    R.toc_ancre()
    R.espace(10)
    R.encadre(
        "Organisation du document",
        [("Corps du rapport (résumé et chapitres 1 à 7) — ", "l'analyse, les "
          "scénarios, les dimensionnements et les résultats économiques."),
         ("Annexes (chapitre 8) — ", "le détail : relevés, calculs complets, "
          "variantes étudiées et écartées, chiffrage poste par poste, points de "
          "vigilance, plan d'action, plan de sobriété, hypothèses et sources. "
          "Chaque renvoi du corps du rapport pointe vers l'annexe "
          "correspondante."),
         "La table des matières ci-dessus est un champ Word : sélectionnez-la et "
         "appuyez sur F9 pour y faire apparaître les numéros de page."],
        couleur=VERT, fond=H_VERT_PALE, size=9.5)
    R.saut_page()


# ==========================================================================
#  RÉSUMÉ DE L'ÉTUDE — compte-rendu synthétique au maître d'ouvrage
# ==========================================================================
def resume():
    titre_hors_numerotation("Résumé de l'étude", dans_sommaire=True)
    R.para("Compte-rendu synthétique à l'attention du maître d'ouvrage",
           size=10, couleur=ANTHRA, italique=True, align="left", space_after=8)

    R.sous_titre("Votre maison aujourd'hui", couleur=ORANGE)
    R.para(
        "Votre maison est une ancienne ferme en pierre de 100 m² habitables, "
        "chauffée par une chaudière propane de 2011 et un poêle à bûches. Elle "
        "est classée G sur les deux axes du diagnostic de performance "
        "énergétique : 622 kWh d'énergie primaire par m² et par an, et 122 kg de "
        "CO₂ par m² et par an. Elle consomme environ deux fois et demie la "
        "moyenne des logements français.")
    R.para(
        "L'enveloppe explique tout. Les murs en pierre de 50 cm ne comportent "
        "aucune isolation : murs extérieurs et mur mitoyen du garage totalisent "
        "61 % de la chaleur perdue ; les fenêtres en simple vitrage 13 % et la "
        "ventilation naturelle 14 %. En revanche vos combles, isolés avec 40 cm "
        "de ouate de cellulose, ne pèsent que 1 % : ce poste est déjà traité et "
        "ne doit surtout pas être refait. Le budget doit aller aux murs, aux "
        "fenêtres et à la ventilation.")

    R.encadre(
        "Le constat le plus important de cette étude",
        ["Vous jugez votre confort d'hiver « très mauvais ». Le calcul vous "
         "donne raison et le chiffre : la chaleur réellement fournie par vos "
         "équipements correspond à une température intérieure moyenne comprise "
         "entre 15 et 16 °C, alors que vous souhaitez 19 °C.",
         ("Vous payez 5 739 € par an d'énergie pour un logement que vous ne "
          "parvenez pas à chauffer correctement.",
          " Ramenée à 19 °C, votre facture atteindrait 8 653 €. Vos dépenses "
          "d'énergie représentent près de 13 % de votre revenu fiscal, alors "
          "qu'on parle de précarité énergétique au-delà de 8 %."),
         "Les travaux proposés ne vous apportent donc pas seulement une "
         "économie : ils vous rendent un logement réellement habitable."],
        couleur=ROUGE, fond=H_ROUGE_PALE, size=9.5, icone="◆")

    R.sous_titre("Les travaux communs aux deux scénarios", couleur=ORANGE)
    R.para(
        "Isolation des murs par l'extérieur en fibre de bois de 180 mm sous "
        "enduit à la chaux, isolation du mur mitoyen du garage par le côté du "
        "garage, remplacement de vos dix menuiseries par du double vitrage bois "
        "posé au nu extérieur, traitement de l'étanchéité à l'air, ventilation "
        "mécanique hygroréglable et remplacement de votre poêle par un modèle "
        "étanche. Ces travaux divisent les déperditions par plus de quatre : le "
        "besoin de chauffage passe de 339 à 63 kWh par m² et par an, et la "
        "puissance nécessaire de 17,1 à 4,1 kW.")

    R.sous_titre("Comparaison des deux scénarios", couleur=ORANGE)
    R.tableau([
        ["", "Aujourd'hui", "Scénario A — global", "Scénario B — par étapes"],
        ["Contenu", "—",
         "Tout en une seule opération : enveloppe, ventilation, eau chaude "
         "thermodynamique et pompe à chaleur air/eau",
         "Étape 1 : enveloppe et ventilation, chaudière propane conservée et "
         "optimisée. Étape 2, trois à cinq ans plus tard : eau chaude "
         "thermodynamique et pompe à chaleur"],
        ["Étiquette DPE", "G", "B", "C après l'étape 1, puis B"],
        ["Coût des travaux", "—", "85 100 € TTC",
         "65 600 € puis 22 500 €, soit 88 100 € TTC"],
        ["Aides estimées", "—", "40 500 €", "36 200 € puis 6 100 €, "
                                            "soit 42 300 €"],
        ["Reste à charge", "—", "44 600 €",
         "29 400 € puis 16 400 €, soit 45 800 €"],
        ["Facture annuelle", "6 009 €", "1 833 €", "2 963 € puis 1 833 €"],
        ["Économie annuelle", "—", "4 176 €", "3 046 € puis 4 176 €"],
        ["Mensualité de l'éco-PTZ", "—", "144 €/mois", "81 €/mois"],
        ["Coût global sur 20 ans", "192 000 €", "99 900 €", "105 900 €"],
    ], largeurs=[0.17, 0.15, 0.32, 0.36], size=8,
        align_centre_cols=(1,), lignes_surlignees=(2,),
        titre="Comparaison des deux scénarios de rénovation")

    R.sous_titre("Les éléments qui doivent guider votre décision",
                 couleur=ORANGE)
    R.puces([
        ("Les deux scénarios s'autofinancent. ", "La mensualité de l'éco-prêt à "
         "taux zéro est très inférieure à l'économie réalisée : 144 € contre "
         "348 € par mois pour le scénario A, 81 € contre 254 € pour l'étape 1 du "
         "scénario B. Votre budget mensuel s'améliore dès la première année, et "
         "votre confort avec lui."),
        ("Le scénario par étapes coûte finalement un peu plus cher. ", "Sa "
         "seconde étape ne fait gagner qu'une classe et sort du dispositif "
         "MaPrimeRénov' « rénovation d'ampleur », beaucoup plus généreux : le "
         "reste à charge cumulé atteint 45 800 € contre 44 600 € en une seule "
         "opération, pour un confort obtenu plusieurs années plus tard."),
        ("La fenêtre réglementaire se referme en septembre 2026. ", "Les "
         "critères actuels permettent encore de conserver une chaudière au "
         "propane dans une opération aidée : c'est ce qui rend l'étape 1 du "
         "scénario B possible. Le dossier doit être déposé avant cette échéance, "
         "et avant toute signature de devis."),
        ("Votre capacité de remboursement est confortable. ", "Avec votre prêt "
         "à la consommation de 300 € par mois, la mensualité de l'éco-prêt porte "
         "votre taux d'endettement à environ 11 %, très en deçà du seuil de "
         "35 %."),
        ("La valeur de votre bien est en jeu. ", "Un logement classé G ne peut "
         "plus être mis en location depuis 2025 et subit une décote estimée "
         "entre 10 et 20 % à la revente."),
    ], size=9.5)

    R.encadre(
        "Recommandation : le scénario A, rénovation globale performante",
        [("Le plus performant : ", "de la classe G à la classe B, cinq classes "
          "gagnées, et des émissions de CO₂ qui chutent de 12,2 tonnes à "
          "0,25 tonne par an."),
         ("Le plus économique sur la durée : ", "99 900 € de coût global sur "
          "20 ans, contre 105 900 € pour le scénario par étapes et 192 000 € si "
          "vous ne faites rien."),
         ("Le moins cher à réaliser : ", "85 100 € contre 88 100 € en deux "
          "temps, et un seul chantier au lieu de deux."),
         ("Si le budget initial vous inquiète, ", "l'étape 1 du scénario B "
          "reste une excellente première décision : quatre classes gagnées et "
          "une facture divisée par deux, à condition de programmer explicitement "
          "l'étape 2.")],
        couleur=VERT, fond=H_VERT_PALE, size=9.5, icone="◆")


# ==========================================================================
#  CHAPITRE 1 — ANALYSE DE LA SITUATION
# ==========================================================================
def chapitre_1():
    R.titre1("Analyse de la situation")
    R.para(
        "L'étude porte sur la rénovation énergétique d'une maison individuelle "
        "située à Saint-Jean-de-Chevelu, en Savoie (73170), en contexte rural, "
        "sur un versant orienté sud-est, à 498 m d'altitude. Le bâtiment est une "
        "ancienne ferme de la fin du XIXᵉ siècle, réhabilitée dans les années "
        "1990. La partie chauffée développe 100 m² habitables sur deux niveaux, "
        "sous des combles perdus. Une partie non chauffée est accolée à l'est : "
        "garage de 36 m², grenier de même surface et appentis à bois. C'est dans "
        "ce garage que se trouvent la chaudière propane et le ballon d'eau "
        "chaude — une implantation dont le diagnostic montrera qu'elle pèse "
        "lourdement sur le rendement.")
    R.para(
        "L'objet de l'étude est d'évaluer la performance actuelle, de "
        "hiérarchiser les sources de déperditions, puis de proposer deux "
        "scénarios de rénovation performante argumentés et chiffrés. "
        "Conformément à l'énoncé, le solaire photovoltaïque et la climatisation "
        "ne sont pas étudiés.")

    R.images_cote_a_cote(
        [(im("reperage_zone_chauffee"), "Repérage de la partie chauffée (en "
                                        "rouge) et de la partie non chauffée"),
         (im("facades_so_se"), "Façades sud-ouest et sud-est")],
        largeurs_cm=[5.8, 5.8],
        legende_globale="Volume chauffé de 100 m² et volume non chauffé accolé "
                        "à l'est")

    R.titre2("Objectifs et besoins du maître d'ouvrage")
    R.tableau([
        ["Thème", "Élément recueilli", "Conséquence pour l'étude"],
        ["Statut du bien", "Propriétaire occupant, résidence principale, bien "
                           "familial hérité, occupé depuis plus de 5 ans",
         "Éligibilité pleine à MaPrimeRénov' ; logique d'investissement de long "
         "terme"],
        ["Foyer et usage", "2 adultes et 2 enfants ; occupation classique, sans "
                           "intermittence marquée",
         "Eau chaude pour 4 personnes ; régulation programmable classique "
         "suffisante"],
        ["Confort ressenti", "Hiver très mauvais ; été acceptable ; aucune gêne "
                             "sur la qualité de l'air ni sur l'acoustique",
         "L'hiver est la priorité ; l'été est à préserver et non à corriger ; "
         "la qualité de l'air devra être maintenue après étanchéification"],
        ["Température souhaitée", "19 °C",
         "Consigne retenue pour tous les calculs de besoins et de puissance"],
        ["Besoins urgents", "Aucun : ni structure, ni toiture, ni panne "
                            "imminente",
         "Le projet peut être construit sereinement, ce qui rend crédible un "
         "scénario par étapes"],
        ["Priorité n° 1", "Économies d'énergie",
         "Réduire d'abord les besoins par l'enveloppe, puis le rendement des "
         "systèmes, puis sortir d'une énergie chère"],
        ["Priorité n° 2", "Amélioration du confort thermique",
         "Supprimer les parois froides, homogénéiser les températures, "
         "permettre d'atteindre réellement 19 °C"],
        ["Priorité n° 3", "Réduction de l'impact environnemental",
         "Matériaux biosourcés, sortie d'une énergie fossile, temps de retour "
         "carbone du chantier"],
    ], largeurs=[0.16, 0.38, 0.46], size=8,
        lignes_surlignees=(6,),
        titre="Situation, confort ressenti et hiérarchie des objectifs")

    R.para(
        "Le maître d'ouvrage n'exprime en revanche aucune demande d'extension, "
        "d'ouverture nouvelle, d'aménagement des combles ou d'aménagement "
        "intérieur ; l'installation électrique est conforme et l'assainissement "
        "individuel satisfait aux exigences du SPANC. Le périmètre est donc "
        "strictement énergétique : toute dépense n'améliorant ni la performance, "
        "ni le confort, ni la sécurité serait hors sujet et pénaliserait le reste "
        "à charge.")

    R.titre2("Moyens et attentes du maître d'ouvrage")
    R.kpi([("45 000 €", "Revenu fiscal de référence", VERT),
           ("10 000 €", "Apport personnel disponible", BLEU),
           ("300 €/mois", "Prêt à la consommation en cours", ORANGE),
           ("0 €", "Prêt immobilier en cours", GRIS)])

    R.para(
        "Avec un revenu fiscal de référence de 45 000 € pour quatre personnes "
        "hors Île-de-France, le foyer relève de la catégorie « intermédiaire » de "
        "l'Agence nationale de l'habitat : le plafond des ménages modestes "
        "s'établit à environ 41 500 € et celui des intermédiaires à environ "
        "58 000 €. Ce classement conditionne directement le taux de "
        "MaPrimeRénov' et constitue donc une donnée d'entrée du plan de "
        "financement.")

    R.para([
        ("Un paradoxe doit être souligné : ", False, NOIR),
        ("bien que classé « intermédiaire », ce foyer est en situation de "
         "précarité énergétique", True, ROUGE),
        (". Ses dépenses d'énergie représentent 12,8 % de son revenu fiscal, "
         "soit une fois et demie le seuil de 8 % retenu par l'Observatoire "
         "national de la précarité énergétique. C'est le montant de la facture, "
         "et non le niveau de revenu, qui crée ici la vulnérabilité.",
         False, NOIR)])

    R.tableau([
        ["Moyen ou attente", "Élément recueilli", "Incidence sur le projet"],
        ["Moyens humains", "Partie administrative et suivi des artisans assurés "
                           "par le maître d'ouvrage, mais aucun travaux réalisé "
                           "par lui-même",
         "Tous les postes sont chiffrés en fourni-posé, main-d'œuvre comprise"],
        ["Relogement", "Possible pendant quelques mois dans la famille",
         "Une isolation par l'intérieur resterait envisageable ; l'étude montre "
         "toutefois que l'isolation par l'extérieur est préférable, et elle "
         "évite d'avoir à mobiliser cette possibilité"],
        ["Règles d'urbanisme", "Aucune contrainte connue",
         "Isolation par l'extérieur a priori réalisable, sous réserve de la "
         "déclaration préalable et de la vérification du PLU"],
        ["Mode de chauffage", "Pas de souhait particulier, mais le maître "
                              "d'ouvrage apprécie le bois",
         "Le bois est conservé en appoint dans les deux scénarios, y compris "
         "lorsqu'il pénalise légèrement l'étiquette énergie"],
        ["Travaux déjà réalisés", "Isolation des combles (40 cm de ouate, "
                                  "R = 10 m².K/W) ; chaudière propane de 2011",
         "Deux postes à ne surtout pas refaire : c'est l'un des points "
         "structurants de cette étude"],
        ["Exigence financière", "Travaux acceptés s'ils sont justifiés par les "
                                "économies et soutenus par les aides",
         "Chaque poste proposé est relié à une déperdition mesurée et chiffré ; "
         "les postes peu rentables sont explicitement étudiés puis écartés"],
    ], largeurs=[0.16, 0.38, 0.46], size=8,
        titre="Moyens, contraintes et attentes en matière de travaux")


# ==========================================================================
#  CHAPITRE 2 — OBJECTIFS DE CONFORT
# ==========================================================================
def chapitre_2():
    R.titre1("Objectifs à atteindre pour l'amélioration du confort des habitants")
    R.para(
        "Le confort est la deuxième priorité du maître d'ouvrage, et il est "
        "indissociable de la première : le chapitre 3 démontrera que le logement "
        "n'est pas chauffé à la température souhaitée, précisément parce que le "
        "coût de l'énergie l'interdit. Économie et confort sont ici les deux "
        "faces d'un même problème.")

    R.titre2("Confort thermique en période de chauffage")
    R.para(
        "L'inconfort d'hiver a quatre causes physiques distinctes, qu'il faut "
        "traiter séparément car chacune appelle une réponse différente.")
    R.para([
        ("La température d'air n'est pas atteinte. ", True, ANTHRA),
        ("La chaleur réellement délivrée correspond à une moyenne de 15 à "
         "16 °C. Le premier objectif n'est donc pas d'améliorer une situation "
         "correcte, mais d'atteindre enfin 19 °C — ce que la division du besoin "
         "de chauffage par 5,4 rend financièrement possible.", False, NOIR)])
    R.para([
        ("L'effet de paroi froide. ", True, ANTHRA),
        ("La sensation de confort dépend de la température opérative, moyenne "
         "entre l'air et les parois. Avec Tsi = Tint − U × Rsi × (Tint − Text), "
         "par − 5 °C extérieurs et 19 °C intérieurs, un mur non isolé "
         "(U = 2,05) se stabilise à 12,6 °C et un simple vitrage (U = 4,90) à "
         "3,7 °C. Après travaux, le mur isolé atteint 18,4 °C et le double "
         "vitrage 15,0 °C. C'est la raison physique pour laquelle une passoire "
         "paraît toujours froide : il faudrait y chauffer l'air à 21 ou 22 °C "
         "pour ressentir le confort obtenu à 19 °C dans un logement isolé.",
         False, NOIR)])
    R.para([
        ("Les courants d'air. ", True, ANTHRA),
        ("L'air se refroidit au contact du simple vitrage, s'alourdit et balaie "
         "le sol ; s'y ajoutent les infiltrations par les mortaises, les grilles "
         "d'entrée d'air, la trappe de comble et les défauts du bâti — une "
         "perméabilité estimée à 3,5 m³/(h·m²) sous 4 Pa. L'objectif est de "
         "descendre sous 1,3 m³/(h·m²), contrôlé par un test d'infiltrométrie.",
         False, NOIR)])
    R.para([
        ("L'hétérogénéité entre les pièces. ", True, ANTHRA),
        ("Il n'existe aucune vanne thermostatique, et le thermostat unique est "
         "placé dans le séjour — la pièce où se trouve aussi le poêle. Quand le "
         "poêle chauffe, le thermostat est satisfait et coupe la chaudière : les "
         "chambres de l'étage ne sont alors plus chauffées du tout. L'objectif "
         "est un réglage propre à chaque pièce : 19 à 20 °C dans les pièces de "
         "vie, 17 °C dans les chambres, 22 °C dans les salles de bains.",
         False, NOIR)])

    R.tableau([
        ["Cause de l'inconfort d'hiver", "État actuel", "Objectif après travaux",
         "Moyen technique"],
        ["Température d'air non atteinte", "15 à 16 °C en moyenne",
         "19 °C toute la saison", "Division du besoin de chauffage par 5,4"],
        ["Effet de paroi froide",
         "Mur à 12,6 °C et vitrage à 3,7 °C par − 5 °C extérieurs",
         "Mur à 18,4 °C et vitrage à 15,0 °C",
         "Isolation par l'extérieur (U de 2,05 à 0,19) et double vitrage "
         "(Uw = 1,30)"],
        ["Courants d'air", "Perméabilité de 3,5 m³/(h·m²)",
         "Perméabilité ≤ 1,3 m³/(h·m²)",
         "Étanchéité à l'air, test d'infiltrométrie, menuiseries neuves"],
        ["Hétérogénéité entre pièces",
         "Aucun réglage ; thermostat faussé par le poêle",
         "Consigne propre à chaque pièce",
         "Robinets thermostatiques, thermostat programmable déporté, loi d'eau"],
    ], largeurs=[0.19, 0.23, 0.22, 0.36], size=8,
        titre="Objectifs de confort thermique d'hiver")

    R.titre2("Confort thermique en période estivale")
    R.para(
        "Le maître d'ouvrage juge son confort d'été « acceptable ». Cette "
        "information définit l'objectif : ne pas dégrader une situation "
        "satisfaisante. Le bon comportement actuel s'explique par la masse "
        "thermique considérable des 50 cm de pierre — de l'ordre de "
        "250 kJ/(m²·K) —, par les 40 cm de ouate de cellulose des combles qui "
        "procurent un déphasage d'environ 11 heures, par l'orientation sud-est "
        "qui expose la façade au soleil du matin plutôt qu'à celui de "
        "l'après-midi, par les volets bois à persiennes qui occultent sans "
        "bloquer l'air, et par l'altitude de 498 m qui garantit des nuits "
        "fraîches.")

    R.encadre(
        "Le choix technique qui protège le confort d'été",
        [("C'est l'argument décisif en faveur de l'isolation par l'extérieur. ",
          "Les 50 cm de pierre restent du côté chauffé : toute leur inertie "
          "continue de travailler pour les occupants. Une isolation par "
          "l'intérieur placerait cette masse hors du volume isolé et la perdrait "
          "entièrement — le logement surchaufferait alors en été, alors qu'il ne "
          "surchauffe pas aujourd'hui."),
         "Deux autres choix vont dans le même sens : la fibre de bois plutôt "
         "qu'un isolant synthétique, sa chaleur spécifique de 2 100 J/(kg·K) lui "
         "donnant un déphasage de 7 à 10 heures contre 2 à 3 heures pour un "
         "polystyrène ; et la conservation des volets à persiennes, souvent "
         "remplacés par des volets roulants pleins, alors qu'ils permettent "
         "d'occulter en journée tout en laissant la fenêtre ouverte — condition "
         "d'une surventilation nocturne efficace et sûre."],
        couleur=VERT, fond=H_VERT_PALE, size=9.5, icone="◆")

    R.para(
        "Un point de vigilance : le double vitrage à isolation renforcée conserve "
        "un peu plus de rayonnement solaire à l'intérieur que le simple vitrage "
        "d'origine, du fait de la couche peu émissive. L'effet reste marginal et "
        "les volets à persiennes le compensent largement, mais il conduit à "
        "retenir un vitrage de facteur solaire modéré, avec un Sw supérieur à 0,3 "
        "pour préserver les apports d'hiver sans rechercher le maximum. Aucune "
        "climatisation n'est nécessaire ni étudiée.")

    R.titre2("Qualité de l'air intérieur")
    R.para(
        "Le maître d'ouvrage ne déclare aucune gêne, ce qui s'explique "
        "simplement : un bâtiment très perméable se ventile abondamment par ses "
        "défauts d'étanchéité. Cette ventilation « gratuite » coûte pourtant "
        "76,5 W/K, soit 14 % des déperditions, et elle est entièrement subie — "
        "très forte par grand vent ou grand froid, au moment où elle coûte le "
        "plus cher, quasi nulle par temps calme. Elle n'assure enfin aucun "
        "balayage organisé, les entrées d'air n'étant présentes que dans les "
        "chambres et le séjour.")

    R.encadre(
        "La ventilation mécanique n'est pas une option mais une obligation",
        ["Dès lors que l'on isole par l'extérieur, que l'on remplace les "
         "menuiseries et que l'on traite l'étanchéité à l'air, cette ventilation "
         "parasite disparaît. Sans ventilation mécanique en contrepartie, on "
         "créerait un problème de qualité de l'air là où il n'en existait pas : "
         "humidité, condensation sur les points froids résiduels, moisissures, "
         "accumulation de composés organiques volatils et de dioxyde de carbone.",
         "C'est également une obligation réglementaire au titre de l'arrêté du "
         "24 mars 1982, qui impose une ventilation générale et permanente avec "
         "balayage de l'ensemble du logement."],
        couleur=ORANGE, fond=H_ORANGE_PALE, size=9.5)

    R.para(
        "Un second point est spécifique au territoire : la Savoie compte de "
        "nombreuses communes classées en zone à potentiel radon de catégorie 3. "
        "Ce gaz radioactif naturel, deuxième cause de cancer du poumon en France, "
        "pénètre par le plancher bas — ici une dalle sur terre-plein non ventilé, "
        "configuration favorable à son accumulation. Une mesure par dosimètre, "
        "d'environ 30 €, est recommandée avant travaux ; au-delà de 300 Bq/m³, "
        "l'étanchement des traversées du plancher et le réglage de la ventilation "
        "suffisent à traiter le problème.")

    R.titre2("Confort visuel")
    R.para(
        "L'éclairage naturel est satisfaisant : 15,45 m² de menuiseries, soit "
        "15,5 % de la surface habitable, dont 80 % orientés au sud-est. Deux "
        "points appellent l'attention. La pose en tunnel, dans des tableaux de "
        "50 cm, réduit l'angle de ciel visible et l'éclairement en fond de "
        "pièce : le repositionnement des menuiseries au nu extérieur, rendu "
        "possible par l'isolation par l'extérieur, corrigera ce défaut. Le "
        "vitrage retenu devra par ailleurs présenter une transmission lumineuse "
        "supérieure à 0,70 pour ne pas assombrir les pièces.")
    R.para(
        "L'éclairage artificiel représente 200 W installés, dont 25 % "
        "d'halogènes, qui consomment cinq à six fois plus qu'une LED de flux "
        "équivalent. Leur remplacement ramène la puissance installée à environ "
        "110 W et la consommation de 300 à 150 kWh par an, avec des sources à "
        "indice de rendu des couleurs supérieur à 80 : 2 700 à 3 000 K dans les "
        "pièces de vie, 4 000 K en cuisine et salles de bains.")


# ==========================================================================
#  CHAPITRE 3 — ANALYSE TECHNIQUE DE L'EXISTANT
# ==========================================================================
def chapitre_3():
    R.titre1("Analyse technique de l'existant")
    R.para(
        "Ce chapitre confronte trois sources : l'observation du bâti lors de la "
        "visite technique, le calcul thermique, et les factures relevées sur "
        "cinq ans. Les relevés détaillés figurent en annexe 8.1 et le détail "
        "des calculs en annexe 8.2.")

    R.titre2("Description et analyse du bâtiment existant")
    R.images_cote_a_cote(
        [(im("plan_rdc"), "Plan du rez-de-chaussée"),
         (im("plan_etage"), "Plan de l'étage")],
        largeurs_cm=[5.9, 5.7],
        legende_globale="Plans cotés — la partie chauffée est accolée au garage "
                        "non chauffé, à droite sur les plans")

    R.para(
        "Le rez-de-chaussée regroupe les pièces de vie et les locaux de service, "
        "l'étage les trois chambres et une seconde salle de bains. Les combles "
        "perdus sont accessibles par une échelle depuis la zone non chauffée — "
        "un détail important pour le traitement de la trappe. Le relevé des "
        "plans cotés donne 99,4 m² habitables, ce qui confirme les 100 m² de "
        "l'énoncé, pour un volume chauffé de 250 m³. La surface déperditive "
        "atteint 308,1 m², soit une compacité de 3,08 — valeur élevée, "
        "caractéristique d'une maison individuelle peu compacte, qui rend "
        "l'isolation d'autant plus déterminante.")

    R.titre3("Conception bioclimatique")
    R.para(
        "Le bâtiment est implanté sur un versant sud-est, à 498 m d'altitude, en "
        "contexte rural. La conception d'origine est intuitivement "
        "bioclimatique : 12,33 m² sur 15,45 m² de vitrage, soit 80 %, se "
        "trouvent sur la façade sud-est, tandis que la façade nord-ouest ne "
        "comporte qu'une lucarne de 0,20 m². Les volumes non chauffés — garage "
        "et grenier — jouent le rôle d'espace tampon à l'est.")

    R.images_cote_a_cote(
        [(im("vue_aerienne"), "Vue aérienne (source IGN, BD ORTHO)"),
         (im("masque_solaire"), "Diagramme du masque solaire lointain")],
        largeurs_cm=[5.8, 5.8],
        legende_globale="Implantation et masque solaire lointain constitué par "
                        "le relief")

    R.para(
        "Le masque lointain formé par le relief écrête les apports en début et "
        "en fin de journée : un coefficient de réduction de 0,8 leur a été "
        "appliqué. L'exposition reste favorable, les apports solaires utiles "
        "étant évalués à 2 200 kWh par an, soit 6 % des besoins bruts de "
        "chauffage. L'altitude place le bâtiment en zone climatique H1c, avec "
        "une température extérieure de base de − 12 °C et des DJU19 corrigés de "
        "2 860 °C.j (calcul au § 3.3). L'inertie des 50 cm de pierre, de l'ordre "
        "de 250 kJ/(m²·K), est un atout majeur pour le confort d'été — à "
        "condition de ne pas la neutraliser par une isolation intérieure.")

    R.titre3("Description des parois opaques et vitrées")
    R.images_cote_a_cote(
        [(im("menuiseries_tunnel"), "Menuiseries bois en simple vitrage, "
                                    "posées en tunnel"),
         (im("facade_so"), "Façade sud-ouest — enduit en bon état, sans "
                           "fissuration")],
        largeurs_cm=[4.8, 6.4],
        legende_globale="Un enduit de façade sain, qui rend l'isolation par "
                        "l'extérieur possible, et des menuiseries entièrement "
                        "à reprendre")

    R.tableau([
        ["Paroi", "Composition", "R (m².K/W)", "U (W/m².K)", "Surface (m²)",
         "État"],
        ["Murs vers extérieur",
         "Pierre calcaire 50 cm (λ = 2,0), enduit de façade, enduit plâtre "
         "intérieur — aucune isolation",
         "0,48", "2,05", "125,0",
         "Enduit sain. Poste de déperdition n° 1"],
        ["Murs vers local non chauffé",
         "Idem, donnant sur le garage (coefficient de réduction b = 0,85)",
         "0,55", "1,81", "52,6",
         "Bon état. Poste souvent négligé : 15 % des pertes"],
        ["Mur de refend", "Pierre — paroi intérieure au volume chauffé", "—",
         "—", "—", "Non déperditif ; contribue à l'inertie"],
        ["Cloisons", "Briques de plâtre", "—", "—", "—",
         "Non déperditives, bon état"],
        ["Plancher bas",
         "Dalle béton sur terre-plein non ventilé, sans isolation ni coupure de "
         "capillarité (2S/P = 4,6)",
         "1,82", "0,55", "57,5",
         "Non isolé ; non traitable à coût raisonnable (§ 4.1)"],
        ["Plancher intermédiaire", "Bois — paroi intérieure", "—", "—", "—",
         "Perméable à l'air en périphérie"],
        ["Plafond sous combles perdus",
         "Plaques de plâtre suspendues sous plancher bois, 40 cm de ouate de "
         "cellulose avec pare-vapeur (λ = 0,039)",
         "10,50", "0,10", "57,5",
         "Récente et performante. Aucun travail à prévoir"],
        ["Menuiseries — fenêtres et portes-fenêtres",
         "Bois, simple vitrage, pose en tunnel, mortaises et grilles d'entrée "
         "d'air",
         "0,20", "4,90", "13,40",
         "Vétustes. Vitrage à 3,7 °C par temps froid"],
        ["Menuiserie — porte d'entrée", "Bois, 50 % vitrée en simple vitrage",
         "0,25", "4,00", "2,05", "Vétuste, à remplacer"],
        ["Couverture", "Tuiles mécaniques récentes, sans écran de sous-toiture",
         "—", "—", "—",
         "Hors volume chauffé ; vigilance sur l'exposition de la ouate"],
        ["Ensemble de l'enveloppe", "", "", "Ubat = 1,55", "308,1", ""],
    ], largeurs=[0.15, 0.27, 0.09, 0.09, 0.10, 0.30], size=8,
        align_centre_cols=(2, 3, 4), lignes_surlignees=(11,),
        titre="Synthèse des parois opaques et vitrées")

    R.encadre(
        "Le point qui distingue cette étude : les combles sont déjà isolés",
        ["Dans la plupart des rénovations de maisons anciennes, l'isolation des "
         "combles est le premier geste : peu coûteuse, très rentable, et la "
         "toiture pèse couramment 25 à 30 % des déperditions.",
         "Ici ce travail a déjà été fait, et bien fait : 40 cm de ouate de "
         "cellulose avec pare-vapeur, R = 10 m².K/W, très au-delà des 7 exigés "
         "pour les aides. Le plafond ne représente plus que 1 % des déperditions.",
         "Il ne faut donc surtout pas refaire ce poste : le budget doit aller "
         "aux murs, aux menuiseries et à la ventilation. Cette particularité "
         "modifie la hiérarchie des travaux, et — comme le montrera le "
         "chapitre 5 — jusqu'au choix du générateur de chauffage."],
        couleur=VERT, fond=H_VERT_PALE, size=9.5, icone="◆")

    R.titre3("Identification des ponts thermiques")
    R.para(
        "Dans un bâtiment entièrement dépourvu d'isolation, les ponts thermiques "
        "sont paradoxalement moins pénalisants qu'ils ne le seront après "
        "travaux : il n'existe pas de rupture d'isolant, puisqu'il n'y a pas "
        "d'isolant. Ils représentent 27,7 W/K, soit 5 % du bilan. Leur "
        "traitement reste essentiel, car après isolation ils deviendraient les "
        "principaux points faibles et les zones privilégiées de condensation.")

    R.tableau([
        ["Jonction", "Longueur", "ψ (W/m·K)", "Déperdition",
         "Proposition de traitement", "ψ traité"],
        ["Mur extérieur / plancher bas", "25,09 m", "0,45", "11,3 W/K",
         "Isolant de soubassement descendu 60 cm sous le niveau du terrain, en "
         "matériau non sensible à l'eau", "0,20"],
        ["Mur extérieur / plafond sous combles", "25,09 m", "0,30", "7,5 W/K",
         "Continuité de l'isolation par l'extérieur jusqu'à la sablière, en "
         "recouvrement de l'isolant des combles", "0,05"],
        ["Mur extérieur / plancher intermédiaire", "25,09 m", "0,10", "2,5 W/K",
         "Traité en continu par l'isolation par l'extérieur", "0,02"],
        ["Tableaux et linteaux de baies", "47,0 m", "0,10", "4,7 W/K",
         "Menuiseries repositionnées au nu extérieur, retour d'isolant de 40 mm "
         "en tableau et sur appuis", "0,02"],
        ["Angles de murs extérieurs", "22,4 m", "0,05", "1,1 W/K",
         "Traités en continu, avec profilés d'angle", "0,01"],
        ["Mur extérieur / mur de refend", "11,0 m", "0,05", "0,6 W/K",
         "Traité en continu par l'isolation par l'extérieur", "0,01"],
        ["Mur extérieur / mur mitoyen du garage", "11,2 m", "—", "Inclus",
         "Retour d'isolant de 1 m dans le garage pour éviter la coupure "
         "d'isolation en angle", "—"],
        ["Total", "", "", "27,7 W/K", "Après travaux : 8,1 W/K, soit − 71 %",
         ""],
    ], largeurs=[0.21, 0.09, 0.09, 0.10, 0.42, 0.09], size=8,
        align_centre_cols=(1, 2, 3, 5), lignes_surlignees=(7,),
        titre="Ponts thermiques identifiés et traitement proposé")

    R.titre3("Étanchéité à l'air et qualité de l'air intérieur")
    R.para(
        "Aucun test d'infiltrométrie n'a été réalisé : la valeur retenue dans "
        "les calculs doit donc être justifiée, car elle pèse 14 % du bilan. Les "
        "indices relevés lors de la visite sont convergents : menuiseries bois "
        "en simple vitrage d'origine posées en tunnel, mortaises et grilles "
        "d'entrée d'air, plancher intermédiaire en bois perméable en périphérie, "
        "trappe de comble non traitée donnant sur un local non chauffé, et "
        "absence de toute membrane ou enduit d'étanchéité à l'air.")
    R.para(
        "Les valeurs de référence s'échelonnent de 2,5 à 4,0 m³/(h·m²) pour une "
        "maison ancienne non traitée, contre 1,3 pour une rénovation performante "
        "et 0,6 pour un bâtiment neuf. La valeur retenue est "
        "Q4Pa-surf = 3,5 m³/(h·m²), hypothèse médiane haute, qui se traduit par "
        "un renouvellement d'air global de 0,90 vol/h — environ 0,45 de "
        "ventilation par les entrées d'air et l'ouverture des fenêtres, et 0,45 "
        "d'infiltrations parasites — soit Dr = 0,34 × 0,90 × 250 = 76,5 W/K. "
        "Cette hypothèse est validée par recoupement avec les factures au "
        "§ 3.3 : un renouvellement notablement plus faible conduirait à un "
        "besoin théorique inférieur à la chaleur réellement délivrée, ce qui "
        "serait incompatible avec l'inconfort déclaré. Un test avant travaux "
        "reste recommandé, pour confirmer cette valeur et localiser les fuites.")
    R.para(
        "Sur la qualité de l'air, le constat est celui d'une ventilation "
        "entièrement subie, développé au § 2.3 : abondante mais erratique, sans "
        "balayage organisé, et appelée à disparaître avec les travaux. Une "
        "ventilation mécanique devra impérativement lui succéder.")

    R.titre3("Description détaillée des systèmes et de leur régulation")
    R.images_cote_a_cote(
        [(im("chaudiere_propane"), "Chaudière propane (2011), dans le garage"),
         (im("ballon_ecs"), "Ballon électrique de 200 L, dans le local non "
                            "chauffé"),
         (im("poele_buches"), "Poêle à bûches de 6 kW (2010), non étanche")],
        largeurs_cm=[3.2, 3.2, 3.2],
        legende_globale="Les trois équipements de production de chaleur, tous "
                        "implantés ou conçus de manière défavorable")

    R.tableau([
        ["Équipement", "Caractéristiques", "Rendement global", "Régulation",
         "État et analyse"],
        ["Chaudière propane",
         "Basse température, 2011, dans le garage non chauffé ; cuve enterrée",
         "0,65 (voir § 5.3)",
         "Thermostat d'ambiance non programmable dans le séjour ; aucune sonde "
         "extérieure",
         "Âgée de 15 ans, encore fonctionnelle. Implantation en local non chauffé "
         "et absence de sonde : rendement fortement dégradé"],
        ["Émetteurs",
         "7 radiateurs fonte 4 colonnes, hauteur 930 mm : 2 de 660 mm (salles "
         "de bains) et 5 de 1 100 mm (cuisine, salon, 3 chambres)",
         "0,95 (émission)", "Aucune vanne thermostatique",
         "Fort volume d'eau (≈ 380 L) et 16,25 kW en 75/65 : atout majeur (§ 5.1)"],
        ["Distribution",
         "Réseau bitube, non isolé, haute température, traversant le garage",
         "0,88 (distribution)", "Aucun équilibrage connu",
         "Chaque mètre non isolé est une perte intégrale : le calorifugeage est "
         "l'un des gestes les plus rentables"],
        ["Appoint bois",
         "Poêle à bûches de 2010, 6 kW, sans label Flamme Verte, non étanche et "
         "sans amenée d'air",
         "0,55", "Manuelle (allure de combustion)",
         "Rendement faible, particules élevées, et risque de sécurité dès qu'une "
         "VMC est installée"],
        ["Eau chaude sanitaire",
         "Ballon électrique ancien de 200 L, dans le garage non chauffé",
         "0,62 (stockage et distribution)",
         "Thermostat de ballon seul, aucune programmation en heures creuses",
         "Effet Joule et pertes aggravées par le local froid : 3 065 kWh pour "
         "1 902 kWh utiles"],
        ["Ventilation",
         "Naturelle, par ouverture des fenêtres, mortaises et grilles d'entrée "
         "d'air", "—", "Aucune",
         "Non conforme à l'arrêté de 1982 ; débits non maîtrisés"],
        ["Production de froid", "Aucune climatisation", "—", "—",
         "Non nécessaire : confort d'été jugé acceptable"],
        ["Éclairage", "200 W installés : 25 % d'halogènes, 75 % de LED", "—",
         "Interrupteurs simples",
         "Puissance ramenée à 110 W pour 300 €"],
        ["Appareils domestiques",
         "Plaques vitrocéramiques et four électriques ; électroménager courant",
         "—", "—",
         "≈ 2 027 kWh/an ; traité dans le plan de sobriété (§ 8.10)"],
    ], largeurs=[0.13, 0.24, 0.11, 0.19, 0.33], size=8,
        titre="Systèmes, rendements et régulation")

    R.encadre(
        "Un défaut de conception à l'origine d'une grande part de l'inconfort",
        ["Le thermostat unique est installé dans le séjour — la pièce où se "
         "trouve aussi le poêle à bûches. Lorsque le poêle fonctionne, le séjour "
         "monte vite en température, le thermostat est satisfait et il coupe la "
         "chaudière. À cet instant, les trois chambres et les salles de bains, "
         "qui ne bénéficient d'aucun apport du poêle, ne sont plus chauffées du "
         "tout — et en l'absence de vannes thermostatiques, aucune correction "
         "n'est possible.",
         "C'est l'explication la plus probable de l'écart de température entre "
         "les pièces, et cela ne coûte que quelques centaines d'euros à "
         "corriger : vannes thermostatiques, thermostat déporté et pilotage par "
         "loi d'eau sur sonde extérieure (§ 5.4)."],
        couleur=BLEU, fond=H_BLEU_PALE, size=9.5)

    R.titre3("Pathologies observées et causes")
    R.para(
        "Aucune pathologie n'a été observée et le maître d'ouvrage n'en signale "
        "aucune. Ce constat favorable conditionne la faisabilité du projet, mais "
        "il n'exclut pas des risques latents qu'il faut lever avant d'engager "
        "les travaux.")

    R.tableau([
        ["Élément examiné", "Constat", "Analyse et conséquence"],
        ["Structure et enduit de façade", "Aucune fissuration ni décollement",
         "Maçonnerie très stable ; un enduit sain traduit l'absence "
         "d'accumulation d'humidité. Condition vérifiée pour l'isolation par "
         "l'extérieur"],
        ["Humidité ascensionnelle", "Aucune trace de salpêtre ni de "
                                    "décollement en pied de mur",
         "Le mur repose néanmoins sur un terre-plein sans coupure de "
         "capillarité : vérification en pied de mur et isolant de soubassement "
         "non sensible à l'eau"],
        ["Condensation et moisissures", "Aucune trace signalée",
         "Expliqué par la très forte ventilation parasite. Le risque "
         "apparaîtrait si l'on étanchéifiait sans ventiler"],
        ["Couverture et isolant des combles",
         "Tuiles récentes, sans écran de sous-toiture ; ouate sans tassement",
         "Vérifier l'absence de pénétration de neige poudreuse sur l'isolant et "
         "la ventilation du comble"],
        ["Réseaux, amiante et plomb",
         "Électricité et assainissement conformes ; absence d'amiante déclarée",
         "Bâtiment antérieur à 1997 : repérage avant travaux recommandé sur les "
         "matériaux des années 1990"],
        ["Appareil à combustion", "Poêle non étanche, sans amenée d'air",
         "Acceptable aujourd'hui grâce à la perméabilité du bâti ; deviendra "
         "dangereux après étanchéification et pose d'une VMC"],
    ], largeurs=[0.18, 0.27, 0.55], size=8,
        lignes_surlignees=(6,),
        titre="Pathologies observées, risques latents et causes")

    R.encadre(
        "Le seul véritable risque identifié : le poêle non étanche et la VMC",
        ["Aujourd'hui, le poêle non étanche ne pose pas de problème : le "
         "bâtiment est si perméable que l'air de combustion arrive sans "
         "difficulté.",
         "Après travaux, la situation s'inverse. L'enveloppe devient étanche et "
         "la VMC met le logement en légère dépression permanente. Le conduit de "
         "fumée devient alors une entrée d'air potentielle : les fumées peuvent "
         "refouler dans la pièce, avec un risque d'intoxication au monoxyde de "
         "carbone.",
         ("Le remplacement du poêle par un modèle étanche raccordé sur air "
          "extérieur n'est donc pas un choix de confort mais une obligation de "
          "sécurité", " dès lors qu'une VMC est installée. Ce poste, chiffré à "
          "5 200 €, est intégré au socle commun des deux scénarios ; il apporte "
          "au passage un gain de rendement de 55 % à 78 % et une forte réduction "
          "des émissions de particules fines.")],
        couleur=ROUGE, fond=H_ROUGE_PALE, size=9.5, icone="◆")

    R.titre3("Travaux déjà réalisés")
    R.para(
        "Deux travaux significatifs ont été réalisés avant l'étude, et leur "
        "identification est essentielle : ils déterminent ce qu'il ne faut pas "
        "refaire. L'isolation des combles perdus, il y a quelques années, met en "
        "œuvre 40 cm de ouate de cellulose en vrac avec pare-vapeur sur le "
        "plancher bois du grenier, soit R > 10 m².K/W — très au-delà des "
        "7 m².K/W exigés pour les aides. Le plafond ne pèse plus que 1 % des "
        "déperditions : aucun travail d'isolation n'est à reprendre, seuls la "
        "trappe d'accès et le raccord périphérique restant à traiter. Le "
        "remplacement de la chaudière, en 2011, a installé une chaudière propane "
        "basse température sur cuve enterrée : équipement de 15 ans, encore "
        "fonctionnel, mais dont le rendement global n'est que de 0,65 du fait de "
        "son implantation et de sa régulation — c'est ce qui rend crédible le "
        "scénario par étapes. La réhabilitation générale des années 1990 n'a "
        "quant à elle comporté aucune isolation thermique, ce qui était l'usage.")

    R.titre2("Bilan des déperditions de l'existant")
    R.calcul([
        "GV = Ds + Dl + Dr",
        "",
        "Ds — déperditions surfaciques = Σ (U × A × b)",
        "   Murs extérieurs        : 125,0 × 2,05                = 256,3 W/K",
        "   Mur mitoyen du garage  :  52,6 × 1,81 × 0,85         =  80,9 W/K",
        "   Menuiseries            : 13,40 × 4,90 + 2,05 × 4,00  =  73,9 W/K",
        "   Plafond sous combles   :  57,5 × 0,10                =   5,8 W/K",
        "   Plancher bas           :  57,5 × 0,55                =  31,6 W/K",
        "                                                  Ds    = 448,5 W/K",
        "Dl — ponts thermiques = Σ (ψ × L)                       =  27,7 W/K",
        "Dr — renouvellement d'air = 0,34 × 0,90 × 250 m³        =  76,5 W/K",
        "=> GV = 552,7, soit 553 W/K",
        "",
        "   Ubat = (448,5 + 27,7) / 308,1 = 1,55 W/m².K",
        "   (référence ≈ 0,50 : enveloppe trois fois moins performante)",
        "   P = GV × (19 − (− 12)) = 553 × 31 = 17 143 W, soit 17,1 kW",
        "   soit 171 W/m² habitable ; 19 kW à installer avec relance",
    ], titre="Coefficient de déperditions, Ubat et puissance de chauffage")

    R.figure(fg("04_deperditions"), largeur_cm=11.6,
             legende="Hiérarchie des déperditions : les murs concentrent 61 % "
                     "des pertes")

    R.para(
        "La hiérarchie est sans ambiguïté et fixe l'ordre des travaux : les "
        "murs extérieurs (46 %) sont la priorité absolue, seul poste dont le "
        "traitement change l'échelle du bilan ; viennent ensuite le mur mitoyen "
        "du garage (15 %), poste souvent négligé mais simple à traiter par le "
        "côté du garage, le renouvellement d'air (14 %) et les menuiseries "
        "(13 %). Le plancher bas (6 %) ne fera l'objet que d'un traitement "
        "périphérique, justifié au § 4.1 ; les ponts thermiques (5 %) sont "
        "traités sans surcoût par l'isolation par l'extérieur ; et le plafond "
        "(1 %), déjà isolé, ne demande aucun travail.")

    R.titre2("Comparaison des consommations théoriques avec les factures")
    R.tableau([
        ["Saison", "Propane (kg)", "Bois (stères)", "Électricité (kWh)",
         "DJU18 station (°C.j)"],
        ["2020-2021", "2 522", "7", "5 680", "2 397,2"],
        ["2021-2022", "2 252", "7", "5 521", "2 422,8"],
        ["2022-2023", "1 456", "7", "5 743", "2 121,9"],
        ["2023-2024", "1 473", "7", "5 521", "2 069,8"],
        ["2024-2025", "1 653", "7", "5 743", "2 142,4"],
        ["Moyenne", "1 871", "7", "5 642", "2 230,8"],
    ], largeurs=[0.20, 0.20, 0.19, 0.21, 0.20], size=8,
        align_centre_cols=(1, 2, 3, 4), lignes_surlignees=(6,),
        titre="Consommations relevées sur cinq saisons de chauffe")

    R.para(
        "Converties en énergie finale — 12,78 kWh par kilogramme de propane et "
        "1 600 kWh par stère de feuillus durs — ces quantités représentent "
        "23 912 kWh de propane, 11 200 kWh de bois et 5 642 kWh d'électricité, "
        "soit 40 754 kWh par an ou 408 kWh/m².an.")

    R.figure(fg("01_consommations"), largeur_cm=11.6,
             legende="Consommations de propane rapportées à la rigueur "
                     "climatique de chaque saison")

    R.titre3("Correction climatique : ce que les factures disent vraiment")
    R.para(
        "Entre 2021-2022 et 2022-2023, la consommation de propane chute de 35 % "
        "en une seule année, tandis que les degrés-jours passent de 2 423 à "
        "2 122. Pour savoir si le climat suffit à l'expliquer, chaque saison est "
        "ramenée à une rigueur commune, la moyenne des cinq années : "
        "consommation corrigée = consommation relevée × (2 230,8 / DJU de "
        "l'année). Le résultat est sans ambiguïté — 2 347, 2 074, 1 531, 1 588 "
        "puis 1 721 kg. À climat constant, la baisse persiste et atteint 27 % en "
        "cinq ans.")
    R.para(
        "Le climat n'explique qu'un tiers de la baisse. Les deux autres tiers "
        "sont comportementaux et coïncident avec la flambée des prix de 2022 : "
        "le foyer a réduit sa consigne pour tenir son budget. Le fait que la "
        "consommation de bois reste rigoureusement fixe à 7 stères confirme cette "
        "lecture — elle correspond à la capacité maximale d'approvisionnement et "
        "de stockage de l'appentis, si bien que le poêle tourne déjà à plein "
        "régime. L'ajustement s'est donc fait uniquement sur le propane, énergie "
        "payante et modulable.")

    R.titre3("Correction des degrés-jours et confrontation aux factures")
    R.calcul([
        "Correction des DJU (saison de chauffe : octobre à mai, 243 jours)",
        "   Altitude : (498 − 235) / 100 × 0,6 °C = 1,58 °C  ->  + 384 °C.j",
        "   Base de température (18 °C vers 19 °C)           ->  + 243 °C.j",
        "=> DJU19 au droit du bâtiment : 2 231 + 384 + 243 = 2 858, soit 2 860 °C.j",
        "   Rapport aux DJU18 bruts : 2 860 / 2 231 = 1,28",
        "",
        "A — Besoin de chauffage théorique à 19 °C",
        "   Besoins bruts = 553 × 2 860 × 24 / 1000            = 37 959 kWh/an",
        "   Apports utiles (internes 2 449 + solaires 2 200) × 0,88 = 4 091 kWh",
        "=> Besoin net : 33 900 kWh/an, soit 339 kWh/m².an",
        "",
        "B — Chaleur réellement délivrée d'après les factures",
        "   Propane : 23 912 × 0,65 (rendement global)  = 15 543 kWh utiles",
        "   Bois    : 11 200 × 0,55 (poêle non labellisé) = 6 160 kWh utiles",
        "=> Chaleur utile fournie : environ 21 700 kWh/an",
        "",
        "C — Écart : il manque 12 200 kWh, soit 36 % du besoin à 19 °C",
        "   DJU équivalent = (21 700 + 4 091) × 1000 / (553 × 24) = 1 943 °C.j",
        "   Écart : (2 860 − 1 943) / 243 = 3,8 °C",
        "=> Température intérieure moyenne réelle : 15 à 16 °C",
    ], titre="Correction des degrés-jours et comparaison théorique / factures",
        couleur=ROUGE)

    R.encadre(
        "Le diagnostic central de cette étude",
        ["Le maître d'ouvrage juge son confort d'hiver « très mauvais ». Le "
         "calcul lui donne raison et le quantifie : le logement est chauffé "
         "entre 15 et 16 °C en moyenne, soit 3 à 4 °C sous la consigne "
         "souhaitée. Concrètement, un salon correct près du poêle et des "
         "chambres à 13 ou 14 °C.",
         "Ce résultat a une conséquence méthodologique : comparer la facture "
         "actuelle à celle d'après travaux revient à comparer deux niveaux de "
         "confort différents, ce qui sous-estime le bénéfice réel. L'analyse "
         "économique présente donc les deux comparaisons, à confort réel et à "
         "confort équivalent de 19 °C.",
         ("À 19 °C, la facture actuelle atteindrait 8 653 € par an.", " C'est le "
          "véritable coût du confort que le foyer ne s'autorise pas.")],
        couleur=ROUGE, fond=H_ROUGE_PALE, size=9.5, icone="◆")

    R.images_cote_a_cote(
        [(fg("03_postes_depense"), "Le chauffage pèse près des trois quarts de "
                                   "la dépense"),
         (fg("13_comparaison_nationale"), "Comparaison à la moyenne du parc "
                                          "français")],
        largeurs_cm=[5.6, 5.9],
        legende_globale="Répartition de la dépense et mise en perspective de la "
                        "consommation")

    R.para([
        ("Rapportée au revenu fiscal de 45 000 €, la dépense de 5 739 € "
         "représente un taux d'effort de ", False, NOIR),
        ("12,8 %", True, ROUGE),
        (", alors que l'Observatoire national de la précarité énergétique "
         "situe le seuil à 8 %. Ramené à 19 °C, ce taux atteindrait 19 % : le "
         "logement est aujourd'hui inhabitable dans des conditions normales de "
         "confort sans que le budget du foyer n'explose. Les prix retenus sont "
         "ceux du marché 2026 — 1,80 €/kg de propane avec 180 € de location de "
         "citerne, 90 € le stère et 0,25 €/kWh d'électricité — et font l'objet "
         "d'une analyse de sensibilité en annexe 8.6.", False, NOIR)])

    R.titre2("Évaluation de l'étiquette DPE de l'existant")
    R.para(
        "Le DPE évalue le logement selon deux axes, la consommation d'énergie "
        "primaire et les émissions de gaz à effet de serre, l'étiquette retenue "
        "étant la plus défavorable. Le calcul est conventionnel, à 19 °C, ce qui "
        "explique que la consommation de propane retenue (42 677 kWh) dépasse "
        "celle des factures : elle correspond au besoin de 33 900 kWh utiles, "
        "diminué de la part couverte par le poêle, et divisé par le rendement "
        "global de 0,65.")

    R.tableau([
        ["Poste", "Énergie", "Énergie finale", "Coef. EP", "Énergie primaire",
         "Facteur CO₂", "Émissions"],
        ["Chauffage — chaudière", "Propane", "42 677 kWh", "1,0", "42 677 kWh",
         "0,272", "11 608 kg"],
        ["Chauffage — poêle", "Bois", "11 200 kWh", "1,0", "11 200 kWh",
         "0,030", "336 kg"],
        ["Eau chaude sanitaire", "Électricité", "3 065 kWh", "2,3", "7 050 kWh",
         "0,079", "242 kg"],
        ["Éclairage", "Électricité", "300 kWh", "2,3", "690 kWh", "0,079",
         "24 kg"],
        ["Auxiliaires", "Électricité", "250 kWh", "2,3", "575 kWh", "0,079",
         "20 kg"],
        ["Total", "", "57 492 kWh", "", "62 192 kWh", "", "12 230 kg"],
        ["Par m² habitable", "", "", "", "622 kWh EP/m².an", "",
         "122 kg CO₂/m².an"],
    ], largeurs=[0.19, 0.11, 0.14, 0.10, 0.16, 0.10, 0.14], size=8,
        align_centre_cols=(1, 2, 3, 4, 5, 6), lignes_surlignees=(6, 7),
        titre="Calcul du DPE de l'existant selon la logique de la méthode 3CL")

    R.figure(fg("05_dpe_existant"), largeur_cm=10.4,
             legende="Étiquettes énergie et climat de l'état existant : "
                     "classe G sur les deux axes")

    R.para(
        "Avec 622 kWh EP/m².an, le seuil de la classe G — fixé à 420 — est "
        "dépassé de moitié ; avec 122 kg CO₂/m².an, celui de 100 l'est également, "
        "le propane en étant responsable à 95 %. Le logement est donc une "
        "passoire thermique au sens de la loi Climat et Résilience, et consomme "
        "environ deux fois et demie la moyenne du parc résidentiel français, "
        "estimée autour de 250 kWh EP/m².an. Cette classe G a une conséquence "
        "juridique : depuis le 1ᵉʳ janvier 2025, ces logements ne peuvent plus "
        "être proposés à la location. Le maître d'ouvrage étant occupant, "
        "l'interdiction ne l'affecte pas directement, mais elle pèse sur la "
        "valeur du bien — les études notariales évaluent la décote d'une "
        "passoire entre 10 et 20 % du prix de vente.")



# ==========================================================================
#  CHAPITRE 4 — LES SCÉNARIOS DE RÉNOVATION
# ==========================================================================
def chapitre_4():
    R.titre1("Les scénarios de rénovation")
    R.para(
        "Les deux scénarios visent une rénovation énergétique performante au "
        "sens du 17° bis de l'article L.111-1 du code de la construction et de "
        "l'habitation : atteindre la classe A ou B — un gain d'au moins deux "
        "classes suffisant pour un bâtiment initialement classé F ou G — et "
        "traiter six postes de travaux ainsi que leurs interfaces.")

    R.tableau([
        ["Poste imposé par le CCH", "Traitement", "Justification"],
        ["Isolation des murs", "Intégral",
         "Isolation par l'extérieur en fibre de bois 180 mm sur les murs "
         "extérieurs (R = 4,74) et laine de roche 140 mm sur le mur mitoyen "
         "(R = 4,00)"],
        ["Isolation des planchers bas", "Partiel",
         "Traitement périphérique par descente de l'isolant en soubassement. "
         "L'isolation complète est écartée au titre du coût manifestement "
         "disproportionné, démontré ci-après"],
        ["Isolation de la toiture", "Déjà réalisé",
         "40 cm de ouate de cellulose, R = 10 m².K/W. Seuls la trappe d'accès et "
         "le raccord périphérique sont repris"],
        ["Remplacement des menuiseries", "Intégral",
         "9 ouvrants et 1 porte d'entrée, Uw = 1,30 W/m².K, pose au nu extérieur"],
        ["Ventilation", "Intégral",
         "VMC hygroréglable de type B, dimensionnée selon l'arrêté du "
         "24 mars 1982, avec traitement de l'étanchéité à l'air"],
        ["Production de chauffage et d'ECS", "Intégral",
         "Pompe à chaleur air/eau et chauffe-eau thermodynamique (scénario A) ; "
         "optimisation puis remplacement (scénario B)"],
        ["Interfaces entre les postes", "Traité",
         "Quinze interfaces identifiées, avec prescription et ordre "
         "d'intervention — détail en annexe 8.4"],
    ], largeurs=[0.22, 0.11, 0.67], size=8,
        titre="Traitement des six postes de la rénovation performante")

    R.calcul([
        "Dérogation invoquée pour le plancher bas (coût manifestement dispro-",
        "portionné, prévu par le CCH) — dalle sur terre-plein, sans vide",
        "sanitaire : la seule solution serait d'isoler par-dessus.",
        "",
        "   Gain thermique : Ue de 0,45 à 0,25  ->  57,5 × 0,20 = 11,5 W/K",
        "   Économie : 11,5 × 2 860 × 24 / 1000 = 789 kWh/an, soit ≈ 60 €/an",
        "   Coût : dépose des sols, isolant, chape, réfection, huisseries",
        "          ≈ 18 000 € TTC, hors relogement, et 12 cm de hauteur perdus",
        "=> Temps de retour supérieur à 250 ans : le poste est écarté",
        "",
        "Solution retenue : l'isolant de façade est descendu 60 cm sous le",
        "niveau du terrain. Ue passe de 0,55 à 0,45 W/m².K et le pont thermique",
        "plancher/mur de 0,45 à 0,20 W/m·K, pour 2 200 € intégrés au lot ITE.",
    ], titre="Justification chiffrée de la dérogation sur le plancher bas",
        couleur=ORANGE)

    R.para(
        "Le cadre réglementaire applicable est détaillé en annexe 8.7. Les "
        "points structurants sont les suivants : une déclaration préalable de "
        "travaux est obligatoire, l'isolation par l'extérieur et le remplacement "
        "des menuiseries modifiant l'aspect extérieur (article R.421-17 du code "
        "de l'urbanisme) ; le PLU et l'existence éventuelle d'un périmètre "
        "protégé doivent être vérifiés en mairie avant toute commande, un avis "
        "défavorable de l'Architecte des Bâtiments de France basculerait le "
        "projet vers une isolation par l'intérieur ; l'article L.113-5-1 du même "
        "code autorise un dépassement des règles d'implantation jusqu'à 30 cm "
        "pour l'isolation par l'extérieur, ce qui couvre les 21 cm du complexe "
        "isolant ; l'arrêté du 3 mai 2007 dit « élément par élément » impose "
        "R ≥ 3,7 m².K/W pour les murs et Uw ≤ 1,3 W/m².K pour les fenêtres, "
        "seuils que les solutions retenues dépassent ; enfin, chaque entreprise "
        "doit être qualifiée RGE, lot par lot, sous peine de perte de la "
        "totalité des aides.")

    R.encadre(
        "Une opportunité réglementaire à saisir : la fenêtre de septembre 2026",
        ["Conformément à l'énoncé, les critères d'aides retenus sont ceux en "
         "vigueur jusqu'en septembre 2026. Ils permettent encore de conserver "
         "une chaudière au gaz — donc au propane — dans une opération de "
         "rénovation d'ampleur aidée par MaPrimeRénov'.",
         "C'est ce qui rend l'étape 1 du scénario B possible : elle conserve la "
         "chaudière de 2011, encore fonctionnelle, tout en bénéficiant des aides "
         "à la rénovation d'ampleur. Cette possibilité disparaîtra ensuite ; le "
         "dossier doit donc être déposé avant l'échéance. Le fioul et le charbon "
         "sont, eux, déjà exclus — le logement n'est pas concerné."],
        couleur=ORANGE, fond=H_ORANGE_PALE, size=9.5)

    R.titre2("Stratégie et socle commun de travaux")
    R.para(
        "Les deux scénarios reposent sur une même stratégie dictée par le "
        "diagnostic : traiter d'abord et complètement l'enveloppe, puis la "
        "ventilation, puis l'eau chaude sanitaire, et n'aborder qu'ensuite le "
        "générateur. Cet ordre n'est pas de convenance : il permet de "
        "dimensionner le générateur sur un besoin de 4,1 kW au lieu de 17,1 kW, "
        "donc d'acheter une machine plus petite, moins chère et fonctionnant "
        "dans de meilleures conditions.")

    R.tableau([
        ["Poste", "Solution retenue", "Performance atteinte",
         "Déperdition traitée"],
        ["Murs extérieurs et soubassement",
         "Isolation par l'extérieur, fibre de bois 180 mm (λ = 0,038), sous "
         "enduit minéral à la chaux ; isolant non sensible à l'eau descendu "
         "60 cm sous le terrain",
         "R = 4,74 ; U de 2,05 à 0,19 W/m².K ; Ue du plancher de 0,55 à 0,45",
         "46 % → 4 %"],
        ["Mur mitoyen du garage",
         "Isolation par le côté du garage, laine de roche 140 mm (λ = 0,035) "
         "sous parement", "R = 4,00 ; U de 1,81 à 0,22 W/m².K", "15 % → 2 %"],
        ["Menuiseries et volets",
         "9 ouvrants et 1 porte d'entrée en bois, double vitrage 4/16/4 argon "
         "peu émissif, pose au nu extérieur ; volets conservés, révisés et "
         "reposés sur gonds rallongés",
         "Uw = 1,30 W/m².K ; Sw ≥ 0,3 ; protection solaire d'été maintenue",
         "13 % → 4 %"],
        ["Étanchéité à l'air et ventilation",
         "Membrane en périphérie, traitement des liaisons, trappe de comble "
         "isolée, deux tests d'infiltrométrie ; VMC hygroréglable de type B avec "
         "entrées d'air intégrées aux menuiseries neuves",
         "Q4Pa-surf de 3,5 à ≤ 1,3 m³/(h·m²) ; renouvellement d'air de 0,90 à "
         "0,45 vol/h", "14 % → 8 %"],
        ["Appoint bois",
         "Poêle à bûches étanche de 5 kW, Flamme Verte 7 étoiles, sur air "
         "extérieur", "Rendement de 55 % à 78 % ; sécurité assurée avec la VMC",
         "—"],
        ["Postes non modifiés",
         "Plafond sous combles : aucune isolation nouvelle, trappe et raccord "
         "périphérique repris. Plancher bas : non isolé, dérogation justifiée. "
         "Éclairage : halogènes remplacés par des LED",
         "R = 10 m².K/W conservé ; éclairage de 200 à 110 W", "1 % → 1 %"],
    ], largeurs=[0.17, 0.38, 0.28, 0.17], size=8,
        titre="Socle commun aux deux scénarios")

    R.calcul([
        "GV après travaux d'enveloppe",
        "   Murs extérieurs        : 125,0 × 0,19               =  23,8 W/K",
        "   Mur mitoyen du garage  :  52,6 × 0,22 × 0,85        =   9,8 W/K",
        "   Menuiseries            : 13,40 × 1,30 + 2,05 × 1,50 =  20,5 W/K",
        "   Plafond sous combles   :  57,5 × 0,10               =   5,8 W/K",
        "   Plancher bas           :  57,5 × 0,45               =  25,9 W/K",
        "   Ponts thermiques                                    =   8,1 W/K",
        "   Renouvellement d'air   : 0,34 × 0,45 × 250          =  38,3 W/K",
        "=> GV = 132 W/K, contre 553 avant travaux, soit − 76 %",
        "   Ubat = 93,9 / 308,1 = 0,31 W/m².K   (niveau BBC rénovation)",
        "   P = 132 × 31 = 4 092 W, soit 4,1 kW",
        "",
        "Besoin de chauffage : 132 × 2 860 × 24 / 1000 = 9 060 kWh bruts",
        "   − apports utiles 2 840  =>  6 220 kWh, retenu 6 300 kWh/an",
        "   avec 2 % de marge, soit 63 kWh/m².an contre 339 avant (− 81 %)",
    ], titre="Performance de l'enveloppe après le socle commun de travaux")

    R.figure(fg("06_gv_avant_apres"), largeur_cm=11.6,
             legende="Effet du socle commun de travaux, poste par poste")

    R.para([
        ("Isolation par l'extérieur plutôt que par l'intérieur. ", True, ANTHRA),
        ("Le maître d'ouvrage pouvant être relogé, une isolation par "
         "l'intérieur était techniquement envisageable ; elle est écartée. Le "
         "facteur décisif est l'inertie : par l'extérieur, les 50 cm de pierre "
         "restent du côté chauffé et le confort d'été — aujourd'hui jugé "
         "acceptable — est préservé, alors qu'une isolation intérieure le "
         "dégraderait. S'y ajoutent le traitement continu des ponts thermiques "
         "(27,7 → 8,1 W/K), l'absence de perte de surface habitable (environ "
         "6 m² auraient été perdus), le maintien du mur du côté chaud et sec, et "
         "la possibilité de rester dans les lieux. La condition — un enduit de "
         "façade sain — a été vérifiée lors de la visite. Le comparatif complet "
         "figure en annexe 8.5.", False, NOIR)])

    R.para([
        ("Interfaces entre lots. ", True, ANTHRA),
        ("C'est sur les interfaces que se joue la différence entre une "
         "rénovation performante et une juxtaposition de travaux. Quinze "
         "interfaces ont été identifiées et font l'objet d'une prescription et "
         "d'un ordre d'intervention (annexe 8.4). Les plus critiques : les "
         "menuiseries se posent avant l'isolant et sont repositionnées au nu "
         "extérieur pour supprimer le pont thermique de tableau ; l'isolant "
         "remonte jusqu'à la sablière en recouvrement de l'isolant des combles ; "
         "l'étanchéité à l'air est traitée et contrôlée avant la pose de la VMC, "
         "faute de quoi celle-ci aspirerait par les fuites ; le poêle étanche "
         "est obligatoire dès la mise en dépression du logement ; et le "
         "générateur est dimensionné après réduction du besoin, jamais avant.",
         False, NOIR)])

    R.titre2("Scénario de rénovation globale — scénario A")
    R.para(
        "Ce scénario réalise l'ensemble en une seule opération : le socle commun, "
        "la production d'eau chaude thermodynamique et le remplacement du "
        "générateur. La chaudière propane est déposée, la cuve enterrée "
        "neutralisée, et le chauffage assuré par une pompe à chaleur air/eau en "
        "régime basse température, complétée par le poêle à bûches étanche.")

    R.tableau([
        ["Critère", "Pompe à chaleur air/eau — retenue",
         "Chaudière à granulés — écartée",
         "Chaudière propane à condensation — écartée"],
        ["Puissance et modulation",
         "6 kW nominal, modulation jusqu'à 1,5 kW : adaptée aux 4,1 kW",
         "8 kW minimum, modulation limitée à 3 kW : cycles courts",
         "Plus petit modèle de 12 kW : fortement surdimensionnée"],
        ["Compatibilité avec les radiateurs fonte",
         "Excellente : 4,94 kW en régime 45/35",
         "Bonne, mais l'atout haute température ne sert plus", "Bonne, même remarque"],
        ["Consommation annuelle", "1 440 kWh d'électricité (SCOP 3,5)",
         "1 193 kg de granulés, soit 1,2 t/an", "553 kg de propane"],
        ["Énergie primaire du logement", "75 kWh EP/m².an — classe B",
         "98 kWh EP/m².an — classe B, moins bon", "112 kWh EP/m².an — classe C"],
        ["Émissions de CO₂", "2,5 kg CO₂/m².an — classe A",
         "3,1 kg CO₂/m².an — classe A", "16 kg CO₂/m².an — classe C"],
        ["Coût de fonctionnement", "≈ 360 €/an de chauffage",
         "≈ 420 €/an, plus 250 € d'entretien",
         "≈ 1 175 €/an, location de citerne comprise"],
        ["Investissement", "14 000 €", "18 000 € avec la trémie", "9 000 €"],
        ["Contraintes", "Entretien annuel, unité extérieure, abonnement porté "
                        "à 9 kVA",
         "Approvisionnement, stockage, cendres, ramonage, accès camion",
         "Maintien du contrat propane et de la location de citerne"],
        ["Verdict",
         "Retenue : meilleure énergie primaire et meilleur coût d'exploitation",
         "Écartée : surdimensionnée, plus chère, moins performante en EP",
         "Écartée : énergie fossile chère, étiquette climat plafonnée"],
    ], largeurs=[0.16, 0.29, 0.28, 0.27], size=8,
        lignes_surlignees=(9,),
        titre="Comparaison argumentée des solutions de production de chaleur")

    R.encadre(
        "Le renversement d'analyse qui justifie la pompe à chaleur",
        ["Sur un bâtiment ancien équipé de radiateurs en fonte haute "
         "température, le réflexe est de retenir une chaudière — à granulés de "
         "préférence — au motif que les émetteurs ne pourraient pas fonctionner "
         "en basse température.",
         "Ce raisonnement est juste avant travaux. Il devient faux après. Le "
         "chapitre 5 démontre par le calcul que les sept radiateurs en fonte, "
         "dont l'énoncé donne les dimensions exactes, délivrent encore 4,94 kW "
         "en régime 45/35 °C, alors que le besoin après isolation n'est plus que "
         "de 4,1 kW. La basse température est donc atteignable sans remplacer un "
         "seul émetteur.",
         ("Ce sont les travaux d'enveloppe qui rendent la pompe à chaleur "
          "possible.", " Ils divisent le besoin par quatre et transforment un "
          "surdimensionnement gênant en réserve de puissance utile — "
          "l'illustration la plus concrète de l'ordre de priorité retenu.")],
        couleur=VERT, fond=H_VERT_PALE, size=9.5, icone="◆")

    R.calcul([
        "Consommations (besoin 6 300 kWh : 80 % pompe à chaleur, 20 % poêle)",
        "   Pompe à chaleur : 6 300 × 0,80 / 3,5 = 1 440 kWh électriques",
        "   Bois            : 6 300 × 0,20 / 0,78 = 1 615 kWh, soit 1,0 stère",
        "   ECS 800 + éclairage 150 + auxiliaires 155",
        "=> Électricité totale : 2 545 kWh/an",
        "",
        "Énergie primaire : 2 545 × 2,3 + 1 615 = 7 469 kWh EP",
        "=> 75 kWh EP/m².an  ->  classe énergie B",
        "Émissions : 2 545 × 0,079 + 1 615 × 0,030 = 249 kg CO₂/an",
        "=> 2,5 kg CO₂/m².an  ->  classe climat A",
        "=> Étiquette DPE du scénario A : classe B (gain de 5 classes)",
    ], titre="Performance du scénario de rénovation globale")

    R.encadre(
        "Transparence : le poêle à bois coûte une classe en énergie",
        ["Le maître d'ouvrage apprécie le bois, et le poêle est conservé dans "
         "les deux scénarios. Il faut cependant dire ce que cela coûte.",
         "Le bois est excellent pour le carbone — 0,030 kg CO₂/kWh contre 0,272 "
         "pour le propane. Mais en énergie primaire, son coefficient est de 1,0 "
         "et le poêle a un rendement de 78 %, soit 1,28 kWh primaire par kWh "
         "utile ; une pompe à chaleur de SCOP 3,5, malgré le coefficient 2,3 de "
         "l'électricité, n'en consomme que 0,66.",
         ("Sans appoint bois, le scénario A tomberait à 67 kWh EP/m².an et "
          "basculerait en classe A.", " Le choix de conserver le bois est "
          "assumé : il répond au souhait du maître d'ouvrage, sécurise le "
          "chauffage en cas de coupure d'électricité — non négligeable en zone "
          "rurale de montagne — et écrête la pointe hivernale, ce qui permet de "
          "dimensionner la pompe à chaleur au plus juste.")],
        couleur=BLEU, fond=H_BLEU_PALE, size=9.5)

    R.titre2("Scénario de rénovation par étapes — scénario B")
    R.para(
        "Ce scénario atteint le même niveau de performance, mais en deux temps. "
        "Il respecte la définition de la rénovation performante par étapes : les "
        "étapes sont cohérentes et ne compromettent ni la faisabilité technique "
        "ni la faisabilité économique des suivantes, et la première fait gagner "
        "au moins deux classes tout en traitant deux postes d'isolation.")

    R.tableau([
        ["", "Étape 1 — année 1", "Étape 2 — années 3 à 5"],
        ["Objet", "L'enveloppe et la ventilation", "Les systèmes de production"],
        ["Contenu",
         "Isolation par l'extérieur des murs (poste d'isolation n° 1), "
         "isolation du mur mitoyen du garage (poste n° 2), remplacement des "
         "menuiseries, étanchéité à l'air, VMC hygroréglable B, poêle étanche, "
         "éclairage LED. Chaudière propane conservée et optimisée : sonde "
         "extérieure et loi d'eau, thermostat programmable, 8 robinets "
         "thermostatiques, calorifugeage du réseau, désembouage et équilibrage",
         "Remplacement du ballon électrique par un chauffe-eau thermodynamique "
         "de 200 L ; dépose de la chaudière et neutralisation de la cuve "
         "enterrée ; pompe à chaleur air/eau de 6 kW en régime 45/35 ; passage "
         "de l'abonnement à 9 kVA"],
        ["Coût", "65 600 € TTC", "22 500 € TTC"],
        ["Classe DPE atteinte", "C — gain de 4 classes", "B — gain de 5 classes"],
        ["Postes d'isolation traités",
         "2 : murs extérieurs et mur sur local non chauffé", "—"],
        ["Facture annuelle", "2 963 €", "1 833 €"],
    ], largeurs=[0.13, 0.46, 0.41], size=8, lignes_surlignees=(4,),
        titre="Contenu et performance des deux étapes")

    R.calcul([
        "Rendement de l'installation propane après optimisation (étape 1)",
        "   Génération (chaudière BT en régime abaissé 45/35)  : 0,89",
        "   Distribution (réseau calorifugé classe 4)          : 0,95",
        "   Émission (robinets thermostatiques)                : 0,96",
        "   Régulation (loi d'eau + thermostat programmable)   : 0,97",
        "=> Rendement global = 0,79, contre 0,65 avant : + 22 % à besoin égal",
        "",
        "Consommations (besoin 6 300 kWh : 75 % chaudière, 25 % poêle ;",
        "ballon ECS électrique conservé)",
        "   Propane 5 981 kWh PCI (468 kg) ; bois 2 019 kWh (1,3 stère)",
        "   Électricité : 3 065 (ECS) + 150 (éclairage) + 135 (aux.) = 3 350 kWh",
        "",
        "Énergie primaire : 5 981 + 2 019 + 3 350 × 2,3 = 15 705 kWh EP",
        "=> 157 kWh EP/m².an  ->  classe énergie C",
        "Émissions : 1 627 + 61 + 265 = 1 953 kg CO₂/an",
        "=> 19,5 kg CO₂/m².an  ->  classe climat C",
        "=> Étiquette DPE après l'étape 1 : classe C (gain de 4 classes)",
    ], titre="Performance de l'étape 1", couleur=BLEU)

    R.encadre(
        "Cohérence des étapes : ce qui garantit que l'étape 2 reste possible",
        [("L'étape 1 réduit le besoin avant de choisir le générateur. ", "La "
          "pompe à chaleur de l'étape 2 sera dimensionnée sur 4,1 kW et non sur "
          "17,1 kW, ce qui divise son coût par deux environ."),
         ("La chaudière conservée est exploitée en régime abaissé. ",
          "L'abaissement de la loi d'eau à 45/35 dès l'étape 1 valide en "
          "conditions réelles le régime que la pompe à chaleur utilisera : "
          "aucune mauvaise surprise à l'étape 2."),
         ("Aucun investissement perdu, aucun travail à défaire. ", "Robinets "
          "thermostatiques et désembouage sont réutilisés par la pompe à "
          "chaleur ; l'étape 2 ne touche que la chaufferie, sans intervenir sur "
          "l'enveloppe, les menuiseries ou la ventilation.")],
        couleur=VERT, fond=H_VERT_PALE, size=9.5)

    R.titre2("Comparaison technique des deux scénarios")
    R.tableau([
        ["Critère", "État initial", "Scénario A — global",
         "Scénario B — étape 1", "Scénario B — étape 2"],
        ["Étiquette DPE", "G", "B", "C", "B"],
        ["Classe énergie", "G — 622", "B — 75", "C — 157", "B — 75"],
        ["Classe climat", "G — 122", "A — 2,5", "C — 19,5", "A — 2,5"],
        ["Gain de classes", "—", "5", "4", "5"],
        ["Coefficient GV", "553 W/K", "132 W/K", "132 W/K", "132 W/K"],
        ["Coefficient Ubat", "1,55", "0,31", "0,31", "0,31"],
        ["Besoin de chauffage", "339 kWh/m².an", "63", "63", "63"],
        ["Puissance de chauffage", "17,1 kW", "4,1 kW", "4,1 kW", "4,1 kW"],
        ["Énergie de chauffage", "Propane et bois", "PAC et bois",
         "Propane optimisé et bois", "PAC et bois"],
        ["Rendement de l'installation", "0,65", "SCOP 3,5", "0,79", "SCOP 3,5"],
        ["Émissions annuelles", "12,2 t CO₂", "0,25 t", "1,95 t", "0,25 t"],
        ["Coût des travaux", "—", "85 100 €", "65 600 €", "22 500 €"],
        ["Facture annuelle", "6 009 €", "1 833 €", "2 963 €", "1 833 €"],
    ], largeurs=[0.22, 0.19, 0.20, 0.20, 0.19], size=8,
        align_centre_cols=(1, 2, 3, 4), lignes_surlignees=(1,),
        titre="Comparaison technique détaillée")



# ==========================================================================
#  CHAPITRE 5 — ÉQUIPEMENTS TECHNIQUES ET DIMENSIONNEMENT
# ==========================================================================
def chapitre_5():
    R.titre1("Équipements techniques et dimensionnement")

    R.titre2("Dimensionnement des équipements de chauffage")
    R.para(
        "L'énoncé fournit les dimensions exactes des radiateurs, ce qui permet "
        "de calculer leur puissance plutôt que de l'estimer. Cette vérification "
        "est déterminante : c'est elle qui décide du choix du générateur.")

    R.calcul([
        "Puissance nécessaire après travaux (NF EN 12831 simplifiée)",
        "   P = GV × (Tint − Tbase) = 132 × (19 − (− 12)) = 4 092 W",
        "=> 4,1 kW, soit 41 W/m² contre 171 W/m² avant travaux",
        "   Avec surpuissance de relance de 10 % : 4,5 kW",
        "",
        "Puissance des émetteurs existants (fonte 4 colonnes H = 930 mm,",
        "0,145 kW par élément à Δθ = 50 K, élément de 60 mm de large)",
        "   Salles de bains : 660 / 60 = 11 éléments × 2 radiateurs",
        "   Autres pièces   : 1 100 / 60 = 18 éléments × 5 radiateurs",
        "   Total 112 éléments  ->  2 × 1,60 + 5 × 2,61 = 16,25 kW à Δθ = 50 K",
        "",
        "Loi d'émission P(Δθ) = P(50) × (Δθ / 50)^n, avec n = 1,3 pour la fonte",
        "   75/65/20 (Δθ 50) : 16,25 kW        50/40/20 (Δθ 25) :  6,60 kW",
        "   65/55/20 (Δθ 40) : 12,19 kW        45/35/20 (Δθ 20) :  4,94 kW",
        "   55/45/20 (Δθ 30) :  8,37 kW",
        "",
        "=> Besoin 4,1 kW  <  4,94 kW disponibles en régime 45/35",
        "=> Les radiateurs existants sont compatibles basse température,",
        "   sans qu'aucun émetteur n'ait à être remplacé",
    ], titre="Puissance de chauffage et vérification des émetteurs existants")

    R.figure(fg("07_emetteurs"), largeur_cm=11.6,
             legende="Puissance des radiateurs selon le régime, comparée au "
                     "besoin avant et après travaux")

    R.encadre(
        "Ce que ce calcul démontre — et ce qu'il explique",
        [("Avant travaux : ", "16,25 kW au régime maximal pour un besoin de "
          "17,1 kW — et seulement 14,2 kW au régime réel d'une chaudière basse "
          "température, environ 70/60. L'installation est structurellement "
          "incapable de tenir la maison par grand froid, ce qui explique à la "
          "fois l'inconfort et le recours systématique aux 7 stères de bois."),
         ("Après travaux : ", "le besoin tombe à 4,1 kW. Les mêmes radiateurs, "
          "auparavant insuffisants, disposent d'une réserve de 20 % en régime "
          "45/35 — le régime de prédilection d'une pompe à chaleur."),
         ("Conséquence : ", "l'argument classique « les radiateurs fonte "
          "imposent la haute température » tombe. La pompe à chaleur devient la "
          "solution la plus performante et la moins coûteuse à l'usage, sans "
          "aucun travail sur les émetteurs.")],
        couleur=VERT, fond=H_VERT_PALE, size=9.5, icone="◆")

    R.calcul([
        "Pompe à chaleur air/eau retenue : inverter, fluide R290",
        "   Puissance nominale (7 °C / 35 °C)        : 6,0 kW",
        "   Puissance disponible à − 7 °C / 45 °C    : environ 4,6 kW",
        "   Besoin à la température de base (− 12 °C) : 4,1 kW",
        "   Appoint électrique intégré 3 kW + poêle étanche 5 kW en secours",
        "   Régime 45/35 ; SCOP normalisé ≈ 4,3, retenu à 3,5 en H1c",
        "",
        "   Débit d'eau : Q = P / (1,163 × Δθ) = 4,1 / (1,163 × 10) = 350 L/h",
        "",
        "Volume d'eau de l'installation",
        "   112 éléments de fonte × 3,4 L = 381 L ; réseau 60 L  ->  441 L",
        "   soit 74 L par kW de pompe à chaleur (minimum usuel : 10 à 20 L/kW)",
        "=> Aucun ballon tampon nécessaire : une bouteille de découplage suffit,",
        "   ce qui économise environ 1 500 €",
    ], titre="Dimensionnement de la pompe à chaleur air/eau")

    R.para(
        "Le fort volume d'eau des radiateurs en fonte, souvent présenté comme un "
        "handicap, devient ici un atout : il apporte l'inertie hydraulique qui "
        "évite les cycles courts, sans avoir à loger ni à payer un ballon "
        "tampon. Deux prescriptions accompagnent ce choix : un désembouage "
        "complet avant mise en service, faute de quoi la surface d'échange réelle "
        "serait inférieure au calcul ; et une implantation soignée de l'unité "
        "extérieure — à l'est contre le mur du garage, sur plots antivibratiles, "
        "à plus de 3 m des limites séparatives, avec un niveau sonore inférieur à "
        "45 dB(A) à 3 m.")

    R.titre2("Adaptation de la loi d'eau — scénario par étapes")
    R.para(
        "Dans le scénario B, la chaudière propane est conservée pendant "
        "l'étape 1. Elle n'a pas à être redimensionnée, mais son régime doit "
        "impérativement être adapté au nouveau besoin : maintenir une loi d'eau "
        "haute température sur un bâtiment isolé conduirait à des cycles courts, "
        "à des surchauffes et à un rendement dégradé.")

    R.calcul([
        "Détermination du régime après isolation",
        "   Puissance à fournir à la température de base : 4,1 kW",
        "   P(Δθ) = 16,25 × (Δθ / 50)^1,3  ->  on cherche P(Δθ) ≥ 4,1",
        "   4,1 / 16,25 = 0,252",
        "   Δθ = 50 × 0,252^(1/1,3) = 50 × 0,347 = 17,4 K",
        "=> 17,4 K suffiraient ; on retient 20 K par sécurité, soit 45/35/20",
        "",
        "Loi d'eau à programmer (température de départ / extérieure)",
        "   − 12 °C -> 45 °C     0 °C -> 36 °C    + 15 °C -> arrêt du chauffage",
        "   −  5 °C -> 40 °C   + 7 °C -> 30 °C    pente de la courbe ≈ 0,5",
        "   Réduit nocturne : − 3 K sur la consigne, de 22 h à 6 h",
        "",
        "Gain : passer d'un départ de 70 °C à un départ moyen de 38 °C améliore",
        "le rendement de génération de 0,86 à 0,89 et réduit fortement les",
        "pertes du réseau, dont la température moyenne baisse de 30 K.",
    ], titre="Adaptation calculée de la loi d'eau de la chaudière conservée",
        couleur=BLEU)

    R.para(
        "Ce réglage ne demande qu'une sonde extérieure et le paramétrage du "
        "régulateur — environ 900 € posés — et produit trois effets : il améliore "
        "immédiatement le rendement de la chaudière conservée, il valide en "
        "conditions réelles, pendant trois à cinq ans, le régime 45/35 que la "
        "pompe à chaleur utilisera à l'étape 2, et il supprime les surchauffes "
        "qui apparaîtraient immanquablement sur un bâtiment dont le besoin a été "
        "divisé par quatre.")

    R.titre2("Analyse du rendement global de l'installation de chauffage")
    R.para(
        "Le rendement global est le produit de quatre rendements partiels. Dans "
        "l'existant : génération 0,86 — chaudière basse température exploitée en "
        "régime haute température et implantée en local non chauffé ; "
        "distribution 0,88 — réseau bitube non isolé traversant le garage ; "
        "émission 0,95 — radiateurs sans vannes thermostatiques ; régulation "
        "0,90 — thermostat non programmable placé dans le séjour où se trouve le "
        "poêle, sans sonde extérieure. Soit un rendement global de 0,65 : 35 % "
        "de l'énergie payée n'atteint jamais les pièces.")
    R.para(
        "Après optimisation (étape 1 du scénario B), ces valeurs deviennent "
        "0,89 grâce à la loi d'eau abaissée, 0,95 grâce au calorifugeage de "
        "classe 4, 0,96 grâce aux robinets thermostatiques et 0,97 grâce à la "
        "programmation, soit un rendement global de 0,79 — une amélioration de "
        "22 % à besoin égal. Dans le scénario A, la pompe à chaleur remplace la "
        "génération par un SCOP de 3,5, les trois autres postes restant "
        "identiques : l'installation délivre alors environ 3,2 kWh utiles par "
        "kWh d'électricité consommé.")

    R.para(
        "Trois des quatre postes de perte s'améliorent sans changer le "
        "générateur. Le calorifugeage du réseau dans le garage est de loin le "
        "plus rentable : pour environ 600 €, il fait gagner sept points de "
        "rendement, soit près de 900 kWh de propane par an dans la situation "
        "actuelle. C'est le type de geste que l'on oublie systématiquement dans "
        "les projets centrés sur le seul remplacement du générateur.")

    R.titre2("Optimisation de la régulation de l'installation")
    R.tableau([
        ["Équipement", "Fonction", "Réglage préconisé", "Coût posé"],
        ["Sonde extérieure et loi d'eau",
         "Adapter la température de départ à la rigueur extérieure, en "
         "anticipation plutôt qu'en réaction",
         "Pente 0,5 ; point de base 45 °C à − 12 °C ; arrêt du chauffage à "
         "+ 15 °C", "900 €"],
        ["8 robinets thermostatiques",
         "Consigne propre à chaque pièce et récupération des apports gratuits",
         "Position 3 en pièces de vie (20 °C), 2 en chambres (17 °C), 4 en "
         "salles de bains (22 °C)", "800 €"],
        ["Thermostat programmable déporté",
         "Réduit nocturne et d'absence ; supprime l'erreur de mesure due au "
         "poêle",
         "19 °C de 6 h à 22 h, 16 °C la nuit et en absence ; implanté dans le "
         "dégagement, à 1,50 m du sol", "350 €"],
        ["Désembouage et équilibrage",
         "Restituer aux radiateurs leur surface d'échange et répartir les débits",
         "Désembouage chimique avec rinçage, puis équilibrage par tés de réglage",
         "900 €"],
        ["Calorifugeage en local non chauffé",
         "Supprimer les pertes intégrales de la traversée du garage",
         "Isolant classe 4 sur l'aller et le retour, vannes et points singuliers "
         "compris", "600 €"],
        ["Total", "", "", "3 550 €"],
    ], largeurs=[0.20, 0.27, 0.42, 0.11], size=8,
        align_centre_cols=(3,), lignes_surlignees=(6,),
        titre="Optimisation de la régulation : équipements, réglages et coûts")

    R.para(
        "Ces 3 550 € constituent la dépense la plus efficace du projet rapportée "
        "à son montant : ils font gagner 22 % de rendement, soit environ "
        "1 100 kWh de propane par an dans la situation actuelle, et résolvent à "
        "eux seuls le problème d'hétérogénéité entre les pièces identifié au "
        "chapitre 2. Ils sont intégrés à l'étape 1 du scénario B ; dans le "
        "scénario A, la sonde extérieure est intégrée à la pompe à chaleur, les "
        "autres postes restant identiques.")

    R.titre2("Production efficace d'eau chaude sanitaire")
    R.calcul([
        "Besoin : 4 personnes × 40 L/jour à 40 °C = 160 L/jour",
        "   E = 160 L × 1,163 Wh/(L·K) × (40 − 12) = 5,21 kWh/jour",
        "=> 1 902 kWh utiles par an",
        "",
        "Volume de stockage : pointe de 2 douches consécutives + usages",
        "   ≈ 150 L à 40 °C, soit 98 L à 55 °C",
        "=> Un ballon de 200 L couvre largement la pointe : volume conservé",
        "",
        "Solution retenue : chauffe-eau thermodynamique 200 L sur air extérieur",
        "   COP normalisé (profil L, air extérieur) : 3,2",
        "   COP saisonnier retenu en climat H1c      : 2,8",
        "   Consommation = 1 902 / 2,8 = 679 kWh + pertes de stockage",
        "=> 800 kWh/an, contre 3 065 kWh aujourd'hui",
        "=> Économie : 2 265 kWh d'électricité par an, soit environ 545 €/an",
    ], titre="Dimensionnement de la production d'eau chaude sanitaire")

    R.para(
        "Cinq autres solutions ont été comparées et écartées (détail en "
        "annexe 8.5) : le ballon électrique conservé ou renouvelé, qui reste en "
        "effet Joule ; le chauffe-eau thermodynamique sur air ambiant du garage, "
        "dont le COP s'effondre lorsque le local descend à 5-8 °C et qui "
        "refroidirait un local mitoyen du volume chauffé ; la production par la "
        "pompe à chaleur, dont le COP chute à 55 °C et qui serait mobilisée tout "
        "l'été ; et le chauffe-eau solaire thermique, techniquement valable mais "
        "dont le temps de retour dépasse 25 ans pour un foyer de quatre "
        "personnes. Trois prescriptions accompagnent le choix retenu : "
        "raccordement sur air extérieur par gainage double, indépendamment du "
        "réseau de VMC ; calorifugeage des liaisons en local non chauffé ; et "
        "programmation en heures creuses, qui réduit d'environ 12 % le coût de ce "
        "poste sans aucun investissement.")

    R.titre2("Dimensionnement de la ventilation")
    R.calcul([
        "Logement de type T4 (séjour + 3 chambres) — arrêté du 24 mars 1982",
        "   Débit total extrait minimal : 90 m³/h",
        "   Débit de pointe en cuisine  : 120 m³/h",
        "",
        "VMC hygroréglable de type B (bouches ET entrées d'air hygroréglables)",
        "   Cuisine (hygro + commande manuelle) : 10 à 45 m³/h, 135 en pointe",
        "   Salle de bains RDC / étage          :  5 à 40 m³/h chacune",
        "   WC RDC / étage                      :  5 à 30 m³/h chacun",
        "   Entrées d'air intégrées aux menuiseries : 2 modules 6-30 m³/h au",
        "   séjour, 1 module par chambre, soit 5 modules",
        "",
        "=> Débit moyen constaté ≈ 55 m³/h, soit 0,22 vol/h (contre 0,90)",
        "   Déperditions de ventilation : 76,5 W/K  ->  38,3 W/K",
    ], titre="Dimensionnement de la ventilation selon l'arrêté du 24 mars 1982")

    R.para(
        "La ventilation double flux, souvent présentée comme la référence en "
        "rénovation performante, a été étudiée et écartée (annexe 8.5). Trois "
        "éléments s'y opposent ici : les combles sont isolés à 40 cm et bien "
        "étanchés, si bien que faire passer un double réseau imposerait de percer "
        "et de reprendre cette isolation ; le gain énergétique, une fois la pompe "
        "à chaleur installée, ne représente qu'une centaine d'euros par an pour "
        "6 000 € de surcoût, soit plus de 25 ans de retour ; et le maître "
        "d'ouvrage a demandé que chaque investissement soit justifié par les "
        "économies produites. Trois prescriptions complètent le dimensionnement : "
        "caisson à moteur basse consommation, inférieur à 15 W et 30 dB(A) ; "
        "gaines isolées dans les combles pour éviter la condensation ; et "
        "détalonnage des portes intérieures de 1 à 2 cm, point de détail "
        "systématiquement oublié qui suffit à rendre l'installation inefficace.")


# ==========================================================================
#  CHAPITRE 6 — ANALYSE ÉCONOMIQUE
# ==========================================================================
def chapitre_6():
    R.titre1("Analyse économique")

    R.titre2("Chiffrage des travaux")
    R.para(
        "Les prix retenus sont des prix de marché en fourni-posé, toutes taxes "
        "comprises, main-d'œuvre et échafaudage inclus, au taux réduit de TVA de "
        "5,5 % applicable aux travaux d'amélioration de la performance "
        "énergétique et aux travaux induits. Aucune économie d'auto-construction "
        "n'est intégrée. Le détail poste par poste figure en annexe 8.6.")

    R.tableau([
        ["Lot", "Contenu", "Montant TTC", "Part"],
        ["Enveloppe opaque",
         "Isolation par l'extérieur des murs (fibre de bois 180 mm sous enduit "
         "à la chaux, 139 m²), soubassement, isolation du mur mitoyen du garage "
         "(laine de roche 140 mm)", "32 550 €", "38 %"],
        ["Menuiseries et volets",
         "9 ouvrants et 1 porte d'entrée en bois double vitrage Uw = 1,30, pose "
         "au nu extérieur ; dépose, révision et repose des volets",
         "14 500 €", "17 %"],
        ["Étanchéité et ventilation",
         "Traitement de l'étanchéité à l'air et deux tests d'infiltrométrie ; "
         "VMC hygroréglable de type B complète", "6 000 €", "7 %"],
        ["Production de chaleur",
         "Pompe à chaleur air/eau 6 kW avec bouteille de découplage et "
         "hydraulique ; poêle à bûches étanche 5 kW ; robinets thermostatiques, "
         "désembouage et équilibrage", "20 900 €", "25 %"],
        ["Eau chaude sanitaire",
         "Chauffe-eau thermodynamique 200 L sur air extérieur gainé",
         "4 200 €", "5 %"],
        ["Dépose et adaptations",
         "Dépose de la chaudière propane, neutralisation de la cuve enterrée, "
         "passage de l'abonnement à 9 kVA, éclairage LED", "3 400 €", "4 %"],
        ["Ingénierie",
         "Audit énergétique réglementaire et Accompagnateur Rénov' agréé, "
         "obligatoires pour le parcours accompagné", "3 500 €", "4 %"],
        ["TOTAL SCÉNARIO A", "", "85 100 €", "100 %"],
    ], largeurs=[0.18, 0.57, 0.14, 0.11], size=8,
        align_centre_cols=(2, 3), lignes_surlignees=(8,),
        titre="Chiffrage du scénario A par lot (détail poste par poste en "
              "annexe 8.6)")

    R.para(
        "L'isolation par l'extérieur représente 31 % du montant, ce qui est "
        "cohérent puisqu'elle traite 46 % des déperditions ; sa part de "
        "main-d'œuvre et d'échafaudage avoisine 40 %, ce qui explique qu'il ne "
        "soit pas rentable de réduire l'épaisseur d'isolant — passer de 180 à "
        "120 mm n'économiserait qu'environ 1 800 € tout en faisant perdre un "
        "tiers de la résistance thermique et en passant sous le seuil "
        "d'éligibilité aux aides.")

    R.tableau([
        ["Étape", "Postes inclus", "Montant TTC"],
        ["Étape 1 — année 1",
         "Postes 1 à 8, 14 et 15, plus l'optimisation de la chaudière propane "
         "conservée : sonde extérieure et loi d'eau, 8 robinets thermostatiques, "
         "thermostat programmable, calorifugeage du réseau, désembouage et "
         "équilibrage (3 550 €)", "65 600 €"],
        ["Étape 2 — années 3 à 5",
         "Postes 9, 10, 12 et 13, plus le montage du second dossier d'aides "
         "(1 200 €)", "22 500 €"],
        ["TOTAL SCÉNARIO B — rénovation par étapes", "", "88 100 €"],
    ], largeurs=[0.20, 0.65, 0.15], size=8,
        align_centre_cols=(2,), lignes_surlignees=(3,),
        titre="Chiffrage du scénario B — rénovation par étapes")

    R.para(
        "Réalisés en deux temps, les mêmes travaux coûtent 3 000 € de plus, soit "
        "3,4 % du montant : l'optimisation de la chaudière conservée n'aurait pas "
        "lieu d'être si l'on remplaçait le générateur immédiatement, et un second "
        "dossier d'aides doit être monté. Ce surcoût n'est pas décisif à lui "
        "seul ; la vraie différence se joue sur les aides.")

    R.titre2("Identification des aides mobilisables")
    R.para(
        "Le foyer relève de la catégorie « intermédiaire » de l'Agence nationale "
        "de l'habitat. Conformément à l'énoncé, les critères retenus sont ceux "
        "applicables jusqu'en septembre 2026 ; ils devront être confirmés auprès "
        "de l'espace conseil France Rénov' avant tout engagement.")

    R.tableau([
        ["Dispositif", "Applicabilité au projet", "Montant estimé"],
        ["MaPrimeRénov' Parcours accompagné",
         "Gain minimum de 2 classes, 2 postes d'isolation, sortie de passoire, "
         "Accompagnateur Rénov' et audit obligatoires. Taux intermédiaires 45 % "
         "+ 10 points de bonus. Plafond de 70 000 € HT au-delà de 4 classes. "
         "L'étape 2 du scénario B, ne gagnant qu'une classe, n'y est pas "
         "éligible", "38 500 € (A)\n34 200 € (B1)"],
        ["MaPrimeRénov' par geste",
         "Seule voie d'aide pour l'étape 2 du scénario B : forfaits "
         "intermédiaires de 3 000 € pour la pompe à chaleur et 400 € pour le "
         "chauffe-eau thermodynamique", "3 400 € (B2)"],
        ["Certificats d'économies d'énergie",
         "Non cumulables avec le parcours accompagné, qui intègre déjà leur "
         "valorisation ; mobilisables sur l'étape 2 (fiches BAR-TH-171 et "
         "BAR-TH-148)", "2 700 € (B2)"],
        ["Éco-prêt à taux zéro",
         "Jusqu'à 50 000 € sur 20 ans, cumulable avec MaPrimeRénov' : le gain de "
         "88 % en énergie primaire dépasse largement les 35 % exigés",
         "34 600 € (A)\n35 800 € (B)"],
        ["TVA à taux réduit de 5,5 %",
         "Applicable à l'ensemble des postes, déjà intégrée aux montants TTC",
         "≈ 12 800 € d'économie"],
        ["Aides locales et fiscalité",
         "Grand Lac, Département de la Savoie, Région Auvergne-Rhône-Alpes ; "
         "exonération possible de taxe foncière (article 1383-0 B du CGI), non "
         "intégrée par prudence", "2 000 €"],
    ], largeurs=[0.21, 0.58, 0.21], size=8,
        titre="Aides mobilisables (inventaire complet en annexe 8.7)")

    R.calcul([
        "SCÉNARIO A",
        "   Travaux 85 100 € TTC  ->  HT = 80 663 €",
        "   Assiette = min (80 663 ; 70 000) = 70 000 € HT   (gain de 5 classes)",
        "   Taux = 45 % (intermédiaires) + 10 points (sortie de passoire) = 55 %",
        "=> MaPrimeRénov' = 70 000 × 0,55 = 38 500 €",
        "   Écrêtement : cumul limité à 80 % du TTC, soit 68 080 € — non atteint",
        "",
        "SCÉNARIO B — étape 1",
        "   Travaux 65 600 € TTC  ->  HT = 62 180 € ; assiette 62 180 € HT",
        "   Gain de 4 classes  ->  plafond 70 000 € HT ; taux 55 %",
        "=> MaPrimeRénov' = 62 180 × 0,55 = 34 200 €",
        "",
        "SCÉNARIO B — étape 2 : gain de C à B, soit 1 classe seulement",
        "   => Non éligible au Parcours accompagné (2 classes exigées)",
        "   MaPrimeRénov' par geste : 3 000 € (PAC) + 400 € (CET)  = 3 400 €",
        "   CEE : 2 500 € (BAR-TH-171) + 200 € (BAR-TH-148)        = 2 700 €",
        "=> Total des aides de l'étape 2 : 6 100 €",
    ], titre="Calcul détaillé des aides mobilisables")

    R.encadre(
        "Le point le plus contre-intuitif de l'analyse économique",
        ["L'étape 2 du scénario B ne fait gagner qu'une classe, de C à B, alors "
         "que le Parcours accompagné en exige deux. Elle sort donc du dispositif "
         "le plus généreux et bascule sur les forfaits « par geste ».",
         "Concrètement, la pompe à chaleur et le chauffe-eau thermodynamique, "
         "aidés à environ 55 % lorsqu'ils sont intégrés au scénario global, ne le "
         "sont plus qu'à hauteur de 27 % lorsqu'ils sont réalisés isolément trois "
         "ans plus tard.",
         ("Le fractionnement se paie donc deux fois", " : 3 000 € de surcoût de "
          "chantier, et un taux d'aide effondré sur la seconde étape. C'est "
          "l'argument économique décisif en faveur de la rénovation globale — et "
          "un point que le maître d'ouvrage n'a aucun moyen de deviner seul.")],
        couleur=ROUGE, fond=H_ROUGE_PALE, size=9.5, icone="◆")

    R.titre2("Analyse en coût global")
    R.tableau([
        ["Élément financier", "Scénario A", "Scénario B — étape 1",
         "Scénario B — étape 2", "Scénario B — total"],
        ["Coût des travaux TTC", "85 100 €", "65 600 €", "22 500 €", "88 100 €"],
        ["MaPrimeRénov'", "− 38 500 €", "− 34 200 €", "− 3 400 €", "− 37 600 €"],
        ["Certificats d'économies d'énergie", "—", "—", "− 2 700 €", "− 2 700 €"],
        ["Aides locales (estimation prudente)", "− 2 000 €", "− 2 000 €", "—",
         "− 2 000 €"],
        ["Total des aides", "− 40 500 €", "− 36 200 €", "− 6 100 €",
         "− 42 300 €"],
        ["Reste à charge", "44 600 €", "29 400 €", "16 400 €", "45 800 €"],
        ["Apport personnel", "− 10 000 €", "− 10 000 €", "—", "− 10 000 €"],
        ["À financer par éco-PTZ", "34 600 €", "19 400 €", "16 400 €",
         "35 800 €"],
        ["Mensualité sur 20 ans", "144 €/mois", "81 €/mois", "68 €/mois",
         "149 €/mois"],
    ], largeurs=[0.26, 0.19, 0.19, 0.18, 0.18], size=8,
        align_centre_cols=(1, 2, 3, 4), lignes_surlignees=(5, 6, 8),
        titre="Plan de financement des deux scénarios")

    R.images_cote_a_cote(
        [(fg("11_financement"), "Structure du financement"),
         (fg("12_autofinancement"), "Mensualité comparée à l'économie mensuelle")],
        largeurs_cm=[5.8, 5.8],
        legende_globale="Plan de financement et autofinancement du projet")

    R.para(
        "Avec un revenu net mensuel estimé à 4 100 € et un prêt à la "
        "consommation de 300 € par mois, la mensualité de l'éco-prêt porte le "
        "taux d'endettement à 10,8 % dans le scénario A et 11,0 % dans le "
        "scénario B — très en deçà du seuil usuel de 35 %. Surtout, la "
        "mensualité est deux à trois fois inférieure à l'économie réalisée : "
        "144 € contre 348 € pour le scénario A, 81 € contre 254 € pour l'étape 1 "
        "du scénario B, soit un gain net de 204 et 173 € par mois dès la première "
        "année.")

    R.titre3("Coûts mensuels avant et après travaux")
    R.tableau([
        ["Poste", "Aujourd'hui (≈ 16 °C)", "Aujourd'hui à 19 °C",
         "Scénario B — étape 1", "Scénario A — global"],
        ["Propane", "1 871 kg — 3 548 €", "3 340 kg — 6 192 €",
         "468 kg — 1 022 €", "Supprimé"],
        ["Bois bûches", "7 stères — 630 €", "7 stères — 630 €",
         "1,3 stère — 117 €", "1,0 stère — 90 €"],
        ["Électricité", "5 642 kWh — 1 561 €", "5 642 kWh — 1 561 €",
         "5 377 kWh — 1 494 €", "4 572 kWh — 1 333 €"],
        ["Total énergie", "5 739 €", "8 383 €", "2 633 €", "1 423 €"],
        ["Entretien et maintenance", "270 €", "270 €", "330 €", "410 €"],
        ["TOTAL ANNUEL", "6 009 €", "8 653 €", "2 963 €", "1 833 €"],
        ["COÛT MENSUEL", "501 €/mois", "721 €/mois", "247 €/mois", "153 €/mois"],
        ["Économie annuelle vs aujourd'hui", "—", "—", "3 046 €", "4 176 €"],
        ["Économie à confort équivalent", "—", "—", "5 690 €", "6 820 €"],
    ], largeurs=[0.24, 0.20, 0.19, 0.19, 0.18], size=8,
        align_centre_cols=(1, 2, 3, 4), lignes_surlignees=(6, 7),
        titre="Coûts mensuels et annuels avant et après travaux")

    R.figure(fg("08_facture"), largeur_cm=11.6,
             legende="Coût annuel d'exploitation avant et après travaux")

    R.para(
        "L'économie de 4 176 € par an du scénario A est une estimation prudente : "
        "elle compare la facture après travaux à celle que le foyer paie "
        "aujourd'hui en se privant de chauffage. À confort équivalent — 19 °C "
        "dans les deux situations — l'économie réelle atteint 6 820 € par an. "
        "Autrement dit, le foyer gagne à la fois 4 176 € par an et 3 à 4 °C de "
        "température intérieure. Son taux d'effort énergétique passe de 12,8 % à "
        "4,1 % avec le scénario A et à 6,6 % avec l'étape 1 du scénario B : dans "
        "les deux cas, il sort de la précarité énergétique.")

    R.titre3("Coût global sur 20 ans avec augmentation du prix de l'énergie")
    R.para(
        "L'analyse additionne sur vingt ans l'investissement restant à charge, "
        "les dépenses d'énergie indexées à + 4 % par an — moyenne observée sur "
        "les vingt dernières années —, l'entretien indexé à + 2 % par an et le "
        "renouvellement des équipements. Les facteurs cumulés sont de 29,78 pour "
        "l'énergie et 24,30 pour l'entretien. Le scénario B est modélisé avec "
        "réalisation de l'étape 2 à l'année 4.")

    R.tableau([
        ["Composante", "Ne rien faire", "Scénario B — par étapes",
         "Scénario A — global"],
        ["Investissement (reste à charge)", "0 €", "45 800 €", "44 600 €"],
        ["Énergie sur 20 ans (+ 4 %/an)", "170 907 €", "47 515 €", "42 377 €"],
        ["Entretien sur 20 ans (+ 2 %/an)", "6 561 €", "9 633 €", "9 963 €"],
        ["Renouvellement des équipements",
         "14 500 € — chaudière propane vers 2031, ballon d'eau chaude, poêle",
         "3 000 € — chauffe-eau thermodynamique en fin de période",
         "3 000 € — chauffe-eau thermodynamique en fin de période"],
        ["COÛT GLOBAL SUR 20 ANS", "192 000 €", "105 900 €", "99 900 €"],
        ["Économie par rapport à l'inaction", "—", "86 100 €", "92 100 €"],
        ["Retour sur investissement", "—",
         "9,7 ans sur l'étape 1 ; 11,0 ans sur l'ensemble", "10,7 ans"],
    ], largeurs=[0.28, 0.24, 0.24, 0.24], size=8,
        align_centre_cols=(1, 2, 3), lignes_surlignees=(5,),
        titre="Analyse en coût global sur 20 ans")

    R.figure(fg("09_cout_global"), largeur_cm=11.6,
             legende="Décomposition du coût global sur 20 ans")

    R.para(
        "Le résultat est net : ne rien faire est de loin l'option la plus "
        "coûteuse — 192 000 € sur vingt ans, soit près du double du scénario A. "
        "Et cette comparaison est encore favorable à l'inaction, puisqu'elle "
        "suppose que le foyer continue de vivre à 15-16 °C ; à confort "
        "équivalent, l'inaction coûterait environ 270 000 €. L'analyse de "
        "sensibilité, détaillée en annexe 8.6, montre que ces conclusions "
        "résistent à une baisse des prix de l'énergie, à une réduction des aides "
        "de 20 % et à un dépassement du budget de 10 %.")

    R.titre2("Conclusion et recommandation")
    R.para(
        "Les deux scénarios répondent aux objectifs du maître d'ouvrage : ils "
        "divisent la facture par plus de deux, rendent le logement réellement "
        "habitable à 19 °C, le sortent du statut de passoire thermique et "
        "s'autofinancent grâce aux aides et à l'éco-prêt à taux zéro.")
    R.para(
        "Le scénario A, rénovation globale performante, est recommandé. Il "
        "atteint la classe B — énergie B et climat A — soit un gain de cinq "
        "classes, réduit les émissions de 12,2 à 0,25 tonne de CO₂ par an, et "
        "ramène la facture de 6 009 à 1 833 € par an. Il est aussi, contrairement "
        "à l'intuition, le moins coûteux : 85 100 € de travaux contre 88 100 €, "
        "un reste à charge de 44 600 € contre 45 800 €, et un coût global sur "
        "vingt ans de 99 900 € contre 105 900 €. Il n'exige enfin qu'une seule "
        "mobilisation d'entreprises, un seul échafaudage et un seul dossier, et "
        "il apporte le confort immédiatement plutôt que dans trois à cinq ans.")
    R.para(
        "Si la trésorerie devait rendre l'opération globale difficile à engager, "
        "le scénario B reste parfaitement défendable : son étape 1 fait gagner "
        "quatre classes, divise la facture par deux et ne demande qu'un reste à "
        "charge de 29 400 €. Sa réussite dépend toutefois d'une condition : "
        "l'étape 2 doit être explicitement programmée et budgétée dès le départ. "
        "Une rénovation par étapes qui s'arrête à la première n'est plus une "
        "rénovation performante — elle laisse le logement en classe C, dépendant "
        "du propane, avec une chaudière qui atteindra sa fin de vie vers 2031.")
    R.para(
        "Dans les deux cas, le calendrier est contraint : les critères d'aide "
        "applicables jusqu'en septembre 2026 permettent encore de conserver une "
        "chaudière au propane dans une opération de rénovation d'ampleur. Le "
        "dossier doit être déposé avant cette échéance, et impérativement avant "
        "la signature des devis.")


# ==========================================================================
#  CHAPITRE 7 — GLOSSAIRE
# ==========================================================================
def chapitre_7():
    R.titre1("Glossaire")
    entrees = [
        ("3CL", "Méthode de calcul réglementaire du DPE, fondée sur un usage "
                "conventionnel du logement (19 °C) et non sur les "
                "consommations facturées."),
        ("b", "Coefficient de réduction appliqué aux déperditions d'une paroi "
              "donnant sur un local non chauffé. Retenu à 0,85 pour le garage."),
        ("BBC rénovation", "Niveau de performance correspondant à environ "
                           "80 kWh d'énergie primaire par m² et par an, tous "
                           "usages."),
        ("CEE", "Certificats d'économies d'énergie : dispositif obligeant les "
                "fournisseurs d'énergie à financer des travaux d'économie."),
        ("CET", "Chauffe-eau thermodynamique : ballon équipé d'une pompe à "
                "chaleur, qui divise par trois environ la consommation d'un "
                "ballon électrique."),
        ("Compacité", "Rapport entre la surface déperditive et la surface "
                      "habitable. Valeur du projet : 3,08."),
        ("Déphasage", "Temps que met une onde de chaleur pour traverser une "
                      "paroi. Un déphasage de 8 à 12 h reporte la chaleur "
                      "estivale au milieu de la nuit."),
        ("DJU", "Degré-jour unifié : somme des écarts quotidiens entre une "
                "température de base et la température extérieure. Les DJU18 "
                "sont en base 18 °C, les DJU19 en base 19 °C — base de la 3CL."),
        ("DPE", "Diagnostic de performance énergétique : classe de A à G selon "
                "deux axes, énergie primaire et émissions de gaz à effet de "
                "serre. L'étiquette retenue est la plus défavorable."),
        ("DTU", "Document technique unifié : norme définissant les règles de "
                "l'art ; son respect conditionne la garantie décennale."),
        ("Éco-PTZ", "Éco-prêt à taux zéro : jusqu'à 50 000 € sur 20 ans, sans "
                    "intérêt, pour financer une rénovation énergétique."),
        ("ECS", "Eau chaude sanitaire."),
        ("Énergie finale / primaire",
         "L'énergie finale est celle livrée et facturée ; l'énergie primaire "
         "intègre la production et le transport, avec un coefficient de 2,3 pour "
         "l'électricité et 1,0 pour les autres énergies. C'est l'indicateur du "
         "DPE."),
        ("Flamme Verte", "Label des appareils de chauffage au bois, classé en "
                         "étoiles selon le rendement et les émissions. Le "
                         "niveau 7 étoiles est le plus exigeant."),
        ("GV", "Coefficient de déperditions du bâtiment, en W/K : puissance "
               "perdue par degré d'écart entre l'intérieur et l'extérieur. "
               "Somme des parois, des ponts thermiques et du renouvellement "
               "d'air."),
        ("Infiltrométrie", "Test mesurant l'étanchéité à l'air, exprimée par le "
                           "Q4Pa-surf en m³/(h·m²) sous 4 pascals de "
                           "dépression."),
        ("ITE / ITI", "Isolation thermique par l'extérieur / par l'intérieur."),
        ("Lambda (λ)", "Conductivité thermique d'un matériau, en W/(m·K). Plus "
                       "elle est faible, plus le matériau est isolant."),
        ("LNC", "Local non chauffé. Ici, le garage et le grenier attenants."),
        ("Loi d'eau", "Courbe de régulation faisant varier la température de "
                      "départ du chauffage selon la température extérieure."),
        ("MaPrimeRénov'", "Aide de l'État dont le montant dépend des revenus et "
                          "de la performance atteinte. Le « Parcours "
                          "accompagné » vise les rénovations d'ampleur, le "
                          "« par geste » les travaux isolés."),
        ("Perspirance (µ)", "Résistance d'un matériau à la migration de la "
                            "vapeur d'eau : plus µ est faible, plus le matériau "
                            "est perspirant. Critère essentiel sur un mur "
                            "ancien en pierre."),
        ("Pont thermique", "Zone où la résistance thermique est localement "
                           "affaiblie, généralement à la jonction de deux "
                           "parois. Quantifié par ψ, en W/(m·K)."),
        ("R", "Résistance thermique d'une paroi, en m².K/W : R = épaisseur / λ. "
              "Plus elle est élevée, plus la paroi est isolante."),
        ("Radon", "Gaz radioactif naturel issu du sous-sol, pénétrant par le "
                  "plancher bas. Deuxième cause de cancer du poumon en France. "
                  "Seuil d'action : 300 Bq/m³."),
        ("RGE", "Reconnu garant de l'environnement : qualification obligatoire "
                "des entreprises pour l'accès aux aides."),
        ("Rsi / Rse", "Résistances thermiques superficielles intérieure "
                      "(0,13 m².K/W en paroi verticale) et extérieure "
                      "(0,04 m².K/W)."),
        ("SCOP", "Coefficient de performance saisonnier d'une pompe à chaleur : "
                 "chaleur produite rapportée à l'électricité consommée sur une "
                 "saison."),
        ("SHAB", "Surface habitable. Ici, 100 m²."),
        ("Sw", "Facteur solaire d'une menuiserie : part du rayonnement solaire "
               "transmise à l'intérieur."),
        ("Température opérative", "Température ressentie, approximativement "
                                  "moyenne entre la température de l'air et "
                                  "celle des parois. Elle explique l'inconfort "
                                  "ressenti dans un logement non isolé."),
        ("U / Ubat", "U est le coefficient de transmission d'une paroi "
                     "(W/m².K, U = 1/R) ; Ubat est le coefficient moyen de "
                     "l'ensemble des parois, indépendamment de la ventilation."),
        ("VMC hygroréglable B", "Ventilation mécanique contrôlée dont les "
                                "bouches et les entrées d'air modulent leur "
                                "débit selon l'humidité, ce qui limite les "
                                "pertes par ventilation."),
    ]
    lignes = [["Terme", "Définition"]] + [[t, d] for t, d in entrees]
    R.tableau(lignes, largeurs=[0.22, 0.78], size=8, size_entete=9,
              premiere_col_gras=True)


# ==========================================================================
#  CHAPITRE 8 — ANNEXES
# ==========================================================================
def chapitre_8():
    R.titre1("Annexes")
    R.para(
        "Les annexes rassemblent le détail des relevés, des calculs, des "
        "variantes étudiées, du chiffrage et de la mise en œuvre. Chaque renvoi "
        "du corps du rapport pointe vers l'annexe correspondante.")

    # ---------------------------------------------------------------- 8.1
    R.titre2("Relevés détaillés du bâtiment")
    R.tableau([
        ["Rez-de-chaussée", "Surface", "Étage", "Surface"],
        ["Cuisine", "13,7 m²", "Chambre 1", "13,3 m²"],
        ["Salon (poêle à bûches)", "13,2 m²", "Chambre 2", "13,1 m²"],
        ["Buanderie / cellier", "11,1 m²", "Chambre 3", "8,9 m²"],
        ["Salle de bains", "7,3 m²", "Salle de bains", "6,6 m²"],
        ["WC", "2,2 m²", "WC", "1,9 m²"],
        ["Dégagement", "2,7 m²", "Couloir", "2,54 m²"],
        ["Escalier", "2,6 m²", "Escalier et palier", "4,4 m²"],
        ["Placard", "0,8 m²", "Placard", "2,1 m²"],
        ["Sous-total", "53,6 m²", "Sous-total", "52,8 m²"],
    ], largeurs=[0.30, 0.16, 0.30, 0.24], size=8,
        align_centre_cols=(1, 3), lignes_surlignees=(9,),
        titre="Relevé des surfaces par niveau (hauteur sous plafond de 2,50 m)")

    R.para(
        "La surface habitable, obtenue en déduisant l'emprise des escaliers, "
        "s'établit à 99,4 m², ce qui confirme les 100 m² annoncés dans l'énoncé "
        "et retenus pour tous les ratios du rapport.")

    R.tableau([
        ["Grandeur géométrique", "Valeur", "Mode d'obtention"],
        ["Surface habitable chauffée", "100 m²",
         "Relevé sur plans (99,4 m²), arrondi à la valeur de l'énoncé"],
        ["Emprise intérieure par niveau", "57,5 m²",
         "6,85 m × 8,39 m, dimensions relevées sur les plans cotés"],
        ["Volume chauffé", "250 m³", "100 m² × 2,50 m de hauteur sous plafond"],
        ["Hauteur du volume chauffé en façade", "5,60 m",
         "Deux niveaux de 2,50 m, planchers compris"],
        ["Murs sur extérieur (partie opaque)", "125,0 m²",
         "Périmètre extérieur 25,09 m × 5,60 m, menuiseries déduites"],
        ["Mur mitoyen du garage", "52,6 m²", "9,39 m × 5,60 m"],
        ["Menuiseries extérieures", "15,45 m²",
         "9 ouvrants et 1 porte d'entrée"],
        ["Plancher bas sur terre-plein", "57,5 m²", "Emprise du rez-de-chaussée"],
        ["Plafond sous combles perdus", "57,5 m²", "Emprise de l'étage"],
        ["Surface déperditive totale", "308,1 m²",
         "Somme des parois en contact avec l'extérieur ou un local non chauffé"],
        ["Compacité", "3,08", "Surface déperditive rapportée à la surface "
                              "habitable"],
    ], largeurs=[0.34, 0.13, 0.53], size=8, align_centre_cols=(1,),
        lignes_surlignees=(10,), titre="Métré de l'enveloppe thermique")

    R.tableau([
        ["Repère", "Local", "Dimensions", "Surface", "Orientation",
         "Occultation"],
        ["M1", "Salle de bains (RDC)", "910 × 1 600 mm, allège 900", "1,46 m²",
         "Sud-ouest", "Volets battants bois"],
        ["M2", "Cuisine — porte d'entrée", "980 × 2 090 mm, 50 % vitrée",
         "2,05 m²", "Sud-est", "Volets battants bois"],
        ["M3", "Cuisine", "910 × 1 600 mm, allège 900", "1,46 m²", "Sud-est",
         "Volets battants bois à persiennes"],
        ["M4", "Salon — porte-fenêtre", "1 600 × 2 085 mm, soubassement opaque",
         "3,34 m²", "Sud-est", "Volets bois accordéon à persiennes"],
        ["M5", "Chambre 3 (8,9 m²)", "910 × 1 600 mm, allège 900", "1,46 m²",
         "Sud-ouest", "Volets battants bois"],
        ["M6", "WC (étage)", "300 × 680 mm, allège 950", "0,20 m²",
         "Nord-ouest", "Aucune"],
        ["M7", "Chambre 1 (13,3 m²)", "910 × 1 600 mm, allège 850", "1,46 m²",
         "Sud-est", "Volets battants bois à persiennes"],
        ["M8", "Chambre 1 (13,3 m²)", "910 × 1 600 mm, allège 850", "1,46 m²",
         "Sud-est", "Volets battants bois à persiennes"],
        ["M9", "Chambre 2 (13,1 m²)", "1 600 × 1 600 mm, allège 850", "2,56 m²",
         "Sud-est", "Volets accordéon bois"],
        ["Total", "9 ouvrants et 1 porte", "Toutes en simple vitrage, huisserie "
                                           "bois, pose en tunnel",
         "15,45 m²", "80 % au sud-est", "Volets bois conservés"],
    ], largeurs=[0.07, 0.19, 0.25, 0.09, 0.13, 0.27], size=8,
        align_centre_cols=(3, 4), lignes_surlignees=(10,),
        titre="Relevé détaillé des menuiseries de l'enveloppe chauffée")

    R.para(
        "La surface vitrée représente 15,5 % de la surface habitable. Deux "
        "menuiseries situées hors du volume chauffé ne sont pas concernées : la "
        "porte du garage (2 500 × 2 500 mm, 6,25 m²) et la fenêtre du grenier "
        "(1 600 × 1 200 mm, 1,92 m²).")

    R.figure(im("coupe"), largeur_cm=9.3,
             legende="Coupe sur la zone chauffée — les combles perdus, isolés "
                     "à R = 10 m².K/W, surmontent l'étage ; l'accès se fait par "
                     "une échelle depuis la zone non chauffée")

    # ---------------------------------------------------------------- 8.2
    R.titre2("Détail des calculs thermiques")
    R.calcul([
        "1 — Coefficients de transmission des parois",
        "",
        "Mur en pierre calcaire de 50 cm (λ = 2,0 W/m·K)",
        "   R = Rsi + R enduit ext. + R pierre + R enduit plâtre + Rse",
        "   R = 0,13 + 0,02 + 0,50/2,0 + 0,043 + 0,04 = 0,483 m².K/W",
        "=> U = 2,05 W/m².K",
        "",
        "Mur mitoyen du garage (Rsi des deux côtés, pas d'enduit extérieur)",
        "   R = 0,13 + 0,25 + 0,043 + 0,13 = 0,553  =>  U = 1,81 W/m².K",
        "   Coefficient de réduction du local non chauffé : b = 0,85",
        "",
        "Plafond, 40 cm de ouate de cellulose (λ = 0,039)",
        "   R isolant = 10,26 ; R total ≈ 10,50  =>  U = 0,10 W/m².K",
        "",
        "Plancher bas sur terre-plein, 2S/P = 2 × 57,5 / 25,09 = 4,58",
        "=> Ue = 0,55 W/m².K (valeur 3CL pour terre-plein non isolé)",
        "",
        "Menuiseries bois simple vitrage en tunnel : Uw = 4,90 W/m².K",
        "Porte d'entrée bois 50 % vitrée : U = 4,00 W/m².K",
    ], titre="Calcul des coefficients de transmission de l'existant")

    R.calcul([
        "2 — Parois après travaux",
        "",
        "Mur extérieur avec fibre de bois 180 mm (λ = 0,038)",
        "   R isolant = 0,180 / 0,038 = 4,74 m².K/W",
        "   R paroi = 0,13 + 0,04 + 4,74 + 0,25 + 0,043 + 0,02 = 5,22",
        "=> U = 0,19 W/m².K  (soit − 91 % par rapport à 2,05)",
        "",
        "Mur mitoyen avec laine de roche 140 mm (λ = 0,035)",
        "   R isolant = 0,140 / 0,035 = 4,00 m².K/W (≥ 3,7 exigé pour les aides)",
        "   R paroi = 0,13 + 0,13 + 4,00 + 0,25 + 0,043 = 4,55",
        "=> U = 0,22 W/m².K, soit U × b = 0,187",
        "",
        "Menuiseries : double vitrage 4/16/4 argon peu émissif, Uw = 1,30",
        "Porte d'entrée : U = 1,50 W/m².K",
        "Plancher bas avec soubassement isolé : Ue = 0,45 W/m².K",
        "Plafond : inchangé, U = 0,10 W/m².K",
    ], titre="Calcul des coefficients après travaux")

    R.calcul([
        "3 — Apports gratuits",
        "",
        "Apports internes : 4,2 W/m² × 100 m² × 243 j × 24 h / 1000 = 2 449 kWh",
        "",
        "Apports solaires avant travaux",
        "   Surface vitrée au sud-est : 12,33 m² ; au sud-ouest : 2,92 m²",
        "   Aire équivalente ≈ 12,33 × 0,68 × 0,85 × 0,8 (masque) = 5,70 m²",
        "                    + 2,92 × 0,70 × 0,85 × 0,8 × 0,95    = 1,32 m²",
        "   Irradiation de saison sur façade sud-est ≈ 320 kWh/m²",
        "=> Apports solaires ≈ 2 200 kWh/an",
        "",
        "Apports solaires après travaux (double vitrage, g = 0,60) ≈ 1 600 kWh",
        "",
        "Facteur d'utilisation des apports",
        "   0,88 avant travaux (bâtiment très déperditif)",
        "   0,70 après travaux (les apports couvrent une part plus grande",
        "        du besoin, donc une part est perdue en surchauffe)",
    ], titre="Calcul des apports internes et solaires")

    R.tableau([
        ["Usage", "Énergie", "Quantité", "Énergie finale", "Coût annuel",
         "Part"],
        ["Chauffage — chaudière", "Propane", "1 871 kg", "23 912 kWh",
         "3 548 €", "62 %"],
        ["Chauffage — appoint", "Bois bûches", "7 stères", "11 200 kWh",
         "630 €", "11 %"],
        ["Auxiliaires de chauffage", "Électricité", "—", "250 kWh", "63 €",
         "1 %"],
        ["Eau chaude sanitaire", "Électricité", "—", "3 065 kWh", "766 €",
         "13 %"],
        ["Éclairage", "Électricité", "—", "300 kWh", "75 €", "1 %"],
        ["Électricité spécifique et cuisson", "Électricité", "—", "2 027 kWh",
         "507 €", "9 %"],
        ["Abonnement électrique", "—", "—", "—", "150 €", "3 %"],
        ["Total", "", "", "40 754 kWh", "5 739 €", "100 %"],
    ], largeurs=[0.26, 0.14, 0.12, 0.15, 0.14, 0.19], size=8,
        align_centre_cols=(1, 2, 3, 4, 5), lignes_surlignees=(8,),
        titre="Répartition des consommations et de la dépense énergétique réelle")

    R.calcul([
        "4 — Vérification de la cohérence du modèle",
        "",
        "Besoin théorique à 19 °C          : 33 900 kWh/an",
        "Chaleur utile réellement délivrée : 21 700 kWh/an (hypothèse basse)",
        "                                    23 937 kWh/an (hypothèse haute)",
        "",
        "Température intérieure moyenne correspondante",
        "   Hypothèse basse : DJU équivalent 1 943  ->  Tint ≈ 15,2 °C",
        "   Hypothèse haute : DJU équivalent 2 112  ->  Tint ≈ 15,9 °C",
        "=> Fourchette retenue : 15 à 16 °C",
        "",
        "Facture à confort équivalent (19 °C) dans l'état actuel",
        "   Besoin 33 900 kWh ; poêle 6 160 kWh utiles (7 stères, maximum)",
        "   Chaudière : (33 900 − 6 160) / 0,65 = 42 677 kWh PCI = 3 340 kg",
        "   Propane 6 192 € + bois 630 € + électricité 1 561 € + entretien 270 €",
        "=> 8 653 €/an, contre 6 009 € réellement payés aujourd'hui",
    ], titre="Cohérence du modèle et estimation du sous-chauffage",
        couleur=ROUGE)

    # ---------------------------------------------------------------- 8.3
    R.titre2("Analyse environnementale des matériaux d'isolation")
    R.para(
        "Sur un mur en pierre calcaire de 50 cm dépourvu de coupure de "
        "capillarité, le premier critère de choix d'un isolant n'est ni sa "
        "conductivité, ni son prix, ni même son bilan carbone : c'est sa "
        "perméabilité à la vapeur d'eau, caractérisée par le coefficient µ. Un "
        "mur en pierre absorbe de l'humidité par le sol, la pluie battante et la "
        "vapeur intérieure, et il doit pouvoir la restituer. Un isolant "
        "fortement résistant à la vapeur — µ de l'ordre de 60 pour le "
        "polystyrène expansé, 100 pour le polyuréthane — sous un enduit "
        "organique lui aussi étanche fermerait la seule voie de séchage. "
        "L'humidité s'accumulerait alors dans la maçonnerie, avec trois "
        "conséquences : une pierre humide conduit mieux la chaleur, donc la "
        "performance réelle s'éloigne du calcul ; les cycles de gel et de dégel "
        "dégradent l'enduit ; et l'humidité migre vers l'intérieur, provoquant "
        "salpêtre et moisissures.")

    R.tableau([
        ["Matériau", "λ (W/m·K)", "R pour 180 mm", "µ", "Déphasage",
         "Énergie grise", "Bilan carbone", "Coût posé"],
        ["Fibre de bois — retenue", "0,038", "4,74", "3 à 5", "7 à 10 h",
         "≈ 250 kWh/m³", "Stockage de carbone biogénique", "≈ 190 €/m²"],
        ["Laine de roche", "0,035", "5,14", "1", "3 à 4 h", "≈ 200 kWh/m³",
         "Neutre à légèrement émetteur", "≈ 150 €/m²"],
        ["Ouate de cellulose insufflée", "0,039", "4,62", "2", "7 à 9 h",
         "≈ 50 kWh/m³", "Stockage de carbone biogénique", "≈ 165 €/m²"],
        ["Liège expansé", "0,040", "4,50", "10", "8 à 10 h", "≈ 90 kWh/m³",
         "Stockage de carbone biogénique", "≈ 230 €/m²"],
        ["Polystyrène expansé graphité", "0,031", "5,81", "60", "2 à 3 h",
         "≈ 450 kWh/m³", "Émetteur, ressource fossile", "≈ 120 €/m²"],
        ["Polyuréthane", "0,024", "7,50", "100", "≈ 2 h", "≈ 1 000 kWh/m³",
         "Fortement émetteur", "≈ 160 €/m²"],
    ], largeurs=[0.21, 0.09, 0.11, 0.07, 0.10, 0.13, 0.19, 0.10], size=7.5,
        align_centre_cols=(1, 2, 3, 4, 5, 7), lignes_surlignees=(1,),
        titre="Comparaison environnementale et technique des isolants")

    R.para(
        "Les valeurs d'énergie grise et de bilan carbone sont des ordres de "
        "grandeur issus des fiches de déclaration environnementale et sanitaire "
        "et des bases de l'ADEME ; elles varient selon les fabricants et devront "
        "être confirmées par les FDES des produits retenus.")

    R.para(
        "Les matériaux retenus découlent directement de ce critère. Pour les "
        "murs extérieurs, la fibre de bois de 180 mm sous enduit minéral à la "
        "chaux : sa perméance de 3 à 5 laisse le mur respirer, son déphasage de "
        "7 à 10 heures conforte le confort d'été, et elle stocke du carbone "
        "biogénique pendant toute la vie du bâtiment. Pour le mur mitoyen du "
        "garage, la laine de roche de 140 mm : sur cette paroi intérieure à un "
        "local abrité, le déphasage n'a pas d'intérêt, et la laine de roche est "
        "moins chère, incombustible — un atout dans un garage — et encore plus "
        "perspirante. Pour le soubassement, un isolant insensible à l'eau et "
        "imputrescible est impératif : liège expansé ou polystyrène extrudé, la "
        "fibre de bois y étant inadaptée. Pour les menuiseries, l'huisserie bois "
        "offre le meilleur bilan carbone et remplace à l'identique l'existant. "
        "Enfin, pour les combles, le meilleur matériau est celui qu'on n'a pas "
        "besoin de produire : conserver les 40 cm de ouate existants évite à la "
        "fois la dépense et l'impact d'une dépose-repose.")

    R.calcul([
        "Carbone incorporé du chantier (estimation, scénario A)",
        "   Isolation par l'extérieur en fibre de bois, 139 m²  : 3 400 kg CO₂e",
        "   Isolation du mur mitoyen en laine de roche           :   900 kg CO₂e",
        "   Menuiseries bois double vitrage, 15,45 m²            : 1 200 kg CO₂e",
        "   VMC hygroréglable                                    :   400 kg CO₂e",
        "   Chauffe-eau thermodynamique                          :   900 kg CO₂e",
        "   Pompe à chaleur (fluide frigorigène compris)         : 1 800 kg CO₂e",
        "   Poêle étanche et conduit                             :   600 kg CO₂e",
        "   Transports, échafaudage, mise en œuvre               :   800 kg CO₂e",
        "=> Total : environ 10 000 kg CO₂e",
        "",
        "Émissions évitées : 12 230 − 249 = 11 981 kg CO₂/an, soit − 98 %",
        "=> Temps de retour carbone : 10 000 / 11 981 = 0,83 an, soit 10 mois",
    ], titre="Temps de retour carbone du projet", couleur=VERT)

    R.para(
        "Dix mois suffisent à « rembourser » le carbone dépensé pour réaliser "
        "les travaux — chiffre exceptionnellement court, qui tient à la situation "
        "de départ : un logement de 100 m² émettant 12,2 tonnes de CO₂ par an à "
        "cause du propane constitue un gisement d'émissions évitées considérable. "
        "Sur trente ans, les émissions évitées représentent environ 360 tonnes de "
        "CO₂. Les 25 m³ de fibre de bois mis en œuvre stockent par ailleurs "
        "l'équivalent d'environ deux tonnes de CO₂ pendant toute la vie de "
        "l'ouvrage.")

    R.para(
        "Quatre critères complètent l'analyse. Les matériaux mis en œuvre à "
        "l'intérieur seront classés A+ pour les émissions de composés organiques "
        "volatils. En fin de vie, la fibre de bois et la ouate sont compostables "
        "ou valorisables énergétiquement et la laine de roche recyclable via les "
        "filières des fabricants, alors que les isolants pétrosourcés écartés "
        "posent un problème non résolu. Pour la pompe à chaleur, il convient de "
        "privilégier un fluide R290, dont le potentiel de réchauffement global "
        "est de 3, plutôt qu'un R32 (675) : ce choix ne coûte rien et divise par "
        "plus de deux cents l'impact d'une fuite éventuelle. Enfin, "
        "l'approvisionnement du bois en circuit court, certifié et séché à moins "
        "de 20 % d'humidité, conditionne à la fois le rendement du poêle et ses "
        "émissions de particules fines.")

    # ---------------------------------------------------------------- 8.4
    R.titre2("Interfaces et interactions entre les lots")
    R.tableau([
        ["Interface", "Risque en l'absence de traitement", "Prescription"],
        ["Isolation extérieure / menuiseries",
         "Pont thermique de tableau conservé, condensation en périphérie de "
         "dormant, infiltrations",
         "Menuiseries repositionnées au nu extérieur, retour d'isolant de 40 mm "
         "en tableau, bandes précomprimées. Les menuiseries se posent AVANT "
         "l'isolant, l'enduit vient ensuite mourir sur le dormant"],
        ["Isolation extérieure / toiture",
         "Coupure d'isolation en tête de mur annulant une partie du gain",
         "L'isolant remonte jusqu'à la sablière et recouvre la périphérie de "
         "l'isolant des combles ; chevronnage rapporté si le débord est "
         "insuffisant"],
        ["Isolation extérieure / soubassement",
         "Remontées capillaires dans un isolant sensible à l'eau, effet de bord "
         "en pied de mur",
         "Isolant non sensible à l'eau descendu 60 cm sous le terrain, profilé "
         "de départ ventilé, vérification préalable de l'humidité"],
        ["Isolation extérieure / mur mitoyen",
         "Coupure d'isolation dans l'angle entre façade et mur du garage",
         "Retour de la laine de roche sur 1 m dans le garage, de part et "
         "d'autre de l'angle"],
        ["Isolation extérieure / réseaux de façade",
         "Descentes d'eaux pluviales, coffret électrique et luminaires noyés ou "
         "arrachés",
         "Dépose et repose systématiques, platines de fixation désolidarisées "
         "traversant l'isolant"],
        ["Isolation extérieure / volets",
         "Volets battants inutilisables, l'isolant avançant le nu de façade de "
         "21 cm",
         "Gonds rallongés, arrêts déportés, dépose et repose incluses au lot "
         "menuiseries"],
        ["Menuiseries / ventilation",
         "Entrées d'air non prévues : la VMC ne peut pas balayer le logement",
         "Entrées d'air hygroréglables intégrées d'usine aux menuiseries des "
         "pièces principales — à spécifier dès le devis"],
        ["Étanchéité à l'air / ventilation",
         "Une VMC sur enveloppe non étanche aspire par les fuites : débits faux "
         "et surconsommation",
         "Ordre imposé : étanchéité, puis test intermédiaire, puis pose et "
         "réglage de la VMC"],
        ["Ventilation / appareil à combustion",
         "Mise en dépression, refoulement des fumées, intoxication au monoxyde "
         "de carbone",
         "Poêle étanche raccordé sur air extérieur par conduit concentrique — "
         "prescription de sécurité impérative"],
        ["Étanchéité à l'air / trappe de comble",
         "Fuite majeure concentrée, condensation dans l'isolant",
         "Trappe isolée à R ≥ 6 et munie d'un joint périphérique, membrane "
         "reprise sur son pourtour"],
        ["Isolation / dimensionnement du chauffage",
         "Générateur surdimensionné, cycles courts, rendement dégradé, surcoût",
         "Le générateur est dimensionné APRÈS calcul du besoin résiduel de "
         "4,1 kW, jamais sur les 17,1 kW actuels"],
        ["Générateur / émetteurs",
         "Radiateurs incapables de délivrer la puissance au régime de la pompe à "
         "chaleur",
         "Vérification calculée au § 5.1 ; désembouage préalable obligatoire"],
        ["Générateur / réseau électrique",
         "Disjonction au démarrage de la pompe à chaleur",
         "Passage de 6 à 9 kVA, vérification du tableau, protection dédiée"],
        ["Chauffe-eau / ventilation",
         "Un chauffe-eau sur air ambiant refroidirait le garage et "
         "concurrencerait la VMC",
         "Raccordement sur air extérieur par gainage double, indépendant du "
         "réseau de VMC"],
        ["Dépose de la chaudière / cuve",
         "Cuve abandonnée sans neutralisation : risque environnemental et "
         "responsabilité du propriétaire",
         "Dégazage, extraction ou remplissage inerte par le distributeur, avec "
         "remise d'un certificat"],
    ], largeurs=[0.19, 0.33, 0.48], size=8,
        titre="Interfaces entre lots : risques identifiés et prescriptions")

    # ---------------------------------------------------------------- 8.5
    R.titre2("Variantes étudiées et écartées")
    R.para(
        "Le choix de l'isolation par l'extérieur plutôt que par l'intérieur, "
        "argumenté au § 4.3, repose sur sept critères. L'inertie : les 50 cm de "
        "pierre restent du côté chauffé et le confort d'été est préservé, alors "
        "qu'une isolation intérieure placerait cette masse hors du volume isolé. "
        "Les ponts thermiques : traités en continu, ils passent de 27,7 à "
        "8,1 W/K, tandis que planchers et refends resteraient traversants par "
        "l'intérieur. La surface habitable : aucune perte, contre environ 6 m² "
        "sur 100. L'occupation : le logement reste habité, sauf pendant la pose "
        "des menuiseries, alors qu'un relogement de plusieurs mois serait "
        "nécessaire. L'humidité : le mur reste du côté chaud et sèche vers "
        "l'extérieur à travers un complexe perspirant, alors qu'il passerait du "
        "côté froid par l'intérieur, avec un risque de condensation et de gel "
        "dans la maçonnerie. Le coût : environ 23 000 € contre 16 000 €, mais "
        "auxquels s'ajouteraient le relogement, la reprise des sols, des "
        "plinthes, de l'électricité et des menuiseries intérieures. Seul "
        "avantage réel de l'isolation intérieure : l'aspect extérieur reste "
        "inchangé, ce qui deviendrait déterminant en cas d'avis défavorable de "
        "l'Architecte des Bâtiments de France.")

    R.tableau([
        ["Solution d'eau chaude sanitaire", "Consommation", "Investissement",
         "Analyse"],
        ["Ballon électrique conservé", "3 065 kWh/an", "0 €",
         "Situation actuelle : effet Joule et pertes aggravées par le local "
         "froid. Poste le moins performant du logement"],
        ["Ballon électrique neuf à isolation renforcée", "2 400 kWh/an",
         "1 200 €",
         "Écartée : améliore les pertes de stockage mais reste en effet Joule ; "
         "le gain ne justifie pas la dépense"],
        ["Chauffe-eau thermodynamique sur air ambiant du garage", "1 100 kWh/an",
         "3 200 €",
         "Écartée : le garage descend à 5-8 °C en hiver, ce qui effondre le COP "
         "quand le besoin est le plus fort, et son refroidissement accroît les "
         "déperditions du mur mitoyen"],
        ["Chauffe-eau thermodynamique sur air extérieur — retenue",
         "800 kWh/an", "4 200 €",
         "Retenue : COP saisonnier de 2,8 indépendant du garage, aucun "
         "refroidissement du local, gain de 2 265 kWh/an, retour de 7,7 ans "
         "avant aides"],
        ["Production par la pompe à chaleur (ballon bi-énergie)", "950 kWh/an",
         "3 000 €",
         "Écartée : le COP chute fortement à 55 °C et la machine serait "
         "mobilisée tout l'été pour l'eau chaude seule"],
        ["Chauffe-eau solaire thermique", "600 kWh/an", "7 500 €",
         "Écartée : temps de retour supérieur à 25 ans pour un foyer de "
         "4 personnes. Techniquement valable mais économiquement injustifiée ici"],
    ], largeurs=[0.28, 0.12, 0.12, 0.48], size=8,
        align_centre_cols=(1, 2), lignes_surlignees=(4,),
        titre="Solutions de production d'eau chaude sanitaire comparées")

    # ---------------------------------------------------------------- 8.6
    R.titre2("Chiffrage détaillé et analyse de sensibilité")
    R.tableau([
        ["Poste", "Métré", "Prix unitaire", "Montant TTC",
         "Observations sur le prix"],
        ["Isolation par l'extérieur des murs", "139 m² traités", "190 €/m²",
         "26 400 €",
         "125 m² de mur opaque et 14 m² de tableaux et appuis ; main-d'œuvre et "
         "échafaudage ≈ 40 % du prix"],
        ["Isolation du soubassement", "15 m²", "forfait", "2 200 €",
         "Terrassement léger, isolant non sensible à l'eau, profilé de départ "
         "ventilé"],
        ["Isolation du mur mitoyen", "52,6 m²", "75 €/m²", "3 950 €",
         "Ossature, laine de roche 140 mm et parement, posés depuis le garage"],
        ["Menuiseries", "15,45 m², 10 ouvrants", "—", "12 700 €",
         "8 fenêtres et portes-fenêtres 10 050 €, porte d'entrée 2 200 €, châssis "
         "de WC 450 € ; dépose totale et habillages compris"],
        ["Volets bois", "9 ensembles", "200 €/unité", "1 800 €",
         "Dépose, révision, traitement, repose sur gonds rallongés"],
        ["Étanchéité à l'air", "—", "forfait", "2 600 €",
         "Membrane, liaisons, traversées, trappe de comble, deux tests "
         "d'infiltrométrie"],
        ["VMC hygroréglable B", "5 bouches, 5 entrées d'air", "forfait",
         "3 400 €",
         "Caisson basse consommation, réseau isolé, mise en service et mesure des "
         "débits"],
        ["Poêle à bûches étanche", "5 kW", "forfait", "5 200 €",
         "Flamme Verte 7 étoiles, conduit concentrique, tubage, dépose de "
         "l'appareil existant"],
        ["Chauffe-eau thermodynamique", "200 L", "forfait", "4 200 €",
         "Sur air extérieur gainé, dépose du ballon existant, calorifugeage des "
         "liaisons"],
        ["Pompe à chaleur air/eau", "6 kW", "forfait", "14 000 €",
         "Inverter R290, bouteille de découplage, hydraulique, raccordement dédié"],
        ["Régulation et réseau", "—", "forfait", "1 700 €",
         "8 robinets thermostatiques, désembouage chimique avec rinçage, "
         "équilibrage par tés de réglage"],
        ["Dépose de l'installation propane", "—", "forfait", "2 600 €",
         "Dépose, dégazage et neutralisation de la cuve avec certificat, "
         "résiliation du contrat"],
        ["Adaptation électrique", "6 → 9 kVA", "forfait", "500 €",
         "Mise à niveau du tableau et protection dédiée"],
        ["Éclairage", "—", "forfait", "300 €",
         "Remplacement des halogènes par des LED à indice de rendu supérieur "
         "à 80"],
        ["Ingénierie", "—", "forfait", "3 500 €",
         "Audit énergétique réglementaire et Accompagnateur Rénov' agréé, "
         "obligatoires pour le parcours accompagné"],
        ["TOTAL SCÉNARIO A", "", "", "85 100 €", ""],
    ], largeurs=[0.19, 0.12, 0.09, 0.11, 0.49], size=7.5,
        align_centre_cols=(1, 2, 3), lignes_surlignees=(16,),
        titre="Chiffrage détaillé du scénario A")

    R.tableau([
        ["Hypothèse testée", "Effet sur le scénario A", "Conclusion"],
        ["Prix bas : propane à 1,50 €/kg, électricité à 0,22 €/kWh",
         "Économie annuelle de 3 522 € au lieu de 4 176 € ; retour porté à "
         "12,7 ans",
         "La rentabilité demeure : le projet reste largement autofinancé"],
        ["Prix haut : propane à 2,20 €/kg, électricité à 0,30 €/kWh",
         "Économie annuelle de 5 007 € ; retour ramené à 8,9 ans",
         "La rentabilité s'améliore. Hypothèse la plus probable compte tenu de "
         "la trajectoire des énergies fossiles"],
        ["Aides réduites de 20 %",
         "Reste à charge porté de 44 600 € à 52 700 € ; retour de 12,6 ans",
         "Le projet reste finançable : la mensualité passerait de 144 à 178 €, "
         "toujours inférieure aux 348 € d'économie mensuelle"],
        ["Coût des travaux dépassé de 10 %",
         "Montant porté à 93 600 € ; l'assiette étant déjà plafonnée, l'aide "
         "reste de 38 500 € et le reste à charge atteint 53 100 €",
         "Une marge d'aléas de 5 à 10 % doit être prévue au budget ; elle ne "
         "remet pas en cause la décision"],
        ["SCOP réel de 3,0 au lieu de 3,5",
         "Consommation de chauffage portée de 1 440 à 1 680 kWh, soit 60 € de "
         "plus par an",
         "Impact marginal : le dimensionnement au juste besoin et le régime "
         "45/35 sécurisent ce paramètre"],
    ], largeurs=[0.24, 0.38, 0.38], size=8,
        titre="Analyse de sensibilité aux principales hypothèses")

    # ---------------------------------------------------------------- 8.7
    R.titre2("Cadre réglementaire et inventaire complet des aides")
    R.tableau([
        ["Domaine", "Règle applicable", "Incidence concrète"],
        ["Autorisation d'urbanisme",
         "Article R.421-17 du code de l'urbanisme : déclaration préalable pour "
         "tout travail modifiant l'aspect extérieur",
         "Obligatoire pour l'isolation par l'extérieur et les menuiseries. "
         "Instruction : un mois, deux en périmètre protégé"],
        ["PLU et patrimoine",
         "PLU de Saint-Jean-de-Chevelu ; périmètre éventuel de monument "
         "historique",
         "À vérifier en mairie avant toute commande : teintes d'enduit, aspect "
         "des menuiseries, encadrements. Un avis défavorable de l'Architecte "
         "des Bâtiments de France basculerait le projet vers une isolation par "
         "l'intérieur"],
        ["Implantation", "Article L.113-5-1 du code de l'urbanisme",
         "Autorise un dépassement des règles d'implantation jusqu'à 30 cm pour "
         "l'isolation par l'extérieur : les 21 cm du complexe sont couverts"],
        ["Thermique",
         "Arrêté du 3 mai 2007 modifié, dit « élément par élément » (la RE2020 "
         "ne s'applique pas à l'existant)",
         "R ≥ 3,7 m².K/W pour un mur isolé par l'extérieur en zone H1 et pour "
         "un mur sur local non chauffé ; Uw ≤ 1,3 W/m².K pour les fenêtres. "
         "Les solutions retenues dépassent ces seuils"],
        ["Ventilation", "Arrêté du 24 mars 1982 modifié",
         "Ventilation générale et permanente avec balayage ; débit total "
         "minimal de 90 m³/h pour un T4"],
        ["Entreprises et règles de l'art",
         "Qualification RGE obligatoire lot par lot ; DTU 45.4, 36.5, 68.3, "
         "24.1 et 65.16",
         "À viser explicitement dans chaque devis ; conditionnent les aides et "
         "la garantie décennale"],
        ["Sécurité et diagnostics",
         "Détecteur de fumée obligatoire, ramonage biannuel ; bâtiment "
         "antérieur à 1997",
         "Détecteur de monoxyde de carbone recommandé avec un appareil à "
         "combustion et une VMC ; repérage amiante avant travaux"],
    ], largeurs=[0.17, 0.33, 0.50], size=8,
        titre="Cadre réglementaire et administratif du projet")

    R.tableau([
        ["Dispositif", "Conditions d'accès", "Applicabilité", "Montant estimé"],
        ["MaPrimeRénov' Parcours accompagné",
         "Gain minimum de 2 classes ; au moins 2 postes d'isolation ; sortie de "
         "passoire si F ou G ; Accompagnateur Rénov' et audit obligatoires ; "
         "entreprises RGE. Taux intermédiaires 45 %, majoré de 10 points en "
         "sortie de passoire. Plafond : 40 000 € HT pour 2 classes, 55 000 € "
         "pour 3, 70 000 € pour 4 et plus",
         "Scénario A : gain de 5 classes. Scénario B étape 1 : gain de "
         "4 classes. L'étape 2, ne gagnant qu'une classe, n'y est pas éligible",
         "38 500 € (A)\n34 200 € (B1)"],
        ["MaPrimeRénov' par geste",
         "Travaux isolés par une entreprise RGE. Forfaits intermédiaires : "
         "3 000 € pour une pompe à chaleur air/eau, 400 € pour un chauffe-eau "
         "thermodynamique. Non cumulable avec le parcours accompagné",
         "Seule voie d'aide pour l'étape 2 du scénario B", "3 400 € (B2)"],
        ["Certificats d'économies d'énergie",
         "Fiches BAR-TH-171 (pompe à chaleur), BAR-TH-148 (chauffe-eau "
         "thermodynamique), BAR-EN-102 (isolation des murs)",
         "Non cumulables avec le parcours accompagné, qui intègre déjà leur "
         "valorisation ; mobilisables sur l'étape 2", "2 700 € (B2)"],
        ["Éco-prêt à taux zéro",
         "Jusqu'à 50 000 € sur 20 ans pour une rénovation globale (gain ≥ 35 % "
         "d'énergie primaire et sortie de passoire) ; cumulable avec "
         "MaPrimeRénov'",
         "Éligible dans les deux scénarios : le gain atteint 88 %",
         "34 600 € (A)\n35 800 € (B)"],
        ["TVA à taux réduit de 5,5 %",
         "Travaux de performance énergétique et travaux induits, logement de "
         "plus de 2 ans", "Applicable à tous les postes, déjà intégrée aux "
                          "montants TTC", "≈ 12 800 € d'économie"],
        ["Aides locales",
         "Communauté d'agglomération Grand Lac, Département de la Savoie, Région "
         "Auvergne-Rhône-Alpes",
         "À instruire auprès de l'espace conseil France Rénov' de Savoie ; "
         "estimation volontairement prudente", "2 000 €"],
        ["Exonération de taxe foncière",
         "Article 1383-0 B du CGI : 50 à 100 % pendant 3 ans, sur délibération "
         "de la collectivité, au-delà de 10 000 € de travaux",
         "À vérifier auprès de la commune ; non intégrée au plan de financement "
         "par prudence", "0 à 900 €"],
        ["Prêt avance rénovation",
         "Prêt hypothécaire remboursable à la vente ou à la succession",
         "Non nécessaire : la capacité de remboursement permet l'éco-prêt "
         "classique. Mentionné comme solution de repli", "—"],
    ], largeurs=[0.16, 0.33, 0.32, 0.19], size=8,
        titre="Inventaire des aides mobilisables et de leur applicabilité")


    R.titre2("Points de vigilance technique et de sécurité")
    R.tableau([
        ["N°", "Point de vigilance", "Risque et mesure à prendre"],
        ["1", "Poêle non étanche et ventilation mécanique",
         "Mise en dépression, refoulement des fumées, intoxication au monoxyde "
         "de carbone — risque vital. Remplacement obligatoire par un poêle "
         "étanche sur air extérieur, détecteur de CO. Ne peut être différé"],
        ["2", "Perspirance du complexe isolant",
         "Piégeage de l'humidité dans le mur en pierre : perte de performance, "
         "gel de l'enduit, salpêtre à l'intérieur. Isolant à faible µ sous "
         "enduit minéral à la chaux ; polystyrène, polyuréthane et enduit "
         "organique à interdire dans le devis"],
        ["3", "Remontées capillaires et soubassement",
         "Le mur repose sur un terre-plein sans coupure de capillarité. "
         "Vérification en pied de mur, isolant de soubassement insensible à "
         "l'eau, profilé de départ ventilé, drainage périphérique si nécessaire"],
        ["4", "Continuité de l'isolation en tête de mur et trappe de comble",
         "Ponts thermiques résiduels et fuites d'air concentrées annulant une "
         "part du gain. L'isolant remonte jusqu'à la sablière en recouvrement de "
         "l'isolant des combles ; trappe isolée à R ≥ 6 avec joint périphérique "
         "et membrane reprise"],
        ["5", "Menuiseries posées en tunnel",
         "Pont thermique de tableau conservé et condensation en périphérie de "
         "dormant. Repositionnement au nu extérieur, retour d'isolant de 40 mm, "
         "appuis à rupture de pont thermique"],
        ["6", "Réseau de chauffage et radiateurs",
         "Pertes intégrales dans le garage et perte de surface d'échange par "
         "embouage. Calorifugeage classe 4 sur l'aller et le retour ; "
         "désembouage chimique avec rinçage puis équilibrage, obligatoire avant "
         "la mise en service de la pompe à chaleur"],
        ["7", "Cuve propane enterrée",
         "Cuve abandonnée sans neutralisation : risque environnemental et "
         "responsabilité du propriétaire. Neutralisation par le distributeur "
         "avec certificat ; vérifier les frais de résiliation et la reprise du "
         "solde de gaz"],
        ["8", "Pompe à chaleur : électricité et bruit",
         "Disjonction au démarrage et gêne pour le voisinage. Passage de 6 à "
         "9 kVA avec protection dédiée ; implantation à l'est contre le mur du "
         "garage, plots antivibratiles, moins de 45 dB(A) à 3 m, distance aux "
         "limites séparatives respectée"],
        ["9", "Urbanisme, patrimoine et amiante",
         "Refus de la déclaration préalable, prescriptions de l'Architecte des "
         "Bâtiments de France, ou présence d'amiante dans les matériaux des "
         "années 1990. Vérifications du PLU et repérage avant toute commande ; "
         "repli possible sur une isolation par l'intérieur"],
        ["10", "Radon, ventilation du comble et ordre des lots",
         "Commune potentiellement en zone de catégorie 3 : mesure par dosimètre "
         "avant travaux. Ne pas obstruer la ventilation du comble. Séquence "
         "imposée : menuiseries, étanchéité à l'air, test intermédiaire, VMC, "
         "réglage des débits"],
    ], largeurs=[0.05, 0.24, 0.71], size=8,
        align_centre_cols=(0,), lignes_surlignees=(1,),
        titre="Points de vigilance technique et de sécurité")

    # ---------------------------------------------------------------- 8.8
    R.titre2("Plan d'action et phasage du projet")
    R.para(
        "Le plan ci-dessous correspond au scénario A. Il intègre une contrainte "
        "majeure : le dossier MaPrimeRénov' doit être déposé avant "
        "septembre 2026 et, en tout état de cause, avant la signature des devis — "
        "un devis signé avant le dépôt fait perdre la totalité de l'aide.")

    R.tableau([
        ["Phase", "Période", "Actions", "Acteurs", "Point de contrôle"],
        ["0 — Préparation", "Mois 1 à 2",
         "Contact France Rénov' ; vérification du PLU et d'un éventuel périmètre "
         "protégé ; mesure du radon ; repérage amiante ; inspection du comble",
         "Maître d'ouvrage, France Rénov', diagnostiqueur",
         "Faisabilité de l'isolation par l'extérieur confirmée"],
        ["1 — Ingénierie", "Mois 2 à 3",
         "Désignation de l'Accompagnateur Rénov' ; audit énergétique "
         "réglementaire ; test d'infiltrométrie initial ; dépôt de la "
         "déclaration préalable",
         "Accompagnateur Rénov', bureau d'études",
         "Audit validé, déclaration préalable déposée"],
        ["2 — Consultation", "Mois 3 à 4",
         "Trois entreprises RGE consultées par lot ; vérification des "
         "qualifications et assurances ; prescriptions intégrées aux devis",
         "Maître d'ouvrage, Accompagnateur Rénov'",
         "Devis conformes aux prescriptions du rapport"],
        ["3 — Financement", "Mois 4 à 5",
         "DÉPÔT DU DOSSIER MaPrimeRénov' AVANT SIGNATURE DES DEVIS ; demande "
         "d'éco-prêt à taux zéro ; instruction des aides locales ; accord de la "
         "déclaration préalable", "Maître d'ouvrage, Anah, banque",
         "Notification d'octroi reçue — condition de la signature"],
        ["4 — Enveloppe", "Mois 6 à 9",
         "Échafaudage ; réseaux de façade ; menuiseries ; isolation par "
         "l'extérieur et soubassement ; enduit ; mur mitoyen ; repose des volets", "Entreprises RGE : menuiserie, isolation, façade",
         "Test d'infiltrométrie intermédiaire : Q4Pa ≤ 1,3"],
        ["5 — Étanchéité et ventilation", "Mois 9",
         "Traitement des liaisons et de la trappe de comble ; pose et réglage "
         "de la VMC ; détalonnage des portes ; mesure des débits",
         "Entreprise de ventilation",
         "Débits mesurés conformes à l'arrêté de 1982"],
        ["6 — Chaufferie", "Mois 9 à 10",
         "Dépose de la chaudière et neutralisation de la cuve ; pompe à chaleur ; "
         "désembouage, équilibrage et robinets thermostatiques ; chauffe-eau "
         "thermodynamique ; poêle étanche ; 9 kVA",
         "Chauffagiste RGE, fumiste, électricien, distributeur propane",
         "Mise en service, réglage de la loi d'eau, certificat de "
         "neutralisation"],
        ["7 — Réception", "Mois 10 à 11",
         "Test d'infiltrométrie final ; réception et lever des réserves ; DPE "
         "après travaux ; solde des aides ; remise des notices",
         "Maître d'ouvrage, Accompagnateur Rénov', entreprises",
         "Classe B confirmée ; solde des aides versé"],
        ["8 — Suivi", "Mois 12 à 24",
         "Relevé mensuel des consommations ; ajustement de la loi d'eau après la "
         "première saison ; premier entretien annuel", "Maître d'ouvrage, mainteneur",
         "Consommations conformes aux prévisions ; confort à 19 °C vérifié"],
    ], largeurs=[0.14, 0.09, 0.38, 0.19, 0.20], size=7.5,
        lignes_surlignees=(4,),
        titre="Plan d'action détaillé du scénario A")

    R.encadre(
        "Trois règles à ne jamais enfreindre",
        [("Ne jamais signer un devis avant la notification de MaPrimeRénov'. ",
          "Un devis signé avant le dépôt du dossier fait perdre l'intégralité de "
          "l'aide, soit 38 500 €. C'est l'erreur la plus fréquente et la plus "
          "coûteuse."),
         ("Vérifier la qualification RGE de chaque entreprise, lot par lot, à la "
          "date de signature. ", "Une qualification expirée ou ne couvrant pas le "
          "geste concerné entraîne le refus de l'aide sur ce poste."),
         ("Respecter l'ordre des lots. ", "Les menuiseries se posent avant "
          "l'isolant ; l'étanchéité à l'air se traite et se contrôle avant la "
          "pose de la VMC ; le désembouage précède la mise en service de la "
          "pompe à chaleur.")],
        couleur=ROUGE, fond=H_ROUGE_PALE, size=9.5, icone="◆")

    R.para(
        "L'isolation par l'extérieur se réalisant depuis l'extérieur, le foyer "
        "peut rester dans les lieux pendant l'essentiel du chantier. Seules deux "
        "périodes demandent une organisation particulière : la semaine de "
        "remplacement des menuiseries, où les pièces sont ouvertes une à une, et "
        "les deux à trois jours de bascule de la chaufferie, à programmer hors "
        "période de grand froid. La faculté de relogement n'a donc pas besoin "
        "d'être mobilisée — avantage supplémentaire de l'isolation par "
        "l'extérieur.")

    R.para(
        "Dans le scénario B, la répartition des lots entre les deux étapes obéit "
        "à une logique stricte. L'étape 1 regroupe tout ce qui touche à "
        "l'enveloppe et à la ventilation, ainsi que les postes qui en dépendent "
        "directement : les menuiseries, indissociables de l'isolation par "
        "l'extérieur puisqu'elles se posent au nu extérieur ; l'étanchéité à "
        "l'air, qui doit précéder la ventilation ; la VMC, obligatoire dès que "
        "l'enveloppe est étanchéifiée ; le poêle étanche, obligation de sécurité "
        "liée à la VMC ; et l'optimisation de la chaudière conservée, peu "
        "coûteuse et qui valide en conditions réelles le régime 45/35 de la "
        "future pompe à chaleur. L'étape 2 ne regroupe que les postes sans "
        "interaction avec l'enveloppe — chauffe-eau thermodynamique, pompe à "
        "chaleur, dépose de la chaudière et de la cuve — et bénéficie du besoin "
        "réduit obtenu à l'étape 1 : la machine est ainsi dimensionnée sur "
        "4,1 kW et non sur 17,1 kW.")

    # ---------------------------------------------------------------- 8.9
    R.titre2("Plan de sobriété remis au maître d'ouvrage")
    R.para(
        "Les travaux réduisent les besoins ; les usages déterminent ce qui est "
        "réellement consommé. Les gestes ci-dessous, sans coût ou presque, "
        "représentent au total 8 à 12 % de la facture après travaux, soit 150 à "
        "220 € par an dans le scénario A.")

    R.tableau([
        ["Domaine", "Geste recommandé", "Gain estimé"],
        ["Températures de consigne",
         "19 °C dans les pièces de vie, 17 °C dans les chambres, 22 °C dans les "
         "salles de bains au seul moment de la toilette. Chaque degré au-dessus "
         "de 19 °C coûte environ 7 % de consommation de chauffage",
         "5 à 7 % du chauffage"],
        ["Programmation",
         "Réduit nocturne de 3 °C entre 22 h et 6 h ; 16 °C en cas d'absence de "
         "plus de deux jours ; programmation hebdomadaire adaptée au rythme du "
         "foyer", "3 à 5 % du chauffage"],
        ["Gestion des volets",
         "Fermeture systématique à la tombée de la nuit en hiver : la lame d'air "
         "ventilée derrière un volet fermé améliore le coefficient de la fenêtre "
         "d'environ 0,3 W/m².K", "2 à 3 % du chauffage"],
        ["Confort d'été",
         "Volets à persiennes fermés dès que la température extérieure dépasse "
         "celle de l'intérieur ; ouverture traversante la nuit pour décharger "
         "l'inertie de la pierre", "Évite tout recours à la climatisation"],
        ["Eau chaude sanitaire",
         "Ballon réglé à 55 °C — suffisant et nécessaire contre la légionelle ; "
         "mitigeurs thermostatiques ; mousseurs ; douches de moins de cinq "
         "minutes ; programmation en heures creuses", "15 à 20 % de l'ECS"],
        ["Bois de chauffage",
         "Bûches séchées à moins de 20 % d'humidité, soit deux ans sous abri "
         "ventilé ; allumage par le haut, qui réduit les émissions de particules "
         "d'environ 80 % ; jamais d'allure réduite prolongée",
         "10 à 15 % de rendement du poêle"],
        ["Ventilation",
         "Ne jamais obstruer les entrées d'air ni les bouches ; les nettoyer deux "
         "fois par an ; aérer brièvement et largement plutôt que longuement et "
         "peu", "Préserve la performance de la VMC"],
        ["Électricité spécifique",
         "Bandeaux multiprises à interrupteur pour supprimer les veilles ; "
         "électroménager de classe A ou B au renouvellement ; lave-linge et "
         "lave-vaisselle remplis et programmés en heures creuses",
         "10 à 15 % des 2 027 kWh"],
        ["Éclairage",
         "Passage intégral en LED, déjà intégré aux travaux ; extinction des "
         "pièces inoccupées ; valorisation de la lumière naturelle du sud-est",
         "150 kWh/an"],
        ["Entretien",
         "Entretien annuel de la pompe à chaleur et du chauffe-eau ; ramonage "
         "deux fois par an ; nettoyage des filtres et bouches ; contrôle de la "
         "pression du circuit", "Préserve 5 à 10 % de rendement dans la durée"],
        ["Suivi des consommations",
         "Relevé mensuel des index ; comparaison d'une année sur l'autre après "
         "correction par les degrés-jours ; vérification que la consommation "
         "réelle rejoint la prévision", "Détecte toute dérive dès son apparition"],
    ], largeurs=[0.17, 0.61, 0.22], size=8,
        titre="Plan de sobriété : gestes, effets et gains attendus")

    R.encadre(
        "Une recommandation particulière après travaux : l'effet rebond",
        ["Après une rénovation performante, les occupants d'un logement "
         "auparavant sous-chauffé élèvent naturellement leur consigne bien "
         "au-delà de 19 °C, parce que le chauffage devient abordable.",
         "C'est légitime et cela fait même partie du bénéfice attendu : le foyer "
         "retrouve un confort dont il était privé. Mais il faut en avoir "
         "conscience, car chaque degré supplémentaire coûte environ 7 % de "
         "consommation de chauffage — une consigne à 22 °C réduirait l'économie "
         "annoncée d'environ 20 %.",
         "La recommandation est donc simple : viser 19 à 20 °C dans les pièces "
         "de vie, ce qui, avec des parois désormais à plus de 18 °C, procurera un "
         "confort très supérieur à celui ressenti aujourd'hui à la même "
         "température d'air."],
        couleur=BLEU, fond=H_BLEU_PALE, size=9.5)

    # ---------------------------------------------------------------- 8.10
    R.titre2("Hypothèses de calcul")
    R.tableau([
        ["Domaine", "Paramètres et valeurs retenues", "Source ou justification"],
        ["Climat",
         "Zone H1c à 498 m ; température extérieure de base − 12 °C ; DJU19 "
         "corrigés 2 860 °C.j ; saison de chauffe de 243 jours (octobre à mai)",
         "Zonage réglementaire ; NF EN 12831 ; correction d'altitude et de base "
         "détaillée au § 3.3 ; énoncé du sujet"],
        ["Contenu énergétique",
         "Propane 12,78 kWh/kg (PCI) ; bois 1 600 kWh/stère",
         "Valeurs conventionnelles ; feuillus durs, bûches de 50 cm à 20 % "
         "d'humidité"],
        ["Coefficients réglementaires",
         "Énergie primaire : 2,3 pour l'électricité, 1,0 sinon. Émissions : "
         "propane 0,272 ; bois 0,030 ; électricité 0,079 kg CO₂/kWh",
         "Arrêtés relatifs au diagnostic de performance énergétique"],
        ["Prix de l'énergie",
         "Propane 1,80 €/kg + 180 €/an de location de citerne ; bois 90 €/stère ; "
         "électricité 0,25 €/kWh (0,22 en heures creuses) ; indexation + 4 %/an",
         "Marché 2026 ; sensibilité testée de 1,50 à 2,20 €/kg et de 0,22 à "
         "0,30 €/kWh ; indexation issue de la moyenne des vingt dernières années"],
        ["Enveloppe",
         "Pierre calcaire λ = 2,0 W/(m·K) ; coefficient de réduction du garage "
         "b = 0,85 ; Q4Pa-surf = 3,5 m³/(h·m²) ; renouvellement d'air 0,90 vol/h "
         "avant et 0,45 après travaux",
         "Valeur conventionnelle pour calcaire dur ; local non chauffé fermé et "
         "surmonté d'un grenier ; estimation justifiée au § 3.1 et recoupée avec "
         "les factures"],
        ["Apports gratuits",
         "Apports internes 4,2 W/m² ; apports solaires 2 200 kWh/an avant et "
         "1 600 après ; facteur d'utilisation 0,88 avant et 0,70 après",
         "Valeur conventionnelle pour 4 personnes ; 12,33 m² de vitrage au "
         "sud-est avec masque pris à 0,8"],
        ["Systèmes",
         "Rendement de l'installation propane 0,65 avant et 0,79 après "
         "optimisation ; poêle 0,55 puis 0,78 ; SCOP de la pompe à chaleur 3,5 "
         "en régime 45/35 ; COP du chauffe-eau thermodynamique 2,8",
         "Produit des rendements de génération, distribution, émission et "
         "régulation (§ 5.3) ; valeurs prudentes en climat H1c, sensibilité du "
         "SCOP testée à 3,0"],
        ["Émetteurs",
         "0,145 kW par élément de fonte 4 colonnes H 930 à Δθ = 50 K ; exposant "
         "de la loi d'émission n = 1,3",
         "Documentation technique des fabricants ; valeur normalisée pour la "
         "fonte"],
        ["Économie",
         "TVA 5,5 % ; analyse en coût global sur 20 ans ; éco-prêt à taux zéro "
         "sur 20 ans",
         "Travaux de performance énergétique et travaux induits ; durée demandée "
         "par la trame ; durée maximale pour une rénovation globale"],
    ], largeurs=[0.14, 0.45, 0.41], size=8,
        titre="Récapitulatif des hypothèses de calcul")

    R.para(
        "Deux limites doivent être signalées. La géométrie de l'enveloppe a été "
        "reconstituée à partir des cotes portées sur les plans fournis ; un "
        "relevé sur site pourrait faire varier les surfaces de quelques "
        "pourcents, sans incidence sur les conclusions. Par ailleurs, aucun test "
        "d'infiltrométrie n'a été réalisé : la perméabilité retenue est une "
        "estimation, justifiée et recoupée avec les factures, mais qu'un test "
        "avant travaux devra confirmer.")

    # ---------------------------------------------------------------- 8.11
    R.titre2("Sources, outils et références")
    R.tableau([
        ["Nature", "Source ou référence", "Usage dans l'étude"],
        ["Données du projet",
         "Sujet 2026-C version 1.1, récapitulatif des échanges avec le maître "
         "d'ouvrage et trame de rapport du Bloc 1 — ASDER",
         "Plans cotés, photographies, description de l'enveloppe et des "
         "systèmes, consommations relevées, profil et priorités du maître "
         "d'ouvrage, structure du rapport et éléments attendus"],
        ["Méthodes de calcul",
         "Méthode 3CL-DPE et arrêtés relatifs au diagnostic de performance "
         "énergétique ; norme NF EN 12831",
         "Coefficients d'énergie primaire, facteurs d'émission, seuils des "
         "classes ; puissance de chauffage à la température de base"],
        ["Réglementation thermique et ventilation",
         "Arrêté du 3 mai 2007 modifié, dit « élément par élément » ; arrêté du "
         "24 mars 1982 modifié",
         "Exigences minimales de résistance thermique et de Uw ; débits "
         "réglementaires d'extraction et d'entrée d'air pour un T4"],
        ["Rénovation performante et urbanisme",
         "Article L.111-1, 17° bis du code de la construction et de "
         "l'habitation ; articles R.421-17 et L.113-5-1 du code de l'urbanisme",
         "Six postes à traiter et dérogation pour coût manifestement "
         "disproportionné ; déclaration préalable et dépassement autorisé pour "
         "l'isolation par l'extérieur"],
        ["Aides et fiscalité",
         "France Rénov' et Agence nationale de l'habitat ; dispositif des "
         "certificats d'économies d'énergie ; article 1383-0 B du code général "
         "des impôts ; espace conseil France Rénov' de Savoie (ASDER)",
         "Plafonds de travaux, taux, conditions d'éligibilité, forfaits par "
         "geste, aides locales et exonération de taxe foncière"],
        ["Données environnementales et sanitaires",
         "ADEME — bases de données environnementales et FDES des fabricants ; "
         "Observatoire national de la précarité énergétique ; carte du potentiel "
         "radon de l'IRSN",
         "Énergie grise, bilan carbone et perméance des isolants ; seuil de 8 % "
         "du taux d'effort ; exposition au radon"],
        ["Données produits et règles de l'art",
         "Documentations techniques des fabricants ; DTU 45.4, 36.5, 68.3, 24.1 "
         "et 65.16",
         "Caractéristiques thermiques, performances normalisées, prix de "
         "marché ; prescriptions de mise en œuvre à intégrer aux devis"],
        ["Données climatiques et cartographiques",
         "Météo-France, station de Chambéry-Aix ; zonage climatique "
         "réglementaire ; IGN — BD ORTHO",
         "Degrés-jours sur cinq saisons, température extérieure de base, "
         "analyse bioclimatique et masque solaire"],
    ], largeurs=[0.20, 0.38, 0.42], size=8,
        titre="Sources, normes et outils mobilisés")

    R.espace(10)
    R.para("Fin du rapport.", size=9.5, couleur=GRIS, italique=True,
           align="center")


# ==========================================================================
#  ASSEMBLAGE
# ==========================================================================
def main():
    R.entete_pied()
    page_de_garde()
    sommaire()
    resume()
    chapitre_1()
    chapitre_2()
    chapitre_3()
    chapitre_4()
    chapitre_5()
    chapitre_6()
    chapitre_7()
    chapitre_8()
    R.remplir_toc()
    chemin = R.enregistrer(SORTIE)
    print("Rapport généré :", chemin)
    print("Figures :", R._nfig, "| Tableaux :", R._ntab)


if __name__ == "__main__":
    main()
