PAGEBREAK

# Partie 4 — Analyse personnelle et prise de recul

Cette partie répond aux critères d'évaluation portant sur l'analyse critique, l'organisation de l'équipe et les axes d'amélioration. Elle est volontairement écrite à la première personne et sans complaisance : un projet dont on ne sait dire que du bien est un projet dont on n'a rien appris.

## 4.1 Ce que le projet a réussi

**1. La démarche a été menée dans le bon ordre.** Le projet n'est pas parti d'une envie de vendre une machine, mais d'un **audit énergétique** conduit selon la méthodologie IPMVP, à partir des consommations réelles ENEDIS/GRDF. Cette séquence — constat terrain → audit objectivé → hiérarchisation des gisements → solution → argumentaire → décision — est celle que la licence CPEBD cherche à faire acquérir. Elle donne une légitimité au discours : on ne propose pas un équipement, on répond à un problème mesuré et à des obligations datées.

**2. Le maillage VINCI Energies a changé la nature de la relation client.** Sans l'ingénieur énergéticien du groupe, l'entreprise aurait au mieux proposé un remplacement de chaudière. L'audit a produit autre chose : un **état réglementaire complet du site** (décret tertiaire, BACS, APER, LOM), une répartition des consommations par usage, et un **bouquet cohérent de cinq actions** à 9,3 ans de retour. Le client n'a plus comparé un prix à un autre prix : il a comparé un scénario d'action à un scénario d'inaction.

**3. Le séquencement a été intelligent.** L'audit recommandait explicitement de **ne pas installer la GTB avant d'avoir changé la production de chauffage**. Cette recommandation a été suivie, tout en posant dès maintenant les **liaisons Modbus/BACnet** : la GTC future se raccordera sans reprise de câblage. C'est de la conception qui pense à deux coups d'avance, et cela ne coûtait que 531,70 € au devis.

**4. Le dimensionnement a été repris à la source.** Remplacer à l'identique aurait conduit à réinstaller **452 kW** là où **70,4 kW** suffisent. Le projet a divisé la puissance installée par **6,4**, avec les économies d'investissement et de rendement en charge partielle que cela implique.

**5. La sécurité a été traitée en amont.** Deux mois de travail de nuit, dans une fenêtre de huit heures entre 19 h 45 et 4 h 45, en hauteur, dans un ERP, sans fermeture du magasin et sans accident : ce résultat tient à l'inspection commune préalable, au plan de prévention, au maintien systématique du binôme et à la discipline de fin de poste.

**6. L'objectif « zéro heure de fermeture » a été tenu**, et il était la condition d'acceptation du projet par le client.

## 4.2 Ce qui aurait pu être mieux fait — analyse critique

**1. Le fluide frigorigène est la vraie faiblesse du projet, et elle est chiffrable.** L'installation contient **38 kg de R-410A (GWP 2 088)**, soit un **potentiel de 79,3 t CO₂e**. Or le gain annuel du projet est de **16,7 t CO₂e/an** : la charge embarquée représente donc **4,8 années de bénéfice climatique**. Une fuite de 20 % du circuit annulerait à elle seule près d'une année entière de gain. La même installation au **R-32 (GWP 675)** n'aurait représenté que **25,7 t CO₂e**, et serait surtout **restée sous le seuil des 50 t CO₂e** : le contrôle d'étanchéité aurait été **annuel au lieu d'être semestriel**, avec l'économie d'exploitation correspondante sur quinze à vingt ans.
> Dans un projet dont la finalité affichée est la réduction des émissions, c'est une contradiction qu'il faut assumer : le choix relève de la gamme VRV IV retenue et de la continuité avec le parc existant du site. Le règlement **(UE) 2024/573** organisant la raréfaction des HFC à fort GWP, **le prix et la disponibilité du fluide pour les recharges se dégraderont** sur la durée de vie de l'installation. Si le projet était refait aujourd'hui, je défendrais une **gamme au R-32** ; à défaut, la qualité d'étanchéité et la rigueur des contrôles semestriels deviennent une **condition de la performance annoncée** — et c'est désormais ma responsabilité de mainteneur.

**2. L'action isolée a un temps de retour long, et il ne faut pas le masquer.** **15 ans après CEE** pour la PAC seule, contre 4,3 ans pour la récupération de chaleur sur les groupes froids. La raison est structurelle : on remplace une énergie bon marché (le gaz) par une énergie chère (l'électricité), et on **ajoute** un usage — la climatisation, soit + 102 MWh et + 9 % d'électricité. Le projet se justifie par la vétusté de la chaudière, le confort et la contrainte réglementaire, pas par sa seule rentabilité énergétique. Le dire est plus solide que de le dissimuler.

**3. L'ordre des actions du bouquet aurait pu être discuté.** Économiquement, la **récupération de chaleur sur les groupes froids (4,3 ans)** et la **GTC (5,3 ans)** étaient plus rentables. On peut défendre l'ordre retenu — la chaudière de 1987 imposait le calendrier, et la récupération de chaleur perd son intérêt si elle alimente un réseau hydraulique voué à disparaître — mais l'arbitrage méritait d'être formalisé et présenté au client sous cette forme.

**4. Les mesures avant travaux ont été insuffisantes.** Aucun **sous-comptage dédié du poste chauffage** n'a été installé avant le démarrage. La répartition par usage provient d'un modèle IPMVP avec des clés sectorielles, pas d'une mesure. Résultat : le gain réel sera difficile à démontrer autrement que par la facture globale, sur laquelle pèsent le froid, l'éclairage et l'activité du magasin. **Sur un prochain projet, j'installerai un comptage dédié pendant la saison de chauffe précédant les travaux.**

**5. L'écart entre le budget de l'audit et le devis réel (− 27 %) n'a pas été exploité.** Passer de 122 800 € à 90 000 € améliore le temps de retour de 21,5 à 15 ans après CEE. Ce recalcul aurait dû être présenté formellement au client : c'était un argument commercial gratuit, et il n'a pas été fait.

**6. Le chiffrage du travail de nuit a été sous-évalué d'un facteur deux.** C'est l'erreur la plus coûteuse du projet, analysée en détail en 3.9.2 : le temps de nuit réellement consommé a été **environ le double du prévisionnel**, absorbé par l'entreprise et non par le client. La cause n'est pas un incident mais une **méthode de chiffrage inadaptée** : on a estimé des temps de pose de chantier de jour sur un chantier de nuit, sans budgéter le temps improductif quotidien d'installation et de repli, ni appliquer de coefficient de productivité nocturne. La correction est simple et je la porterai sur mes prochains devis : **distinguer au chiffrage le temps de production du temps de mise en place et de repli**, et appliquer un coefficient explicite au travail en nacelle en site occupé.

**7. La formalisation du projet a été plus faible que sa réalisation.** Le chantier a été bien conduit, mais la traçabilité écrite — planning formalisé, registre des risques tenu à jour, comptes rendus structurés — a souvent cédé le pas à l'urgence du terrain. La préparation de ce rapport m'a fait mesurer l'écart entre « avoir fait » et « pouvoir démontrer qu'on a fait ».

**8. La mesure de la satisfaction client n'a pas été formalisée.** Le retour est bon, mais oral. Une enquête écrite en fin d'opération aurait produit un élément valorisable commercialement et un retour d'expérience exploitable.

## 4.3 L'organisation de l'équipe : forces, faiblesses et axes d'amélioration

Le référentiel attend une analyse de l'organisation de l'équipe projet, de son suivi, et de la prise en compte des spécificités de chacun.

### 4.3.1 La répartition des rôles

| Acteur | Rôle dans le projet | Part de l'avancement |
|---|---|---|
| Responsable d'affaires (J.-M. BERJAUD) | Cadrage commercial, chiffrage final, relation contractuelle, arbitrages | Décision |
| **Moi (chargé de maintenance)** | **Participation à l'audit** (visite, relevé de l'existant, historique d'exploitation, échanges sur les scénarios CVC), **réalisation d'une partie du chantier** de nuit, puis reprise de l'installation en maintenance | Contribution technique et exécution |
| Responsable chantier | Organisation, moyens, sécurité, encadrement | Encadrement |
| Binôme de nuit (2 compagnons) | Réalisation | Exécution |
| Ingénieur énergéticien VINCI Energies | Audit énergétique complet : modélisation IPMVP, assujettissements réglementaires, chiffrage des neuf actions, bouquet de travaux | Expertise |
| Fonctions support (achats, QSE, logistique) | Approvisionnement, prévention, moyens | Appui |

### 4.3.2 Les points forts de l'organisation

- **Une chaîne de décision très courte** : trois niveaux entre le compagnon et le décideur, ce qui permet de trancher un aléa en une nuit.
- **La polyvalence du binôme** : frigorifique, aéraulique, électricité, mise en service — indispensable quand on est deux.
- **La continuité entre travaux et maintenance** : l'installation a été conçue et posée par celui qui la maintient, ce qui a orienté des choix concrets (accessibilité des filtres, position des vannes et des trappes de visite, repérage).
- **La disponibilité de l'encadrement**, y compris sur des horaires décalés.

### 4.3.3 Les points faibles

- **La vulnérabilité d'un effectif de deux** : une absence, et le planning est compromis.
- **La transmission d'informations entre la nuit et le jour** : les comptes rendus circulent mal quand les horaires ne se recouvrent pas, et les décisions se prenaient parfois avec 24 heures de décalage. L'équipe de nuit est aussi plus isolée : moins de visites de l'encadrement, moins d'appui immédiat en cas de difficulté technique.
- **La charge mentale du travail de nuit** : accumulation de fatigue, impact sur la vie personnelle, récupération plus difficile en fin de chantier — d'autant plus marquée que le volume d'heures a doublé par rapport au prévisionnel.

### 4.3.4 Les axes d'amélioration proposés

| Axe | Mesure concrète |
|---|---|
| **Fiabiliser la transmission jour/nuit** | Compte rendu photo standardisé envoyé en fin de poste ; recouvrement de 30 minutes entre l'encadrement et l'équipe de nuit une fois par semaine |
| **Réduire la vulnérabilité de l'effectif** | Identifier un troisième compagnon formé et disponible en renfort, prévu au planning sur les phases lourdes |
| **Prendre en compte la pénibilité du travail de nuit** | Alternance des tâches les plus physiques, limitation de la durée des périodes de nuit consécutives, respect strict des repos compensateurs |
| **Prendre en compte les spécificités individuelles** | Recueil des contraintes personnelles avant affectation (situation familiale, éloignement, restrictions médicales) ; volontariat ; pour un collaborateur en situation de handicap, étude systématique d'un **aménagement de poste** avec le médecin du travail et le référent handicap — accessibilité des zones, adaptation des horaires, choix des moyens d'accès, aménagement du poste de préfabrication au sol plutôt qu'en nacelle |
| **Entretenir la motivation** | Point d'avancement visuel (linéaire de gaines posé, nombre d'unités raccordées), reconnaissance explicite des étapes franchies, association du binôme aux décisions techniques |
| **Capitaliser** | Retour d'expérience écrit en fin de chantier, partagé avec la cellule : ce qui a marché, ce qui a coûté du temps, ce qu'on refera autrement |

## 4.4 Ce que le projet m'a apporté

**Sur le plan technique** : la maîtrise du **dimensionnement d'une installation DRV en site occupé** (bilan thermique, foisonnement, réseau de gaines, pression statique disponible) ; la compréhension fine des **spécificités thermiques d'un supermarché**, en particulier l'interaction entre le froid alimentaire et le confort d'ambiance, qui fausse les raisonnements de dimensionnement classiques ; l'approfondissement de la **réglementation fluides** et de ses conséquences sur les choix de conception.

**Sur le plan réglementaire** : avant ce projet, le décret tertiaire était pour moi un sigle. Je sais aujourd'hui **identifier si un bâtiment est assujetti, calculer l'objectif 2030 en valeur relative (369,2 → 221,5 kWh/m² sur ce site), situer les échéances, décrire les sanctions, et articuler le tout avec les décrets BACS, la loi APER, la loi LOM et la réglementation F-Gas**. C'est, concrètement, ce qui me permet de parler à un chef d'entreprise et non seulement à un technicien.

**Sur le plan de la gestion de projet** : le passage d'une logique de **tâche** à une logique de **projet** (objectifs, parties prenantes, planning, risques, indicateurs) ; l'apprentissage — **par l'erreur** — du chiffrage d'un chantier atypique (nuit, hauteur, site occupé) ; et l'apprentissage de la **conduite d'un client** — convaincre ne consiste pas à énoncer des arguments techniques, mais à traduire un enjeu technique dans le langage du décideur : euros, risques, image, continuité d'exploitation.

**Sur le plan personnel**, ce projet a marqué mon passage d'un rôle d'exécution technique à celui de contributeur d'un projet. J'ai découvert que la partie la plus difficile n'est pas la technique — elle s'apprend — mais **l'anticipation** : voir un mois à l'avance le problème qui n'existe pas encore. Le doublement du temps de nuit en est l'illustration exacte.

## 4.5 Prise de recul sur le secteur et le métier

**1. La contrainte réglementaire est devenue le premier moteur du marché.** Pendant longtemps, l'efficacité énergétique se vendait sur le seul retour sur investissement — donc mal, puisque les temps de retour sont longs. Ce projet en est l'illustration : **15 ans de retour** pour l'action isolée, ce qui ne se vend pas. Ce qui l'a rendu possible, c'est la combinaison d'une **obligation datée** (− 40 % en 2030), d'un **équipement en fin de vie** et d'un **besoin de confort**. Notre métier consiste de plus en plus à **accompagner une trajectoire réglementaire**, et de moins en moins à vendre un équipement.

**2. Le métier d'installateur se déplace vers le conseil et l'exploitation.** Le client achète une performance mesurée dans la durée, ce qui suppose des compétences en mesure, en régulation et en analyse de données — et rend le poste de mainteneur stratégique, puisqu'il est le seul à voir l'installation vivre toute l'année.

**3. Il existe un décalage réel entre l'ambition réglementaire et le terrain.** Sur ce site, le client ignorait être assujetti à la loi LOM depuis le 1<sup>er</sup> janvier 2025, à la loi APER pour 2028, et se trouvait déjà hors délai sur le décret BACS du fait de sa chaudière de 452 kW. Ce décalage est à la fois un risque collectif et une opportunité pour les entreprises capables de faire le lien entre réglementation et travaux.

**4. La limite honnête de ce type de projet.** Sur ce site, le bâti est correctement isolé : agir sur les systèmes était le bon choix. Mais il faut regarder la répartition des consommations en face — **le froid alimentaire représente 37 % des consommations avant travaux et 58 % après**, l'éclairage 27 % puis 17 %, quand le chauffage pesait 13 %. Autrement dit, **le projet le plus visible n'était pas le plus lourd énergétiquement**. La suite du travail sur ce magasin est dans la fermeture des meubles frigorifiques, la gestion de l'éclairage et les ombrières photovoltaïques — et un projet honnête dit cela au client dès le départ.

**5. La question des fluides frigorigènes restera un point de vigilance.** On substitue un impact carbone lié à la combustion par un impact **potentiel** lié à la fuite de fluide. Avec du **R-410A à GWP 2 088**, quelques kilogrammes échappés annulent une partie du bénéfice climatique de plusieurs années de fonctionnement. L'étanchéité du circuit et le sérieux des contrôles périodiques deviennent donc une **condition de la performance environnementale annoncée**, et pas seulement une obligation administrative. C'est une responsabilité directe de mon métier, et le meilleur argument en faveur d'un contrat de maintenance sérieux.

## 4.6 Mon projet professionnel

Ce projet confirme l'orientation que je souhaite donner à ma carrière : évoluer vers une fonction de **chargé d'affaires ou de chargé de projet en efficacité énergétique**, en conservant l'ancrage terrain qui fait ma crédibilité. La licence CPEBD m'apporte les méthodes (diagnostic, réglementation, gestion de projet, calcul économique) ; mon poste m'apporte la matière et la relation client. Le parcours « pépinière » de VINCI Energies, ouvert aux profils de niveau licence, constitue une suite logique, de même qu'une montée en compétence sur la **mesure et le pilotage des consommations** (GTB, supervision, exploitation des données), qui est à mon sens le prochain gisement de valeur de notre métier.

# Conclusion

Le projet décrit dans ce rapport est parti d'une situation banale pour un chargé de maintenance — une **chaudière gaz de 1987**, des pannes, un magasin sans climatisation et un client qui subissait sa facture — pour aboutir à une opération structurante : le remplacement du chauffage de la surface de vente par une **pompe à chaleur réversible DRV DAIKIN de 70,4 kW**, avec **59 mètres de gaine diffusante** au-dessus de la ligne de caisses, réalisée **de nuit, de mi-avril à mi-juin 2026, sans un seul jour de fermeture**, pour **90 000 € HT dont 11 000 € financés par les CEE**.

Ce parcours illustre ce que le bloc 4 cherche à évaluer :

- **une problématique réelle**, objectivée par un **audit IPMVP** qui a chiffré l'écart à combler : **330,6 kWh/m²/an contre 221,5 exigés en 2030** ;
- **un argumentaire construit**, croisant technique, économie, environnement et réglementation — décret tertiaire, décret BACS, lois APER et LOM, règlement F-Gas — pour amener un décideur à agir en lui montrant que **l'inaction a un coût** ;
- **des objectifs formalisés**, un **budget détaillé**, un **financement CEE** et un **calendrier** de deux mois ;
- **une planification sous contraintes fortes** : fenêtre de huit heures entre 19 h 45 et 4 h 45, ERP en exploitation, 70 % des tâches en nacelle ;
- **une évaluation finale** assortie d'indicateurs d'impact et d'une **analyse critique** assumée : le fluide R-410A, un temps de retour de quinze ans, l'absence de sous-comptage préalable.

Mon niveau d'intervention, je l'ai dit clairement : j'ai **participé** à l'audit sans en être l'auteur, et j'ai **réalisé une partie** du chantier sans en avoir été le chef. C'est précisément ce qui rend ce projet formateur : il m'a fait passer du poste de **chargé de maintenance** — entretiens, dépannages, devis de remplacement de petites installations — au rôle de contributeur d'un projet de transition énergétique à 90 000 €, en en comprenant chaque dimension. Car **le rôle d'un chargé de projet en transition énergétique n'est pas de proposer la meilleure solution technique, mais de rendre une solution possible** : économiquement acceptable pour le client, réalisable pour l'équipe, sûre pour les compagnons et conforme pour le bâtiment.
