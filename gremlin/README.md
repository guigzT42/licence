# Projet GREMLIN — sources des livrables

Reconstruction du dossier de conduite de projet et du diaporama de soutenance
à partir du sujet (Cas n° 1 — essai en soufflerie, phase de préparation de la maquette).

## Livrables (à la racine du dépôt)
- `Projet_GREMLIN_Dossier.docx` — dossier complet (sommaire auto, 7 parties + annexe).
- `Projet_GREMLIN_Presentation.pptx` — diaporama de soutenance (12 diapositives).

## Régénérer
```bash
python3 gremlin/gen_risques.py      # matrice des risques
python3 gremlin/build_dossier.py    # -> Projet_GREMLIN_Dossier.docx
python3 gremlin/build_pptx.py       # -> Projet_GREMLIN_Presentation.pptx
```
Dépendances : `python-docx`, `python-pptx`, `matplotlib`, `Pillow`.

## Note sommaire
Le sommaire du Word est un champ qui se met à jour à l'ouverture dans Word.
Pour le rafraîchir manuellement : clic droit sur le sommaire > « Mettre à jour les champs » (F9).
