---
title: XEI.ContoLavoro – Installation, licence et menus
description: Comment installer XEI.ContoLavoro, activer la licence et trouver les menus.
lang: fr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro – Installation, licence et menus

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Système | Microsoft .NET Framework 4.8 sur le poste du client SAP |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |

## Installation

1. Téléchargez le package `XEI.ContoLavoro.zip`.
2. Dans SAP Business One, ouvrez l'**Extension Manager**, importez le package et affectez-le à la société.
3. Au premier démarrage, l'add-on crée les tables, les champs, l'objet de l'ordre de sous-traitance et la recherche
   formatée du fournisseur sous-traitant sur le magasin. SAP affiche le message de modification de la structure de la
   base de données : répondez **Oui** et attendez la fin avant d'utiliser le client.

Chaque mise à jour de l'add-on s'installe de la même façon.

Après l'installation : remplissez la **Configuration**, puis dans SAP associez à chaque magasin du sous-traitant son
fournisseur (champ *Fornitore terzista* (Fournisseur sous-traitant) de la fiche du magasin) et marquez les articles en
sous-traitance (manuel d'utilisation, chapitres 3 et 6).

## Licence

L'add-on fonctionne avec un **code de licence** délivré par XEI.

- **Essai** : après la demande d'essai, vous recevez par e-mail un **code d'essai**, valable 30 jours à compter de
  l'envoi dans n'importe quelle société.
- **Achat** : envoyez à XEI les deux codes de la fenêtre **Licenza** (Licence) et recevez le code de licence.

La fenêtre **Licenza** (Licence) :

- Sans code valide, l'add-on est **bloqué** : son menu ne contient plus que *Informazioni* (Informations) et
  *Licenza* (Licence), et la fenêtre **Licenza** s'ouvre automatiquement au démarrage avec le statut et le motif.
- La fenêtre affiche le **code de la société** et le **code du serveur** : pour acheter la licence, envoyez-les avec
  *Copia* (Copier) à [license@xeisrl.com](mailto:license@xeisrl.com).
- Un utilisateur SAP **super-utilisateur** colle le code reçu dans *Inserisci un codice di licenza* (Saisir un code
  de licence) et clique sur *Salva codice* (Enregistrer le code) : l'add-on est débloqué immédiatement, sans
  redémarrer SAP.
- Le code d'essai est valable dans n'importe quelle société. Le code de licence est valable pour la société (base de
  données) ou le serveur des codes envoyés.
- La même fenêtre s'ouvre à tout moment depuis le menu *Licenza* : statut, échéance, numéro et périmètre de la
  licence.

## Menus

Les entrées se trouvent dans **XEI-Addon › Sous-traitance**. Le sous-menu **Sous-traitance** apparaît aussi dans le
module SAP choisi dans la Configuration (*Achats - Fournisseurs* ou *Production*).

| Entrée | Fonction |
|---|---|
| Ordre de sous-traitance | ouverture, recherche et création des ordres de sous-traitance (manuel d'utilisation, chapitres 4 et 5) |
| Créer des ordres depuis les ordres de fabrication | ordres de sous-traitance à partir des façons externes des ordres de fabrication (chapitre 6) |
| Réception du sous-traitant | réception des produits d'un bon de livraison du sous-traitant sur plusieurs ordres de sous-traitance (entrée des produits et sortie des composants) |
| Transfert en masse des composants | envoi des composants pour plusieurs ordres de sous-traitance, si activé dans la Configuration (chapitre 9) |
| Transfert de composants entre ordres | déplace le stock déjà chez le sous-traitant d'un ordre de sous-traitance à un autre (chapitre 9) |
| Clôture en masse des réceptions de produits | clôture les réceptions de marchandises des produits restées ouvertes (chapitre 9) |
| Prix de façon des sous-traitants | prix des façons par sous-traitant et produit (chapitre 9) |
| Configuration | options de l'add-on (chapitre 3) |
| Informazioni (Informations), Traduzioni (Traductions), Licenza (Licence) | entrées communes des add-ons XEI ; Licenza : statut et code de licence |
