---
title: XEI.ItemGenerator – Manuel d'utilisation
description: Comment configurer les bases, les valeurs et les variantes et générer les articles avec XEI.ItemGenerator.
lang: fr
prodotto: XEI.ItemGenerator
versione: 1.5.0
stato: approvato
---

# XEI.ItemGenerator – Manuel d'utilisation

L'installation, la licence, les menus et les autorisations sont décrits dans le
[manuel d'installation](installazione.md).

## 1. Ce que fait l'add-on

XEI.ItemGenerator crée dans les données article des articles dont les codes se **composent** en
choisissant des valeurs, niveau par niveau : type de produit, dimension, matériau... Vous définissez
une seule fois l'arborescence des choix ; ensuite, au lieu d'inventer les codes et les descriptions
à la main, vous les composez dans une fenêtre : l'add-on calcule le code, la description, le prix,
le poids, les dimensions, le groupe, les propriétés et la nomenclature, et crée les articles en
copiant un article modèle.

- **Codes cohérents** : le code est « parlant » (p. ex. `PE090` = élément haut de 90) suivi d'un
  numéro séquentiel qui distingue les variantes (couleur, poignée...).
- **Aucun doublon** : la même composition génère toujours le même article ; s'il existe déjà,
  l'add-on le retrouve.
- **De nombreux articles en une seule fois** : plusieurs dimensions et plusieurs options donnent
  toutes les combinaisons.
- **Articles complets** : les descriptions (également en langue étrangère), les données article, le
  prix de la liste de prix et la nomenclature proviennent de la configuration.
- **Depuis le document** : dans les offres de vente et les commandes client, vous configurez
  l'article de la ligne sans quitter le document.

### Points forts

- Génération dans une fenêtre redimensionnable au-dessus de SAP : arborescence des codes et
  arborescence des variantes avec cases à cocher (même sur des branches différentes), recherche,
  liste des articles avec statut, prix et résultat ; SAP reste utilisable. Aspect du client SAP,
  messages dans le même style, textes modifiables par clic droit.
- Prix, poids, dimensions, groupes, propriétés, nom étranger et nomenclature composés à partir des
  valeurs et des options.
- Formule de description avec codes, options et parties facultatives.
- Configurer l'article depuis les offres de vente et les commandes client ; générer des articles
  similaires à partir d'un article généré.
- Vérification de la configuration avec ouverture des données à corriger ; import/export avec
  Excel ; duplication.
- Autorisations SAP par fonction ; textes en cinq langues.

## 2. Concepts : bases, valeurs, variantes et structures

Le code d'un article se compose d'un **code neutre** + un **suffixe** :

- le **code neutre** est la partie parlante : la concaténation des codes des **valeurs** choisies
  niveau par niveau. Chaque niveau est une **base** (p. ex. *Type de meuble*, *Largeur*) avec une
  longueur fixe et ses valeurs ; chaque valeur mène au **sous-niveau** suivant ou est la dernière ;
- le **suffixe** est un numéro séquentiel de N chiffres (paramètres) qui distingue les articles ayant
  le même code neutre et des **variantes** différentes ; avec 0 chiffre, le code est le code neutre ;
- une **variante** (p. ex. *Couleur*) a des **options** (p. ex. blanc, chêne). Les variantes à
  demander pour une valeur sont regroupées dans une **structure de variantes** liée à la valeur.

Tout au long du manuel, nous utilisons cet exemple, contenu dans le fichier
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx), à importer avec
*Import / export Excel* :

```
Tipo mobile cucina (CU, 2 caractères)         structure CUSC : Colore
├── BA Mobile base     → Larghezza
└── PE Mobile pensile  → Larghezza
Larghezza (CL, 3 caractères)                  structure CUSM : Colore anta + Maniglia, hérite des variantes
├── 060 Larghezza 60 cm
└── 090 Larghezza 90 cm
Colore (CUCOL)     BI Bianco · RO Rovere
Maniglia (CUMAN)   AL Maniglia alluminio · NE Maniglia nera
```

L'élément haut de 90 avec poignée en aluminium a le code neutre `PE090` ; en générant ensemble le
blanc et le chêne, avec un suffixe de 3 chiffres, le blanc (BI vient avant RO) devient `PE090001`
et le chêne `PE090002`.

La **composition** (valeurs de chaque niveau + options choisies) identifie l'article : si vous
générez à nouveau la même composition, l'add-on retrouve l'article existant au lieu d'en créer un
autre.

## 3. Paramètres

![Paramètres](../../_img/itemgenerator/02_configurazione.png)

*La fenêtre des paramètres.*

| Option | Effet | Par défaut |
|---|---|---|
| Chiffres du suffixe | numéro séquentiel après le code neutre (0-10) ; 0 = code égal au code neutre (un seul article par code neutre) | 0 |
| Formule de description | mode de composition de la description (chapitre 8) ; vide = descriptions des niveaux dans l'ordre | vide |
| Descriptions en majuscules | description, description étendue et nom étranger en majuscules | Non |
| Liste de prix | liste de prix dans laquelle le prix de l'article est écrit (somme des prix des valeurs et des options), dans la devise locale | aucune |
| Unité de longueur | unité des dimensions (longueur, largeur, hauteur) des valeurs et des articles ; vide = dimensions non reportées | aucune |
| Unité de poids | unité du poids des valeurs et des options ; vide = poids non reporté | aucune |
| Nomenclature | type de nomenclature créée avec les composants : Aucune, Production, Vente, Assemblage, Modèle | Production |
| Menu après création | menu à lancer pour chaque article créé (intégration avec d'autres add-ons, chapitre 14) | vide |
| Miniature | image de l'article dans l'en-tête des données article (chapitre 14) | Non |
| Ajouter à la liste vide d'abord la liste | dans la génération, *Ajouter à la liste* remplace la liste par la dernière sélection ; sans cette option, les articles s'accumulent et se retirent avec *Vider la liste* (chapitre 9) | Oui |
| Thème des fenêtres | couleurs des fenêtres de l'add-on (la génération), comme les deux thèmes du client SAP : **SAP SQL** (en-tête foncé, boutons dorés) ou **SAP HANA** (en-tête bleu, boutons bleu clair). S'applique à tous les add-ons XEI de la société ; les fenêtres ouvertes changent immédiatement | selon la base de données |

Les paramètres s'appliquent à toute la société ; si la génération est déjà ouverte, elle les
utilise à sa réouverture.

## 4. Variantes et structures de variantes

### Définition des variantes et des options

Une variante a un code, une description et ses **options** (onglet *Options*). Dans l'en-tête,
comme pour les bases, vous pouvez indiquer une **table utilisateur** et un **champ utilisateur
article** : à la création de l'article, l'option choisie est ajoutée à la table (si elle n'y est
pas) et son code est écrit dans le champ utilisateur de l'article (chapitre 6).

![Variante Couleur avec les options](../../_img/itemgenerator/03_varianti.png)

*La variante Couleur avec ses options.*

| Colonne | Utilisation |
|---|---|
| Option, Description | code et description de l'option ; la description est le texte de l'option dans la description de l'article |
| Desc. étrangère | texte de l'option dans le nom étranger (vide = le texte italien) |
| Alias | texte libre |
| Prix | contribution au prix de l'article |
| Poids | contribution au poids de l'article |
| Propriétés | propriétés article à activer : nombres de 1 à 64 séparés par une virgule (p. ex. `2, 12`) |
| Actif | les options désactivées n'apparaissent pas dans la génération |

Dans l'onglet *Composants*, vous indiquez les composants de la nomenclature apportés par les options
(chapitre 7).

![Composants des options](../../_img/itemgenerator/04_varianti_componenti.png)

*Composants des options de la poignée : deux poignées du magasin 01.*

### Structures de variantes

Une structure regroupe les variantes à demander pour une valeur de base, avec la **position**
(ordre dans la génération ; toutes différentes) et la **position de description** (ordre de l'option
choisie à la fin de la description ; 0 = ne va pas à la fin). La description de la ligne, si elle
est indiquée, remplace celle de la variante (p. ex. « Couleur de la porte »).

![Structure de variantes](../../_img/itemgenerator/05_strutture.png)

*La structure CUSM : couleur de la porte et poignée.*

Une variante utilisée par une structure ne peut pas être supprimée, ni une structure utilisée par
une base.

## 5. Bases et valeurs

En-tête de la base : code, description, **longueur des codes** (toutes les valeurs ont cette
longueur), classification, table utilisateur et champ utilisateur article. L'onglet *Valeurs*
contient une ligne par valeur :

![Base avec les valeurs](../../_img/itemgenerator/06_basi_valori.png)

*La base CU avec ses valeurs : descriptions, sous-niveau, structure de variantes.*

![Colonnes des valeurs](../../_img/itemgenerator/06b_basi_valori.png)

*Les colonnes suivantes : données pour l'article (groupe, propriétés, prix, dimensions, poids).*

Les colonnes sont nombreuses : **en agrandissant la fenêtre**, le tableau s'élargit et toutes les
colonnes sont visibles.

| Colonne | Utilisation |
|---|---|
| Code, Description | code de la valeur (de la longueur exacte indiquée dans la base) et description |
| Desc. article | texte de la valeur dans la description de l'article |
| Desc. étrangère | texte de la valeur dans le nom étranger de l'article (vide = le texte italien) |
| Sous-niveau | base du niveau suivant (liste de choix ; la flèche ouvre la base) ; vide = dernier niveau |
| Structure variantes | variantes à demander pour la valeur (la flèche ouvre la structure) |
| Hériter variantes | les variantes déjà présentes à un niveau précédent partent avec les options choisies à ce niveau, **proposées** : elles peuvent être modifiées sur la valeur (clic droit dans la génération pour revenir aux options proposées). Tant qu'elles suivent la proposition, l'option ne compte qu'une seule fois |
| Forcer l'héritage | avec Hériter variantes : le choix du niveau précédent s'applique et ne peut pas être modifié sur la valeur (la variante n'apparaît pas à son niveau) |
| Actif | les valeurs désactivées n'apparaissent pas dans la génération |
| UM stock / achat / vente | unités de mesure textuelles de l'article |
| Groupe d'articles, Groupe UM | groupe d'articles et groupe d'unités de mesure de l'article |
| Propriétés | propriétés article à activer (1-64) |
| Prix, Poids | contributions au prix et au poids de l'article |
| Longueur, Largeur, Hauteur | dimensions de l'article |

L'utilisation de ces données pour l'article est expliquée au chapitre 6. Dans l'onglet
*Composants*, vous indiquez les composants de la nomenclature apportés par les valeurs :

![Composants des valeurs](../../_img/itemgenerator/07_basi_componenti.png)

*L'élément haut apporte deux équerres.*

- **Table utilisateur** (une table utilisateur sans objet, par exemple une table des couleurs) : à
  la création de l'article, la valeur choisie y est ajoutée (code et description), si elle n'y est
  pas.
- **Champ utilisateur article** (par exemple un champ *Couleur* des données article) : à la
  création, le code de la valeur choisie y est écrit.
- Les bases de **premier niveau** sont celles qui ne sont le sous-niveau d'aucune valeur.

À l'enregistrement, l'add-on contrôle les longueurs, les codes répétés, le sous-niveau différent de
la base elle-même, les propriétés et les composants ; le motif d'une erreur s'affiche dans la barre
d'état et l'enregistrement n'a pas lieu. Une base utilisée par des articles générés ou qui est le
sous-niveau d'une autre base ne peut pas être supprimée.

> **Dupliquer** (dans les bases, les variantes et les structures) : avec un enregistrement ouvert,
> prépare un nouvel enregistrement avec les mêmes données et toutes les lignes ; saisissez le
> nouveau code et cliquez sur *Ajouter*. Pratique pour des bases similaires (p. ex. une autre gamme
> de dimensions).

## 6. Données de l'article créé

Chaque donnée de l'article provient des valeurs de la composition et des options choisies, selon
deux règles :

- **le dernier niveau qui l'indique s'applique** : un niveau suivant redéfinit les niveaux
  précédents ; une donnée vide ou à zéro n'efface pas celle d'un niveau précédent ;
- **elle s'additionne** : toutes les valeurs et les options choisies y contribuent. Une option
  héritée ne compte qu'une seule fois, au niveau où elle a été choisie, tant que le niveau qui en
  hérite la suit ; un choix propre à ce niveau compte aussi à ce niveau (même s'il s'agit de la même
  option).

| Donnée de l'article | Provenance | Règle |
|---|---|---|
| Code | codes des valeurs | code neutre + suffixe (50 caractères max.) |
| Description, description étendue | desc. article des valeurs, descriptions des options | formule (chapitre 8) ; la description est tronquée à 200 caractères, la description étendue est complète dans le champ *Description étendue* |
| Nom étranger | desc. étrangère des valeurs et des options | même formule ; vide si aucune n'a de desc. étrangère |
| Remarques | composition | arborescence avec les valeurs et les options choisies |
| Groupe d'articles | valeurs | dernier niveau ; aucun = celui du modèle |
| Groupe UM | valeurs | dernier niveau ; avec un groupe, les UM textuelles ne sont pas utilisées |
| UM stock / achat / vente | valeurs | dernier niveau, chacune indépendamment |
| Propriétés | valeurs et options | s'additionnent : elles sont toutes activées |
| Longueur, largeur, hauteur | valeurs | dernier niveau, chacune indépendamment ; en achat et en vente |
| Poids | valeurs et options | s'additionne ; en achat et en vente |
| Prix | prix des valeurs et des options | s'additionne ; dans la liste de prix des paramètres |
| Nomenclature | composants des valeurs et des options | s'additionnent (chapitre 7) |

Exemple : élément haut de 90 en chêne avec poignée en aluminium (la couleur est choisie au
niveau 1 et héritée par le 090).

| Niveau | Choix | Prix | Poids | Dimensions | Groupe | Propriétés |
|---|---|---|---|---|---|---|
| 1 Type | PE Élément haut | 100 | 10 | largeur 350, hauteur 720 | 101 | 1, 3 |
| 1 Couleur | RO Chêne | 30 | 1,5 | | | 2 |
| 2 Largeur | 090 L90 | 40 | 3 | longueur 900 | | 5 |
| 2 Poignée | AL Aluminium | 5 | 0,2 | | | |
| **Article** | | **175** | **14,7** | **900 × 350 × 720** | **101** | **1, 2, 3, 5** |

Tout le reste (comptes, données de planification, fournisseur, magasins...) provient de l'**article
modèle** choisi dans la génération : les nouveaux articles en copient les données, sans stocks,
prix, codes-barres, nomenclature, derniers prix ni nom étranger.

![L'article créé](../../_img/itemgenerator/12_articolo.png)

*L'article créé : description, nom étranger, groupe, prix dans la liste de prix.*

![Propriétés](../../_img/itemgenerator/13_articolo_proprieta.png)

*Propriétés activées par les valeurs et les options.*

![Dimensions et poids](../../_img/itemgenerator/14_articolo_misure.png)

*Dimensions et poids dans les données de vente.*

## 7. Nomenclature

Chaque valeur de base et chaque option de variante peut avoir des **composants** (onglet
*Composants* des deux définitions) : l'article composant, la **quantité pour une unité** de l'article
généré et, facultativement, le **magasin** de prélèvement (vide = celui par défaut du composant).
À la création, l'add-on crée la nomenclature de l'article avec les composants de toute la
composition :

1. pour chaque niveau, du premier au dernier, les composants de la valeur choisie, puis ceux des
   options choisies ;
2. les options **héritées** n'apportent pas une nouvelle fois leurs composants ;
3. le **même article avec le même magasin** devient une seule ligne avec les quantités
   additionnées ;
4. la nomenclature a la quantité 1 et le **type** défini dans les paramètres (production, vente,
   assemblage, modèle) ; avec *Aucune*, ou si la composition n'a pas de composants, la nomenclature
   n'est pas créée ;
5. l'article et la nomenclature sont enregistrés ensemble : si la nomenclature ne peut pas être
   créée, l'article n'est pas créé non plus et le motif figure dans la colonne *Résultat* de la
   génération.

> SAP n'accepte chaque type de nomenclature que sur des articles adaptés (par exemple la
> nomenclature de production sur un article géré en stock, celles de vente et d'assemblage sur un
> article de vente non géré en stock) : l'article modèle doit avoir les caractéristiques adaptées au
> type choisi dans les paramètres.

Dans l'exemple, l'élément haut apporte 2 équerres, l'option chêne 1 porte, la poignée en aluminium
2 poignées du magasin 01. L'élément haut de 90 en chêne avec poignée en aluminium a cette
nomenclature :

![Nomenclature](../../_img/itemgenerator/15_distinta.png)

*La nomenclature créée avec l'article.*

Dans la génération, la colonne *Composants* de la liste indique combien de lignes la nomenclature
aura ; après la création, le résultat indique « Avec nomenclature (n composants) ». La vérification
de la configuration signale les composants inexistants, avec une quantité nulle ou avec des magasins
inexistants.

## 8. Formule de description

La formule (paramètres) détermine comment se composent la description, la description étendue et le
nom étranger.

| Espace réservé | Devient |
|---|---|
| `{1}`, `{2}`... | la *desc. article* de la valeur choisie au niveau 1, 2... |
| `{C:1}`, `{N:1}` | le code et la description de la valeur choisie au niveau 1 |
| `{V:CUCOL}` | la description de l'option choisie pour la variante `CUCOL` |
| `{VC:CUCOL}` | le code de l'option choisie pour la variante `CUCOL` |
| `{NEUTRO}` | le code neutre |
| `[ ... ]` | partie facultative : elle n'apparaît que si tous les espaces réservés qu'elle contient ont une valeur |

- **Formule vide** : les desc. article des niveaux dans l'ordre.
- **À la fin** viennent les descriptions des options dont la position de description est supérieure
  à zéro, dans cet ordre, si la formule ne cite pas déjà leur variante avec `{V:...}` ou `{VC:...}`.
- Un espace réservé sans valeur devient vide ; à l'intérieur de `[ ]`, il supprime toute la partie,
  séparateurs compris.
- Les doubles espaces sont supprimés ; avec *Descriptions en majuscules*, tout est en majuscules ;
  les majuscules et les minuscules ne comptent pas dans les espaces réservés.
- **Nom étranger** : la même formule avec les desc. étrangères (les italiennes là où elles
  manquent) ; vide si aucune valeur et aucune option n'a de desc. étrangère.
- Un espace réservé inconnu reste dans le texte, pour qu'il soit visible ; la vérification de la
  configuration le signale, ainsi que les crochets non fermés ou imbriqués.

Exemples avec l'élément haut de 60 en chêne avec poignée en aluminium :

| Formule | Description |
|---|---|
| *(vide)* | `Pensile L60 Rovere Maniglia alluminio` |
| `{1} {V:CUCOL} {2}` | `Pensile Rovere L60 Maniglia alluminio` |
| `{N:1} {C:2} - {NEUTRO}` | `Mobile pensile 060 - PE060 Rovere Maniglia alluminio` |
| `{1} {2}[ con {V:CUMAN}]` | `Pensile L60 con Maniglia alluminio Rovere` ; sans poignée : `Pensile L60 Rovere` |
| *(vide)*, majuscules | `PENSILE L60 ROVERE MANIGLIA ALLUMINIO` |
| *(vide)*, nom étranger | `Wall unit L60 Oak Maniglia alluminio` |

## 9. Génération des articles

La génération est une **fenêtre séparée, au-dessus de SAP** : elle s'agrandit, se réduit et se
redimensionne comme toute fenêtre Windows (les panneaux s'adaptent ; les séparateurs entre les
panneaux se déplacent par glisser). La position, les dimensions, les séparateurs et la largeur des
colonnes sont mémorisés par utilisateur ; la première fois, la fenêtre s'ouvre en plein écran.
Pendant qu'elle est ouverte, SAP reste utilisable, même pendant la création des articles. Les
couleurs suivent le **Thème des fenêtres** des paramètres (chapitre 3) : l'en-tête affiche le format
du code et, en dessous, un panneau indique d'où la génération a été ouverte (ligne d'un document,
article similaire) ou ce qui ne va pas.

Les opérations longues (ouvrir de nombreux niveaux, rechercher, cocher une branche entière, ajouter
ou créer de nombreux articles) **affichent ce qu'elles font** en bas de la fenêtre (message avec
l'avancement, barre) et s'arrêtent avec *Interrompre* ; pendant ce temps, les commandes sont
bloquées et la fenêtre reste active. Les résultats s'affichent en bas, avec une icône (verte,
orange, rouge). Une erreur imprévue s'affiche dans un message et la fenêtre reste utilisable.

![Génération avec variantes](../../_img/itemgenerator/09_genera_varianti.png)

*Largeurs 060 et 090 de l'élément bas et de l'élément haut cochées (sur deux branches), couleurs
blanc et chêne, poignées aluminium et noire : 16 articles à composer.*

1. **Article modèle** (en haut, facultatif, mémorisé d'une session à l'autre) : les nouveaux
   articles en copient les données (chapitre 6). Le bouton *...* (ou F2) recherche l'article par code
   ou par description ; à côté du code s'affiche la description, ou *Article introuvable dans les
   données article*. Sans modèle, les articles sont créés avec les seules données de la
   configuration.
2. **Arbre des codes** (à gauche) : les bases du premier niveau avec leurs valeurs ; le signe **+**
   ouvre le sous-niveau d'une valeur. Les valeurs avec variantes sont en bleu ; en passant la souris
   sur une valeur, vous voyez la description de l'article, les variantes et le sous-niveau. **Cochez
   les valeurs du dernier niveau** (les seules avec une case à cocher), même plusieurs et **même sur
   des branches différentes** : à côté des branches s'affiche le nombre de valeurs cochées en dessous
   (*✓ 2*) et, sous l'arbre, leurs codes neutres.
   - **Chercher** : un code neutre complet (p. ex. `PE090`) mène directement à sa valeur ; sinon, la
     recherche mène à la valeur suivante qui contient le texte dans le code ou dans la description
     (Entrée pour la suivante, Ctrl+F pour revenir à la recherche). La recherche porte aussi sur les
     niveaux pas encore ouverts.
   - **Tout développer**, **Réduire**, **Tout décocher** ; **Code neutre** affiche le code neutre à
     côté de chaque valeur.
   - Clic droit sur une branche : *Cocher les valeurs du dernier niveau en dessous*, *Décocher en
     dessous*, *Développer en dessous*. Double-clic ou barre d'espace sur une valeur du dernier
     niveau : la coche ou la décoche.
3. **Variantes et options** (à droite) : la **structure de la valeur sélectionnée** dans l'arbre
   (clic ou flèches), avec ses variantes dans l'ordre de la structure, les options à cocher et leur
   contribution au prix ; le titre indique de quelle valeur il s'agit. Une variante héritée l'indique
   à côté de son nom : *proposé par le niveau 1, Type : modifiable* (elle suit le choix fait plus
   haut), *choix propre, différent du niveau 1* (avec le clic droit *Revenir aux options
   proposées*), *comme le niveau 1 : héritage forcé* (chapitre 5). La même variante au même niveau
   se choisit **une seule fois** pour toutes les valeurs cochées. La case *Toutes les variantes des
   valeurs cochées, par niveau* affiche en revanche toutes les variantes des valeurs cochées
   regroupées par niveau, avec *seulement pour 060* si une variante ne concerne que certaines
   valeurs. Plusieurs options de la même variante donnent plusieurs articles ; une variante sans
   option cochée n'entre pas dans la composition. Clic droit : *Cocher toutes les options* /
   *Décocher toutes les options*. En dessous s'affiche le nombre d'articles qui seront composés.
4. **Ajouter à la liste** : compose toutes les combinaisons dans la liste du bas, avec le code, la
   description, le prix, le nombre de composants de la nomenclature et le statut. Par défaut
   (option *Ajouter à la liste vide d'abord la liste*, chapitre 3), la liste est vidée et ne contient
   que la dernière sélection ; si l'option est désactivée, les articles s'accumulent et ceux déjà
   présents dans la liste ne sont pas répétés. Les coches des valeurs et des options restent (elles
   se retirent avec *Tout décocher*) : vous changez une option ou une valeur et vous ajoutez à
   nouveau.
5. **Générer les articles (n)** : crée les articles cochés de la liste (n sur le bouton), un par un,
   avec le résultat ligne par ligne et la barre de progression. *Interrompre* arrête la création
   après l'article en cours. À la fin, en bas de la fenêtre, s'affiche le récapitulatif : *Articles
   créés : n.*, puis, seulement s'il y en a, ceux qu'un autre utilisateur avait déjà créés entre-temps
   et ceux en erreur ; la liste se positionne sur le premier article créé.

![Liste des articles composés](../../_img/itemgenerator/08_genera.png)

*Les 16 articles composés (la fin de la liste) : 15 déjà dans les données article (en jaune) et un à
créer, PE060004, avec le prix et le nombre de composants.*

| Statut | Signification |
|---|---|
| À créer | code = code neutre + premier suffixe libre (ni dans les données article ni déjà dans la liste) |
| Déjà existant | la même composition est déjà dans les données article : le code est celui de l'article existant (jaune) |
| Créé | article créé (vert) ; le résultat indique s'il a une nomenclature |
| Erreur | le motif figure dans la colonne *Résultat* (rouge) : code déjà utilisé, suffixes épuisés, code trop long, erreur de SAP. Vous pouvez corriger et générer à nouveau |

![Résultat de la génération](../../_img/itemgenerator/11_genera_esito.png)

*Résultat de la génération : les éléments bas de 60 et de 90 en blanc créés (en vert) et le
récapitulatif en bas ; sans composants, ils n'ont pas de nomenclature (avec des composants, le
résultat indique « Avec nomenclature »).*

Dans la liste, la case à cocher (uniquement sur les articles à créer ou en erreur) détermine quels
articles créer. Un **double-clic** (ou Entrée) sur un article créé ou déjà existant l'ouvre dans les
données article de SAP (la génération se réduit et se rouvre depuis la barre des tâches). Un article
encore à créer n'ouvre rien : en bas de la fenêtre s'affiche *L'article ... n'est pas encore dans
les données article* ; il en va de même si l'article a été supprimé entre-temps dans SAP. Clic
droit : *Ouvrir dans les données article*, *Copier le code*, *Retirer de la liste*, *Tout cocher*,
*Tout décocher* ; Suppr retire les lignes sélectionnées, Ctrl+C en copie les codes. *Vider la liste*
repart de zéro. Si la liste contient des articles pas encore créés, la fermeture ou le vidage
demande une confirmation.

### Messages et textes de la fenêtre

Les questions et les messages de la génération (par exemple *Créer 2 articles dans les données
article ?*) ont le même aspect que la fenêtre : Entrée choisit le bouton mis en évidence, Échap
répond Non. Les utilisateurs disposant de l'autorisation **Modifica testi add-on XEI** peuvent
modifier les textes de la fenêtre comme dans les fenêtres de SAP : clic droit sur une étiquette, un
bouton, le titre d'un panneau, l'en-tête d'une colonne ou le texte d'un message, puis **Modifica
testo...** (Modifier le texte) ; **Testi di questa finestra...** (Textes de cette fenêtre) (également à la fin des menus des arbres et de la liste)
les liste tous. Le texte personnalisé s'applique à tous les utilisateurs dans la langue utilisée et
s'affiche immédiatement.

![Question avant la création](../../_img/itemgenerator/25_messaggio.png)

*La question avant la création, dans le style de la fenêtre.*

![Modifica testo](../../_img/itemgenerator/26_modifica_testo.png)

*Modifica testo (Modifier le texte) par clic droit sur le bouton Chercher : texte d'origine et texte personnalisé.*

Avant de créer chaque article, l'add-on vérifie à nouveau que personne n'a créé entre-temps la même
composition ni utilisé le code. Chaque article est créé en une seule opération (article,
nomenclature, tables utilisateur, composition) : une erreur ne laisse pas de données incomplètes.

## 10. Articles depuis les offres de vente et les commandes client

Dans les **offres de vente** et les **commandes client**, clic droit sur une ligne › **Configurer
l'article...** :

![Configurer l'article depuis la ligne](../../_img/itemgenerator/17_ordine_menu.png)

*Configurer l'article depuis la ligne de la commande.*

La génération s'ouvre pour cette ligne (le titre de la fenêtre et le panneau du haut l'indiquent).
Vous composez et créez l'article comme d'habitude ; ensuite, **Utiliser dans la ligne** place dans la
ligne du document l'article sélectionné dans la liste (créé ou déjà existant ; si la liste n'en
contient qu'un, il n'est pas nécessaire de le sélectionner), ferme la génération et ramène le
document au premier plan. SAP remplit la ligne comme si le code avait été saisi à la main :
description, prix de la liste de prix du client, magasin.

![Génération ouverte depuis la ligne](../../_img/itemgenerator/18_genera_documento.png)

*Génération ouverte depuis la ligne 2 de la commande : l'article qui vient d'être créé est
sélectionné et « Utiliser dans la ligne ».*

![Article dans la ligne](../../_img/itemgenerator/19_ordine_riga.png)

*L'article dans la ligne de la commande.*

- Si la ligne contient déjà un article généré par le configurateur, la génération part de sa
  configuration : il suffit de changer une option pour obtenir la bonne variante.
- Si la génération est déjà ouverte, elle passe à la nouvelle ligne ; la liste reste, ce qui permet
  de réutiliser un article composé auparavant.
- Le document doit rester ouvert ; un document fermé ou non modifiable ne change pas (le motif
  s'affiche en bas de la fenêtre).

## 11. Articles similaires

Dans les données d'un article créé par le configurateur, clic droit › **Générer des articles
similaires...** : la génération s'ouvre avec la configuration de l'article déjà définie (sa valeur
finale cochée dans l'arbre, déjà développé jusqu'à elle, et les options choisies) et avec l'article
lui-même comme modèle. Vous changez les valeurs et les options et ajoutez les articles à la liste.
Si la génération est déjà ouverte (même réduite), elle revient au premier plan avec la configuration
de l'article ; la liste reste.

![Clic droit sur un article généré](../../_img/itemgenerator/16_simili_menu.png)

*Le clic droit sur un article généré.*

![Génération d'articles similaires](../../_img/itemgenerator/20_simili.png)

*Génération à partir de la configuration de PE090001 (thème SAP HANA) : élément haut de 90, chêne et
poignée en aluminium déjà cochés ; l'article lui-même comme modèle.*

Si la configuration a changé entre-temps (valeurs supprimées ou désactivées, sous-niveaux
différents), la génération part de zéro, avec un avertissement ; les options qui n'existent plus
sont ignorées.

## 12. Vérification de la configuration

Contrôle toute la configuration (y compris les valeurs et les options désactivées) et affiche les
problèmes, d'abord les erreurs puis les avertissements. Un **double-clic** sur une ligne ouvre les
données à corriger sur l'enregistrement ; *Vérifier à nouveau* répète le contrôle après les
corrections. En agrandissant la fenêtre (même en plein écran), la liste des problèmes suit.

![Vérification de la configuration](../../_img/itemgenerator/21_verifica.png)

*Vérification de la configuration de l'exemple : aucun problème trouvé.*

| Type | Contrôle |
|---|---|
| Erreur | base sans longueur ; code d'une longueur différente de celle de la base ; code répété |
| Erreur | sous-niveau, structure de variantes, groupe d'articles, groupe UM inexistants ; propriétés non valides |
| Erreur | variante inexistante dans une structure ; option répétée |
| Erreur | composant sans article, avec un article ou un magasin inexistant, avec une quantité nulle, pour une valeur ou une option qui n'existe pas |
| Erreur | base sous-niveau d'elle-même (cycle, avec le chemin) ; aucune base de premier niveau |
| Avertissement | base sans valeurs actives ; structure sans variantes ; variante sans options actives |
| Avertissement | base non atteignable depuis le premier niveau (sous-niveau uniquement de valeurs désactivées) |
| Avertissement | chemin qui donne des codes de plus de 50 caractères, suffixe compris |
| Avertissement | valeur qui hérite des variantes sans variantes identiques aux niveaux précédents ; Forcer l'héritage sans Hériter variantes |
| Avertissement | formule avec des espaces réservés inconnus ou des crochets incorrects |

## 13. Import et export avec Excel

![Import depuis Excel](../../_img/itemgenerator/22_excel.png)

*Import du fichier d'exemple réussi.*

**Exporter...** demande où enregistrer et écrit toute la configuration dans un fichier .xlsx, une
feuille par type de données, avec l'en-tête en gras et figé. **Importer** lit le fichier indiqué
(*Parcourir...*). En agrandissant la fenêtre, le nom du fichier et la liste des résultats
s'élargissent.

| Feuille | Une ligne par | Colonnes |
|---|---|---|
| Basi | valeur (les données de la base se répètent) | Base, Descrizione base, Lunghezza, Classificazione, Tabella utente, Campo utente, Codice, Descrizione, Desc. articolo, Desc. straniera, Sotto livello, Struttura varianti, Eredita varianti, Forza ereditarietà, Attivo, UM magazzino, UM acquisti, UM vendite, Valore, Dim. 1, Dim. 2, Dim. 3, Peso, Gruppo articoli, Gruppo UM, Proprietà, Note |
| Componenti basi | composant | Base, Valore, Componente, Descrizione, Quantità, Magazzino, Note |
| Varianti | option | Variante, Descrizione variante, Tabella utente, Campo utente, Opzione, Descrizione, Desc. straniera, Alias, Valore, Peso, Proprietà, Note, Attivo |
| Componenti varianti | composant | Variante, Opzione, Componente, Descrizione, Quantità, Magazzino, Note |
| Strutture | variante | Struttura, Descrizione struttura, Variante, Descrizione variante, Posizione, Pos. descrizione |

- Les colonnes sont reconnues par leur **titre** : l'ordre ne compte pas et les colonnes inconnues
  sont ignorées. Le fichier peut ne contenir que certaines feuilles.
- Nombres au format italien (`1.234,5`) ou anglais (`1234.5`) ; oui/non avec Y, S, Sì, X, 1, Vero.
- Les codes avec des zéros initiaux (`060`) doivent être saisis comme du texte (dans Excel avec
  l'apostrophe : `'060`), sinon Excel les transforme en nombres.
- L'import **contrôle d'abord tout** le fichier : en cas d'erreur, il n'écrit rien et la liste
  affiche la feuille, la ligne et le motif de chaque erreur.
- Il écrit ensuite tout en une seule fois : chaque base, variante ou structure du fichier est ajoutée
  ou mise à jour et ses lignes **remplacent** les lignes existantes ; les composants ne changent que
  pour les bases et les variantes présentes dans les feuilles des composants ; ce qui ne figure pas
  dans le fichier reste inchangé.

Utilisations typiques : exporter, modifier dans Excel (nouvelles valeurs, prix mis à jour) et
réimporter ; copier la configuration dans une autre société ; partir d'un exemple comme
[esempio-cucine.xlsx](../../_file/itemgenerator/esempio-cucine.xlsx).

## 14. Données article, contrôle de cohérence, autres add-ons

### Miniature de l'image

Avec l'option *Miniature*, les données article affichent l'image de l'article (champ Image, dans le
dossier des images de SAP) dans l'espace libre de l'en-tête, à gauche des cases Article géré en
stock/de vente/d'achat. Le cadre prend les proportions de l'image et se masque si l'article n'a pas
d'image. Les données article ne sont pas ralenties.

![Miniature dans les données article](../../_img/itemgenerator/24_miniatura.png)

*La miniature dans les données article.*

### Contrôle de cohérence

Recalcule la composition de tous les articles générés. Utile si les données de la configuration ont
été modifiées en dehors de l'add-on ; supprime aussi les compositions des articles supprimés dans
SAP.

### Intégration avec d'autres add-ons

Avec un *Menu après création* dans les paramètres, pour chaque article créé, l'add-on lance ce menu
après en avoir enregistré le code dans la table XEI `@XEI_IG_EVENTS` : un autre add-on à l'écoute
de ce menu peut compléter l'article.
