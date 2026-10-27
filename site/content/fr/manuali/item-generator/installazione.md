---
title: XEI.ItemGenerator – Installation, licence, menus et autorisations
description: Comment installer XEI.ItemGenerator, activer la licence, trouver les menus et attribuer les autorisations.
lang: fr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator – Installation, licence, menus et autorisations

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Système | Microsoft .NET Framework 4.8 sur le poste du client SAP |
| Langues du programme | italien, anglais, allemand, français, espagnol |

## Installation

1. Téléchargez le package `XEI.ItemGenerator.zip`.
2. Dans SAP Business One, ouvrez l'**Extension Manager**, importez le package et affectez-le à la
   société.
3. Au premier démarrage, l'add-on crée lui-même les tables, les champs, les objets et les entrées
   des autorisations.
4. Une fois l'opération terminée, **redémarrez le client SAP une fois** : les fenêtres des bases et
   des variantes lisent les champs de l'add-on au démarrage de SAP.

Chaque mise à jour de l'add-on s'installe de la même manière, avec le même redémarrage.

## Licence

L'add-on fonctionne avec un **code de licence** délivré par XEI.

- **Essai** : après la demande d'essai, vous recevez par e-mail un **code d'essai**, valable 30 jours
  à compter de l'envoi dans n'importe quelle société.
- **Achat** : envoyez à XEI les deux codes de la fenêtre **Licence** et recevez le code de licence.

La fenêtre Licence :

- Sans code valide, l'add-on est **bloqué** : son menu ne contient plus que *Informations* et
  *Licence*, et la fenêtre **Licence** s'ouvre automatiquement au démarrage avec le statut et le
  motif.
- La fenêtre affiche le **code de la société** et le **code du serveur** : pour acheter la licence,
  envoyez-les avec *Copier* à [license@xeisrl.com](mailto:license@xeisrl.com).
- Un utilisateur SAP **superutilisateur** colle le code reçu dans *Saisir un code de licence* et
  clique sur *Enregistrer le code* : l'add-on est débloqué immédiatement, sans redémarrer SAP.
- Le code d'essai est valable dans n'importe quelle société. Le code de licence est valable pour la
  société (base de données) ou le serveur des codes envoyés.
- La même fenêtre s'ouvre à tout moment depuis le menu *Licence* : statut, échéance, numéro et
  périmètre de la licence.

![La fenêtre Licence avec l'add-on bloqué](../../_img/itemgenerator/27_licenza.png)

*La fenêtre Licence avec l'add-on bloqué : motif, codes de la société et du serveur, champ pour le
code.*

## Menus

Les entrées se trouvent dans **Modules › Gestion › Add-ons › XEI-Addon › Configurateur de codes**
et, à l'identique, dans **Stocks › Gestion des articles › Configurateur de codes**.

| Entrée | Fonction |
|---|---|
| 0. Paramètres | paramètres de l'add-on (manuel d'utilisation, chapitre 3) |
| 1. Définition des bases | bases et valeurs : l'arborescence du code (chapitre 5) |
| 2. Variantes et options | variantes avec leurs options (chapitre 4) |
| 3. Structures de variantes | groupes de variantes à demander pour une valeur (chapitre 4) |
| 4. Générer les articles | composition et création des articles (chapitre 9) |
| 5. Contrôle de cohérence | recalcul des compositions des articles générés (chapitre 14) |
| 6. Vérifier la configuration | contrôle de toute la configuration (chapitre 12) |
| 7. Import / export Excel | configuration dans un fichier Excel (chapitre 13) |
| Informations, Traductions, Licence | entrées communes aux add-ons XEI (uniquement sous XEI-Addon) ; Licence : statut et code de licence |

Par clic droit, vous disposez aussi de **Configurer l'article...** sur les lignes des offres de
vente et des commandes client (chapitre 10) et de **Générer des articles similaires...** dans les
données d'un article généré (chapitre 11).

## Autorisations

Dans **Gestion › Initialisation système › Autorisations › Autorisations générales**, l'add-on
ajoute la branche **Configuratore codici XEI**. Pour chaque entrée, vous pouvez attribuer
*Autorisation totale*, *Lecture seule* ou *Aucune autorisation*. Les superutilisateurs disposent
toujours d'un accès complet.

![La branche du configurateur dans les autorisations générales](../../_img/itemgenerator/23_autorizzazioni.png)

*La branche du configurateur dans les autorisations générales, pour un utilisateur sans
autorisations.*

| Entrée | Totale | Lecture seule |
|---|---|---|
| Definizione basi | modifier les bases | consulter |
| Definizione varianti | modifier les variantes | consulter |
| Strutture varianti | modifier les structures | consulter |
| Generazione articoli | créer des articles (également depuis les offres et les commandes) | composer la liste sans créer |
| Configurazione, verifica, import/export | enregistrer les paramètres, importer depuis Excel, contrôle de cohérence | voir les paramètres, vérifier, exporter |

Sans autorisation, l'entrée de menu affiche « Fonction non autorisée » dans la barre d'état.

## Assistance

Pour les licences : [license@xeisrl.com](mailto:license@xeisrl.com). Pour l'assistance :
[info@xeisrl.com](mailto:info@xeisrl.com). Dans votre demande, indiquez la version de l'add-on (menu
*Informations*) et une description du problème.
