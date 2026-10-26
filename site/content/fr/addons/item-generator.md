---
title: XEI.ItemGenerator – Configurateur de codes article
description: Créez dans SAP Business One des articles avec code, descriptions, données, prix et nomenclature composés selon vos propres règles.
lang: fr
prodotto: XEI.ItemGenerator
versione: 1.4.0
stato: approvato
---

# XEI.ItemGenerator

**Configurateur de codes article pour SAP Business One.** Choisissez les
caractéristiques du produit et l'add-on crée l'article dans les données article avec
code, descriptions, données, prix et nomenclature déjà renseignés.

## Description

Les entreprises qui vendent des produits en de nombreuses combinaisons (dimensions,
finitions, couleurs, accessoires) perdent du temps à créer à la main un article par
combinaison et risquent d'avoir des codes et des descriptions différents pour un même
produit.

Avec XEI.ItemGenerator, vous définissez les règles une seule fois et l'add-on compose
les articles :

- le **code** naît des valeurs choisies niveau par niveau (par exemple
  `PE` élément haut → `MU` mural → `070` hauteur 70 cm = `PEMU070`), plus un numéro
  séquentiel qui distingue les variantes ;
- les **variantes** (par exemple couleur ou finition) ont leurs options, qui peuvent
  être héritées des niveaux précédents ;
- **descriptions, groupes, unités de mesure, propriétés, dimensions, poids et prix**
  de l'article sont déduits des valeurs et des options choisies ;
- la **nomenclature** est composée avec les composants de chaque valeur et option.

Si une combinaison existe déjà, l'add-on retrouve l'article existant au lieu d'en créer
un doublon.

## Fonctions principales

- **Définition des bases, variantes et structures** avec les données de base de l'add-on
  dans SAP.
- **Génération des articles** dans une fenêtre redimensionnable, avec l'arborescence des
  codes et celle des variantes ; SAP reste utilisable pendant que la fenêtre est ouverte.
- **Configurer l'article depuis les offres de vente et les commandes client** : clic
  droit sur la ligne du document, composition de l'article et insertion dans la ligne.
- **Générer des articles similaires** depuis les données d'un article déjà généré : il
  suffit de changer une option.
- **Formule de description** pour composer la description, la description étendue et le
  nom étranger.
- **Vérification de la configuration**, avec la liste des erreurs et l'ouverture directe
  de la donnée à corriger.
- **Import et export Excel** de la configuration, également pour la copier dans une
  autre société.
- **Autorisations** dédiées dans les Autorisations générales de SAP.
- **Miniature de l'image** de l'article dans les données article.

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Langues du programme | italien, anglais, allemand, français, espagnol |
| Système | Microsoft .NET Framework 4.8 sur le poste du client SAP |
| Installation | Extension Manager de SAP Business One |
| Licence | code de licence XEI, à saisir dans le menu **Licence** de l'add-on (essai gratuit de 30 jours) |

## Version actuelle

**1.4.0** – voir les [notes de version](../../manuali/fr/itemgenerator/note-rilascio-1.4.0.md).
