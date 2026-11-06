---
title: XEI.ContoLavoro – Manuel d'utilisation
description: Comment gérer avec XEI.ContoLavoro les ordres de sous-traitance, les envois de composants, les réceptions des produits et la sous-traitance depuis les ordres de fabrication.
lang: fr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Manuel d'utilisation

L'installation, la licence et les menus sont également décrits dans le
[guide d'installation](installazione.md).

## 1. Ce que fait l'add-on

XEI.ContoLavoro gère les façons confiées à des **sous-traitants** (fournisseurs externes) qui reçoivent des
composants de l'entreprise, les travaillent et restituent un produit fini ou semi-fini. Pour chaque façon, on ouvre un
**ordre de sous-traitance** qui réunit :

- les **produits** à obtenir, avec leur nomenclature (composants à expédier et façons à payer) ;
- la **commande d'achat** au sous-traitant, alignée automatiquement sur l'ordre de sous-traitance ;
- les **envois de composants** au magasin du sous-traitant, les **retours** et les **rebuts** ;
- la **réception des produits** : réception de marchandises des produits et des façons, sortie des composants
  consommés, réception de production pour les produits qui proviennent d'un ordre de fabrication (chapitre 6) ;
- la situation en temps réel : ce qui a été expédié et utilisé, ce qui reste chez le sous-traitant et ce qui manque.

L'ordre de sous-traitance se clôture tout seul quand tous les produits sont réceptionnés et qu'il ne reste aucun
composant chez le sous-traitant.

### Points forts

- En-tête comme un transfert de stock, avec propagation des magasins aux lignes et magasin du sous-traitant protégé
  après les mouvements.
- Lots et numéros de série choisis dans l'add-on : proposition à partir des lots de l'ordre chez le sous-traitant
  (traçabilité) et FEFO, modifiable à la main ; lot du produit en entrée par un script SQL configurable ; réception
  des produits en une seule transaction.
- Dossier Documents avec tous les documents liés, regroupés et faciles à ouvrir.
- Coûts des produits recalculés à chaque enregistrement ; commande d'achat alignée automatiquement.
- Ordres de sous-traitance depuis les ordres de fabrication, transfert en masse et entre ordres, clôture en masse des
  réceptions de marchandises.
- Même fonctionnement sous SQL Server et SAP HANA ; textes traduisibles.

## 2. Installation et menus

### Installation

- Le package `XEI.ContoLavoro.zip` s'importe dans l'Extension Manager de SAP Business One.
- Au premier démarrage, l'add-on crée les tables, les champs, l'objet (UDO) `XEI_CL_COMMESSA` et la recherche
  formatée du fournisseur sous-traitant sur le magasin. SAP demande de confirmer que *« la structure de la base de
  données a été modifiée »* : répondre et attendre la fin avant d'utiliser le client.

### Menus

**Modules › Gestion › Add-ons › XEI-Addon › Sous-traitance** :

| Entrée | Fonction |
|---|---|
| Ordre de sous-traitance | ouverture, recherche et création des ordres de sous-traitance |
| Créer des ordres depuis les ordres de fabrication | ordres de sous-traitance à partir des façons externes des ordres de fabrication (chapitre 6) |
| Réception du sous-traitant | un bon de livraison du sous-traitant avec des produits de plusieurs ordres : on choisit le fournisseur, on indique les quantités reçues sur les produits ouverts de ses ordres (*Proposer* = solde) et *Enregistrer* effectue la réception ordre par ordre, avec entrée des produits et sortie des composants |
| Transfert en masse des composants | envoi de composants pour plusieurs ordres (actif avec l'option correspondante) |
| Transfert de composants entre ordres | déplace le stock déjà chez le sous-traitant d'un ordre à un autre |
| Clôture en masse des réceptions de produits | clôture les réceptions de marchandises des produits restées ouvertes |
| Prix de façon des sous-traitants | prix des façons par fournisseur et produit |
| Configuration | options de l'add-on |
| Informazioni (Informations), Traduzioni (Traductions), Licenza (Licence) | entrées communes aux add-ons XEI ; Licenza : statut et code de licence |

Les mêmes entrées, sauf *Configuration*, *Informazioni*, *Traduzioni* et *Licenza*, se trouvent aussi dans le module
SAP choisi dans la configuration (chapitre 3), à la position choisie : **Modules › Achats - Fournisseurs ›
Sous-traitance** (par défaut) ou **Modules › Production › Sous-traitance**.

### Licence

L'add-on fonctionne avec un **code de licence** délivré par XEI. Après la demande d'essai, on reçoit par email un
**code d'essai**, valable 30 jours à compter de l'envoi dans n'importe quelle société ; pour l'achat, on envoie à XEI
les deux codes de la fenêtre **Licenza** (Licence) et on reçoit le code de licence.

- Sans code valide, l'add-on est **bloqué** : son menu ne contient plus que *Informazioni* (Informations) et
  *Licenza* (Licence), et au démarrage la fenêtre **Licenza** s'ouvre toute seule avec le statut et le motif.
- La fenêtre affiche le **code de la société** et le **code du serveur** : pour acheter la licence, avec *Copia*
  (Copier) on les envoie à [license@xeisrl.com](mailto:license@xeisrl.com).
- Un utilisateur SAP **superutilisateur** colle le code reçu dans *Inserisci un codice di licenza* (Saisissez un code
  de licence) et clique sur *Salva codice* (Enregistrer) : l'add-on est débloqué immédiatement, sans redémarrer SAP.
- Le code de licence est valable pour la société (base de données) ou pour le serveur des codes envoyés.
- La même fenêtre s'ouvre à tout moment depuis le menu *Licenza* : statut, échéance, numéro et portée de la licence.

## 3. Configuration

Les options se définissent dans un formulaire à onglets (l'onglet *Lots* est décrit au chapitre 7). Les options
valent pour toute la société ; les formulaires déjà ouverts les utilisent à leur réouverture.

![Prix](../../_img/contolavoro/11_config_prezzi.png)

*Prix*

![Stock](../../_img/contolavoro/12_config_magazzino.png)

*Stock*

| Option | Effet | Par défaut |
|---|---|---|
| **Général** | | |
| Commande d'achat d'origine | champ pour lier l'ordre de sous-traitance à la commande d'achat dont il découle | Non |
| Commande client d'origine | colonne commande client sur les lignes produit | Non |
| Produits sans nomenclature | autorise des produits sans nomenclature : on la compose à la main | Non |
| Clôturer la réception de marchandises du produit | après la réception des produits, la réception de marchandises du produit est clôturée (elle n'est pas facturée) | Non |
| Recalculer le prix de la réception produit | si le prix de façon change, met à jour la réception de marchandises du produit | Non |
| Offres fournisseur depuis les OF | lors de la création depuis les OF, lie les offres fournisseur | Non |
| Transfert en masse | active l'entrée de menu | Non |
| Nomenclature sous-traitant | affiche la colonne « Nomenclature sous-traitant » dans la nomenclature | Oui |
| Contrats fournisseur | prix de façon depuis les contrats (SQL Server uniquement) | Non |
| Liste de prix par défaut | liste de prix des coûts proposée sur les nouveaux ordres | – |
| Menu aussi dans le module SAP | module avec le sous-menu *Sous-traitance* : Achats - Fournisseurs ou Production | Achats - Fournisseurs |
| Position dans le menu du module | en bas, en haut ou après une entrée du module | en bas |
| **Prix** | | |
| Prix de façon / des composants modifiable | prix modifiables dans la nomenclature de l'ordre | Non |
| Prix de façon / du composant de la nomenclature | le prix de la nomenclature en priorité (composant : OF uniquement) | Non |
| Répartir le coût de façon | répartit le coût total sur les produits (depuis OF uniquement) | Non |
| Ne pas bloquer avec des prix à zéro | la réception des produits est autorisée même avec des prix à zéro | Non |
| Réévaluer les composants | réévaluation des composants à la sortie de production (inventaire permanent) | Non |
| **Stock** | | |
| Magasin par défaut de l'article | les lignes composant partent du magasin par défaut de l'article | Oui |
| Stock comme expédié | pour les composants indiqués, le stock chez le sous-traitant vaut comme expédié | Non |
| Composants par ligne | composants gardés séparés par produit | Non |
| Besoin variable | répartit la quantité expédiée sur les produits | Non |
| Demandes de transfert | envoi des composants par une demande de transfert de stock au lieu du transfert de stock | Non |
| Liste de prélèvement | crée aussi la liste de prélèvement (active les demandes) | Non |
| **Séries et motifs** | | |
| Séries | commande d'achat, réceptions de marchandises des produits et des façons, transferts | par défaut SAP |
| Motifs de transport | pour les transferts, la commande, la réception de marchandises, les sorties, les entrées (si la société utilise les motifs de transport) | – |
| **Lots** | | |
| Script du lot en entrée | SQL avec {ItemCode}, {WhsCode}, {DocEntry} qui renvoie le lot du produit réceptionné (voir chapitre 7) | ordre-numéro séquentiel |

## 4. L'ordre de sous-traitance

### En-tête

L'en-tête est organisé comme celui du transfert de stock : à gauche fournisseur, référence du fournisseur, projet et
commandes liées ; à droite numérotation, statut, dates, liste de prix des coûts et les deux magasins.

- **Fournisseur** : à la sélection, propose le magasin de l'utilisateur et le **magasin du sous-traitant** lié au
  fournisseur (champ *Fornitore terzista* (Fournisseur sous-traitant) des données de base du magasin) ou celui marqué
  par défaut.
- **Du magasin** : magasin de l'entreprise ; c'est d'ici que partent les composants, ici que reviennent les produits
  et sur ce magasin que naissent les lignes de la commande d'achat.
- **Mag. sous-trait.** : ne peut être modifié que tant que l'ordre n'a pas de mouvements de composants ; ensuite le
  champ est désactivé et l'enregistrement refuse de toute façon la modification.
- Si l'on change un magasin de l'en-tête, il est proposé, comme dans le transfert de stock, de le reporter sur les
  lignes de la nomenclature **pas encore mouvementées**.

### Produits

On choisit l'article (aussi plusieurs articles à la fois dans la liste) et la quantité à produire : la nomenclature
est copiée de SAP et ramenée à une pièce (en tenant compte de la quantité de base de la nomenclature). Les colonnes
affichent la quantité à produire, réceptionnée, le solde, le coût des composants et des façons.

### Nomenclature

Pour chaque produit : composants (articles en stock à expédier) et façons (services payés au sous-traitant). Avec
**Modifier la nomenclature**, on change les magasins et les prix des lignes pas encore mouvementées ; avec *Ajouter
une ligne* / *Supprimer la ligne* de SAP, on ajoute des composants et des façons ou on retire ceux qui ne sont pas
mouvementés. Depuis le menu contextuel de la ligne produit : **Retravailler** (le produit retourne au sous-traitant
comme composant avec les nouvelles façons) et **Recomposer la nomenclature** (remplace la nomenclature par les
composants choisis).

### Composants

Les composants de tous les produits regroupés par article et magasins : besoin, utilisé, disponible dans l'entreprise,
stock dans le magasin du sous-traitant, demandes et listes de prélèvement, expédié, solde à expédier, stock de l'ordre
chez le sous-traitant, retours et rebuts. Les mouvements se font avec les boutons en bas de l'ordre : **Envoyer les
composants** et **Retours et rebuts** (*Retour des composants du sous-traitant*, *Transférer les rebuts*, *Sortie des
rebuts chez le sous-traitant*). Chacun ouvre une fenêtre avec les quantités à mouvementer dans les cellules jaunes :
*Proposer* les remplit, *Remettre à 0* les vide, et on peut les modifier à la main.

### Documents

Tous les documents SAP liés à l'ordre, un par ligne par ordre chronologique, avec le lien pour les ouvrir ; *Afficher*
filtre par type de document. En dessous, dans *Lignes du document*, les lignes du document choisi avec lots, numéros
de série et emplacements.

## 5. Déroulement

1. **Ordre de sous-traitance** : fournisseur, magasins, produits et quantités ; *Ajouter*.
2. **Commande sous-traitant** : la fenêtre *Commande au sous-traitant* crée la commande d'achat, avec une ligne par
   produit et une pour chaque façon ; si la commande existe déjà, le bouton l'ouvre. Les modifications ultérieures de
   l'ordre (produits nouveaux ou supprimés, quantités, prix, dates) sont reportées sur la commande à l'enregistrement ;
   les lignes déjà réceptionnées ne changent qu'en quantité.
3. **Envoyer les composants** : dans la fenêtre *Transfert de composants*, la colonne *À expédier* propose le solde à
   expédier (modifiable à la main) ; *OK* crée le transfert de stock vers le magasin du sous-traitant. Avec l'option
   correspondante, une demande de transfert de stock avec liste de prélèvement est créée.
4. **Réceptionner les produits** : dans la fenêtre *Réception des produits*, la colonne *À réceptionner* propose le
   solde (modifiable à la main) et *Type de mouvement* permet de choisir entre *Entrée produits et sortie composants*,
   *Entrée produits uniquement* et *Sortie composants uniquement* ; puis *OK*. Sont créées : la réception de
   marchandises des façons et des produits depuis la commande d'achat, la sortie de marchandises des composants du
   magasin du sous-traitant, les réceptions de production pour les produits issus d'OF (chapitre 6).

> Le produit entre au coût complet (composants + façon) ; avec l'option « Clôturer la réception de marchandises du
> produit », la réception est clôturée et n'est pas facturée : on facture les façons.

Si un composant à sortir dépasse le stock de l'ordre chez le sous-traitant, l'add-on demande s'il faut sortir le stock
restant (Oui / Non / Oui pour tous).

## 6. Sous-traitance depuis les ordres de fabrication

Quand certaines phases d'un **ordre de fabrication (OF)** sont réalisées chez des sous-traitants, l'add-on crée les
ordres de sous-traitance à partir des lignes de l'OF. À chaque réception des produits, il sort pour l'OF les
composants consommés par le sous-traitant et, quand toutes les façons externes sont revenues, il enregistre la
réception de production du produit fini.

### Paramétrage dans SAP

> La façon externe est un **article non géré en stock** avec le champ **Conto lavoro** (Sous-traitance) = Oui, pas une
> ressource SAP : une façon définie comme ressource n'apparaît pas dans la liste des OF.

| Où | Ce que vous définissez | Dans l'exemple |
|---|---|---|
| Données article de l'article de la façon | article non géré en stock, champ utilisateur **Conto lavoro** (Sous-traitance) = Oui ; le **fournisseur préféré** est le sous-traitant proposé dans la liste | `LAV-SALD` Soudure du châssis, fournisseur `F-TER01` ; `LAV-MONT` Montage de l'essieu, fournisseur `F-TER02` |
| Nomenclature du produit fini | une ligne pour chaque façon externe, avec la quantité par pièce ; sur les lignes des composants à envoyer au sous-traitant, le champ **Lavorazione terzista** (Façon du sous-traitant) avec le code de la façon et la méthode de sortie **Manuelle** | `CMP-01`, `CMP-02` → `LAV-SALD` ; `CMP-03`, `CMP-04` → `LAV-MONT` |
| Nomenclature du produit fini | **Nomenclature sous-traitant** = Oui si le produit fini est complet quand toutes les façons externes sont revenues : l'add-on enregistre la réception de production. Avec Non, c'est vous qui enregistrez la réception de production dans SAP | `PF-100` = Oui |
| Données de base du magasin du sous-traitant | champ **Fornitore terzista** (Fournisseur sous-traitant) (chapitre 4) | `T-TER01` → `F-TER01` ; `T-TER02` → `F-TER02` |
| *Prix de façon des sous-traitants* | prix par sous-traitant, produit fini et façon (ordre de recherche du prix au chapitre 9) | `F-TER01` / `PF-100` / `LAV-SALD` 12,00 ; `F-TER02` / `PF-100` / `LAV-MONT` 3,50 |

Les composants en consommation automatique liés à la façon ne sont pas envoyés au sous-traitant : c'est la réception
de production qui les sort du magasin de la ligne de l'OF. La colonne **Motif / avertissements** de la liste le
signale. Les autres composants de la nomenclature, qui n'ont pas de façon, restent comme dans tout OF.

> **Contrôle à l'enregistrement de la nomenclature.** Quand vous enregistrez une nomenclature dont le champ
> **Lavorazione terzista** (Façon du sous-traitant) est renseigné, l'add-on contrôle les codes indiqués. Si quelque chose
> ne va pas, l'avertissement *« Nomenclature PF-100, champ "Lavorazione terzista" : »* apparaît avec un point pour
> chaque cas ; la nomenclature reste enregistrée.
>
> - Ressource : *« LAV-SALD est une ressource : la façon externe doit être créée comme article non géré en stock avec
>   "Conto lavoro" = Oui, et les composants doivent être liés à ce code. »*
> - Code qui n'est pas un article : *« LAV-SALD n'est pas un article. »*
> - Article sans Conto lavoro : *« L'article LAV-SALD n'a pas "Conto lavoro" = Oui dans les données de base. »*
> - Façon qui n'est pas une ligne de la nomenclature : *« LAV-SALD n'est pas une ligne de la nomenclature : l'OF
>   n'aura pas la ligne de la façon et l'ordre de sous-traitance ne pourra pas être créé. »*
> - Composants en consommation automatique : *« Composants en consommation automatique avec la façon LAV-SALD : ils
>   ne sont pas envoyés au sous-traitant (méthode de sortie manuelle nécessaire). »*

### Exemple pas à pas

Le produit fini `PF-100` Chariot a deux façons externes : la soudure du châssis chez `F-TER01` « Sous-traitant
Exemple 1 » et le montage des essieux chez `F-TER02` « Sous-traitant Exemple 2 ». Chaque chariot a un châssis et
deux essieux. L'OF n° 500 est lancé pour 100 chariots dans le magasin `01` :

| Ligne | Article | Quantité | Sortie | Lavorazione terzista | Prix |
|---|---|---|---|---|---|
| 1 | `LAV-SALD` Soudure du châssis (façon) | 100 | | | 12,00 |
| 2 | `CMP-01` Tube (m) | 250 | Manuelle | `LAV-SALD` | 4,00 |
| 3 | `CMP-02` Plaque | 400 | Manuelle | `LAV-SALD` | 1,50 |
| 4 | `LAV-MONT` Montage de l'essieu (façon) | 200 | | | 3,50 |
| 5 | `CMP-03` Roue | 400 | Manuelle | `LAV-MONT` | 5,00 |
| 6 | `CMP-04` Axe | 200 | Manuelle | `LAV-MONT` | 2,00 |
| 7 | `CMP-05` Vis | 1 600 | consommation automatique | | |

| Étape | Document SAP créé | Effet sur l'OF |
|---|---|---|
| 1. **Sous-traitance › Créer des ordres depuis les ordres de fabrication** : vous sélectionnez les deux lignes de l'OF 500 et cliquez sur *Créer les ordres* | aucun document SAP : ordre de sous-traitance 1001 (`F-TER01`, de `01` à `T-TER01`, produit `LAV-SALD` 100, nomenclature `CMP-01` 2,5 et `CMP-02` 4 par pièce) et ordre 1002 (`F-TER02`, de `01` à `T-TER02`, produit `LAV-MONT` 200, nomenclature `CMP-03` 2 et `CMP-04` 1 par pièce) | aucun |
| 2. Dans chaque ordre, cliquez sur *Commande sous-traitant* et confirmez la fenêtre *Commande au sous-traitant* | commande d'achat à `F-TER01` : `LAV-SALD` 100 × 12,00 ; commande d'achat à `F-TER02` : `LAV-MONT` 200 × 3,50 | aucun |
| 3. Dans chaque ordre, cliquez sur *Envoyer les composants* puis, avec les quantités proposées, sur *OK* | transfert de stock de `01` vers `T-TER01` : `CMP-01` 250, `CMP-02` 400 ; de `01` vers `T-TER02` : `CMP-03` 400, `CMP-04` 200 | aucun |
| 4. 60 châssis reviennent : dans l'ordre 1001, cliquez sur *Réceptionner les produits*, dans la fenêtre *Réception des produits* saisissez 60 dans *À réceptionner* et cliquez sur *OK* | réception de marchandises depuis la commande : `LAV-SALD` 60 × 12,00 ; sortie pour production de `T-TER01` : `CMP-01` 150, `CMP-02` 240 | composants des lignes 2 et 3 sortis ; pas de réception : les essieux manquent, et un message le dit (*« OF 500 : le produit fini entrera en stock lorsque la façon LAV-MONT sera également revenue. »*) |
| 5. 100 essieux reviennent : ordre 1002, *Réceptionner les produits*, 100 dans *À réceptionner*, *OK* | réception de marchandises `LAV-MONT` 100 × 3,50 ; sortie pour production de `T-TER02` : `CMP-03` 200, `CMP-04` 100 ; réception de production `PF-100` **50** | 60 châssis et 100 essieux suffisent pour 50 chariots : 50 terminés ; SAP sort en consommation automatique `CMP-05` 800 |
| 6. 100 autres essieux reviennent : ordre 1002, *Réceptionner les produits*, 100 dans *À réceptionner*, *OK* | réception de marchandises `LAV-MONT` 100 ; sortie pour production `CMP-03` 200, `CMP-04` 100 ; réception de production `PF-100` **10** | 60 terminés, les autres attendent les châssis (*« OF 500 : 10 pièces du produit fini entrées en stock ; les autres entreront lorsque la façon LAV-SALD sera également revenue. »*) ; l'ordre 1002 se clôture tout seul |
| 7. Les 40 derniers châssis reviennent : ordre 1001, *Réceptionner les produits*, 40 dans *À réceptionner*, *OK* | réception de marchandises `LAV-SALD` 40 ; sortie pour production `CMP-01` 100, `CMP-02` 160 ; réception de production `PF-100` **40** | 100 terminés ; l'ordre 1001 se clôture tout seul. C'est vous qui clôturez l'OF dans SAP |

> La réception de production vaut le coût des façons externes par pièce : pour chaque façon, composants et prix de la
> façon, multipliés par la quantité par pièce. Dans l'exemple, un chariot vaut
> (2,5 × 4,00 + 4 × 1,50 + 12,00) + 2 × (2 × 5,00 + 1 × 2,00 + 3,50) = 28,00 + 31,00 = **59,00**.

### Cas particuliers

- **Plusieurs OF** : les lignes avec le même fournisseur et le même magasin de retour (colonne *Mag. retour*) vont
  dans le même ordre, un produit par ligne ; avec des magasins de retour différents, des ordres différents sont créés.
- **Services du sous-traitant** : un composant non géré en stock avec **Lavorazione terzista** (Façon du sous-traitant)
  (par exemple un contrôle) devient une façon de l'ordre, avec une ligne de plus dans la commande au sous-traitant.
- **Nomenclature sous-traitant = Non** : l'add-on enregistre la réception de marchandises de la façon et la sortie des
  composants ; c'est vous qui enregistrez la réception de production dans SAP, par exemple après un montage interne.
- **Réceptions de production enregistrées dans SAP** sur le même OF : l'add-on les déduit, le produit fini n'entre
  pas deux fois.
- **Ordre interrompu** : si vous interrompez un ordre de sous-traitance, la façon revient dans la liste et vous pouvez
  en créer un autre.
- **Composants en consommation automatique** : les composants en consommation automatique liés à la façon ne sont pas
  envoyés au sous-traitant ; la colonne **Motif / avertissements** le signale.
- **Nomenclature de l'ordre** : pour les produits issus d'OF, elle ne se modifie pas ; vous changez le prix de la
  façon (colonne *Coût façon*), qui est reporté sur la commande au sous-traitant à l'enregistrement. Avec l'option
  *Répartir le coût de façon*, le *Coût façon total* de l'en-tête est réparti sur les produits au prorata de la
  quantité.
- L'option *Clôturer la réception de marchandises du produit* ne s'applique pas aux ordres issus d'OF : la réception
  de marchandises de la façon reste ouverte, à facturer.
- **Offres fournisseur** : avec l'option *Offres fournisseur depuis les OF*, *Offre fournisseur* lie à la ligne une
  ligne d'offre, avec son fournisseur, son prix et sa date de livraison ; les lignes d'offre non choisies sont
  clôturées.

### Pourquoi un OF n'apparaît pas dans la liste

La liste affiche les façons prêtes à devenir un ordre de sous-traitance. Activez **Afficher aussi les lignes non
prêtes** : les autres apparaissent aussi, avec le motif et ce qu'il faut faire dans la colonne **Motif /
avertissements**. Les lignes non prêtes ne se sélectionnent pas ; si vous cliquez sur leur case de sélection, le motif
apparaît aussi dans la barre d'état.

| Motif (exemple à l'écran) | Que faire |
|---|---|
| Déjà dans l'ordre de sous-traitance n° 1001. | rien : ouvrez l'ordre depuis la colonne *Ordre* |
| LAV-SALD est une ressource : la façon externe doit être créée comme article non géré en stock avec "Conto lavoro" = Oui, et les composants doivent être liés à ce code. | créez l'article de la façon et saisissez son code dans **Lavorazione terzista** (Façon du sous-traitant) sur les composants |
| Les composants indiquent la façon LAV-SALD, qui n'est pas un article. | corrigez **Lavorazione terzista** sur les composants ou créez l'article |
| L'article LAV-SALD n'a pas "Conto lavoro" = Oui dans les données de base. | mettez **Conto lavoro** (Sous-traitance) = Oui dans les données de l'article |
| L'OF n'a pas de ligne pour la façon LAV-SALD : l'ajouter à l'OF (ou à la nomenclature du produit). | ajoutez la ligne à l'OF, ou à la nomenclature pour les prochains OF |
| Aucun composant à envoyer : sur les lignes des composants indiquer "Lavorazione terzista" = LAV-SALD et la méthode de sortie manuelle. | renseignez les composants à envoyer, avec la méthode de sortie Manuelle |
| OF non lancé : le lancer dans SAP. | lancez l'OF |

Une façon définie comme ressource SAP est une cause fréquente : la façon externe doit être créée comme article non
géré en stock avec **Conto lavoro** (Sous-traitance) = Oui.

Sur les lignes prêtes, la même colonne donne les avertissements qui n'empêchent pas la sélection :

| Avertissement | Que faire |
|---|---|
| Composants en consommation automatique avec cette façon : ils ne sont pas envoyés au sous-traitant (méthode de sortie manuelle nécessaire). | s'ils doivent être envoyés, mettez la méthode de sortie Manuelle |
| Indiquer le fournisseur. | choisissez le fournisseur dans la colonne *Fournisseur* |
| Le fournisseur F-TER01 n'a aucun magasin de sous-traitant lié. | liez le magasin du sous-traitant au fournisseur (champ **Fornitore terzista** (Fournisseur sous-traitant)) : sans cela, l'ordre n'est pas créé |

## 7. Lots, numéros de série et emplacements

Pour les transferts, les retours, les rebuts et la sortie des composants lors de la réception des produits, les lots
et les numéros de série se choisissent dans une fenêtre de l'add-on, **avant** de créer les documents. Tous les
documents sont ensuite créés en une seule opération.

- **Proposition automatique** : depuis le magasin du sous-traitant (sortie des composants, retour, rebuts), d'abord
  les lots **expédiés à cet ordre** (colonne « De l'ordre », tirée du journal des mouvements de lots de SAP), puis par
  date d'expiration (FEFO) ; depuis le magasin de l'entreprise, par date d'expiration (FEFO).
- **Choix manuel** : la colonne « À utiliser » est modifiable ; la quantité est limitée au stock du lot (déduction
  faite des autres lignes sur le même lot) et à 1 pour les numéros de série. *Proposer* refait la proposition,
  *Remettre à 0* vide tout. La confirmation n'est possible que lorsque chaque ligne a exactement la quantité demandée.
- Seuls les lots et numéros de série **libérés** sont proposés (ni bloqués, ni non accessibles).
- Les demandes de transfert de stock ne mouvementent pas de lots : aucune sélection ne s'ouvre pour elles.

### Lot du produit en entrée

Le lot du produit réceptionné est calculé par un **script SQL** configurable (Configuration › Lots), avec trois
paramètres fixes : `{ItemCode}` article, `{WhsCode}` magasin de réception, `{DocEntry}` ordre de sous-traitance. Le
script par défaut renvoie le numéro de l'ordre + un numéro séquentiel (p. ex. `20160256-1`) ; *Vérifier* l'exécute
avec des données de test. Le lot créé apparaît dans le message de fin de réception.

![Script du lot en entrée](../../_img/contolavoro/19_config_lotti.png)

*Script du lot en entrée*

### Documents en brouillon

Le document est créé en brouillon, à compléter dans le formulaire SAP, avec des magasins à **emplacements**, des
produits en entrée avec **numéros de série**, un script du lot vide ou sans résultat et dans le transfert en masse. On
complète le document et on clique sur *Ajouter* : l'add-on supprime le brouillon et continue.

## 8. Retours et rebuts

- **Retours et rebuts › Retour des composants du sous-traitant** : quantité dans *À retourner* (*Proposer* = stock de
  l'ordre chez le sous-traitant), puis *OK* : transfert du magasin du sous-traitant vers le magasin de l'entreprise.
- **Retours et rebuts › Transférer les rebuts** : quantité dans *À rebuter* ; déplace les rebuts du sous-traitant
  vers un magasin au choix.
- **Retours et rebuts › Sortie des rebuts chez le sous-traitant** : dans la fenêtre *Sortie des rebuts*, sortie de
  marchandises des rebuts directement depuis le magasin du sous-traitant.

Les composants mis au rebut reviennent dans le solde à expédier.

## 9. Fonctions de service

### Ordres de sous-traitance depuis les ordres de fabrication

Liste les façons externes des OF lancés, prêtes à devenir un ordre de sous-traitance, et crée **un ordre par
fournisseur et magasin de retour**. Avec *Afficher aussi les lignes non prêtes*, explique pourquoi une façon n'est pas
prête. Paramétrage, exemple complet et cas particuliers au chapitre 6.

### Transfert en masse des composants

Analyse les ordres ouverts (filtres par dates, fournisseur, composant) et propose les composants ayant un solde à
expédier, en respectant la disponibilité partagée entre les ordres si la société bloque les stocks négatifs. Crée un
transfert par fournisseur (en brouillon si des lots ou des emplacements sont nécessaires). Les lignes dont le magasin
du sous-traitant manque ou est identique à celui de départ sont exclues et signalées.

### Transfert de composants entre ordres

Déplace le stock déjà chez le sous-traitant d'un ordre à un autre sans mouvement de stock (simple enregistrement).
C'est pourquoi il n'est possible qu'entre ordres **ouverts** ayant le **même magasin du sous-traitant** : la liste ne
propose que ceux-là ; avec des magasins différents, l'opération est bloquée et la marchandise doit être retournée puis
renvoyée. Le stock est relu au moment de la confirmation.

### Clôture en masse des réceptions de produits et prix de façon

*Clôture en masse des réceptions de produits* liste les réceptions de marchandises des produits encore ouvertes et
clôture celles qui sont choisies. *Prix de façon des sous-traitants* est la table des prix des façons par
sous-traitant et produit.

Ordre de recherche du prix d'une façon : contrats fournisseur (option, SQL Server uniquement), prix par sous-traitant,
nomenclature (option), prix fournisseur SAP, liste de prix de l'ordre.

## 10. Données, champs et types de mouvement

| Table | Contenu |
|---|---|
| `@XEI_CL_OCNT` | en-tête de l'ordre (UDO `XEI_CL_COMMESSA`, avec séries) |
| `@XEI_CL_CNT1` | produits |
| `@XEI_CL_CNT2` | nomenclature (composants et façons) |
| `@XEI_CL_PRZLAV` | prix des façons par sous-traitant et produit |
| `@XEI_CL_TRCOMM` | transferts entre ordres |

Champs sur les tables SAP (préfixe `XEI_CL_`) :

| Champ | Tables | Contenu |
|---|---|---|
| `U_XEI_CL_ENTRY` | lignes des documents | ordre de sous-traitance (DocEntry) |
| `U_XEI_CL_LINENUM` | lignes des documents | ligne produit ou de nomenclature |
| `U_XEI_CL_TYPE` | lignes des documents | type de mouvement (table ci-dessous) |
| `U_XEI_CL_TXT`, `U_XEI_CL_OPIT`, `U_XEI_CL_ITEM`, `U_XEI_CL_WKEY`, `U_XEI_CL_ENBL` | lignes des documents | texte, article et OF de référence, offres utilisables |
| `U_XEI_CL_ICNT` | articles | article en sous-traitance |
| `U_XEI_CL_TERZF`, `U_XEI_CL_DFTR` | magasins | fournisseur sous-traitant du magasin, magasin du sous-traitant par défaut |
| `U_XEI_CL_DISTTERZ` | nomenclatures | nomenclature sous-traitant (réception de production depuis OF) |
| `U_XEI_CL_ILAV` | lignes de nomenclature et d'OF | façon à laquelle appartient le composant |

Si la société les utilise, l'add-on renseigne aussi le code commercial, le motif de transport, le port et le
transporteur des documents.

| Type | Document | Signification |
|---|---|---|
| EMP | commande d'achat, réception de marchandises | produit |
| OAL | commande d'achat, réception de marchandises | façon |
| UMC | sortie de marchandises (sortie pour production si depuis OF) | composants consommés |
| TSO | transfert de stock ou demande | composants envoyés au sous-traitant |
| TSI | transfert de stock | retour des composants |
| TSS | transfert de stock | transfert des rebuts |
| UMR | sortie de marchandises | rebuts chez le sous-traitant |
| EPR | réception de production | produit fini de l'OF (chapitre 6) |

Les documents annulés sont exclus des calculs et les retours sont déduits ligne par ligne.

## 11. Langues

L'add-on suit la langue du client SAP. Sont disponibles l'**italien** (langue de base), l'**anglais**, l'**allemand**,
le **français**, l'**espagnol** et le **turc** : menus, formulaires, colonnes, boutons, messages et remarques des
documents créés. Avec une langue non prévue, l'italien est utilisé.

| Langue SAP | Textes de l'add-on | Commessa terzista | Terzista |
|---|---|---|---|
| Italian (Italy) | italien | Commessa terzista | terzista |
| English (United States / United Kingdom) | anglais | Subcontracting Job | subcontractor |
| German | allemand | Lohnfertigungsauftrag | Lohnfertiger |
| French | français | Ordre de sous-traitance | sous-traitant |
| Spanish (Spain / Latin America) | espagnol | Orden de subcontratación | subcontratista |
| Turkish | turc | Fason iş emri | fasoncu |

Les termes suivent ceux de SAP Business One dans la même langue (par exemple *Vendor*, *Posting Date*, *Inventory
Transfer*, *Bill of Materials*, *Batch* en anglais ; *Tedarikçi*, *Kayıt tarihi*, *Stok nakli*, *Ürün ağacı*,
*Parti* en turc).

### Changer de langue

1. **Gestion › Définition › Général › Utilisateurs**, onglet *Affichage*, champ *Langue*, puis *Actualiser*.
2. SAP avertit que toutes les fenêtres ouvertes seront fermées : répondre *Oui*.
3. L'add-on recharge tout seul les textes et recrée les menus dans la nouvelle langue : il n'est pas nécessaire de le
   redémarrer.

### Personnaliser les textes

Chaque texte peut être modifié pour un client donné depuis le menu **Traduzioni** (Traductions) de l'add-on ou avec
le clic droit sur les formulaires (*Modifica testo…* (Modifier le texte…), *Testi di questa form…* (Textes de ce
formulaire…)). L'autorisation `XEI_TEXTS` est nécessaire (les superutilisateurs l'ont toujours). Les personnalisations
sont conservées lors des mises à jour de l'add-on.

Les textes enregistrés dans la base de données par SAP restent en italien, par exemple les descriptions des champs
utilisateur et le titre de la table *Prezzi lavorazioni terzisti* (Prix de façon des sous-traitants). Les entrées
*Informazioni*, *Traduzioni* et *Licenza* du framework, avec leurs fenêtres, sont en italien dans toutes les langues.
