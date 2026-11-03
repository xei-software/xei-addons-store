---
title: XEI Rate Updater pour SAP Business One 1.0.0 – Notes de version
lang: fr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater pour SAP Business One 1.0.0 – Notes de version

## Fonctions de cette version

- **Taux de change dans SAP Business One** avec les taux de la Banque centrale européenne, de la Banque d'Italie ou
  d'Open Exchange Rates : pour les taux de change d'un jour, les taux publiés la veille s'appliquent.
- **Uniquement les devises de la société**, dans le sens de la société (taux direct ou indirect), tronquées à six
  décimales.
- **Monnaie locale autre que l'euro** : taux croisés par rapport à la monnaie locale.
- **Mise à jour manuelle** depuis la page Taux de change, avec le résultat de chaque devise.
- **Mise à jour automatique** chaque jour à l'heure choisie, ou depuis le Planificateur de tâches de Windows avec la
  commande `XEI.RateUpdater.exe aggiorna`.
- **Historique** des exécutions de chaque société, avec les taux et le résultat de chaque devise.
- **Licence XEI** libre, par serveur ou par société ; essai gratuit de 30 jours.
- **Langues du programme** : italien, anglais, allemand, français, espagnol et turc.

## Installation

- Programme pour Windows 10 et 11 et Windows Server 2016 et ultérieur, 64 bits : extrayez le dossier du zip et lancez
  `XEI.RateUpdater.exe` ; .NET est déjà inclus.
- Nécessite Microsoft Edge WebView2 Runtime, généralement déjà présent, et le Service Layer de SAP Business One 10.0
  ou ultérieure.
