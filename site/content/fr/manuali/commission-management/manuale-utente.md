---
title: XEI.CommissionManagement – Manuel d'utilisation
description: "Commissions des agents commerciaux dans SAP Business One : configuration, règles, calcul, liquidation, régularisations et relevés."
lang: fr
prodotto: XEI.CommissionManagement
versione: 1.1.1
stato: approvato
---

# XEI.CommissionManagement – Manuel d'utilisation

| | |
|---|---|
| SAP Business One | 10.0 ou versions ultérieures |
| Base de données | Microsoft SQL Server ou SAP HANA (sur SAP HANA, un essai pendant l'installation est conseillé) |
| Langues du programme | italien, anglais, allemand, français, espagnol, turc |

## 1. Ce que fait l'add-on

XEI.CommissionManagement calcule et liquide les **commissions des agents commerciaux** à partir des documents
de SAP Business One. Chaque ligne de facture (et de facture d'acompte ou d'avoir) porte jusqu'à quatre
pourcentages : un pour l'**agent** du document et un pour chacun de ses supérieurs, **chef de zone**, **chef
de secteur** et **directeur**. L'add-on :

- **affecte les pourcentages** aux lignes pendant la saisie des documents, selon des règles par client, groupe
  de clients, article, groupe d'articles, liste de prix, période et remise (ou selon les pourcentages par défaut de
  l'agent) ;
- **calcule** les commissions des documents d'une période et les divise en **parts** : une partie est acquise à
  la facturation, le reste à l'encaissement (échéance par échéance ou quand tout le document est encaissé) ;
- **liquide** les parts au fur et à mesure que SAP enregistre les encaissements, et **extourne** celles des
  échéances qui redeviennent impayées ;
- produit pour chaque agent le **relevé** de ce qui a été calculé, de ce qui reste à liquider et de ce qui lui
  revient sur la période (liquidé plus **régularisations** manuelles), exportable en CSV pour Excel, imprimable
  en PDF et envoyable par e-mail à chaque agent ;
- au choix (options dans Configuration) : estime la commission à l'enregistrement d'un document, calcule
  automatiquement les factures dès leur ajout, protège les pourcentages corrigés à la main, liquide les
  encaissements partiels, clôt les périodes déjà remises, calcule les **primes** sur le chiffre d'affaires annuel,
  prépare les **brouillons des factures** des agents et signale les anomalies (**Contrôles**).

Tout se trouve dans SAP : champs utilisateur sur les employés de vente et sur les lignes des documents, tables
utilisateur pour les règles, les commissions et les régularisations, aucune base de données externe. Le
fonctionnement est identique sur Microsoft SQL Server et SAP HANA ; sur SAP HANA, un essai pendant
l'installation est conseillé.

## 2. Les notions : bénéficiaires, pourcentages, parts, liquidation

### Qui reçoit la commission (bénéficiaires)

L'**employé de vente** du document est l'agent. Dans Agents, on peut lui indiquer un **chef de zone**, un
**chef de secteur** et un **directeur** : ce sont les autres bénéficiaires de ses documents. Chacun a son propre
pourcentage sur chaque ligne (les quatre colonnes *Provv. % agente / capo zona / capo area / direttore*
(Comm. % agent / chef de zone / chef de secteur / directeur)).

- Un employé ne reçoit des commissions que s'il a un **rôle** (Agent, Chef de zone, Chef de secteur,
  Directeur). Un employé sans rôle n'est pas « géré » : ses documents ne génèrent pas de commissions et, s'il
  est indiqué comme supérieur de quelqu'un, sa part n'est pas calculée.
- Le rôle « Agent » vaut pour ceux qui figurent comme employé de vente sur les documents ; « Chef de zone »,
  « Chef de secteur » et « Directeur » sont les titres avec lesquels un employé peut être choisi comme
  supérieur. Celui qui a un rôle de supérieur peut quand même avoir ses propres documents : sur ceux-ci, il est
  l'agent.

### Les pourcentages

Les pourcentages d'une ligne proviennent des **règles** (chapitre 7) ou, si aucune règle ne s'applique, des
**pourcentages par défaut** de l'agent du document (chapitre 6). Ils s'affectent automatiquement pendant la
saisie du document (chapitre 8), peuvent être corrigés à la main et peuvent être contrôlés et rectifiés en bloc
avant le calcul (chapitre 9).

### Les parts : à la facturation et à l'encaissement

La commission d'un document n'est pas due entièrement tout de suite. Pour chaque bénéficiaire, l'add-on la
divise en parts :

- la part **à la facturation** (échéance 0), égale au « % à la facturation » de l'employé, est acquise à la
  date d'enregistrement du document ;
- le reste est acquis **à l'encaissement** : avec la liquidation **par échéance**, une part pour chaque
  échéance du document, au prorata de l'échéance, liquidable quand cette échéance est encaissée ; avec la
  liquidation **sur le total**, une seule part (échéance -1), liquidable quand toutes les échéances sont
  encaissées.

Exemple : facture de 1.350 de montant HT avec 5 % de commission = 63,00 ; agent avec 30 % à la facturation et
liquidation par échéance, document en deux échéances à 50 % : part 0 = 18,90 à l'enregistrement, échéance 1 =
22,05 et échéance 2 = 22,05 aux dates d'échéance respectives.

### La liquidation

Liquider une part signifie la reconnaître à l'agent avec une date de liquidation. L'add-on propose les parts à
liquider en lisant les encaissements de SAP (paiements, effets, lettrages, avoirs) et propose l'**extourne**
des parts déjà liquidées dont les échéances ne sont pas soldées (impayés). Une part **figée** est définitive :
elle ne s'extourne pas et la commission ne peut pas être recalculée.

## 3. Installation et premier démarrage

- Package pour l'Extension Manager : `XEI.CommissionManagement.zip`, depuis la page de téléchargement du
  site XEI. Dans SAP Business One, on ouvre l'**Extension Manager**, on importe le package et on l'affecte à la
  société.
- Au premier démarrage, l'add-on crée les champs, les tables, les index et les autorisations. La création des
  champs sur les lignes des documents demande **quelques minutes** : SAP affiche plusieurs fois le message de
  modification de la structure de la base de données, qui ferme toutes les fenêtres ouvertes et demande s'il faut
  continuer — répondre **Oui**.
- Le menu se trouve dans **XEI-Addon › Commissions** :

    Commissions
      Configuration                     options (six onglets) et ordre de recherche des règles
      Agents                            rôle, supérieurs, % par défaut, % à la facturation, liquidation, fournisseur, utilisateur SAP
      Règles de pourcentage             % par client / groupe / article / groupe d'articles / liste de prix
      Paliers et primes                 primes sur le CA annuel (si activées dans Configuration)
      Contrôle et affectation %         comparaison documents / règles et correction en bloc
      Calcul des commissions            calcul sur factures, acomptes et avoirs
      Commissions calculées             consultation, correction, recalcul, suppression
      Liquidation                       parts encaissées à liquider, impayés à extourner
      Régularisations                   montants manuels par agent et par mois, brouillons factures agents
      Relevé des commissions            calculées, à liquider, liquidées + régularisations ; CSV, impression/PDF, e-mail
      Contrôles                         anomalies à vérifier
      Informazioni (Informations), Traduzioni (Traductions), Licenza (Licence) (entrées communes des add-ons XEI)

> Après l'installation : remplir la **Configuration**, puis les **Agents** (rôles, supérieurs,
> pourcentages), puis les **Règles**. Ce n'est qu'à partir de ce moment que les documents reçoivent les
> pourcentages. Aux utilisateurs qui ne sont pas super-utilisateurs, il faut attribuer les **autorisations**
> (chapitre 17).

### Licence

L'add-on fonctionne avec un **code de licence** délivré par XEI.

- **Essai** : après la demande d'essai sur le site, on reçoit par e-mail un **code d'essai**, valable 30
  jours à compter de l'envoi dans n'importe quelle société.
- **Achat** : on envoie à XEI les deux codes de la fenêtre **Licenza** (Licence) (code de la société et code
  du serveur, avec *Copia* (Copier)) et on reçoit le code de licence, valable pour la société ou pour le serveur
  de ces codes.
- Sans code valide, l'add-on est **bloqué** : dans son menu restent *Informazioni* (Informations) et
  *Licenza* (Licence), et au démarrage la fenêtre **Licenza** s'ouvre d'elle-même avec l'état et le motif.
- Un utilisateur SAP **super-utilisateur** colle le code dans *Inserisci un codice di licenza* (Saisir un code
  de licence) et clique sur *Salva codice* (Enregistrer le code) : l'add-on se débloque immédiatement, sans
  redémarrer SAP.

### Langues

L'add-on utilise la langue du client SAP (dans SAP : Utilisateurs - Définition \> Affichage \> Langue) :
italien, anglais, allemand, français, espagnol ou turc ; avec les autres langues, il reste en italien. Lors d'un
changement de langue, SAP ferme les fenêtres ouvertes et l'add-on redémarre de lui-même. Les textes peuvent être
adaptés un par un depuis **Commissions \> Traduzioni** (Traductions). Restent en italien dans toutes les langues
les textes que SAP enregistre une seule fois dans la base de données : les noms des autorisations (Autorisations
générales \> Provvigioni (Commissions)) et les titres des champs ajoutés aux documents et aux employés de vente
(ex. « Provv. % manuali » (Comm. % manuels), « % agente » (% agent)) ; les messages les citent sous ces noms,
pour qu'on les retrouve dans SAP.

## 4. Le travail de chaque mois, en bref

1.  **Pendant le mois**, les documents reçoivent automatiquement les pourcentages ; la personne qui les saisit
    peut les corriger.
2.  **Contrôle et affectation %** sur les factures du mois : on voit les lignes dont les pourcentages ne
    correspondent pas aux règles et on les corrige en bloc (facultatif mais conseillé).
3.  **Calcul des commissions** du mois : factures, factures d'acompte, avoirs.
4.  **Commissions calculées** : contrôle par sondage, corrections de commissions individuelles.
5.  **Liquidation** avec date limite en fin de mois : confirmation des parts encaissées et des éventuelles
    extournes.
6.  **Régularisations** du mois (primes, récupérations, ajustements manuels) et, si activés, les **brouillons
    factures** des agents.
7.  **Relevé des commissions** « liquidées et régularisations » du mois : c'est le montant à reconnaître à chaque
    agent ; CSV pour Excel, impression/PDF ou e-mail à chaque agent.
8.  Quand les relevés sont remis, **période close** jusqu'à la fin du mois (si l'option est utilisée).

Les **Contrôles** (chapitre 16) peuvent être lancés à tout moment, avant le calcul ou avant les relevés, pour
trouver les documents non calculés, les agents modifiés, les lignes sans pourcentage, les encaissements non
liquidés. En fin d'année, **Paliers et primes** (chapitre 15) enregistre les primes sur le chiffre d'affaires
comme régularisations de décembre.

## 5. Configuration

La Configuration comporte six onglets. L'onglet **Général** contient les options de base et l'ordre des règles ;
les autres (**Documents**, **Liquidation**, **Agents**, **E-mail**, **Alertes**) contiennent les fonctions
complémentaires, toutes **désactivées** au départ : chacune est suivie d'une explication et d'un exemple, et
s'active en la cochant quand on en a besoin. Il faut l'autorisation « Configurazione » (Configuration)
(chapitre 17).

![Configuration, onglet Général](../../_img/commissionmanagement/cfg.png)

*Configuration des commissions, onglet Général*

### Onglet Général

Affecter les pourcentages aux lignes des documents de vente pendant la saisie  
Active l'affectation automatique (chapitre 8). Si elle est désactivée, les pourcentages se saisissent à la main
ou avec le Contrôle.

Remise de ligne des règles  
La remise avec laquelle les règles comparent leur « remise minimale » : le *% de remise* de la ligne ou un
champ utilisateur pourcentage des lignes (par exemple une remise « effective » calculée par un autre add-on).

Prix nets  
Pour qui vend à prix net sans indiquer la remise : si la ligne n'a pas de remise, l'add-on calcule la **remise
effective** comme écart entre le prix de la liste de prix du client et le prix de la ligne (liste de prix 100,
prix 80 = remise 20 %), l'écrit dans la colonne *Provv. sconto effettivo* (Comm. remise effective) et l'utilise
pour les règles.

Pourcentages aussi sur les lignes « taxe seulement »  
Normalement, les lignes « taxe seulement » n'ont pas de commission (pourcentages à zéro).

Commissions sur les factures d'acompte  
Avec l'option active, les factures d'acompte sont calculées et leur commission est ensuite **déduite** de la
facture finale qui les solde ; ainsi, la commission globale est celle du montant entier.

Liquidation par défaut à l'encaissement du document entier  
Vaut pour les employés avec la liquidation « Selon configuration » : oui = une seule part quand tout le
document est encaissé ; non = une part par échéance.

Avoirs liquidés à l'échéance  
Normalement, la commission (négative) d'un avoir est liquidée à la date d'enregistrement. Avec l'option, elle
l'est à l'échéance la plus lointaine entre l'avoir et les factures auxquelles il se rapporte.

Ordre de recherche des règles  
Les 16 combinaisons de champs possibles pour une règle, dans l'ordre où elles sont essayées. On modifie le numéro
dans la colonne *Ordre* : l'ordre 1 est essayé en premier. Voir le chapitre 7.

### Onglet Documents

![Configuration, onglet Documents](../../_img/commissionmanagement/cfg_documenti.png)

*Onglet Documents : estimation, lignes manuelles, calcul automatique*

Afficher la commission estimée à l'enregistrement d'un document de vente  
Après l'ajout ou la mise à jour d'une commande, d'une offre, d'une livraison ou d'une facture, la barre d'état
indique ce que touchera chaque bénéficiaire avec les pourcentages actuels des lignes. Exemple : *« Commissions
estimées (Commande client 1250) : Rossi 63,00 ; Bianchi 9,00 - total 72,00 »*. C'est une simple information :
rien n'est enregistré (chapitre 8).

Protéger les pourcentages modifiés à la main sur les lignes des documents  
Celui qui corrige un pourcentage sur la ligne la rend « manuelle » (colonne *Provv. % manuali* (Comm. %
manuels)) : si le client ou l'agent change, cette ligne n'est pas réaffectée. Exemple : Rossi passe la ligne de
5 % à 4 % pour un accord avec le client ; puis il change de client : les autres lignes sont réaffectées, celle-ci
reste à 4 %. Sans l'option, la réaffectation écrase toutes les lignes. En décochant « manuel », la ligne
redevient automatique.

Calculer les commissions dès l'ajout d'une facture, d'une facture d'acompte ou d'un avoir  
Le calcul se fait à l'enregistrement dans le client SAP (avec le dernier choix fait sur la remise globale dans le
Calcul) : ainsi, il n'est pas nécessaire d'ouvrir Calcul des commissions chaque mois. Exemple : la facture 1001
de Rossi ajoutée, la barre d'état affiche *« Commissions calculées (Facture 1001) : Rossi 63,00 ; Bianchi
9,00 »*. Les documents créés par des imports ou par d'autres programmes (DI API) ne passent pas par le client :
pour ceux-ci, on utilise Calcul des commissions et les Contrôles.

### Onglet Liquidation

![Configuration, onglet Liquidation](../../_img/commissionmanagement/cfg_liquidazione.png)

*Onglet Liquidation : encaissements partiels et période close*

Encaissements partiels : liquider la part de commission proportionnelle au montant encaissé sur l'échéance  
Sans l'option, une part n'est liquidée que lorsque l'échéance est entièrement soldée : avec des acomptes ou des
remises, la commission reste bloquée. Exemple : échéance de 500 avec part de 22,05 ; le client paie 250 → on
liquide 11,03 ; au solde, les 11,02 restants. Si un encaissement est annulé, seul l'excédent est extourné
(chapitre 12).

Période close : bloquer les commissions jusqu'au (date)  
Jusqu'à cette date incluse, on ne peut pas recalculer ou supprimer de commissions, modifier de parts, liquider ou
enregistrer de régularisations. Exemple : une fois remis les relevés de mars, on saisit 31/03 : les factures de
mars ne peuvent pas être recalculées (une facture jamais calculée peut encore être calculée). Pour corriger
quelque chose dans la période close : reculer la date (ou décocher), corriger, puis la remettre.

### Onglet Agents

Générer depuis les régularisations les brouillons de factures fournisseur des agents liés à un fournisseur  
Dans Régularisations, le bouton **Brouillons factures agents** crée pour chaque agent un brouillon de facture
fournisseur (avoir fournisseur si le montant est négatif) avec une ligne de service : montant = parts liquidées
dans le mois + régularisations et primes du mois. Exemple : Rossi (fournisseur F0010), avril : 22,05 + 50,00 -
20,00 = 52,05. Le **compte de la ligne** est obligatoire (le compte de charges des commissions, ex. 7xxxx
Commissions versées) ; le **code TVA** est celui des factures de l'agent (vide = celui par défaut du
fournisseur). Chapitre 13.

Paliers de chiffre d'affaires annuel avec prime  
Active le menu **Paliers et primes** : une fois atteint le seuil de montant HT annuel, l'agent reçoit une prime
(% du CA de l'année ou montant fixe) enregistrée comme régularisation. Exemple : paliers 100.000 → 0,5 % et
200.000 → 1 % ; Rossi facture 150.000 en 2026 : prime de 750,00 dans la régularisation de décembre. Chapitre 15.

Retenue indicative dans le relevé des liquidées : % et description  
Purement informative (sans minimum ni plafond) : l'impression et l'e-mail du relevé « liquidées et
régularisations » montrent une ligne « retenue » et le net indicatif. Exemple : 8,5 et « Enasarco quota
agente » : liquidé 1.000,00 → retenue indicative -85,00, net indicatif 915,00. Vide ou 0 = aucune ligne.

![Configuration, onglet Agents](../../_img/commissionmanagement/cfg_agenti.png)

*Onglet Agents : brouillons factures, paliers et retenue indicative (8,5 % Enasarco)*

### Onglet E-mail

![Configuration, onglet E-mail](../../_img/commissionmanagement/cfg_email.png)

*Onglet E-mail : envoi du relevé aux agents*

Envoi du relevé aux agents par e-mail  
Active le bouton **Envoyer aux agents** dans le Relevé des commissions : chaque agent ne reçoit que son propre
relevé (pièce jointe HTML, lisible et imprimable dans n'importe quel navigateur) à l'adresse e-mail de l'employé
de vente (ou du fournisseur lié). Il faut indiquer le serveur SMTP, le port, SSL/TLS, l'utilisateur et le mot de
passe de la boîte et l'expéditeur ; exemple : `smtp.office365.com`, port 587, SSL oui, expéditeur
`provvigioni@azienda.it`. Le mot de passe est enregistré chiffré.

Tester l'envoi  
Envoie un message de test à l'adresse indiquée avec les valeurs saisies dans l'onglet (même non encore
enregistrées) : en cas de problème, le message d'erreur du serveur s'affiche immédiatement.

### Onglet Alertes

![Configuration, onglet Alertes](../../_img/commissionmanagement/cfg_avvisi.png)

*Onglet Alertes*

Part encaissée et non liquidée : anomalie après (jours)  
Dans les Contrôles, la recherche « Encaissements non liquidés » signale les parts dont l'échéance a été encaissée
depuis plus de ce nombre de jours et que personne n'a liquidées. Exemple : 30 ; échéance encaissée le 05/04 et
aujourd'hui le 10/05 : la part figure parmi les anomalies jusqu'à sa liquidation.

Au démarrage de l'add-on, signaler les anomalies rapides dans la barre d'état  
Contrôles rapides à chaque démarrage : documents des 90 derniers jours à calculer, documents annulés avec
commissions, agent modifié après le calcul. Exemple : *« Commissions : 3 anomalies à contrôler (Commissions \>
Contrôles) »*. Chapitre 16.

> À l'enregistrement, la Configuration vérifie que les options actives sont complètes : date de la période
> close, compte existant et imputable pour les brouillons, retenue entre 0 et 99,99, serveur, port et
> expéditeur pour l'e-mail.

## 6. Agents

![Agents](../../_img/commissionmanagement/agenti.png)

*Agents : tous les employés de vente de SAP, modifiables dans la grille*

La grille affiche tous les employés de vente de SAP. On remplit les colonnes et on clique sur **Enregistrer** :
seuls les employés modifiés sont enregistrés (les mêmes champs sont visibles aussi dans le formulaire standard
des employés de vente, onglet des champs utilisateur).

| Colonne                                                 | Signification                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rôle                                                    | Agent, Chef de zone, Chef de secteur, Directeur ou *(non géré)* : aucune commission.                                                                                                                                                                                                                                                                                                                       |
| Chef de zone, Chef de secteur, Directeur                | Les supérieurs de cet employé : ils reçoivent leur pourcentage sur ses documents. Les listes déroulantes affichent les employés qui ont ce rôle : affecter d'abord les rôles et enregistrer, puis les supérieurs. Un supérieur déjà affecté qui a un autre rôle, ou aucun, apparaît comme *« nom (rôle différent) »* : il ne reçoit pas de commissions tant qu'on ne lui donne pas ce rôle (les Contrôles le signalent aussi). |
| % agent, % chef de zone, % chef de secteur, % directeur | Pourcentages **par défaut** des documents de cet employé, utilisés quand aucune règle ne s'applique à la ligne.                                                                                                                                                                                                                                                                                             |
| % à la facturation                                      | Partie de la commission **de cet employé** (en tant que bénéficiaire) acquise à l'enregistrement du document ; le reste est acquis à l'encaissement. 100 = tout à la facturation, 0 = tout à l'encaissement.                                                                                                                                                                                              |
| Liquidation                                             | Pour la partie à l'encaissement : *Par échéance*, *Sur le total* ou *Selon configuration* (suit l'option de la Configuration).                                                                                                                                                                                                                                                                              |
| Fournisseur                                             | Le fournisseur (partenaire) par lequel l'agent facture les commissions : titulaire des **brouillons factures** (chapitre 13) ; son e-mail sert à l'envoi du relevé si l'employé n'en a pas.                                                                                                                                                                                                                |
| Utilisateur SAP                                         | L'utilisateur SAP qui correspond à cet employé. Un utilisateur sans l'autorisation « Estratto di tutti gli agenti » (Relevé de tous les agents) ne voit dans le Relevé des commissions que lui-même et les employés dont il est chef de zone, chef de secteur ou directeur (chapitre 17).                                                                                                                  |
| E-mail (employé de vente)                               | L'e-mail de l'employé de vente (données SAP, en lecture seule) : destinataire du relevé par e-mail.                                                                                                                                                                                                                                                                                                        |

Contrôles à l'enregistrement : pourcentages entre 0 et 100, fournisseur et utilisateur SAP existants, un
employé ne peut pas être son propre supérieur. Exemple utilisé dans ce manuel :

| Employé | Rôle         | Chef de zone | Chef de secteur | % ag. | % ch. zone | % ch. sect. | % à la fact. | Liquidation          |
|---------|--------------|--------------|-----------------|-------|------------|-------------|--------------|----------------------|
| Rossi   | Agent        | Bianchi      | Neri            | 2     | 0,5        | 0,2         | 30           | Par échéance         |
| Bianchi | Chef de zone |              |                 | 3     |            |             | 0            | Selon configuration  |
| Neri    | (non géré)   |              |                 |       |            |             |              |                      |
| Verdi   | Agent        |              |                 | 1,5   |            |             | 100          | Selon configuration  |

Sur les documents de Rossi, les bénéficiaires sont Rossi (agent) et Bianchi (chef de zone) ; Neri, bien
qu'indiqué comme chef de secteur, ne reçoit rien tant qu'il n'a pas de rôle.

## 7. Règles de pourcentage

![Règles de pourcentage](../../_img/commissionmanagement/regole.png)

*Règles de pourcentage de l'exemple*

Une règle dit : « pour les lignes avec *ces caractéristiques*, les pourcentages sont ceux-ci ». Les
caractéristiques possibles sont client, groupe de clients, article, groupe d'articles et liste de prix (la liste
de prix du client) ; on remplit **uniquement les champs nécessaires** et l'add-on reconnaît de lui-même la
**combinaison** (colonne Combinaison). Les combinaisons admises sont au nombre de 16 :

| Type | Combinaison                               | Type | Combinaison                                           |
|------|-------------------------------------------|------|-------------------------------------------------------|
| 1    | Client / Article / Liste de prix          | 9    | Groupe de clients / Groupe d'articles / Liste de prix |
| 2    | Client / Article                          | 10   | Groupe de clients / Groupe d'articles                 |
| 3    | Client / Groupe d'articles / Liste de prix | 11  | Groupe de clients / Liste de prix                     |
| 4    | Client / Groupe d'articles                | 12   | Groupe de clients                                     |
| 5    | Client / Liste de prix                    | 13   | Article / Liste de prix                               |
| 6    | Client                                    | 14   | Article                                               |
| 7    | Groupe de clients / Article / Liste de prix | 15 | Groupe d'articles / Liste de prix                     |
| 8    | Groupe de clients / Article               | 16   | Groupe d'articles                                     |

Client et groupe de clients ensemble (ou article et groupe d'articles ensemble) ne sont pas admis : la règle ne
s'enregistre pas.

Les autres champs de la règle :

- **Agent** : la règle ne vaut que pour les documents de cet employé ; *(tous)* = pour tous ;
- **Du / Au** : période de validité comparée à la date du document ; une seule des deux dates suffit ;
- **Remise minimale** : la règle vaut si la remise de la ligne est au moins égale à cette valeur (0 =
  toujours). Elle sert à donner des pourcentages plus bas aux ventes les plus remisées ;
- **Active** : une règle désactivée reste archivée mais ne s'applique pas.

### Comment la règle d'une ligne est choisie

1.  Les combinaisons sont essayées dans l'**ordre de la Configuration** (par défaut 1 → 16, de la plus
    spécifique à la plus générale).
2.  Pour chaque combinaison, on cherche d'abord les règles de l'**agent du document** (s'il en a au moins une),
    puis celles pour tous. La première combinaison qui trouve une règle valable l'emporte : une règle « pour
    tous » plus spécifique (ex. Client / Groupe d'articles) l'emporte sur une règle de l'agent plus générale
    (ex. Groupe d'articles).
3.  Entre plusieurs règles de la même combinaison, l'emporte celle dont la date de début est la plus récente,
    puis celle dont l'échéance est la plus proche, puis celle dont la remise minimale atteinte est la plus
    élevée.
4.  Si aucune règle ne s'applique, on utilise les pourcentages par défaut de l'agent.

Exemple avec les règles de la figure (R1 client C001 + groupe d'articles GA100 → 6/1 ; R2 seulement Rossi,
groupe GA100 → 7/1 ; R3 article A1 → 4/0,5 ; R4 article A1 avec remise minimale 10 → 3/0,5 ; R5 groupe de
clients A, année 2026 → 5/1) :

| Ligne                                           | Pourcentages agent / chef de zone | Pourquoi                                                          |
|-------------------------------------------------|-----------------------------------|-------------------------------------------------------------------|
| Rossi, client C001, article A9 (groupe GA100)   | 6 / 1                             | R1 : Client / Groupe d'articles passe avant la règle de Rossi     |
| Rossi, client C002, article A9                  | 7 / 1                             | R2 : règle de l'agent                                             |
| Verdi, client C002, article A9                  | 1,5 / 0                           | aucune règle : pourcentages par défaut de Verdi                   |
| Verdi, client C002, article A1, remise 12       | 3 / 0,5                           | R4 : remise minimale 10 atteinte (l'emporte sur R3)               |
| Verdi, client C002, article A1, remise 5        | 4 / 0,5                           | R3                                                                |
| Verdi, client C003 (groupe A), article A1       | 5 / 1                             | R5 : Groupe de clients passe avant Article                        |
| comme ci-dessus mais en 2027                    | 4 / 0,5                           | R5 échue, reste R3                                                |

### Le formulaire

- **Filtres** (agent, client, article, actives seules) et **Rechercher**.
- **Ajouter ligne**, **Dupliquer lignes** et **Supprimer lignes** sur les lignes sélectionnées (clic sur
  l'en-tête de ligne, à gauche) ; les modifications deviennent définitives avec **Enregistrer**. Tous les champs
  se modifient dans la grille (les flèches ouvrent le client et l'article).
- **Exporter CSV** enregistre les règles affichées dans un fichier avec le séparateur « ; » (il s'ouvre dans
  Excel) ; **Importer CSV** ajoute les lignes d'un fichier avec les mêmes colonnes (Agente, Cliente,
  GruppoClienti, Articolo, GruppoArticoli, Listino, Dal, Al, ScontoMinimo, PercAgente, PercCapoZona, PercCapoArea,
  PercDirettore, Attiva) : les lignes importées doivent être contrôlées et enregistrées.
- Si l'on ferme ou lance une recherche avec des modifications non enregistrées, l'add-on demande confirmation.

## 8. Les pourcentages sur les documents de vente

![Commande client](../../_img/commissionmanagement/ordine.png)

*Commande client : les colonnes Provv. avec les pourcentages affectés et, avec les prix nets, la remise effective*

Avec l'affectation active, sur les offres, commandes, livraisons, retours, factures, avoirs et factures
d'acompte :

- quand on saisit ou modifie l'**article**, la **remise** ou le **prix** d'une ligne, l'add-on écrit les
  quatre pourcentages de la ligne (et la remise effective, avec les prix nets) ;
- en choisissant plusieurs articles dans la liste, les lignes ajoutées sont elles aussi complétées ;
- en changeant le **client** ou l'**employé de vente** d'un document en cours de création, toutes les lignes sont
  réaffectées. Attention : quand on change de client, SAP reprend l'employé de vente par défaut de ce client ; si
  c'est « aucun », les lignes restent telles quelles jusqu'à ce qu'on choisisse l'agent.

Les pourcentages restent **modifiables à la main** et sont enregistrés avec le document ; ils ne sont réécrits
que si l'on modifie encore l'article, le prix ou la remise de cette ligne. Les documents copiés (commande →
livraison → facture) emportent les pourcentages des lignes.

> Les colonnes *Provv. % agente*, *% capo zona*, *% capo area*, *% direttore* (Comm. % agent, % chef de zone,
> % chef de secteur, % directeur) et *Provv. sconto effettivo* (Comm. remise effective) sont rendues visibles
> et modifiables par l'add-on à l'ouverture du document ; pour les avoir toujours à la position préférée, on peut
> les disposer une fois dans les paramètres du formulaire (icône en haut à droite de la grille). Dans les
> documents sans employé de vente, ou avec un employé sans rôle, rien n'est écrit.

La case « taxe seulement » d'une ligne ne génère pas d'événement dans le client : les pourcentages s'adaptent à
la modification suivante de l'article, du prix ou de la remise de la ligne (ou en changeant d'agent).

### Lignes manuelles (option « protéger les pourcentages modifiés à la main »)

![Commande avec ligne manuelle](../../_img/commissionmanagement/ordine_manuale.png)

*Commande : la ligne au pourcentage corrigé à la main est cochée dans « Provv. % manuali » et n'est pas réaffectée*

Avec l'option active, l'add-on affiche aussi la colonne *Provv. % manuali* (Comm. % manuels). Dès qu'on saisit
à la main l'un des quatre pourcentages d'une ligne, la ligne est **marquée manuelle** et, à partir de ce moment,
n'est pas réaffectée : ni en changeant l'article, le prix ou la remise de la ligne, ni en changeant le client ou
l'agent du document, ni en choisissant d'autres articles dans la liste. Les autres lignes continuent de suivre
les règles. Pour revenir à l'automatique, il suffit de décocher : à la modification suivante, la ligne reçoit
encore une fois les pourcentages des règles. L'indicateur passe aux documents copiés et se voit dans le Contrôle
(colonne *% manuels*), où les lignes manuelles ne sont pas proposées pour la correction.

### Estimation et calcul automatique à l'enregistrement

![Estimation dans la barre d'état](../../_img/commissionmanagement/stima.png)

*Après l'ajout de la commande, la barre d'état affiche la commission estimée pour chaque bénéficiaire*

Deux options de l'onglet Documents agissent quand le document est **enregistré** dans le client SAP :

- **Estimation** : pour les offres, commandes, livraisons, retours, factures, avoirs et factures d'acompte, la
  barre d'état affiche ce qui serait acquis avec les pourcentages actuels des lignes, bénéficiaire par
  bénéficiaire, par exemple *« Commissions estimées (Commande client 1250) : PRV Rossi 6,00 ; PRV Bianchi
  1,00 - total 7,00 »*. La remise globale est prise en compte ou non selon le dernier choix fait dans le Calcul.
  Rien n'est enregistré.
- **Calcul automatique** : les factures, les avoirs et (si activées) les factures d'acompte **ajoutés** depuis
  le client sont calculés immédiatement, comme si l'on avait lancé Calcul des commissions sur ce seul document ;
  la barre d'état affiche *« Commissions calculées (Facture 1001) : ... »*. Dans Commissions calculées,
  l'origine est « Automatique à l'enregistrement ». Si le calcul n'est pas possible (acompte déjà déduit,
  période close, agent non géré), un avertissement s'affiche et le document reste normalement enregistré : on le
  calcule ensuite depuis Calcul des commissions, et les Contrôles le signalent parmi les « À calculer ».

> Les documents créés par des imports, par le Service Layer ou par la DI API ne passent pas par le client SAP :
> pour ceux-ci, on utilise toujours Calcul des commissions (ou le calcul de toute la période, qui ne prend que
> les documents pas encore calculés).

## 9. Contrôle et affectation %

![Contrôle et affectation des pourcentages](../../_img/commissionmanagement/controllo.png)

*Contrôle : pourcentages du document (« Doc. ») et proposés par les règles, lignes différentes mises en évidence*

Avant le calcul, il est utile de vérifier que les pourcentages sur les documents de la période correspondent aux
règles (la personne qui a saisi la facture peut les avoir modifiés, ou les règles peuvent avoir été mises à jour
entre-temps).

1.  Choisir l'agent (ou tous), la période et les types de document : factures, factures d'acompte, avoirs **pas
    encore calculés** et, si on le souhaite, commandes clients ouvertes. Cliquer sur **Contrôler**.
2.  Pour chaque ligne, la grille affiche les pourcentages actuels (*Doc.*), ceux que les règles donneraient
    aujourd'hui (*Proposé*) et l'*Origine proposition* (règle pour tous, règle de l'agent, pourcentages par
    défaut). Les lignes différentes sont mises en évidence et déjà cochées ; avec « Lignes différentes de la
    proposition », on ne voit que celles-ci.
3.  Décocher les lignes à laisser telles quelles (les corrections voulues) et cliquer sur **Appliquer les %
    proposés**.

Ce qui arrive aux lignes cochées :

- **commandes clients ouvertes** : la commande est mise à jour ; les pourcentages corrigés passent aux documents
  qui en seront copiés ;
- **factures, factures d'acompte et avoirs** : ce sont des documents enregistrés et SAP n'en permet pas la
  modification (pas même des champs utilisateur des lignes). Les pourcentages corrigés sont enregistrés par
  l'add-on dans sa propre table et utilisés par le calcul à la place de ceux du document ; le document SAP reste
  tel quel. La colonne *Déjà corrigée* le signale et la colonne *Doc.* affiche à partir de ce moment les
  pourcentages corrigés.

![Contrôle avec lignes manuelles](../../_img/commissionmanagement/controllo_manuale.png)

*Contrôle sur les commandes ouvertes : les lignes manuelles différentes de la proposition ne sont pas cochées (« avec % manuels : 3 »)*

Un double-clic sur une ligne ouvre le document. Les documents dont les commissions sont déjà calculées
n'apparaissent pas : pour les corriger, on utilise Commissions calculées (chapitre 11). La colonne *% manuels*
affiche les lignes dont les pourcentages ont été corrigés à la main sur le document : avec l'option « protéger
les pourcentages modifiés à la main », elles ne sont pas cochées (on peut les cocher exprès). Avec la période
close active, les documents enregistrés avec une date dans la période ne se corrigent pas.

## 10. Calcul des commissions

![Calcul des commissions](../../_img/commissionmanagement/calcolo.png)

*Calcul des commissions avec le résultat par document*

Choisir la période (date du document), les types (factures, factures d'acompte si activées dans Configuration,
avoirs) et s'il faut **tenir compte de la remise globale** (le document entier remisé réduit le montant HT de
chaque ligne). **Calculer** traite tous les documents de la période **non annulés**, avec un agent géré et **pas
encore calculés** : d'abord les factures d'acompte, puis les factures et les avoirs. La grille affiche pour
chaque document combien de bénéficiaires ont une commission, le total et le résultat ; un double-clic ouvre le
document.

Avec **Seul le document** (type et numéro), on calcule ou **recalcule** un document précis, par exemple après
une correction des pourcentages ; le recalcul n'est possible que si aucune de ses parts n'est liquidée ou figée.

### Comment se fait le calcul, pas à pas

Pour chaque bénéficiaire (agent et supérieurs avec un rôle) :

1.  **Montant HT de la ligne** = total de la ligne en devise locale, réduit de la remise globale si demandé ;
    négatif dans les avoirs. Les lignes à zéro (articles gratuits) ne comptent pas.
2.  **Commission de la ligne** = montant HT × pourcentage de la ligne pour ce rôle. Les lignes avec un
    pourcentage 0 ne comptent pas.
3.  **Total** = somme des commissions des lignes. Des factures qui soldent un acompte, on retire la commission
    déjà calculée sur l'acompte (au prorata du montant déduit).
4.  **Parts** : la part à la facturation (échéance 0) à la date d'enregistrement ; le reste par échéance
    (échéance n à la date d'échéance de l'échéance n, au prorata de son pourcentage, la dernière échéance prenant
    les arrondis) ou sur le total (échéance -1 à la date d'échéance de la dernière échéance). Les avoirs ont une
    seule part négative (échéance 0 à l'enregistrement ou, avec l'option, à l'échéance).

Les montants sont arrondis à 2 décimales ; le total de la commission est toujours la somme des parts.

### Exemple : facture 1001

Rossi (30 % à la facturation, par échéance), client C001, **remise globale 10 %**, deux échéances à 50 % (31/03
et 30/04) :

| Ligne          | Total ligne | Montant HT (−10 %) | % agent | Comm. agent | % chef de zone | Comm. chef de zone |
|----------------|-------------|--------------------|---------|-------------|----------------|--------------------|
| A1             | 1.000,00    | 900,00             | 5       | 45,00       | 1              | 9,00               |
| A2             | 500,00      | 450,00             | 4       | 18,00       | 0              | \-                 |
| A3 (gratuit)   | 0,00        | \-                 | 5       | \-          |                |                    |
| Total          |             | 1.350,00           |         | 63,00       |                | 9,00               |

| Bénéficiaire                                | Part                          | Échéance              | Montant |
|---------------------------------------------|-------------------------------|-----------------------|---------|
| Rossi (agent, 30 % à la facturation)        | échéance 0 – à la facturation | 10/03 (enregistrement) | 18,90  |
|                                             | échéance 1 (35 %)             | 31/03                 | 22,05   |
|                                             | échéance 2 (35 %)             | 30/04                 | 22,05   |
| Bianchi (chef de zone, 0 % à la facturation) | échéance 1 (50 %)            | 31/03                 | 4,50    |
|                                             | échéance 2 (50 %)             | 30/04                 | 4,50    |

Neri (chef de secteur) ne reçoit rien parce qu'il n'a pas de rôle, même si la ligne A1 a 0,5 % dans sa colonne.

### Factures d'acompte

SAP enregistre une facture d'acompte avec les lignes entières de la commande et une remise globale égale au
complément de l'acompte (acompte de 30 % = remise de 70 %) : l'add-on utilise toujours cette remise, donc le
montant HT est la part de l'acompte (10.000 × 30 % = 3.000 → 150,00 à 5 %). Quand la facture finale déduit
l'acompte, de sa commission (10.000 × 5 % = 500,00) on retire les 150,00 déjà calculés : il reste 350,00,
répartis dans les parts comme d'habitude. Tant que la facture finale a des commissions calculées, l'acompte ne
peut être ni recalculé ni supprimé (il faut corriger la facture).

### Ce qui ne se recalcule pas

- les documents avec des parts **liquidées ou figées** (il faut d'abord retirer la liquidation, chapitre 11) ;
- les factures d'acompte déjà déduites d'une facture calculée ;
- les documents annulés : ils ne se calculent pas ; s'ils avaient été calculés avant l'annulation, leur
  commission doit être supprimée à la main depuis Commissions calculées (la Liquidation les ignore).

## 11. Commissions calculées : consulter et corriger

![Commissions calculées](../../_img/commissionmanagement/provvigioni.png)

*Commissions calculées : liste, lignes du document avec le % du bénéficiaire et parts*

La liste du haut affiche une ligne par document et bénéficiaire (filtres par agent, type, période, numéro, non
liquidées seulement) : montant HT, commission, liquidé, à liquider, date de calcul. En cliquant sur une ligne,
apparaissent en dessous les **lignes du document** avec le pourcentage de ce bénéficiaire et les **parts**. Un
double-clic ouvre le document dans SAP.

Recalculer avec % modifiés  
On modifie le pourcentage dans les lignes du bas (colonne *%*) et on recalcule cette seule commission. Le
document SAP n'est pas modifié : cela sert à corriger un cas isolé sans modifier les règles. Exemple : ligne A2
de 4 % à 6 % → 63,00 devient 72,00 et les parts 21,60 / 25,20 / 25,20.

Recalculer du document  
Recalcule avec les pourcentages actuels des lignes du document (ou corrigés par le Contrôle) : annule les
modifications faites avec le bouton précédent et prend en compte les corrections faites sur le document.

Enregistrer parts  
La date de liquidation, le montant liquidé et la case *Figée* des parts peuvent être modifiés à la main
(liquidations hors procédure, ajustements) : Enregistrer parts les enregistre et met à jour le liquidé de
l'en-tête.

Supprimer commission  
Retire la commission de ce bénéficiaire sur le document ; le document redevient calculable depuis le Calcul
(seul le document ou dans la période).

Le recalcul et la suppression sont bloqués si une part est déjà liquidée ou figée (« Commissions déjà liquidées ou
figées : retirer d'abord la liquidation » : dans Enregistrer parts, mettre le liquidé à zéro), si le document est
dans la **période close** (onglet Liquidation de la Configuration) et, par prudence, si l'employé ne fait pas
partie de la hiérarchie de l'agent du document (le recalcul le supprimerait : utiliser Supprimer commission si
c'est voulu).

**Traçabilité** : chaque en-tête et chaque part affichent *Origine*, *Utilisateur* et *Dernière modification* :
qui a écrit cette donnée en dernier et comment. Origines des en-têtes : *Calcul* (depuis le menu),
*Automatique à l'enregistrement* (à l'ajout de la facture), *Recalcul depuis le document*, *Recalcul avec %
modifiés* ; des parts : *Calcul*, *Liquidation*, *Extourne impayé*, *Manuelle* (Enregistrer parts).

## 12. Liquidation

![Liquidation](../../_img/commissionmanagement/liquidazione.png)

*Liquidation : propositions des parts à liquider au 31/03*

1.  Indiquer la **date limite** (normalement la fin du mois), s'il faut inclure les avoirs et, si on le
    souhaite, cocher les agents à traiter (aucun = tous). **Traiter**.
2.  La grille propose :
    - **Liquider** – parts pas encore liquidées et non figées dont l'échéance est antérieure ou égale à la date
      limite :
      - la part à la facturation (échéance 0) toujours, à son échéance (date d'enregistrement du document) ;
      - la part d'une échéance quand cette échéance est **soldée** dans SAP ; la part sur le total (échéance -1)
        quand toutes les échéances sont soldées ;
      - la **date de liquidation** proposée est la plus récente entre la date d'échéance et la date
        d'encaissement. La date d'encaissement tient compte des encaissements (date du paiement ou son échéance si
        elle est postérieure), des effets remis et honorés, des lettrages avec des écritures de journal ou des
        avoirs, des avoirs émis sur la facture ; si elle ne peut pas être déterminée, c'est l'échéance qui vaut.
    - **Extourner** (lignes rouges) – parts déjà liquidées et non figées dont les échéances ne sont pas soldées
      (encaissement annulé, impayé) : la liquidation est retirée et le montant redevient à liquider.
3.  Décocher les lignes à ne pas enregistrer, corriger si besoin la date de liquidation, cocher **Figer** sur les
    parts à rendre définitives. Les totaux en bas se mettent à jour avec les coches.
4.  **Confirmer** enregistre les lignes cochées ; le liquidé des documents se met à jour et un traitement
    ultérieur ne les propose pas une deuxième fois.

![Extourne](../../_img/commissionmanagement/liquidazione_storno.png)

*Après l'annulation d'un encaissement : proposition d'extourne des parts liquidées*

Exemple : la facture 1001 a sa première échéance (31/03) encaissée le 05/04. En traitant au 30/04, sont
proposées la part de l'échéance 1 de Rossi (22,05) et celle de Bianchi (4,50) avec la date de liquidation 05/04.
Si l'encaissement est annulé, le traitement suivant propose l'extourne des deux parts ; si la part de Rossi avait
été figée, seule l'extourne de Bianchi est proposée.

> Une part **figée** est définitive : elle ne s'extourne pas et la commission du document ne peut pas être
> recalculée. Figer les parts quand les commissions ont été payées à l'agent.

### Encaissements partiels (option)

![Liquidation avec encaissement partiel](../../_img/commissionmanagement/liquidazione_parziale.png)

*Encaissement partiel : lignes jaunes avec la partie liquidable, la part entière et le déjà liquidé*

Normalement, la part d'une échéance n'est liquidée que lorsque l'échéance est **soldée** : si le client paie un
acompte, la commission reste bloquée. Avec l'option **Encaissements partiels**, la part est liquidée au prorata
du montant encaissé : échéance de 816,75 avec une part de 22,05, le client paie 408,38 (la moitié) → la
liquidation de **11,03** est proposée (ligne jaune, avec les colonnes *Part entière* 22,05 et *Déjà liquidé*
0), à la date de l'encaissement si elle est postérieure à l'échéance ; au solde, le reste est proposé,
**11,02**. Si un encaissement est annulé, l'extourne ramène le liquidé à la partie qui reste encaissée (tout, si
rien ne reste encaissé). Les parts à la facturation (échéance 0) ne changent pas ; pour les parts « sur le total
du document », la proportion porte sur l'encaissé de toutes les échéances.

### Période close (option)

Quand les relevés d'un mois ont été remis, on peut **clore la période** jusqu'à cette date (onglet Liquidation
de la Configuration) : à partir de ce moment, pour les documents dont la date se trouve dans la période, on ne
recalcule ni ne supprime de commissions, on ne modifie pas de parts et on ne liquide ni n'extourne avec une date
dans la période, on n'enregistre ni régularisations ni primes dans les mois clos et le Contrôle ne corrige pas les
documents enregistrés. Dans tous les cas, le message indique *« Période close jusqu'au jj/mm/aaaa »*, avant toute
demande de confirmation (si les parts sont déjà liquidées, il indique plutôt *« Commissions déjà liquidées ou
figées »*). Une facture de la période jamais calculée peut encore être calculée. Pour corriger quelque chose :
reculer la date (ou décocher), corriger, puis la remettre.

## 13. Régularisations

![Régularisations](../../_img/commissionmanagement/conguagli.png)

*Régularisations d'un mois*

Montants manuels par agent et par mois, positifs ou négatifs (primes, remboursements, récupérations,
ajustements), avec un ordre et une description. On choisit l'année et le mois (flèches \< et \> pour changer de
mois, **Afficher**), on ajoute ou on supprime des lignes et on clique sur **Enregistrer** : les lignes du mois
sont remplacées par celles de la grille. Les régularisations figurent dans le relevé « liquidées et
régularisations » du mois. La colonne *Type* distingue les régularisations *manuelles* (« Manuelle ») des
*primes* (« Prime de palier ») enregistrées par les paliers (chapitre 15), visibles ici mais non modifiables.
Avec la période close active, les mois clos ne s'enregistrent pas.

### Brouillons factures agents (option)

![Brouillons factures agents](../../_img/commissionmanagement/bozze.png)

*Régularisations : en bas, les brouillons de factures générés pour le mois, avec le lien vers le brouillon et le fournisseur*

Quand l'agent facture les commissions à l'entreprise, le bouton **Brouillons factures agents** prépare le
document à sa place. Pour le mois choisi, pour chaque agent géré qui a un **fournisseur** lié (chapitre 6) :

- montant = parts **liquidées dans le mois** (par date de liquidation) + **régularisations et primes** du
  mois ;
- montant positif → brouillon de **facture fournisseur** ; négatif → brouillon d'**avoir fournisseur** ;
  zéro → rien ;
- le brouillon a une ligne de service sur le compte indiqué dans Configuration, avec le code TVA choisi (ou
  celui par défaut du fournisseur) et le montant comme total de la ligne.

Exemple : Rossi (fournisseur V20000), avril : échéance liquidée le 05/04 de 22,05 + régularisations +50,00 et
-20,00 = brouillon de facture fournisseur de **52,05**. À la fin, un message récapitule agent par agent
(brouillon créé, aucun fournisseur, montant zéro, brouillon déjà présent). Les brouillons du mois se trouvent dans
la grille du bas avec l'**état** (ouvert, clos c'est-à-dire déjà transformé en facture, supprimé), la date et
l'utilisateur ; la flèche jaune ouvre le brouillon ou le fournisseur. Un agent ayant un brouillon encore existant
pour ce mois est ignoré : pour le régénérer, supprimer le brouillon dans SAP. Le brouillon doit ensuite être
complété et enregistré dans SAP comme n'importe quel autre brouillon (numéro et date de la facture de l'agent).

## 14. Relevé des commissions

![Relevé des commissions](../../_img/commissionmanagement/estratto.png)

*Relevé « liquidées et régularisations » d'avril, regroupé par agent*

Trois relevés, pour une période et pour un agent ou tous, regroupés par agent (flèches pour développer et
réduire), avec le total en bas et **Exporter CSV** (une ligne « Total » pour chaque agent, à ouvrir dans
Excel) :

| Relevé                                   | Ce qu'il affiche                                                                                  | Période rapportée à  |
|------------------------------------------|---------------------------------------------------------------------------------------------------|----------------------|
| Commissions calculées                    | une ligne par document et bénéficiaire : montant HT, commission, liquidé                          | date du document     |
| Commissions à liquider                   | les parts pas encore liquidées (ou liquidées en partie) et non figées                              | échéance de la part  |
| Commissions liquidées et régularisations | les parts liquidées plus les régularisations des mois de la période : **c'est ce qu'il faut reconnaître à l'agent** | date de liquidation |

### Imprimer / PDF

![Relevé imprimé](../../_img/commissionmanagement/estratto_stampa.png)

*Le relevé ouvert dans le navigateur : un bloc par agent, totaux et retenue indicative*

Le bouton **Imprimer / PDF** ouvre le relevé affiché dans le navigateur, mis en page : en-tête avec la société, le
type de relevé et la période, un bloc pour chaque agent avec ses lignes et le total. De là, on l'imprime ou on
l'enregistre en PDF (Imprimer → « Enregistrer au format PDF »). Si la **retenue indicative** est indiquée dans
Configuration (ex. 8,5 « Enasarco quota agente »), le relevé « liquidées et régularisations » affiche aussi pour
chaque agent la ligne de la retenue et le **net indicatif** : ce sont des informations pratiques pour l'agent,
sans minimum ni plafond.

### Envoyer aux agents (option)

Avec l'envoi par e-mail actif (onglet E-mail de la Configuration), le bouton **Envoyer aux agents** envoie à
chaque agent du relevé affiché un message avec en pièce jointe **son seul relevé** en HTML (lisible et
imprimable dans n'importe quel navigateur). L'adresse est celle de l'employé de vente ou, à défaut, celle du
fournisseur lié. À la fin, un récapitulatif indique pour chaque agent si l'envoi a réussi, si l'adresse manque
ou quelle erreur le serveur a renvoyée. Le bouton n'est actif que pour ceux qui ont l'autorisation complète sur
le relevé de tous les agents.

### Chaque chef voit ses agents

Un utilisateur SAP lié à un employé (colonne *Utilisateur SAP* dans Agents) qui n'a pas l'autorisation
« Estratto di tutti gli agenti » (Relevé de tous les agents) ne trouve dans la liste déroulante que *(mes
agents)* et son nom et ceux de ses subordonnés (les employés dont il est chef de zone, chef de secteur ou
directeur) : un chef de zone peut consulter le relevé de ses agents sans voir les autres. Celui qui n'est lié à
aucun employé, sans l'autorisation, ne voit rien.

## 15. Paliers et primes

![Paliers et primes](../../_img/commissionmanagement/scaglioni.png)

*Paliers et primes : en haut les paliers, en bas les primes calculées pour l'année*

Avec l'option « paliers de chiffre d'affaires annuel avec prime » (onglet Agents de la Configuration), le menu
**Paliers et primes** gère les primes de fin d'année liées au chiffre d'affaires. Un **palier** comporte :
agent (ou *tous*), année (ou *chaque année*), seuil de montant HT annuel, type de prime (*% du CA annuel* ou
*montant fixe*), prime, description, actif. On ajoute, modifie et supprime des lignes dans la grille du haut et
on clique sur **Enregistrer paliers**.

| Agent   | Année            | Seuil  | Type             | Prime  | Description       |
|---------|------------------|--------|------------------|--------|-------------------|
| (tous)  | (chaque année)   | 1.000  | % du CA annuel   | 0,5    | Premio base       |
| (tous)  | (chaque année)   | 10.000 | % du CA annuel   | 1      | Premio 10.000     |
| Rossi   | 2026             | 12.000 | montant fixe     | 500,00 | Premio Rossi 2026 |

**Calculer primes** pour une année : le chiffre d'affaires de chaque agent est la somme des montants HT de ses
commissions calculées (factures et avoirs datés de l'année ; pas les factures d'acompte, déjà comprises dans les
factures finales). Le palier atteint est celui dont le **seuil est le plus élevé** sans dépasser le chiffre
d'affaires ; les paliers de l'agent priment sur ceux pour tous et l'année spécifique sur « chaque année ».
Prime = chiffre d'affaires × % ou montant fixe. Exemple avec les paliers ci-dessus : Rossi 13.150 → palier 12.000
de l'agent → **500,00** ; Bianchi 2.900 → palier 1.000 → 0,5 % = **14,50** ; Verdi 1.488 → **7,44**. La
colonne *Déjà enregistré* affiche la prime de la même année déjà enregistrée.

**Enregistrer primes cochées** : les lignes cochées deviennent des régularisations de type *Prime de palier* dans
le mois choisi (normalement décembre) : de là, elles entrent dans le relevé « liquidées et régularisations »,
dans les brouillons factures et dans les totaux du mois comme les autres régularisations. Si l'on enregistre une
deuxième fois la même année, la prime existante est remplacée (pas dupliquée) ; une prime à zéro la retire. Avec
la période close active, les mois clos ne s'enregistrent pas.

## 16. Contrôles et alertes au démarrage

![Contrôles](../../_img/commissionmanagement/verifiche.png)

*Contrôles : anomalies de la période, erreurs en rouge*

Le menu **Contrôles** recherche dans une période tout ce qui peut faire manquer ou fausser une commission. On
indique la période, s'il faut chercher aussi les encaissements non liquidés (c'est la recherche la plus lente) et
on clique sur **Contrôler** : chaque anomalie a une gravité (**Erreur** en rouge, **Avertissement**), le contrôle
qui l'a trouvée, l'agent, le document et l'explication avec ce qu'il faut faire. Un double-clic ouvre le document.

| Contrôle                    | Ce qu'il signale                                                                                                                         | Que faire                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| À calculer                  | factures, acomptes et avoirs de la période avec agent géré et sans commissions                                                           | Calcul des commissions                                   |
| Sans agent                  | documents sans employé de vente ou avec un employé sans rôle                                                                             | vérifier si c'est voulu ; donner le rôle dans Agents     |
| Lignes sans %               | documents avec agent géré dont toutes les lignes ont des pourcentages à zéro                                                             | Contrôle et affectation % ou règles manquantes           |
| Agent modifié               | documents calculés dont l'employé de vente dans SAP n'est pas celui de la commission                                                    | Recalculer dans Commissions calculées                    |
| Annulé                      | documents annulés avec commissions calculées                                                                                             | Supprimer commission                                     |
| Hiérarchie des agents       | supérieur sans rôle (sa part n'est pas acquise), pourcentage par défaut d'un rôle sans le supérieur, utilisateur SAP inexistant          | corriger dans Agents                                     |
| Règles qui se chevauchent   | deux règles actives identiques (mêmes champs, remise et employé) dont les périodes se chevauchent : une seule des deux s'applique        | corriger les règles                                      |
| Encaissements non liquidés  | parts dont l'échéance est encaissée depuis plus de jours que ceux indiqués dans Configuration et pas encore liquidées                     | Liquidation                                              |

Avec l'option **alertes au démarrage**, à chaque démarrage de l'add-on les contrôles rapides sont exécutés
(documents des 90 derniers jours à calculer, agent modifié et annulés de la dernière année) et, s'ils trouvent
quelque chose, ils l'indiquent dans la barre d'état quelques secondes après le démarrage, c'est-à-dire après les
éventuels messages de la licence : *« Commissions : 3 anomalies à contrôler (Commissions \> Contrôles) »*. Sans
anomalie, rien n'est affiché.

## 17. Autorisations et traçabilité

L'add-on crée dans les **Autorisations générales** de SAP (Gestion › Initialisation système › Autorisations)
l'entrée **Provvigioni** (Commissions) sous *Autorisations utilisateur*, avec cinq sous-entrées. Les
super-utilisateurs ont toujours tout ; aux autres utilisateurs, on attribue pour chaque entrée *Aucune
autorisation*, *Lecture seule* ou *Autorisation complète* :

![Autorisations générales](../../_img/commissionmanagement/autorizzazioni.png)

*Autorisations générales : l'entrée Provvigioni (Commissions) avec les cinq sous-entrées, pour un utilisateur sans autorisation*

| Autorisation                                                                       | Lecture seule                                                           | Complète                                                                              |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Configurazione (Configuration)                                                        | –                                                                       | ouvrir et enregistrer la Configuration                                                |
| Agenti, regole e scaglioni (Agents, règles et paliers)                             | consulter                                                               | enregistrer agents, règles et paliers                                                 |
| Controllo, calcolo e verifiche (Contrôle, calcul et vérifications)                 | consulter Contrôle, Calcul, Commissions calculées, Contrôles            | appliquer les %, calculer, recalculer, enregistrer les parts, supprimer               |
| Liquidazione, conguagli e bozze fatture (Liquidation, régularisations et brouillons factures) | consulter Liquidation et Régularisations                     | confirmer les liquidations, enregistrer les régularisations, enregistrer les primes, générer les brouillons |
| Estratto di tutti gli agenti (Relevé de tous les agents)                           | voir le relevé de tous les agents (sans : seulement les siens, chapitre 14) | aussi l'envoi par e-mail                                                          |

Sans autorisation, l'entrée de menu répond dans la barre d'état *« Fonction non autorisée : il faut
l'autorisation « … » (Autorisations générales \> Provvigioni) »* ; avec la lecture seule, la fenêtre s'ouvre mais
les boutons qui modifient répondent *« Opération non autorisée : il faut l'autorisation complète sur « … » »*.

**Traçabilité** : les en-têtes et les parts des commissions enregistrent l'origine, l'utilisateur et la date de
la dernière écriture (chapitre 11) ; les régularisations, l'utilisateur et la date de modification ; les
brouillons factures, qui les a générés et quand. Le journal de l'add-on (chapitre 19) enregistre les erreurs et
les mises à jour de la structure.

## 18. Questions fréquentes et problèmes

Les pourcentages ne sont pas écrits sur le document  
Vérifier : l'option dans Configuration ; que le document ait un employé de vente avec un rôle ; que le client
soit renseigné. Après un changement de client, choisir l'agent une autre fois.

J'ai corrigé un pourcentage sur la facture mais SAP ne me laisse pas l'enregistrer  
Les factures enregistrées ne se modifient pas. Utiliser Contrôle et affectation % (avant le calcul) ou
Commissions calculées → Recalculer avec % modifiés (après).

« Commissions déjà liquidées ou figées »  
Pour recalculer ou supprimer, dans Commissions calculées, mettre à zéro le liquidé des parts (Enregistrer parts)
et décocher *Figée*. Si les parts ont réellement été payées à l'agent, mieux vaut ne pas y toucher : enregistrer
la différence comme régularisation.

« Acompte déjà déduit d'une facture aux commissions calculées »  
Corriger ou supprimer d'abord la commission de la facture finale, puis l'acompte, puis recalculer la facture.

Une part n'est pas proposée en liquidation  
L'échéance n'est pas soldée dans SAP (paiement partiel ou pas encore enregistré), l'échéance est postérieure à
la date limite, ou la part est déjà liquidée/figée. Les parts des documents annulés ne sont pas proposées :
supprimer la commission.

Au premier démarrage, SAP demande de fermer toutes les fenêtres  
C'est normal quand des champs utilisateur sont créés : répondre Oui jusqu'à la fin de la création (quelques
minutes). Cela vaut aussi quand une mise à jour de l'add-on ajoute des champs ; si le client est fermé en cours de
route, la création reprend au redémarrage de l'add-on.

« Période close jusqu'au... »  
L'opération concerne une date comprise dans la période close (Configuration, onglet Liquidation). Si la
correction est vraiment nécessaire : reculer la date du blocage, corriger, puis la remettre.

« Fonction non autorisée »  
L'utilisateur SAP n'a pas l'autorisation (chapitre 17) : l'attribuer dans les Autorisations générales, entrée
Provvigioni (Commissions).

La facture a été enregistrée mais la barre d'état affiche « Commissions non calculées »  
Le calcul automatique n'était pas possible (acompte déjà déduit, période close, agent non géré) : le document est
enregistré normalement ; le calculer depuis Calcul des commissions (les Contrôles le listent parmi les « À
calculer »).

L'envoi par e-mail renvoie une erreur  
Utiliser « Tester l'envoi » dans l'onglet E-mail de la Configuration : le message du serveur indique si le
serveur, le port, SSL ou les identifiants sont erronés. Les agents « sans e-mail » doivent être complétés dans
les données de l'employé de vente ou du fournisseur lié.

Une ligne du document ne prend pas les pourcentages des règles  
Avec l'option « protéger les pourcentages modifiés à la main », la ligne est marquée manuelle (colonne Provv. %
manuali (Comm. % manuels)) : décocher et modifier l'article, le prix ou la remise, ou bien corriger à la main.

Pendant que l'add-on travaille, SAP ne répond pas  
Pendant Contrôler, Calculer, Traiter et Appliquer, SAP attend l'add-on (barre d'état « Veuillez patienter... ») :
ne pas fermer la fenêtre et ne pas arrêter l'add-on, sinon le client reste en attente et doit être redémarré.

## 19. Données et notes techniques

| Où                                                              | Quoi                                                                                                                                                                                                 |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLP (employés de vente)                                        | champs `U_XEI_PRV_Ruolo`, `_CapoZona`, `_CapoArea`, `_Direttore`, `_PercAg`, `_PercCZ`, `_PercCA`, `_PercDI`, `_Fatturato`, `_Liquida`, `_Fornitore`, `_Utente` (utilisateur SAP)                     |
| Lignes des documents de marketing (RDR1, INV1, RIN1, DPI1...)   | `U_XEI_PRV_Ag`, `_CZ`, `_CA`, `_DI` (pourcentages), `_ScEff` (remise effective), `_Man` (ligne manuelle)                                                                                              |
| `@XEI_PRV_REGOLE`                                               | règles des pourcentages                                                                                                                                                                              |
| `@XEI_PRV_DOC`, `@XEI_PRV_RIGHE`, `@XEI_PRV_RATE`               | commissions calculées : en-tête par document et bénéficiaire, lignes, parts (code = type-DocEntry-employé\[-ligne/échéance\], ex. `13-386-61-2`) ; en-têtes et parts avec origine, utilisateur et date de modification |
| `@XEI_PRV_PERC`                                                 | pourcentages corrigés par le Contrôle pour les lignes de documents enregistrés                                                                                                                      |
| `@XEI_PRV_CONG`                                                 | régularisations (type M manuelle / P prime, année de référence de la prime)                                                                                                                         |
| `@XEI_PRV_SCAG`, `@XEI_PRV_BOZZE`                               | paliers ; brouillons factures générés (agent, mois, brouillon, fournisseur, montant)                                                                                                                 |
| `@XEI_SETTINGS` (domaine XEI.CommissionManagement)              | options de la Configuration (mot de passe SMTP chiffré) et version de la structure des données                                                                                                     |
| Autorisations (OUPT)                                            | `XEI_PRV` et sous-entrées `XEI_PRV_P_CFG`, `_ANAG`, `_CALC`, `_LIQ`, `_EST`                                                                                                                         |

- Types de document : 13 facture, 203 facture d'acompte, 14 avoir, 17 commande (uniquement dans le contrôle).
- Tout passe par la DI API de SAP (aucune connexion directe à la base de données).
- Performances : sur les documents, les lignes sont lues en bloc (un seul appel) et seules les cellules qui
  changent sont écrites ; les clients, articles et listes de prix sont lus une fois par fenêtre. Dans la
  liquidation, les dates d'encaissement (la recherche la plus lourde) ne sont calculées que pour les parts
  effectivement liquidables.
- Journal : `%LOCALAPPDATA%\XEI\logs\XEI.CommissionManagement.log`.
