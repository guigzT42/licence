## 3.8 Planification et phasage du chantier

### 3.8.1 Les données de cadrage

| Paramètre | Valeur |
|---|---|
| **Période de réalisation** | **de mi-avril à mi-juin 2026** |
| Durée du chantier | **2 mois** |
| Régime horaire | **Travail de nuit**, entre la fermeture (**19 h 45**) et la réouverture (**4 h 45**) |
| Effectif | **2 compagnons** |
| Part des travaux en nacelle | **≈ 70 %** |
| Contrainte absolue | Magasin **exploitable, propre et sécurisé à 4 h 45 chaque matin** |
| Ouvrage à réaliser | 2 groupes VRV IV en cour arrière, 1 gainable + 4 cassettes, **59 ml de gaine perforée Ø 550**, liaisons frigorifiques 2 tubes, 65 m de condensats, électricité et régulation |
| Coût chiffré de la contrainte horaire | **9 715,85 € HT** (poste A.9 du devis) |
| Volume d'heures **prévu** | 2 personnes × durée des postes sur 2 mois |
| Volume d'heures **réalisé** | **environ le double du prévisionnel** (voir l'analyse de l'aléa en 3.9.2) |

**Le choix de la période n'est pas anodin.** Réaliser les travaux **de mi-avril à mi-juin** signifie intervenir **en sortie de saison de chauffe** : la chaudière de 1987 pouvait être déposée sans risque de laisser le magasin sans chauffage, et la nouvelle installation disposait de plusieurs semaines pour être mise au point **avant les premières chaleurs de l'été**, qui constituaient précisément l'un des objectifs du projet. C'est une décision de planification simple, mais qui supprime à elle seule le risque le plus lourd de l'opération.

### 3.8.2 Le phasage retenu

Le chantier a été découpé en phases, dans un ordre dicté par deux logiques : **d'abord ce qui est structurant et irréversible**, ensuite ce qui est ajustable ; et **d'abord les zones les moins gênantes** pour l'exploitation, en terminant par les zones sensibles (entrée, caisses, rayon frais).

| Phase | Contenu | Durée indicative | Points de vigilance |
|---|---|---|---|
| **P0 — Préparation** (avant chantier) | Études d'exécution, plans d'implantation, commandes matériel, réservation nacelle et grue, plan de prévention, inspection commune, permis de feu, autorisations de conduite | 〈à compléter〉 | Délais fournisseurs : c'est le chemin critique |
| **P1 — Installation de chantier** | Accès, zone de stockage, balisage, protections, repérage des réseaux existants, point zéro avec l'exploitant | 1 à 2 nuits | Zone de stockage sans gêne pour l'exploitation |
| **P2 — Mise en place des groupes extérieurs** | Manutention des RXYQ20U et RXYQ16U en **cour arrière sur dalle béton**, supports Grand Rubber Foot, plots antivibratiles, sectionneurs de proximité | 〈à compléter〉 | Masse des groupes, cheminement dégagé et éclairé, nuisances sonores nocturnes |
| **P3 — Supportage et pose des unités intérieures** | Fixation sur rails type Mupro en raccord avec la structure, pose du **gainable FXMQ-250A** et des **4 cassettes Roundflow 125** | 〈à compléter〉 | Travail en nacelle, charges suspendues, coactivité |
| **P4 — Réseau frigorifique** | Chemins de câbles galvanisés, cuivre frigo 2 tubes isolé, **raccords Refnet**, brasage sous azote, capotage des parties extérieures | 〈à compléter〉 | Permis de feu, propreté du circuit, longueurs constructeur, passage dans les locaux existants |
| **P5 — Réseau aéraulique** | Plénum isolé 25 mm et **59 ml de gaine acier perforée diffusante Ø 550** sur toute la longueur du magasin, supportages | 〈à compléter〉 | **Phase la plus longue en nacelle**, alignement et rectitude de la gaine, désenfumage non entravé |
| **P6 — Évacuation des condensats** | 65 m de PVC M1 DN 40, 5 siphons à culot démontable, raccordements sur réseaux EU, essais à l'eau | 〈à compléter〉 | Essais impératifs : réseau situé au-dessus des rayons |
| **P7 — Électricité et régulation** | Coffret CVC, câblage puissance et bus LIYCY, sondes déportées, 5 télécommandes MADOKA, kit été/hiver, **liaisons Modbus/BACnet vers la future GTB** | 〈à compléter〉 | Consignations, coordination avec le magasin |
| **P8 — Essais et mise en service** | Tirage au vide, contrôle d'étanchéité, **charge R-410A**, **mise en service constructeur DAIKIN**, dossier **DESP**, équilibrage, paramétrage des consignes 19 °C / 26 °C | 〈à compléter〉 | Traçabilité fluides, mesures de réception |
| **P9 — Dépose de l'ancien système, réception et repli** | **Dépose des aérothermes et de la chaudière gaz de 452 kW** une fois la PAC en service, levée des réserves, nettoyage final, formation du client, remise du DOE | 〈à compléter〉 | Ne jamais déposer avant mise en service de la nouvelle production ; vérifier l'absence d'amiante avant dépose |

### 3.8.3 Représentation du planning

```
Semaine       1    2    3    4    5    6    7    8
P0 Prépa   ████ (avant démarrage)
P1 Install ██
P2 Groupes   ████
P3 UI          ██████
P4 Frigo         ████████
P5 Gaines          ██████████████
P6 Condens               ████
P7 Élec/Rég                ██████
P8 MES                        ██████
P9 Récep                          ████
```
*Trame indicative à ajuster avec le planning réel du chantier.*

### 3.8.4 Le rituel de nuit — l'organisation réellement appliquée

C'est ce qui a permis de tenir l'objectif « zéro heure de fermeture ». Chaque poste de nuit suivait la même séquence :

| Moment | Action |
|---|---|
| **Arrivée (fermeture du magasin)** | Point avec le responsable présent, vérification des consignes, relevé des éventuelles anomalies signalées la veille |
| **Avant démarrage** | Analyse de risques du jour (« minute sécurité »), vérification de la nacelle, mise en place du balisage et des protections des rayons |
| **Début de poste** | Tâches à risque et tâches bruyantes : levage, carottage, brasage — vigilance maximale |
| **Milieu de poste** | Pose et raccordements, avancement du linéaire de gaines |
| **Fin de poste (− 1 h)** | Arrêt des travaux à risque, surveillance post-brasage, contrôle des points chauds |
| **Fin de poste (− 30 min)** | Repli du matériel, retrait des protections, **nettoyage de la zone**, remise en service de la détection incendie, contrôle visuel de la surface de vente |
| **Départ** | Compte rendu écrit / photo, information de l'exploitant, verrouillage selon la procédure du site |

Cette discipline de fin de poste — **une demi-heure « perdue » chaque nuit** — a été le meilleur investissement du chantier : elle a supprimé toute réclamation du client sur l'état du magasin à l'ouverture.

### 3.8.5 La méthodologie de gestion de projet appliquée

| Outil / méthode | Usage sur le projet |
|---|---|
| **Note de cadrage et objectifs SMART** | Formalisation des objectifs avec le client (3.1.5) |
| **Analyse des parties prenantes** | Attentes et contraintes de chacun (3.1.6) |
| **Découpage en phases (WBS) et planning de type Gantt** | Structuration en 10 phases, séquencement, chemin critique (3.8.2 et 3.8.3) |
| **Analyse de risques projet** | Registre des risques avec criticité et mesures (3.9.1) |
| **Points d'avancement et comptes rendus** | Hebdomadaire avec le responsable d'affaires et le client, quotidien avec l'exploitant |
| **Revue de réception** | Liste de réserves, procès-verbal, levée des réserves |
| **Retour d'expérience** | Analyse finale et capitalisation (3.11 et partie 4) |

## 3.9 Conduite du projet, aléas et adaptations

### 3.9.1 Le registre des risques projet

| Risque | Probabilité | Impact | Mesure préventive | Mesure corrective prévue |
|---|---|---|---|---|
| Retard de livraison du matériel VRV | Moyenne | Fort (décalage de tout le chantier) | Commande anticipée dès la signature, confirmation des délais | Réordonnancement des phases : avancer les gaines avant les unités |
| Indisponibilité de la nacelle | Faible | Fort (70 % des travaux) | Location ferme sur toute la durée, contrat avec dépannage sous 24 h | Nacelle de substitution du loueur |
| Découverte d'amiante lors des percements ou de la dépose de la chaufferie de 1987 | **Moyenne** | Très fort (arrêt du chantier) | Consultation du DTA, **repérage avant travaux obligatoire** | Arrêt immédiat, prélèvement, entreprise spécialisée |
| Panne de la chaudière de 1987 avant la mise en service de la PAC | Moyenne | Fort (magasin non chauffé) | Maintien de la chaufferie en service jusqu'à la mise en service de la PAC, pièces de dépannage identifiées | Chauffage d'appoint temporaire, accélération du phasage |
| Réseaux existants non repérés en plénum | Moyenne | Moyen | Relevés préalables, sondages | Adaptation du tracé |
| Panne d'un équipement du magasin pendant nos travaux | Moyenne | Moyen (suspicion réciproque) | Point zéro contradictoire en début de chantier, traçabilité des consignations | Diagnostic immédiat, transparence |
| Nuisances sonores nocturnes en cour arrière (riverains) | Moyenne | Moyen | Manutention et essais bruyants en début de nuit, information préalable | Décalage des tâches bruyantes, adaptation des horaires |
| Fatigue de l'équipe | Moyenne | Fort | Respect des durées et des repos, rotation des tâches | Renfort ponctuel, allègement du poste |
| Gêne perçue par les clients du magasin | Faible | Moyen | Nettoyage quotidien, repli complet | Réaction immédiate à toute remarque |
| Dépassement budgétaire | Moyenne | Moyen | Suivi des heures et des achats, provision pour aléas | Avenant justifié, arbitrage avec le RA |

### 3.9.2 L'aléa majeur : un temps de travail de nuit multiplié par deux

**Le fait.** Le chantier a demandé **environ deux fois plus d'heures de nuit que ce qui avait été prévu au chiffrage**. La période calendaire a été tenue — les travaux se sont bien déroulés de mi-avril à mi-juin 2026 — mais la **charge horaire réelle a doublé** par rapport au prévisionnel.

**Pourquoi c'est l'aléa le plus intéressant du projet.** Ce n'est pas un incident technique : c'est un **écart de productivité structurel**, c'est-à-dire exactement le type d'erreur qui ne se voit pas sur un plan et qui se paie en fin d'affaire.

**Les facteurs qui expliquent cet écart :**

| Facteur | Effet sur la productivité |
|---|---|
| **Fenêtre utile réduite** | Entre la fermeture (19 h 45) et la réouverture (4 h 45), il reste 8 heures, dont il faut retirer l'installation du chantier en début de poste et **le repli et le nettoyage complets en fin de poste**. Le temps réellement productif est nettement inférieur à la durée de présence |
| **Remise en état quotidienne** | Chaque nuit, tout est monté puis redescendu : balisage, protections des rayons, nacelle, outillage. Sur un chantier de jour, on laisse en place |
| **Travail en nacelle** | 70 % des tâches : chaque déplacement de la nacelle, chaque changement de zone impose une réinstallation, un contrôle de sol, un rebalisage |
| **Linéaire et précision de la gaine** | 59 mètres de gaine perforée Ø 550 à aligner en hauteur, avec supportage et rectitude visibles depuis la surface de vente |
| **Passage des liaisons dans les locaux existants** | Contrainte identifiée dès l'audit : les cheminements depuis la cour arrière traversent des locaux occupés, ce qui impose des reprises de tracé |
| **Baisse de vigilance nocturne** | La nuit, on travaille plus lentement, et c'est souhaitable : la sécurité prime sur la cadence |
| **Fatigue cumulée** | Sur deux mois de nuit à deux, le rythme se dégrade mécaniquement en fin de chantier |

**Les conséquences.**

1. **Économiques.** Le devis prévoyait **9 715,85 € HT** de « prestation en horaire décalé », soit 10,5 % du montant. Un doublement des heures de nuit dégrade directement la marge de l'affaire — et dans un chantier où la main-d'œuvre est le premier poste réel, l'impact est significatif.
2. **Humaines.** Deux compagnons sur deux mois de nuit, sans marge d'effectif : le doublement de la charge s'est traduit par de la fatigue, avec le risque de sécurité que cela implique.
3. **Contractuelles.** L'objectif « zéro heure de fermeture du magasin » a néanmoins été tenu : **c'est l'entreprise qui a absorbé l'écart, pas le client**.

**Les adaptations mises en œuvre** : priorisation des tâches à risque et bruyantes en début de poste, préfabrication au sol de ce qui pouvait l'être pour réduire le temps en nacelle, regroupement des tâches par zone pour limiter les repositionnements, et maintien intégral du rituel de repli — la seule chose sur laquelle il ne fallait surtout pas rogner.

**Ce que j'en retiens, et c'est l'enseignement principal du projet :** un chantier de nuit en site occupé ne se chiffre pas avec les ratios d'un chantier de jour. Il faut appliquer un **coefficient de productivité** au temps de pose, et **budgéter explicitement le temps improductif quotidien** — installation, repli, nettoyage — qui, sur une fenêtre de huit heures, peut représenter une à deux heures par nuit, soit 15 à 25 % du poste. Sur un prochain chiffrage, je proposerai de distinguer au devis le **temps de production** du **temps de mise en place et de repli**, afin que la contrainte soit visible et discutable avec le client plutôt que subie par l'entreprise.

> 〈**À préciser si tu disposes des éléments** : le nombre de nuits réellement effectuées et la répartition des heures par phase. Cela permettrait de chiffrer l'écart en euros et de le présenter comme un retour d'expérience exploitable par l'entreprise pour ses prochains chiffrages de nuit.〉

### 3.9.3 La coordination des acteurs

Les échanges ont été organisés selon une cadence adaptée à chaque interlocuteur : **quotidienne** avec le directeur du magasin (point en début et en fin de poste, plus un point hebdomadaire formel) et avec le responsable chantier ; **hebdomadaire** avec le responsable d'affaires, complétée d'un appel à chaque aléa significatif ; **ponctuelle** avec le fournisseur et le constructeur (commande, livraisons, mise en service), le loueur de nacelle (livraison, pannes), les éventuels sous-traitants (étanchéité, levage) et le service QSE (préparation, événement de sécurité).

## 3.10 Réception, mise en service et suite donnée au projet

### 3.10.1 Les opérations de réception et les livrables

| Opération | Contenu | Document produit |
|---|---|---|
| Contrôle d'étanchéité et tirage au vide | Mise sous pression azote, maintien, déshydratation du circuit | Fiche d'intervention fluides |
| Charge en fluide | **Charge R-410A** calculée selon la longueur des liaisons, pesée | Fiche fluides + registre |
| **Mise en service constructeur DAIKIN** | Contrôle des paramètres, activation de la garantie, **dossier DESP** | PV de mise en service |
| Équilibrage et mesures | Débits, températures de soufflage et de reprise, intensités, pressions | Tableau de mesures |
| Essais de régulation | Programmation horaire, consignes **19 °C / 26 °C**, essais des 5 télécommandes MADOKA | Fiche de paramétrage |
| Essais des condensats | Mise en eau du réseau DN 40, contrôle des siphons | PV d'essai |
| Contrôle de sécurité incendie | Traversées rebouchées, désenfumage non entravé, registre de sécurité à jour | Attestation |
| Réception avec le client | Visite contradictoire, liste de réserves puis levée | **PV de réception** |

**Livrables remis au client** : le **Dossier des Ouvrages Exécutés** (plans de récolement, schémas, fiches techniques, notices, PV d'essais, dossier DESP) ; une **notice d'utilisation simplifiée** de la régulation rédigée pour un utilisateur non technicien ; la **formation du personnel** du magasin (télécommandes, consignes réglementaires 19 °C / 26 °C, fermeture des portes, conduite à tenir en cas de défaut) ; les **fiches de traçabilité des fluides frigorigènes** ; une **proposition de contrat de maintenance préventive** intégrant les contrôles d'étanchéité réglementaires ; et les **éléments justificatifs pour la déclaration OPERAT** et pour le dossier **CEE** auprès de TotalEnergies / GreenFlex.

### 3.10.3 Les perspectives : ce que ce projet ouvre

Le projet VRV traite le poste chauffage-climatisation. Il ne règle pas à lui seul la trajectoire décret tertiaire du magasin. J'ai donc présenté au client une **feuille de route d'actions complémentaires**, hiérarchisée par rapport gain/coût :

| Priorité | Action | Gain attendu | Investissement | Statut |
|---|---|---|---|---|
| 1 | **Récupération de chaleur sur les groupes froids** (ballon échangeur 3 000 L) | 6 400 €/an — **TRA 4,3 ans** | 34 200 € HT | Retenue au bouquet |
| 2 | **GTC classe A/C** (surface de vente et bureaux) | 5 400 €/an — **TRA 5,3 ans** ; conformité **décret BACS** | 39 000 € HT | Retenue — **liaisons déjà posées** |
| 3 | **Ballons thermodynamiques pour les labos** (2 × 200 L) | 1 410 €/an — **TRA 6,3 ans** | 8 840 € HT | Retenue au bouquet |
| 4 | **Ombrières photovoltaïques** (271,9 kWc sur le parking) | 43 830 €/an — **TRA 8,4 ans** ; > 90 % d'autoconsommation | 368 000 € HT | Retenue — répond aussi à la **loi APER (2028)** |
| 5 | **Bornes de recharge** (loi LOM) et **gestion de l'éclairage** (27 % des consommations, aujourd'hui en commande manuelle) | Conformité et gisement important | Modéré | À proposer — compétences internes Santerne |
| 6 | **Fermeture des meubles frigorifiques** (froid = 37 %, et 58 % après travaux) | Premier gisement restant | Élevé | À proposer |
| 7 | **Suivi des consommations et déclaration OPERAT** | Pilotage de la trajectoire réglementaire | Faible | À contractualiser |

Cette feuille de route transforme une opération ponctuelle en **démarche de progrès continu** — et, du point de vue de l'entreprise, en relation commerciale durable.

## 3.11 Résultats, indicateurs d'impact et évaluation finale du projet

### 3.11.1 L'évaluation des objectifs

| Obj. | Objectif | Cible | Résultat | Atteint ? |
|---|---|---|---|---|
| O1 | Substitution du chauffage gaz par une PAC réversible | PAC couvrant la surface de vente | **70,4 kW chaud / 89,5 kW froid installés**, chaudière de 452 kW déposée | ✔ |
| O2 | Contribution au décret tertiaire | Trajectoire vers 221,5 kWh/m² | Gain estimé par l'audit : **16,7 t CO₂e/an** et contribution au bouquet menant à 211,2 kWh/m² | ✔ (à confirmer par OPERAT) |
| O3 | Confort d'été sur toute la surface de vente | ≤ 26 °C | Ligne de caisses et fond de magasin traités par gaine diffusante, reste par cassettes | ✔ (à mesurer sur un été complet) |
| O4 | Confort d'hiver | 19 °C | Consignes paramétrées à la mise en service | ✔ |
| O5 | Aucune fermeture du magasin | 0 h | **0 h** | ✔ |
| O6 | Aucun accident | 0 | 〈à confirmer〉 | 〈〉 |
| O7 | Délai de 2 mois | 2 mois | 〈à confirmer〉 | 〈〉 |
| O8 | Réduction des émissions | — | **16 679 kgCO₂e/an** estimés (audit) | ✔ (estimation) |
| O9 | Anticipation du décret BACS | Liaisons GTB | **Liaisons Modbus/BACnet posées** (poste A.8) | ✔ |

### 3.11.2 Les indicateurs d'impact pour la transition énergétique

Ce sont les indicateurs explicitement attendus par le référentiel du bloc 4. Je propose de les structurer ainsi :

**a) Indicateurs énergétiques**

| Indicateur | Unité | Avant | Après | Méthode de mesure |
|---|---|---|---|---|
| Consommation totale du site | kWh<sub>ef</sub>/an | **1 219 000** | 〈à mesurer〉 — objectif bouquet : 779 000 | Factures, OPERAT |
| Ratio surfacique | kWh<sub>ef</sub>/m²/an | **330,6** | 〈à mesurer〉 — objectif bouquet : 211,2 | Calcul sur 3 690 m² |
| Objectif 2030 (décret tertiaire) | kWh<sub>ef</sub>/m²/an | — | **221,5** | OPERAT / audit |
| Consommation de gaz du poste chauffage | kWh<sub>ef</sub>/an | Chauffage = **13 %** du total | Supprimée sur la surface de vente | Factures GRDF |
| Consommation électrique supplémentaire liée à la climatisation | MWh/an | — | **+ 102 (+ 9 %)** estimés par l'audit | Modèle IPMVP |
| Efficacité saisonnière réelle constatée | SCOP estimé | — | 〈à relever〉 (annoncé ETAS chaud 162,4 %) | Relevés d'exploitation |

**b) Indicateurs environnementaux et économiques**

| Indicateur | Unité | Valeur |
|---|---|---|
| Émissions évitées par l'action PAC | kgCO₂e/an | **16 679** (équivalent 76 650 km en citadine essence) |
| Émissions évitées par le bouquet complet | kgCO₂e/an | **64 830**, soit **− 70 %** |
| Émissions évitées cumulées sur 15 ans (action PAC) | t CO₂e | ≈ **250** |
| **Impact potentiel du fluide frigorigène** (38 kg de R-410A × GWP 2 088) | t CO₂e | **79,3** — soit l'équivalent de **4,8 années** du gain annuel de l'installation |
| Économie annuelle estimée sur la facture d'énergie | €/an | **5 260** (action seule) — **58 590** (bouquet) |
| Investissement net après CEE / temps de retour | € / ans | **79 000 € HT** / ≈ **15 ans** (action seule) — 9,3 ans (bouquet) |

**c) Indicateurs de conduite de projet**

| Indicateur | Valeur |
|---|---|
| Respect du délai calendaire | **Tenu** (mi-avril → mi-juin 2026) |
| Respect du volume d'heures prévu | **Non : environ × 2** — principal enseignement du projet |
| Respect du budget | Devis à **90 000 € HT**, soit **− 27 %** par rapport au budget de l'audit (122 800 €) |
| Nombre d'accidents / presqu'accidents | 〈〉 |
| Heures de fermeture du magasin imputables au chantier | **0** |
| Nombre de réserves à la réception / délai de levée | 〈à compléter〉 |
| Satisfaction client | 〈à recueillir formellement — proposition : courte enquête écrite auprès du directeur〉 |

### 3.11.3 Méthode de vérification des gains : une précaution indispensable

Comparer brutalement la facture de l'année N-1 à celle de l'année N serait méthodologiquement faux : les hivers ne se ressemblent pas, les prix de l'énergie varient, l'activité du magasin évolue. Pour une évaluation honnête, je propose :

1. **La correction climatique** des consommations par les **degrés-jours unifiés (DJU)** de la station météorologique de référence, afin de comparer des hivers comparables ;
2. **Le raisonnement en énergie (kWh) avant de raisonner en euros**, pour neutraliser l'effet prix ;
3. **L'isolement du poste CVC** par sous-comptage ou, à défaut, par analyse du talon et de la courbe de charge ;
4. **La comparaison sur une année pleine** minimum, deux de préférence ;
5. **La déclaration OPERAT**, qui constitue la preuve officielle de la trajectoire.

> **⚠ Pièce restant à obtenir** : les **relevés de consommation après travaux** sur une période représentative (une saison de chauffe complète au minimum). C'est l'élément qui transformera l'estimation de l'audit en **résultat démontré**. La plateforme **ENERGISME**, déjà utilisée pour l'audit, et la déclaration **OPERAT** du site constituent les deux sources à exploiter.
