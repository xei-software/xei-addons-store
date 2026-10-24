---
title: XEI.ItemGenerator 1.4.0 – Notes de version
lang: fr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator 1.4.0 – Notes de version

## Nouveautés

- **Héritage des variantes sous forme de proposition.** Avec *Hériter variantes*, les
  options choisies à un niveau précédent sont proposées, mais elles peuvent être
  modifiées au niveau qui en hérite. Le clic droit propose **Revenir aux options
  proposées**.
- **Forcer l'héritage.** Nouvelle option sur les valeurs des bases : elle impose le choix
  du niveau précédent, qui ne peut pas être modifié sur la valeur.
- **Table et champ utilisateur sur les variantes.** Dans *Variantes et options*, on peut
  indiquer une table utilisateur et un champ utilisateur article : à la création des
  articles, les options choisies sont ajoutées à la table et reportées dans le champ.
- **Fenêtre Générer les articles plus lisible.** Le panneau des variantes n'affiche que
  les variantes de la valeur sélectionnée dans l'arborescence ; une case à cocher active
  la vue complète par niveau.
- **Liste des articles à générer.** Nouveau paramètre *Ajouter à la liste vide d'abord la
  liste des articles à générer* (activé par défaut) : la liste ne contient que la
  dernière sélection. S'il est désactivé, les articles s'accumulent.
- **Menus numérotés.** Les entrées du Configurateur de codes sont numérotées de 0 à 7
  dans l'ordre de travail : Paramètres, Définition des bases, Variantes et options,
  Structures de variantes, Générer les articles, Contrôle de cohérence, Vérifier la
  configuration, Import / export Excel.
- **Sous-niveau avec liste de choix.** Dans *Définition des bases*, la colonne
  Sous-niveau se remplit à l'aide de la liste de choix des bases et la flèche ouvre la
  base liée. Un code saisi à la main est refusé si la base n'existe pas.

## Améliorations

- Vérification de la configuration et import / export Excel mis à jour avec les nouveaux
  champs.
- En-têtes des fenêtres plus compacts, alignés sur le style de SAP Business One.
- Traductions mises à jour en anglais, allemand, français et espagnol.

## Mise à jour

- Nécessite XEICore 1.1.1, inclus dans le package.
- Au premier démarrage, l'add-on met à jour lui-même la structure des données (version 3).
- Le code de licence déjà saisi reste valable.
