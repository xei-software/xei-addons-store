---
title: XEI.ContoLavoro – Sous-traitance
description: Gère dans SAP Business One les travaux confiés aux sous-traitants, de la commande et de l'envoi des composants jusqu'au retour du produit fini.
lang: fr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro

**La sous-traitance dans SAP Business One.** Un ordre de sous-traitance pour chaque travail regroupe la commande au
sous-traitant, les composants envoyés, les retours et la réception du produit fini, avec une situation toujours à jour.

## Description

Suivre la sous-traitance à la main oblige à garder alignés commandes d'achat, transferts et réceptions, et à savoir à
tout moment ce qui se trouve chez chaque sous-traitant. Avec XEI.ContoLavoro, c'est SAP Business One qui s'en charge :

- pour chaque travail, on ouvre un **ordre de sous-traitance** avec les produits à obtenir et leur nomenclature :
  composants à envoyer et façons à payer ;
- la **commande d'achat au sous-traitant** est créée à partir de l'ordre de sous-traitance et reste alignée à chaque
  modification ;
- les **composants** sont envoyés au magasin du sous-traitant, avec les retours et les rebuts ;
- la **réception** enregistre en une seule opération l'entrée du produit et des façons et la sortie des composants
  consommés ;
- l'ordre de sous-traitance montre à tout moment ce qui a été expédié, ce qui a été utilisé, ce qui reste chez le
  sous-traitant et ce qui manque, et se clôture tout seul lorsqu'il est terminé.

## Fonctions principales

- **Ordre de sous-traitance** avec les onglets Produits, Nomenclature, Composants et Documents : tous les documents SAP
  liés, regroupés et prêts à ouvrir.
- **Sous-traitance à partir des ordres de fabrication** : les phases externes d'un ordre de fabrication deviennent des
  ordres de sous-traitance, les composants sont prélevés à chaque retour et le produit fini entre en stock lorsque
  toutes les façons sont revenues.
- **Lots et numéros de série** proposés à partir des lots de l'ordre de sous-traitance chez le sous-traitant et par
  date d'expiration, modifiables à la main ; lot du produit entrant calculé par un script configurable.
- **Coûts** des produits recalculés à chaque enregistrement, avec les **prix de façon** par sous-traitant et produit.
- **Transfert en masse** des composants, **transfert entre ordres de sous-traitance** chez le même sous-traitant et
  **clôture en masse** des réceptions de marchandises.

## Configuration requise

| | |
|---|---|
| SAP Business One | 10.0 ou ultérieure |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un test lors de l'installation est conseillé) |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |
| Système | Microsoft .NET Framework 4.8 sur le poste du client SAP |
| Installation | Extension Manager de SAP Business One |
| Licence | code de licence XEI, à saisir dans le menu **Licenza** (Licence) (essai gratuit de 30 jours) |

## Version actuelle

**1.2.0** – voir les [notes de version](../../manuali/fr/contolavoro/note-rilascio-1.2.0.md) et le manuel
d'utilisation.
