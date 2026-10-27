---
title: XEI.CommissionManagement – Commissions des agents
description: Calcule et liquide dans SAP Business One les commissions des agents, chefs de zone, chefs de secteur et directeurs, des règles jusqu'au relevé de chaque agent.
lang: fr
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement

**Commissions des agents commerciaux dans SAP Business One.** Les pourcentages s'appliquent automatiquement aux lignes
des documents, l'add-on calcule les commissions, les liquide au fur et à mesure des paiements des clients et prépare le
relevé de chaque agent.

## Description

Calculer les commissions à la main ou sur des tableurs oblige à reprendre chaque mois factures, encaissements et
accords avec les agents, avec un risque d'erreurs et de relevés différents de ce que dit l'ERP.

Avec XEI.CommissionManagement, tout reste dans SAP Business One :

- chaque ligne de facture porte jusqu'à **quatre pourcentages** : agent, chef de zone, chef de secteur et directeur ;
- les pourcentages viennent des **règles** par client, groupe de clients, article, groupe d'articles, liste de prix,
  période et remise, ou des pourcentages par défaut de l'agent, et peuvent être corrigés à la main ;
- la commission se divise en une part **à la facturation** et des parts **à l'encaissement**, échéance par échéance
  ou sur le total du document ;
- la **liquidation** propose les parts encaissées et extourne celles des échéances redevenues impayées ;
- le **relevé** de chaque agent s'exporte en CSV, s'imprime en PDF ou s'envoie par e-mail.

## Fonctions principales

- **Agents et hiérarchie** : rôle, chef de zone, chef de secteur, directeur, pourcentages par défaut, part à la
  facturation et type de liquidation pour chaque employé de vente.
- **Règles de pourcentage** avec un ordre de recherche paramétrable, une remise minimale et une période de validité,
  exportables et importables en CSV.
- **Pourcentages sur les documents de vente** pendant la saisie, avec estimation de la commission à l'enregistrement
  et protection des lignes corrigées à la main.
- **Contrôle et affectation des %** : compare les pourcentages des documents aux règles et les corrige en bloc.
- **Calcul** sur les factures client, factures d'acompte et avoirs, aussi automatiquement à l'enregistrement de la
  facture.
- **Liquidation** des parts encaissées, aussi au prorata des encaissements partiels, avec période clôturée.
- **Ajustements**, **paliers et primes** sur le chiffre d'affaires annuel et **projets de factures** des agents.
- **Vérifications** des anomalies et **autorisations** dédiées dans les Autorisations générales de SAP.

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |
| Système | Microsoft .NET Framework 4.8 sur le poste du client SAP |
| Messagerie | serveur de messagerie SMTP accessible, uniquement pour envoyer les relevés aux agents par e-mail (Configuration › E-mail) |
| Installation | Extension Manager de SAP Business One |
| Licence | code de licence XEI, à saisir dans le menu **Licenza** (Licence) de l'add-on (essai gratuit de 30 jours) |

## Version actuelle

**1.1.1** – voir les [notes de version](../../manuali/fr/commissionmanagement/note-rilascio-1.1.1.md) et le
[manuel d'utilisation](../../manuali/fr/commissionmanagement/manuale-utente.md).
