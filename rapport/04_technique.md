## 3.3 L'audit énergétique : méthode, résultats et hiérarchisation

### 3.3.1 Cadre et méthode

L'audit énergétique a été réalisé par l'**ingénieur énergéticien de VINCI Energies**, avec ma participation sur le volet relevé et connaissance des installations.

| Élément | Donnée |
|---|---|
| Visite du site | **17/04/2025** — relevé de l'état existant et entretien avec les occupants |
| Date du rapport | **30/07/2025** |
| Documentation exploitée | Plan CVC 2022, DOE de l'extension 2023, factures gaz et électricité 2025 |
| Données réseaux | Courbes de charge **ENEDIS / GRDF** et données fournisseurs |
| Plateforme de suivi | **ENERGISME** |
| Outil de modélisation | Outil interne **FLASH ENERGY**, méthodologie **IPMVP** |

La méthode **IPMVP** (*International Performance Measurement and Verification Protocol*) consiste à construire, à partir des consommations réelles et des données relevées, un **modèle mathématique du bâtiment** (« archétype »), validé statistiquement, puis à identifier les postes les plus critiques pour proposer des actions d'amélioration. L'outil répartit ensuite les consommations par usage à partir de clés propres au secteur d'activité. Les coûts annoncés sont des **budgets** établis sur la tendance du marché, explicitement destinés à être confortés par un chiffrage réel — ce que le devis a fait ensuite, avec un écart significatif analysé en partie 4.

### 3.3.2 État des lieux énergétique

| Indicateur | Valeur |
|---|---|
| **Consommation totale (état existant)** | **1 219 000 kWh<sub>ef</sub>/an**, soit **330,6 kWh<sub>ef</sub>/m²/an** |
| **Coût énergétique associé** | **165 340 € HT/an** |
| Énergies | Gaz naturel (chauffage) + électricité (tous autres usages) |
| Base de référence décret tertiaire (hypothèse 2023/2024) | 1 361 440 kWh<sub>ef</sub>, soit **369,2 kWh/m²** |

**Répartition des consommations par usage — état existant**

| Usage | Part |
|---|---|
| **Production de froid alimentaire** | **37 %** |
| **Éclairage** | **27 %** |
| Autres (serveurs, bureautique, équipements) | 18 % |
| **Chauffage** | **13 %** |
| Climatisation | 4 % |
| ECS | 1 % |
| Ventilation | 0 % |

Ce tableau est essentiel pour la prise de recul : **le chauffage ne représente que 13 % des consommations du site**. Le premier poste est le froid alimentaire, le deuxième l'éclairage. Le projet traité ici n'est donc **pas** le plus gros gisement d'économies en valeur absolue : il a été retenu parce qu'il cumulait un **équipement en fin de vie**, un **besoin de confort d'été non satisfait** et une **contribution réelle à la trajectoire réglementaire**. Le dire clairement est plus honnête — et plus solide devant un jury — que de présenter le chauffage comme l'enjeu principal d'un supermarché.

### 3.3.3 Caractéristiques thermiques du bâti

Le relevé montre un bâti globalement correct. Les **murs principaux** (10 cm de béton cellulaire doublés d'environ 8 cm de laine de verre) et ceux de l'extension (bardage double peau, ≈ 20 cm de laine de verre) sont jugés **bons**, de même que le **plancher** sur vide sanitaire (flocage isolant de 12 cm) et la **toiture de l'extension** (18 cm de laine de roche d'après le DOE). Sont jugés **moyens** : la **toiture du bâtiment principal** (10 à 15 cm d'isolant supposés d'après les plans et l'ancienneté) et les **menuiseries** (aluminium double vitrage 4/12/4, le sas combinant un simple vitrage côté intérieur et un 4/6/4 côté extérieur) ; celles de l'extension, en 4/16/4, sont **bonnes**.

Le bâti n'est donc **pas le point faible du site** : c'est un constat déterminant, car il justifie d'agir en priorité sur les **systèmes** plutôt que sur l'enveloppe.

### 3.3.4 Les actions étudiées et la hiérarchisation

L'audit a chiffré neuf actions de performance énergétique (APE). Le tableau ci-dessous les classe par temps de retour, et indique celles retenues au bouquet.

| Action de performance énergétique | Coût (€ HT) | Économie (€ HT/an) | TRA (ans) | Gain GES (kgCO₂e/an) | Retenue |
|---|---|---|---|---|---|
| **Récupération de chaleur sur les groupes froids** (ballon échangeur 3 000 L) | 34 200 | 6 400 | **4,3** | 17 160 | ✔ |
| **GTC — Gestion Technique Centralisée** (classe A surface de vente, C bureaux) | 39 000 | 5 400 | **5,3** | 7 323 | ✔ |
| Calorifuge des réseaux de chaufferie (si chauffage gaz conservé) | 1 680 | 220 | 6,5 | 586 | ✘ (sans objet si dépose de la chaufferie) |
| **Ballons thermodynamiques pour les labos** (2 × 200 L, COP 3,1 à 7 °C) | 8 840 | 1 410 | **6,3** | 647 | ✔ |
| **Ombrières photovoltaïques** (271,9 kWc, modules 440 Wc, parking) | 368 000 | 43 830 | **8,4** | 19 094 | ✔ |
| Solution « Air Booster » (capteurs solaires verticaux, façade sud, 255 m²) | 69 800 | 6 300 | 11,0 | 17 160 | ✘ (suppression d'arbres nécessaire) |
| Remplacement de la chaudière gaz par un modèle à condensation | 47 800 | 2 250 | 21,4 | 5 960 | ✘ (ne permet ni la climatisation ni un gain significatif) |
| Destratificateurs (29 unités Airius) | 44 100 | 1 600 | 21,4 | 4 170 | ✘ |
| **Chauffage de la surface de vente par pompe à chaleur réversible (DRV)** | **122 800** | **5 260** | **21,5** | **16 679** | **✔ — objet de ce rapport** |

**Le bouquet de travaux retenu** comprend donc cinq actions : **PAC réversible pour la surface de vente**, **ECS thermodynamique**, **ombrières photovoltaïques**, **GTC**, **récupération de chaleur sur les groupes froids**.

| Indicateur du bouquet complet | Valeur |
|---|---|
| Enveloppe d'investissement | **572 940 € HT** |
| Gain financier annuel | **58 590 € /an** |
| Subventions (bonus) | 26 700 € |
| **Retour sur investissement** | **9,3 ans** |
| Gain GES | **64 830 kgCO₂e/an**, soit **− 70 %** |
| Consommation après travaux | **779 000 kWh<sub>ef</sub>/an**, soit **211,2 kWh/m²/an** (contre 221,5 exigés en 2030) |
| Coût énergétique après travaux | 108 880 € HT/an |

**Gains énergétiques par usage** (bouquet complet) :

| Usage | Gain (MWh<sub>ef</sub>/an) | Réduction |
|---|---|---|
| Chauffage & ECS | 115,7 | 9 % |
| Autres (électricité) | 321,1 | 26 % |
| Climatisation | 3,0 | 0 % |
| Production de froid | 0,0 | 0 % |
| **Total** | **439,8** | **36 %** |

**Répartition après travaux** : production de froid 58 %, éclairage 17 %, autres 11 %, chauffage 7 %, climatisation 6 %, ECS 1 %. Le froid alimentaire devient mécaniquement prépondérant — ce qui désigne le prochain chantier.

> **Point de méthode important.** L'audit signale que la mise en place d'une climatisation sur l'ensemble de la surface de vente entraîne une **consommation électrique supplémentaire estimée à 102 MWh, soit + 9 %**. Autrement dit : **le projet améliore le confort et réduit le gaz, mais il augmente la consommation d'électricité**. C'est précisément pour cette raison que l'audit le couple aux **ombrières photovoltaïques** : le profil de consommation d'un supermarché, très diurne, permet d'autoconsommer plus de 90 % de la production. Le bouquet est cohérent ; l'action isolée l'est moins. J'y reviens en partie 4.

## 3.4 La solution technique retenue

### 3.4.1 Le principe retenu par l'audit

La fiche APE « Chauffage de la surface de vente par pompe à chaleur réversible » préconisait :

| Paramètre | Préconisation de l'audit |
|---|---|
| Équipement | **DRV + module de régulation**, réseau de diffusion en gaine |
| **SCOP** | **≥ 4,2** |
| **SEER** | **≥ 6,0** |
| Positionnement des groupes | **Cour arrière** |
| Contraintes / atouts | Passage des liaisons dans les locaux existants et encombrement extérieur ; en contrepartie : redimensionnement selon les besoins réels, régulation programmable, **confort au niveau des caisses**, dépose des aérothermes et de la chaudière gaz, gain au regard du décret tertiaire |

### 3.4.2 Pourquoi le DRV plutôt qu'une autre solution

| Solution | Pourquoi elle a été écartée ou retenue |
|---|---|
| Chaudière gaz à condensation | **Écartée** : 47 800 € pour 2 250 €/an d'économie (21,4 ans), et surtout **aucune réponse au besoin de climatisation**, ni sortie du gaz |
| Rooftops | Écartés : rendement inférieur au DRV en charge partielle, emprise et charge en toiture, zonage grossier |
| PAC air/eau sur réseau existant | Écartée : réseau hydraulique et aérothermes conservés donc rendement d'émission dégradé, pas de climatisation |
| **DRV réversible à détente directe** | **Retenue** : rendement élevé à charge partielle, réversibilité (chauffage **et** rafraîchissement d'un seul investissement), zonage, pose compatible avec un magasin en exploitation, **pas d'eau en surface de vente** |

Sur le plan du rendement, l'écart est décisif : la chaudière de 1987 travaillait avec un rendement utile de l'ordre de **0,7 à 0,8**, quand le groupe installé affiche une **efficacité énergétique saisonnière (ETAS) de 162,4 % en chaud et de 250,8 % en froid**. Pour un même besoin de chaleur, la consommation d'énergie finale est divisée par un facteur de l'ordre de **4 à 5** — l'énergie change simplement de vecteur, du gaz vers l'électricité.

### 3.4.3 L'installation réellement mise en œuvre

**Unités extérieures** — implantées en **cour arrière**, sur **dalle béton**, et non en toiture :

| Élément | Caractéristique |
|---|---|
| Groupes | **DAIKIN RXYQ36U**, soit **RXYQ20U (20 CV) + RXYQ16U (16 CV)** — VRV IV réversible, gamme standard |
| **Puissance chaud à − 10 °C** | **70,4 kW** |
| **Puissance froid** | **89,5 kW** |
| **ETAS chaud / froid** | **162,4 % / 250,8 %** |
| Fluide frigorigène | **R-410A — charge totale de l'installation : 38 kg**, soit **79,3 t CO₂e** |
| Mise en place | Manutention sur dalle bétonnée, **2 supports type Grand Rubber Foot avec 4 plots antivibratiles**, sectionneurs de proximité |
| Mise en service | **Mise en service constructeur DAIKIN** + dossier **DESP** |

**Unités intérieures — 5 au total, toutes en surface de vente :**

| Repère | Type | Référence | Puissance | Zone traitée |
|---|---|---|---|---|
| UI 1 | **Caisson gainable** | DAIKIN **FXMQ-250 A** | **28,0 kW chaud / 31,5 kW froid — 4 440 m³/h** | **Ligne de caisses et fond de magasin**, par gaine diffusante |
| UI 2 à 5 | **Cassettes 900 × 900** | DAIKIN **Roundflow taille 125** | **16 kW chaud / 14 kW froid** (monophasé) | Reste de la surface de vente |

**Distribution d'air** : le gainable souffle dans un **plénum sur mesure en acier galvanisé isolé 25 mm**, puis dans une **gaine acier galvanisé perforée diffusante de type GMD (marque SIONAIR), Ø 550 mm, sur 59 mètres linéaires**, thermolaquée, à diamètre constant, supportage compris. C'est cette gaine qui **traverse le magasin sur toute sa longueur** et assure une diffusion homogène au-dessus de la ligne de caisses — la zone historiquement la plus inconfortable, été comme hiver.

**Réseaux et équipements associés :**

- **Liaisons frigorifiques** en cuivre frigo dégraissé **« 2 tubes »**, isolées, avec **raccords Refnet** et une **charge totale de 38 kg de R-410A** ; pose sur **chemins de câbles en acier galvanisé** avec capotage des liaisons extérieures ;
- **Évacuation des condensats** : **65 m de PVC M1 rigide DN 40**, 5 siphons à culot démontable, 2 raccordements sur réseaux EU ;
- **Alimentations électriques** : liaisons entre unités et coffret CVC, sondes déportées, télécommandes, **liaisons bus LIYCY blindé**, **kit connecteur été/hiver** ;
- **Régulation** : **5 télécommandes filaires DAIKIN MADOKA BRC1H52** (une par unité intérieure) ;
- **Interopérabilité** : **liaisons Modbus ou BACnet pour raccordement à la GTB du site** — c'est l'anticipation du décret BACS décrite en 3.2.2 ;
- **Divers** : percements, fourreaux, ragréages et rebouchages après passage des canalisations.


**Schéma de principe**

```
   COUR ARRIÈRE — sur dalle béton                    SURFACE DE VENTE (2 596 m²)
   ┌───────────────┐  ┌───────────────┐
   │ RXYQ20U 20 CV │  │ RXYQ16U 16 CV │              [Cassette]  [Cassette]
   └───────┬───────┘  └───────┬───────┘                 900x900     900x900
           └────────┬─────────┘                       [Cassette]  [Cassette]
        liaisons frigorifiques 2 tubes R-410A            900x900     900x900
        (cuivre isolé, Refnet, chemins de câbles)
                    │
             [ Gainable FXMQ-250A ] → plénum isolé 25 mm
                    │
        ══════ GAINE DIFFUSANTE PERFORÉE Ø550 — 59 ml ══════►
              (ligne de caisses → fond de magasin)

   Régulation : 5 × MADOKA BRC1H52  +  liaisons Modbus/BACnet → future GTB
```

## 3.5 Étude technique et dimensionnement

### 3.5.1 Ce que dit le dimensionnement retenu

| Vérification | Valeur | Commentaire |
|---|---|---|
| Puissance chaud installée | **70,4 kW à − 10 °C** | Contre **452 kW** de chaudière déposée |
| Puissance froid installée | **89,5 kW** | Besoin estival dimensionnant en surface commerciale |
| Somme des puissances des unités intérieures (chaud) | 28,0 + 4 × 16 = **92 kW** | Soit un **taux de foisonnement d'environ 130 %** par rapport aux 70,4 kW du groupe |
| Ratio de puissance chaud rapporté à la surface de vente | 70,4 kW / 2 596 m² ≈ **27 W/m²** | Cohérent avec un bâti correctement isolé et fortement chargé en apports internes |
| Débit d'air du gainable | **4 440 m³/h** | Diffusion sur 59 ml de gaine Ø 550 |

**Le facteur 6,4 entre l'ancienne chaudière (452 kW) et la nouvelle production (70,4 kW) est l'enseignement technique majeur du projet.** Il ne signifie pas que le bâtiment était sous-chauffé, mais que la chaudière de 1987 était **très largement surdimensionnée** — comme la plupart des installations de cette époque, calculées avec de fortes marges sur un bâti alors moins isolé ; que le bâtiment a été **isolé et modifié** depuis ; que les **apports internes** d'un supermarché sont considérables (éclairage, occupants, et surtout **rejets des groupes de froid alimentaire**, 37 % de la consommation du site, dont une grande partie finit en chaleur dans le bâtiment) ; et que le rendement d'émission d'un DRV à détente directe est sans commune mesure avec celui d'aérothermes à eau chaude pilotés en loi d'eau.

Ce constat est un argument fort en soutenance : **remplacer à l'identique aurait conduit à réinstaller une puissance six fois supérieure au besoin réel**, avec le surcoût d'investissement et les mauvais rendements en charge partielle que cela implique.

### 3.5.2 Méthode de vérification du dimensionnement

Le bilan thermique repose sur les **déperditions hivernales** — *P = Σ(U<sub>i</sub> × A<sub>i</sub>) × ΔT + 0,34 × q<sub>v</sub> × ΔT + ponts thermiques − apports internes* — avec une **température extérieure de base de − 8 à − 10 °C** pour la zone **H1c** (cohérente avec la puissance constructeur annoncée à − 10 °C), une consigne de **19 °C** et un débit de renouvellement d'air majoré par les ouvertures du sas ; et sur les **charges estivales** (transmission, apports solaires, apports internes d'éclairage, d'occupants et d'équipements, air neuf).

**Spécificités d'un supermarché, intégrées au dimensionnement :**

| Spécificité | Effet | Conséquence |
|---|---|---|
| Meubles frigorifiques ouverts | Refroidissent l'ambiance en permanence (« allée froide ») | Ne pas surdimensionner le froid ; besoin de chauffage parfois accru localement |
| Rejets des groupes de froid | Apport de chaleur gratuit non maîtrisé | **Gisement de récupération** — action retenue au bouquet (4,3 ans de retour) |
| Éclairage et occupants | Apports internes importants et permanents aux heures d'ouverture | Réduction du besoin de chauffage, augmentation du besoin de froid |
| Grande hauteur sous plafond | Stratification de l'air chaud | Diffusion par gaine perforée haute, action « destratificateurs » étudiée |
| Ouvertures du sas | Infiltrations d'air extérieur | Traitement renforcé de la zone d'entrée et des caisses |
| Amplitude 4 h 45 – 19 h 45 | Longue plage de fonctionnement | Programmation horaire et réduit de nuit indispensables |

### 3.5.3 Dimensionnement aéraulique

Le réseau de diffusion est le point technique le plus sensible : **59 mètres de gaine perforée à diamètre constant Ø 550 mm alimentée par une seule unité de 4 440 m³/h**.

| Vérification | Valeur de référence | Enjeu sur ce chantier |
|---|---|---|
| Vitesse en gaine principale | 5 à 8 m/s | À Ø 550 mm et 4 440 m³/h, la vitesse d'entrée est de l'ordre de **5,2 m/s** — dans la plage acceptable |
| Vitesse de soufflage en zone d'occupation | < 0,25 m/s | Pas de courant d'air ressenti par les clients ni par le personnel de caisse |
| Perte de charge | Compatible avec la pression statique disponible du gainable | Facteur critique sur 59 ml : un sous-dimensionnement se traduirait par un débit insuffisant en extrémité |
| Diffusion à diamètre constant | Répartition homogène sur la longueur | C'est l'intérêt de la gaine perforée de type GMD : la perforation est calculée pour un débit réparti |
| Acoustique | Niveau compatible avec une surface de vente | Gaine textile ou acier perforée : diffusion basse vitesse, peu bruyante |
| Réaction au feu et traversées | Matériaux conformes, clapets coupe-feu aux parois | Exigences ERP — voir 3.7.3 |

### 3.5.4 Points de vigilance techniques du chantier

| Point de vigilance | Risque | Mesure |
|---|---|---|
| Longueur des liaisons frigorifiques (cour arrière → surface de vente) | Perte de puissance, **charge de fluide élevée : 38 kg** | Respect des longueurs maximales constructeur, appoint de charge calculé et tracé sur la fiche d'intervention, chemins de câbles dédiés |
| Passage des liaisons dans les locaux existants | Contrainte identifiée dès l'audit | Repérage préalable, tracé validé avec l'exploitant, capotage des parties extérieures |
| Condensats au-dessus des rayons | Dégât des eaux sur marchandises | Pentes respectées, siphons à culot démontable, essais à l'eau avant remise en service |
| Support et vibrations des groupes | Bruit transmis, nuisance pour les riverains | Dalle béton, supports Grand Rubber Foot, 4 plots antivibratiles |
| Concentration limite de fluide en cas de fuite | 38 kg de R-410A répartis sur la surface de vente | Vérification selon **NF EN 378** du rapport charge/volume des locaux — sans difficulté ici compte tenu du volume de 2 596 m² de surface de vente en grande hauteur |
| Dépose de la chaudière et des aérothermes | Coupure du chauffage en cours de saison | Phasage : mise en service de la PAC **avant** dépose de l'ancien système |
| Coactivité avec le froid alimentaire | Coupure accidentelle d'un groupe froid | Consignations tracées, repérage préalable, coordination avec le frigoriste du magasin |
| Propreté à l'ouverture | Magasin non présentable à 4 h 45 | Nettoyage systématique en fin de poste (voir 3.8.4) |
