---
title: XEI.ContoLavoro 1.2.0 – Notes de version
description: Fonctions et corrections de XEI.ContoLavoro 1.2.0 pour SAP Business One.
lang: fr
prodotto: XEI.ContoLavoro
versione: 1.2.0
stato: approvato
---

# XEI.ContoLavoro 1.2.0 – Notes de version

## Fonctions de cette version

- Dans la liste « Créer des ordres depuis les ordres de fabrication », avec la case « Mostra anche le righe non
  pronte » (Afficher aussi les lignes non prêtes), apparaissent aussi les façons qui ne peuvent pas devenir un ordre de
  sous-traitance, avec le motif et ce qu'il faut faire dans la colonne « Motif / avertissements ».
- Lorsque vous enregistrez une nomenclature, un avertissement signale les codes à corriger dans le champ
  « Lavorazione terzista » (Façon du sous-traitant) : ressources, codes qui ne sont pas des articles, articles sans
  « Conto lavoro » (Sous-traitance), façons qui ne sont pas des lignes de la nomenclature, composants en
  consommation automatique (backflush).
- Licence XEI avec la fenêtre **Licenza** (Licence) dans le menu de l'add-on : statut, codes de la société et du
  serveur, saisie du code ; essai gratuit de 30 jours.

## Corrections de cette version

- Un ordre de sous-traitance interrompu n'empêche pas de créer un autre ordre de sous-traitance à partir de la même
  ligne de l'ordre de fabrication.
- Les composants en consommation automatique (backflush) liés à une façon externe ne sont pas envoyés au
  sous-traitant et l'ordre de fabrication ne les prélève qu'une seule fois.
