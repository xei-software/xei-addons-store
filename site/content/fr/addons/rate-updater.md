---
title: XEI Rate Updater pour SAP Business One – Taux de change
description: Met à jour chaque jour les taux de change dans SAP Business One avec les taux officiels de la BCE, de la Banque d'Italie ou d'Open Exchange Rates.
lang: fr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater pour SAP Business One

**Les taux de change dans SAP Business One, mis à jour automatiquement.** Chaque jour, le programme récupère les taux
d'une source officielle et les écrit dans SAP Business One, dans le sens et avec les décimales qu'utilise SAP.

## Description

Mettre à jour les taux de change à la main, c'est copier chaque matin les taux d'un site dans la table des taux de
change de SAP, devise par devise, avec le risque d'oublier un jour ou d'inverser un taux.

XEI Rate Updater pour SAP Business One le fait à votre place :

- il récupère les taux de la **Banque centrale européenne**, de la **Banque d'Italie** ou d'**Open Exchange Rates** ;
- pour les taux de change d'un jour, il utilise les taux publiés **la veille** ; le week-end et les jours fériés, il
  utilise le dernier jour publié ;
- il n'écrit dans SAP que les **devises gérées par la société**, dans le sens qu'utilise la société (taux direct ou
  indirect), tronquées à six décimales ;
- avec une **monnaie locale autre que l'euro**, il calcule les taux croisés par rapport à celle-ci ;
- il s'utilise **manuellement**, en choisissant la date, ou **chaque jour automatiquement** ;
- il conserve l'**historique** de chaque mise à jour : qui l'a faite, la source, les taux et le résultat de chaque
  devise.

## Fonctions principales

- **Taux de change** : date des taux de change, source et bouton *Mettre à jour les taux dans SAP* ; le résultat
  affiche pour chaque devise le taux direct, le taux indirect et si elle a été écrite dans SAP.
- **Historique** : les exécutions de la société, de la plus récente à la plus ancienne ; chaque ligne s'ouvre sur les
  devises.
- **Mise à jour automatique** : chaque jour à l'heure choisie, ou depuis le Planificateur de tâches de Windows.
- **Erreurs sous contrôle** : une erreur sur une devise n'arrête pas les autres ; chaque exécution indique ce qui n'a
  pas fonctionné.
- **Connexion avec l'utilisateur SAP** de chacun, avec ses autorisations sur les taux de change ; l'administrateur
  attribue à chaque utilisateur les fonctions *Mise à jour des taux* et *Historique*.

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure, avec le Service Layer |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Système | Windows 10 et 11, Windows Server 2016 et ultérieur, 64 bits ; Microsoft Edge WebView2 Runtime |
| Réseau | accès à internet vers la source des taux choisie (BCE, Banque d'Italie ou Open Exchange Rates avec sa clé API) |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |
| Installation | on extrait le dossier du programme, sans installation ; .NET est déjà inclus |
| Licence | code de licence XEI, libre, par serveur ou par société (essai gratuit de 30 jours) |

## Version actuelle

**1.0.0** – voir les [notes de version](../../manuali/fr/rateupdater/note-rilascio-1.0.0.md) et le
[manuel d'utilisation](../../manuali/fr/rateupdater/manuale-utente.md).
