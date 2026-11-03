---
title: XEI Rate Updater pour SAP Business One – Installation, premier démarrage, licence et mise à jour planifiée
description: Comment installer XEI Rate Updater pour SAP Business One, le connecter à SAP Business One, activer la licence et planifier la mise à jour quotidienne des taux de change.
lang: fr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater pour SAP Business One – Installation, premier démarrage, licence et mise à jour planifiée

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure, avec le Service Layer |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Système | Windows 10 et 11, Windows Server 2016 et ultérieur, 64 bits ; Microsoft Edge WebView2 Runtime |
| Réseau | accès à internet vers la source des taux choisie |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |

## Installation

1. Téléchargez le zip du programme depuis la page de téléchargement.
2. Extrayez le dossier du zip sur le PC, par exemple dans `C:\XEI\RateUpdater`.
3. Lancez **XEI.RateUpdater.exe**. Le programme contient déjà .NET. Il nécessite **Microsoft Edge WebView2 Runtime**,
   qui est généralement déjà présent : s'il manque, le programme le signale et propose de le télécharger.

Le programme ne s'installe pas. Les paramètres et l'historique se trouvent dans le dossier de données de Windows commun
à tous les utilisateurs du PC. Pour mettre à jour le programme, remplacez le dossier par le nouveau : les paramètres et
l'historique sont conservés.

## Premier démarrage

À la première ouverture, la page **Premier démarrage** s'ouvre, avec le code du premier démarrage déjà saisi.

1. **Connexion à SAP** : *Adresse du Service Layer* et *Sociétés SAP* ; puis **Tester la connexion**.
2. **Connexion et premier administrateur** :
   - *Connexion des opérateurs* : **Utilisateur SAP de chacun** ou **Utilisateurs propres et utilisateur SAP
     technique** ;
   - *Utilisateur SAP du premier administrateur* (par exemple `manager`) ;
   - *Utilisateur SAP technique* et mot de passe : ils servent à la mise à jour automatique. De préférence un
     utilisateur dédié, avec la seule autorisation d'écrire les taux de change.
3. **Enregistrer et redémarrer**.

Ensuite, ces mêmes paramètres se trouvent dans **Paramètres › SAP**. La source des taux et la mise à jour automatique
se trouvent dans **Paramètres › Taux de change**.

## Licence

Le programme fonctionne avec un **code de licence** délivré par XEI.

| Portée | Valable pour |
|---|---|
| Par société | une base de données SAP |
| Par serveur | toutes les sociétés de l'instance SQL Server ou SAP HANA |
| Libre | n'est pas liée à une base de données |

- **Essai** : 30 jours, libre.
- Menu **Licence** : statut, échéance et portée. Le code reçu de XEI se colle dans **Saisir un code de licence** et il
  est valable immédiatement, sans redémarrage.
- Pour une licence par société ou par serveur, le programme doit être connecté, en lecture seule, à la base de données
  de la licence (*Paramètres › Licence*, **Tester la connexion**) : là et dans la page Licence apparaissent les codes
  de la société et du serveur, à envoyer à [license@xeisrl.com](mailto:license@xeisrl.com).

## Mise à jour planifiée avec Windows

Ainsi, les taux de change se mettent à jour chaque jour, même avec le programme fermé.

1. Définissez l'**utilisateur SAP technique** (Paramètres › SAP).
2. Dans Windows, ouvrez le **Planificateur de tâches** et créez une tâche de base, par exemple tous les jours à 7:00.
3. Action **Démarrer un programme** : `XEI.RateUpdater.exe` dans le dossier du programme, avec l'argument `aggiorna`.
4. Dans les propriétés de la tâche, choisissez **Exécuter même si l'utilisateur n'est pas connecté**.

La commande met à jour les taux du jour et se ferme sans fenêtre ; l'exécution apparaît dans l'**Historique**. Avec
plusieurs sociétés, ajoutez `--societa <database SAP>`, une tâche par société. Résultat pour le Planificateur de
tâches : **0** réussie, **1** échouée ou avec une devise refusée, **2** arguments incorrects.

Sinon, avec le programme ouvert, il suffit d'activer la **Mise à jour automatique** dans *Paramètres › Taux de change*.

## Assistance

Pour les licences : [license@xeisrl.com](mailto:license@xeisrl.com). Pour l'assistance :
[info@xeisrl.com](mailto:info@xeisrl.com). Dans votre demande, indiquez la version du programme (menu *Informations*)
et une description du problème.
