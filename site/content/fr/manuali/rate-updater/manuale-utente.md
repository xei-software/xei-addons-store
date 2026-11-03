---
title: XEI Rate Updater pour SAP Business One – Manuel d'utilisation
description: "Taux de change dans SAP Business One : installation, premier démarrage, mise à jour manuelle et automatique, historique et licence."
lang: fr
prodotto: XEI.RateUpdater
versione: 1.0.0
stato: approvato
---

# XEI Rate Updater pour SAP Business One – Manuel d'utilisation

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure, avec le Service Layer |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Système | Windows 10 et 11, Windows Server 2016 et ultérieur, 64 bits ; Microsoft Edge WebView2 Runtime |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |

## 1. Ce que fait le programme

XEI Rate Updater pour SAP Business One met à jour les **taux de change** dans SAP Business One avec les taux publiés
par une source officielle :

1. il récupère les taux de la **source** choisie pour la date demandée ;
2. il lit dans la société SAP la **monnaie locale** et le **sens** des taux de change : taux direct (monnaie locale
   pour une unité de devise étrangère) ou taux indirect (devise étrangère pour une unité de monnaie locale) ;
3. si la monnaie locale n'est pas l'euro, il calcule les **taux croisés** par rapport à celle-ci ;
4. pour chaque **devise gérée par la société**, il écrit dans SAP le taux de change à la date, dans le sens de la
   société, tronqué à six décimales ;
5. il enregistre l'exécution dans l'**historique**.

Une erreur sur une devise n'arrête pas les autres.

### La date des taux

Les taux d'un jour sont publiés en fin de journée. Pour les taux de change d'un jour dans SAP, le programme utilise donc
les taux publiés **la veille**. Les jours sans publication (week-end, jours fériés), c'est le dernier jour publié
auparavant qui s'applique.

*Exemple* : les taux de change du lundi 24 février 2025 sont les taux du vendredi 21 février. La date des taux de change
ne peut pas être dans le futur.

### Les sources des taux

| Source | Remarques |
|---|---|
| Banque centrale européenne (BCE) | par défaut, gratuite, sans clé |
| Banque d'Italie | taux de change officiels italiens, nombreuses devises |
| Open Exchange Rates | nécessite une clé API Open Exchange Rates (Paramètres › Taux de change) |

Toutes les sources publient les taux par rapport à l'euro. Avec une monnaie locale autre que l'euro, la source doit la
coter.

### Les devises

Le programme reconnaît les devises à leur **code ISO** (par exemple `USD`, `CHF`). Dans SAP, les devises étrangères
doivent avoir le code ISO comme code. Pour la monnaie locale, si elle a un autre code dans SAP (par exemple « Eu » ou
« € » pour l'euro), indiquez le code ISO dans *Paramètres › Taux de change*.

## 2. Installation

1. Extrayez le dossier du zip sur le PC, par exemple dans `C:\XEI\RateUpdater`.
2. Lancez **XEI.RateUpdater.exe**. Le programme contient déjà .NET. Il nécessite **Microsoft Edge WebView2 Runtime**,
   qui est généralement déjà présent : s'il manque, le programme le signale et propose de le télécharger.

Le programme ne s'installe pas. Les paramètres et l'historique se trouvent dans le dossier de données de Windows commun
à tous les utilisateurs du PC : ils valent donc pour toute personne qui utilise le programme sur ce PC et pour la mise
à jour planifiée.

## 3. Premier démarrage

À la première ouverture, le programme affiche la page **Premier démarrage** : il n'est pas encore connecté à SAP. Le
code du premier démarrage est déjà saisi.

1. **Connexion à SAP** :
   - *Adresse du Service Layer* ;
   - *Sociétés SAP* : les bases de données que l'on peut choisir à la connexion ;
   - **Tester la connexion**.
2. **Connexion et premier administrateur** :
   - *Connexion des opérateurs* : **Utilisateur SAP de chacun** (chacun se connecte avec son propre utilisateur SAP)
     ou **Utilisateurs propres et utilisateur SAP technique** ;
   - *Utilisateur SAP du premier administrateur* (par exemple `manager`) ;
   - *Utilisateur SAP technique* et son mot de passe : ils servent à la **mise à jour automatique**. De préférence un
     utilisateur dédié, avec la seule autorisation d'écrire les taux de change.
3. **Enregistrer et redémarrer** : le programme se rouvre sur la page de connexion.

Ces mêmes paramètres se modifient ensuite dans **Paramètres › SAP**.

![Premier démarrage](../../_img/rateupdater/00b-primo-avvio.png)

*Premier démarrage : connexion à SAP, portée de la licence et premier administrateur.*

![Paramètres › SAP](../../_img/rateupdater/05-impostazioni-sap.png)

*Paramètres › SAP : adresse du Service Layer, sociétés et connexion des opérateurs.*

## 4. Connexion

Vous vous connectez avec votre **utilisateur SAP Business One** et son mot de passe. L'utilisateur et la société
s'affichent en haut à droite.

![Connexion](../../_img/rateupdater/00-accesso.png)

*Connexion avec l'utilisateur SAP Business One.*

Avec *Utilisateur SAP de chacun*, le programme écrit les taux de change avec l'utilisateur de la personne qui travaille :
ses autorisations SAP sur les taux de change s'appliquent.

### Fonctions des utilisateurs

Un administrateur attribue les fonctions à chaque utilisateur depuis la page **Utilisateurs** du menu, identique pour
les utilisateurs SAP et pour les utilisateurs propres :

| Fonction | Ce qu'elle permet |
|---|---|
| Mise à jour des taux | mettre à jour les taux de change dans SAP depuis la page Taux de change |
| Historique | consulter les exécutions de la mise à jour, manuelles et automatiques |

L'administrateur dispose de toutes les fonctions. Le premier administrateur est l'utilisateur SAP indiqué lors du
Premier démarrage.

## 5. Taux de change

Menu **Taux de change**.

1. **Date des taux de change dans SAP** : par défaut, la date du jour ; elle ne peut pas être dans le futur. En dessous
   figurent les taux utilisés et la source définie.
2. Cliquez sur **Mettre à jour les taux dans SAP**.
3. Le **résultat** indique la date, la source, le jour des taux, le nombre de devises écrites et la monnaie locale. Le
   tableau affiche pour chaque devise de la source :

| Colonne | Contenu |
|---|---|
| Devise | code ISO |
| Taux direct | monnaie locale pour une unité de devise étrangère |
| Taux indirect | devise étrangère pour une unité de monnaie locale |
| Résultat | **écrite dans SAP**, **non gérée** (la société n'utilise pas cette devise) ou refusée, avec l'erreur de SAP |

En dessous figure l'état de la **mise à jour automatique**, avec la dernière exécution.

![Taux de change](../../_img/rateupdater/01-cambi.png)

*Taux de change : date, source et état de la mise à jour automatique.*

![Résultat de la mise à jour](../../_img/rateupdater/02-cambi-esito.png)

*Résultat : taux de la source, devises écrites dans SAP et devises que la société ne gère pas.*

## 6. Historique

Menu **Historique** : les exécutions de la société, de la plus récente à la plus ancienne.

| Colonne | Contenu |
|---|---|
| Démarrée | date et heure de l'exécution |
| Par | l'utilisateur, ou *automatique* |
| Taux au | la date des taux de change dans SAP |
| Source | la source des taux |
| Taux publiés le | le jour des taux utilisés |
| Devises écrites | le nombre de devises écrites dans SAP |
| Résultat | **réussie** ou **échouée** |

Une ligne s'ouvre sur les devises, avec les taux et le résultat de chacune. L'historique conserve les dernières
exécutions (100 par défaut, dans *Paramètres › Taux de change*).

![Historique](../../_img/rateupdater/03-storico.png)

*Historique : mises à jour manuelles et automatiques de la société.*

![Historique avec les devises](../../_img/rateupdater/03b-storico-valute.png)

*Une ligne ouverte : taux et résultat de chaque devise.*

## 7. Paramètres › Taux de change

Réservé aux administrateurs. Après les modifications, cliquez sur **Enregistrer les paramètres**.

| Paramètre | Effet |
|---|---|
| Source des taux | Banque centrale européenne (par défaut), Banque d'Italie ou Open Exchange Rates |
| Code ISO de la monnaie locale | seulement si dans SAP la monnaie locale a un code différent du code ISO ; vide = pris dans SAP |
| Clé API Open Exchange Rates | seulement avec la source Open Exchange Rates ; enregistrée chiffrée |
| Mise à jour automatique | chaque jour, le programme met à jour tout seul les taux du jour de chaque société, avec l'utilisateur SAP technique |
| Heure de la mise à jour automatique | au format HH:mm (par défaut 07:00) |
| Exécutions dans l'historique | nombre d'exécutions à conserver pour chaque société, de 10 à 1000 (100 par défaut) |

![Paramètres › Taux de change](../../_img/rateupdater/04-impostazioni-cambi.png)

*Paramètres › Taux de change : source, monnaie locale, mise à jour automatique et historique.*

## 8. Mise à jour automatique

Les taux du jour se mettent à jour chaque jour de deux manières.

### Avec le programme ouvert

Lorsque la **Mise à jour automatique** est activée, une fois l'heure définie passée, le programme met à jour les taux du
jour de chaque société avec l'utilisateur SAP technique et enregistre l'exécution dans l'historique (*Par* :
automatique). Si le programme était fermé à l'heure prévue, il fait la mise à jour dès sa réouverture. Si la source ou
SAP ne répondent pas, il réessaie peu après.

### Avec le Planificateur de tâches de Windows

Ainsi, les taux se mettent à jour même sans ouvrir le programme.

1. Effectuez le premier démarrage et définissez l'**utilisateur SAP technique** (Paramètres › SAP).

   ![Utilisateur SAP technique](../../_img/rateupdater/05b-impostazioni-sap-tecnico.png)

   *L'utilisateur SAP technique dans Paramètres › SAP.*

2. Dans Windows, ouvrez le **Planificateur de tâches** et créez une tâche de base, par exemple tous les jours à 7:00.
3. Comme action, choisissez **Démarrer un programme** :
   - programme : `XEI.RateUpdater.exe` dans le dossier du programme ;
   - arguments : `aggiorna`.
4. Dans les propriétés de la tâche, choisissez **Exécuter même si l'utilisateur n'est pas connecté**, avec un
   utilisateur Windows du PC.

La commande met à jour les taux du jour avec l'utilisateur SAP technique et se ferme, sans fenêtre. Elle utilise les
mêmes paramètres et le même historique que le programme. Arguments facultatifs :

| Argument | Signification |
|---|---|
| `--societa <database SAP>` | la société à mettre à jour ; inutile avec une seule société configurée |
| `--data aaaa-mm-gg` | la date des taux de change, si ce n'est pas la date du jour |

Le Planificateur de tâches reçoit le résultat : **0** réussie, **1** échouée ou avec une devise refusée, **2**
arguments incorrects. Le détail figure dans l'historique. Si la commande a déjà mis à jour les taux du jour, le
programme ouvert ne refait pas la mise à jour.

## 9. Licence

Le programme fonctionne avec un **code de licence** délivré par XEI, selon trois portées :

| Portée | Valable pour |
|---|---|
| Par société | une base de données SAP |
| Par serveur | toutes les sociétés de l'instance SQL Server ou SAP HANA |
| Libre | n'est pas liée à une base de données |

L'**essai gratuit** dure 30 jours et il est libre.

![Licence](../../_img/rateupdater/06-licenza.png)

*La page Licence : statut, échéance, portée et champ pour le code.*

![Paramètres › Licence](../../_img/rateupdater/06b-impostazioni-licenza.png)

*Paramètres › Licence : les trois portées de la licence.*

Menu **Licence** : statut, échéance et portée de la licence. Le code reçu de XEI se colle dans **Saisir un code de
licence** et il est valable immédiatement, sans redémarrage. Pour une licence par société ou par serveur, le programme
doit être connecté, en lecture seule, à la base de données de la licence (*Paramètres › Licence*, **Tester la
connexion**) : les codes de la société et du serveur à envoyer à XEI apparaissent là et dans la page Licence.

Pour les licences : [license@xeisrl.com](mailto:license@xeisrl.com).

## 10. Questions fréquentes et problèmes

| Ce que vous voyez | Pourquoi | Que faire |
|---|---|---|
| Une devise est *non gérée* | La société SAP n'utilise pas cette devise | Rien : seules les devises de la société sont écrites |
| Une devise de la société n'est pas mise à jour | Dans SAP, la devise n'a pas le code ISO comme code | Utilisez le code ISO dans SAP (par exemple `USD`) |
| L'exécution s'arrête aussitôt avec une erreur sur la monnaie locale | La source ne cote pas la monnaie locale, ou elle a un code non ISO dans SAP | Indiquez le code ISO dans *Paramètres › Taux de change* ou choisissez une autre source |
| Le résultat d'une devise est une erreur de SAP | SAP a refusé le taux de change (par exemple à cause des autorisations de l'utilisateur) | Lisez l'erreur ; vérifiez les autorisations SAP de l'utilisateur sur les taux de change |
| La mise à jour automatique ne démarre pas | Elle est désactivée, ou l'utilisateur SAP technique manque | Activez-la dans *Paramètres › Taux de change* et définissez l'utilisateur technique dans *Paramètres › SAP* |
| Le programme demande d'installer WebView2 | Microsoft Edge WebView2 Runtime manque | Acceptez le téléchargement proposé, ou installez-le depuis le site de Microsoft |

## 11. Assistance

Pour les licences : [license@xeisrl.com](mailto:license@xeisrl.com). Pour l'assistance :
[info@xeisrl.com](mailto:info@xeisrl.com). Dans votre demande, indiquez la version du programme (menu *Informations*)
et une description du problème.
