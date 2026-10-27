---
title: XEI.CommissionManagement – Installation, licence, menus et autorisations
description: Comment installer XEI.CommissionManagement, activer la licence, trouver les menus et attribuer les autorisations.
lang: fr
prodotto: XEI.CommissionManagement
versione: 1.1.0
stato: approvato
---

# XEI.CommissionManagement – Installation, licence, menus et autorisations

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Système | Microsoft .NET Framework 4.8 sur le poste du client SAP |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |
| Messagerie | serveur de messagerie SMTP accessible, uniquement pour envoyer les relevés aux agents par e-mail (Configuration › E-mail) |

## Installation

1. Téléchargez le package `XEI.CommissionManagement.zip`.
2. Dans SAP Business One, ouvrez l'**Extension Manager**, importez le package et affectez-le à la société.
3. Au premier démarrage, l'add-on crée les champs, les tables, les index et les autorisations. La création des champs
   sur les lignes des documents demande **quelques minutes** : SAP affiche plusieurs fois le message de modification
   de la structure de la base de données, qui ferme toutes les fenêtres ouvertes et demande s'il faut continuer :
   répondez **Oui**.

Chaque mise à jour de l'add-on s'installe de la même façon.

Après l'installation : remplissez la **Configuration**, puis les **Agents** (rôles, supérieurs, pourcentages), puis
les **Règles**. Ce n'est qu'à partir de ce moment que les documents reçoivent les pourcentages. Aux utilisateurs qui
ne sont pas super-utilisateurs, il faut attribuer les **autorisations** (voir plus bas).

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

Les entrées se trouvent dans **XEI-Addon › Commissions**.

| Entrée | Fonction |
|---|---|
| Configuration | options (six onglets) et ordre de recherche des règles (manuel d'utilisation, chapitre 5) |
| Agents | rôle, supérieurs, % par défaut, % à la facturation, liquidation, fournisseur, utilisateur SAP (chapitre 6) |
| Règles de pourcentage | % par client, groupe de clients, article, groupe d'articles, liste de prix (chapitre 7) |
| Paliers et primes | primes sur le CA annuel, si activées dans Configuration (chapitre 15) |
| Contrôle et affectation % | comparaison des documents avec les règles et correction en bloc (chapitre 9) |
| Calcul des commissions | calcul sur factures, factures d'acompte et avoirs (chapitre 10) |
| Commissions calculées | consultation, correction, recalcul, suppression (chapitre 11) |
| Liquidation | parts encaissées à liquider, impayés à extourner (chapitre 12) |
| Régularisations | montants manuels par agent et par mois, brouillons des factures des agents (chapitre 13) |
| Relevé des commissions | calculées, à liquider, liquidées et régularisations ; CSV, impression/PDF, e-mail (chapitre 14) |
| Contrôles | anomalies à vérifier (chapitre 16) |
| Informazioni (Informations), Traduzioni (Traductions), Licenza (Licence) | entrées communes des add-ons XEI ; Licenza : statut et code de licence |

## Autorisations

Dans les **Autorisations générales** de SAP (Gestion › Initialisation système › Autorisations), l'add-on crée l'entrée
**Provvigioni** (Commissions) sous *Autorisations utilisateur*, avec cinq sous-entrées. Les super-utilisateurs ont
toujours tout ; aux autres utilisateurs, on attribue pour chaque entrée *Aucune autorisation*, *Lecture seule* ou
*Autorisation complète*.

![Autorisations générales](../../_img/commissionmanagement/autorizzazioni.png)

*Autorisations générales : l'entrée Provvigioni (Commissions) avec les cinq sous-entrées, pour un utilisateur sans
autorisation.*

| Autorisation | Lecture seule | Complète |
|---|---|---|
| Configurazione (Configuration) | – | ouvrir et enregistrer la Configuration |
| Agenti, regole e scaglioni (Agents, règles et paliers) | consulter | enregistrer agents, règles et paliers |
| Controllo, calcolo e verifiche (Contrôle, calcul et vérifications) | consulter Contrôle, Calcul, Commissions calculées, Contrôles | appliquer les %, calculer, recalculer, enregistrer les parts, supprimer |
| Liquidazione, conguagli e bozze fatture (Liquidation, régularisations et brouillons factures) | consulter Liquidation et Régularisations | confirmer les liquidations, enregistrer les régularisations, enregistrer les primes, générer les brouillons |
| Estratto di tutti gli agenti (Relevé de tous les agents) | voir le relevé de tous les agents (sans : seulement les siens) | aussi l'envoi par e-mail |

Sans autorisation, l'entrée de menu répond dans la barre d'état *« Fonction non autorisée : il faut l'autorisation
« … » (Autorisations générales > Provvigioni) »* ; avec la lecture seule, la fenêtre s'ouvre, mais les boutons qui
modifient répondent *« Opération non autorisée : il faut l'autorisation complète sur « … » »*.

## Assistance

Pour les licences : [license@xeisrl.com](mailto:license@xeisrl.com). Pour l'assistance :
[info@xeisrl.com](mailto:info@xeisrl.com). Dans votre demande, indiquez la version de l'add-on (menu
*Informazioni*) et une description du problème.
