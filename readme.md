# CAHIER DES CHARGES FONCTIONNEL — BANGS 224

# Projet : SaaS de gestion commerciale
# Entreprise : Bangs 224
# Version : V1 — cadrage fonctionnel
# Approche : Web + Mobile, API REST, multi-boutiques, multi-pays, multilingue

# 1. Vision du produit

Bangs 224 est une solution SaaS destinée aux commerçants permettant de gérer leur activité commerciale quotidienne.

Le système doit permettre notamment de :

gérer une ou plusieurs boutiques ;
gérer les produits et catégories ;
gérer les stocks ;
enregistrer les ventes ;
gérer les caisses ;
gérer les clients ;
gérer les fournisseurs ;
effectuer des commandes d'achat ;
gérer les employés ;
suivre l'activité de la boutique ;
consulter des indicateurs commerciaux ;
fonctionner sur Web et Mobile ;
fonctionner partiellement hors connexion ;
recevoir des notifications ;
gérer les abonnements.

Notre objectif n'est pas seulement de faire une application qui « fonctionne ».

Nous voulons construire un produit :

robuste + sécurisé + maintenable + évolutif + commercialisable.

# 2. Modèle économique

Le produit est un SaaS.

Le parcours global sera :

Visite du site
      ↓
Création d'un compte
      ↓
Création / configuration de l'espace
      ↓
Choix de l'offre
      ↓
Paiement
      ↓
Activation de l'abonnement
      ↓
Création / activation de la boutique
      ↓
Utilisation
      ↓
Renouvellement
Offre initiale
Offre	Prix	Plateforme
Web	15 $ / mois	Web
Mobile	35 $ / mois	Android / iOS
Web + Mobile	50 $ / mois	Web + Mobile

Important :

Web et Mobile sont indépendants.

Si le commerçant possède uniquement Mobile :

Mobile
   ↓
Données Mobile

S'il possède uniquement Web :

Web
 ↓
Données Web

S'il possède les deux :

             Backend
             /     \
          Web       Mobile
           \         /
            mêmes données

Cette décision sera importante lorsque nous concevrons notre architecture.

# 3. Les acteurs du système

Nous allons distinguer plusieurs catégories d'acteurs.

# 3.1 Notre équipe Bangs 224

C'est l'équipe qui exploite la plateforme SaaS.

Elle pourra notamment gérer :

les commerçants ;
les abonnements ;
les paiements ;
les instances / espaces ;
la configuration globale ;
les incidents ;
la supervision.
# 4. Le commerçant

Le commerçant est le client de Bangs 224.

Il possède son espace de gestion.

Un commerçant peut posséder :

Commerçant
   │
   ├── Boutique A
   ├── Boutique B
   └── Boutique C

Chaque boutique peut être située dans une localité différente.

Exemple :

Entreprise : ABC Commerce


Boutique 1 → Conakry
Boutique 2 → Kindia
Boutique 3 → Kankan
# 5. Les employés

Une boutique peut avoir plusieurs employés.

Nous avons déjà défini les rôles principaux :

Administrateur

Il possède les permissions administratives.

Il peut notamment :

gérer les employés ;
ajouter un vendeur ;
supprimer un vendeur ;
gérer les produits ;
modifier les prix ;
gérer la boutique ;
consulter les informations autorisées.
Vendeur

Responsable principalement des ventes.

Il peut :

effectuer une vente ;
consulter les produits nécessaires à la vente ;
consulter les informations nécessaires à son travail.

Il ne peut pas :

supprimer un produit ;
modifier le prix d'un produit ;
modifier directement le stock.
Gestionnaire de stock

Responsable de la gestion du stock.

Il peut notamment :

consulter le stock ;
effectuer les opérations de stock autorisées ;
créer une catégorie ;
effectuer des ajustements autorisés.

Il ne peut pas :

enregistrer une vente.
# 6. Principe fondamental de sécurité

Nous avons déjà établi cette règle :

Un utilisateur ne doit jamais pouvoir accéder aux données qui ne lui appartiennent pas.

Cela signifie que notre système devra contrôler :

Utilisateur
     ↓
Entreprise
     ↓
Boutique
     ↓
Ressource

Par exemple :

Vendeur Boutique A
       ↓
Produit Boutique A       ✅


Vendeur Boutique A
       ↓
Produit Boutique B       ❌

Cette règle sera extrêmement importante lorsque nous construirons notre API REST.

# 7. Gestion des boutiques

Un commerçant peut créer plusieurs boutiques.

Lors de la création d'une boutique, il devra renseigner notamment :

nom de la boutique ;
pays ;
région/localité ;
activité ;
coordonnées ;
informations nécessaires à l'identification.
Pays

Pour la première version, nous ciblerons 5 pays africains.

Nous déciderons précisément lesquels dans le cahier des charges.

Le système devra cependant être conçu pour pouvoir ajouter facilement un sixième, septième, etc.

Donc nous ne devons surtout pas coder :

if country == "Guinée"

partout dans l'application.

Nous voulons plutôt une architecture :

Pays
 ├── Guinée
 ├── Sénégal
 ├── Côte d'Ivoire
 ├── ...

Cela nous permettra d'évoluer.

# 8. Catégories d'activité

Lors de la création de la boutique, le commerçant pourra sélectionner son activité.

Exemples inspirés de notre analyse :

Téléphonie & Accessoires
Alimentation générale / Épicerie
Vêtements & Mode
Quincaillerie / Matériaux
Pharmacie / Parapharmacie
Électronique & Électroménager
Cosmétique & Beauté
Moto & Pièces
Matériel électrique
Matériaux de construction
Divers

Mais attention :

Ce sont des catégories d'activité.

Elles sont différentes des :

catégories de produits.

Exemple :

Activité de la boutique
    ↓
Téléphonie


Catégories de produits
    ├── Smartphones
    ├── Chargeurs
    ├── Écouteurs
    └── Coques

C'est une distinction importante pour notre modèle métier.

# 9. Produits

Une boutique peut créer ses propres produits.

Un produit pourra posséder notamment :

nom ;
catégorie ;
référence/SKU ;
description ;
attributs ;
prix d'achat ;
prix de vente ;
prix dégressifs ;
stock initial ;
seuil d'alerte ;
image.

Exemple :

Produit
 ├── Nom
 ├── SKU
 ├── Catégorie
 ├── Prix achat
 ├── Prix vente
 ├── Stock
 ├── Seuil stock faible
 └── Attributs
# 10. Produits identiques dans plusieurs boutiques

Nous avons décidé quelque chose d'important :

Deux boutiques peuvent avoir les mêmes produits.

Exemple :

Boutique Conakry
    └── iPhone 13


Boutique Kindia
    └── iPhone 13

Cela ne signifie pas nécessairement qu'il s'agit du même stock.

Chaque boutique possède sa propre gestion commerciale.

# 11. Gestion du stock

Le stock est une partie centrale du système.

Nous voulons éviter que chaque fonctionnalité modifie directement le stock de manière anarchique.

Les mouvements de stock doivent provenir d'opérations métier.

Vente
Stock initial
      ↓
Vente
      ↓
Stock - quantité vendue
Réception d'achat
Stock initial
      ↓
Réception fournisseur
      ↓
Stock + quantité reçue
Ajustement
Stock système
      ↓
Inventaire physique
      ↓
Écart
      ↓
Ajustement autorisé
# 12. Alerte de stock faible

Chaque produit peut avoir un seuil.

Exemple :

Stock = 10
Seuil = 5

Lorsque :

stock <= seuil

le système doit signaler le stock faible.

Et tu avais ajouté une règle très intéressante :

L'alerte doit pouvoir apparaître avant même la vente.

Exemple :

Vendeur sélectionne produit
        ↓
Stock = 5
Seuil = 5
        ↓
⚠️ Stock faible

Cela permet au commerçant de prendre une décision.

# 13. Ventes

Le vendeur pourra ouvrir une caisse et effectuer une vente.

Flux simplifié :

Ouverture caisse
       ↓
Recherche produit
       ↓
Ajout au panier
       ↓
Quantité
       ↓
Calcul
       ↓
Réduction éventuelle
       ↓
Taxe éventuelle
       ↓
Choix moyen de paiement
       ↓
Validation
       ↓
Vente enregistrée
       ↓
Stock diminué
# 14. Caisse

Nous aurons la notion de session de caisse.

Exemple :

08:00
   ↓
Ouverture caisse
   ↓
Ventes
   ↓
Ventes
   ↓
Ventes
   ↓
18:00
   ↓
Fermeture caisse

La caisse devra notamment conserver :

utilisateur ;
boutique ;
heure d'ouverture ;
heure de fermeture ;
montant initial ;
montant théorique ;
informations des ventes ;
état de la session.

Nous détaillerons plus tard les règles de calcul.

# 15. Clients

La boutique peut gérer ses clients.

Informations initiales :

nom ;
téléphone ;
éventuellement d'autres informations.

Le système pourra ensuite permettre :

Client
  ↓
Historique des achats
  ↓
Montants
  ↓
Dettes éventuelles
  ↓
Informations commerciales

Nous déciderons plus tard si nous intégrons le crédit/dette client dans V1 ou dans une version ultérieure.

# 16. Fournisseurs

Une boutique peut avoir plusieurs fournisseurs.

Un fournisseur peut également être une autre boutique présente sur Bangs 224.

La relation peut être :

Boutique A
     │
     │ ajoute
     ▼
Boutique B
     │
     └── fournisseur

Le rattachement peut être réalisé via un code fournisseur.

# 17. Catalogue fournisseur

Un fournisseur pourra publier certains produits dans son catalogue.

Mais :

publier un produit ≠ donner accès au stock privé.

Le fournisseur contrôle ce qu'il expose.

# 18. Commandes d'achat

Une boutique peut créer une commande auprès d'un fournisseur.

Flux :

Sélection fournisseur
       ↓
Sélection produits
       ↓
Quantités
       ↓
Commande
       ↓
Envoi
       ↓
Acceptation
       ↓
Livraison
       ↓
Réception
       ↓
Stock augmenté
Règle fondamentale

La création d'une commande ne modifie pas le stock.

Seule la réception confirmée modifie le stock.

# 19. Réception partielle

Exemple :

Commande : 100 unités


Réception 1 : 60
Réception 2 : 40

Le système doit être capable de suivre :

Commandé : 100
Reçu : 60
Restant : 40

Puis :

Reçu : 100
Restant : 0

C'est une exigence importante pour la robustesse du système.

# 20. Journal d'activité

Le système doit conserver les actions importantes.

Exemple :

14 août 2026
10:32


Utilisateur : Jean
Action : modification du prix
Produit : iPhone 13
Ancien prix : 4 000 000
Nouveau prix : 3 900 000

Cela nous donnera de la traçabilité.

C'est également utile pour :

sécurité ;
audit ;
support ;
résolution d'incidents ;
responsabilité des utilisateurs.
# 21. Notes

Chaque boutique pourra avoir un espace de notes partagé.

Exemple :

Titre :
Fermeture exceptionnelle


Contenu :
La boutique sera fermée vendredi...

Les notes sont visibles selon les permissions définies.

# 22. Tableau de bord

Le commerçant pourra voir notamment :

ventes du jour ;
bénéfice ;
commandes ;
articles vendus ;
produits en rupture ;
évolution des ventes ;
produits les plus vendus ;
performance des vendeurs.

Mais attention :

Le tableau de bord ne doit pas devenir un énorme calculateur.

Nous devrons réfléchir plus tard à :

performances ;
agrégations ;
cache ;
requêtes SQL ;
pagination ;
indexation.

Cela fera partie de notre apprentissage d'architecture.

# 23. Multilingue

La première version :

Français 🇫🇷
Anglais 🇬🇧

Mais l'architecture doit permettre d'ajouter :

Portugais
Espagnol
Arabe
etc.

sans réécrire l'application.

# 24. Mobile

L'application mobile sera développée avec Flutter.

Cibles :

Flutter
 ├── Android
 └── iOS

Elle devra supporter :

authentification ;
gestion commerciale ;
notifications ;
mode offline ;
synchronisation ;
gestion des conflits.

Le mode offline sera un gros sujet technique que nous étudierons sérieusement.

# 25. Web

Le Web devra également supporter un mode offline pour certaines fonctionnalités.

Architecture cible :

React / Next.js / Vite
             ↓
          API REST
             ↓
          Backend
             ↓
         Database

Mobile :

Flutter
   ↓
API REST
   ↓
Backend
   ↓
Database

Donc Web et Mobile partageront un même contrat API lorsqu'ils doivent partager les données.

# 26. Notifications

Le système devra envoyer notamment :

Abonnement
24h avant expiration
       ↓
Notification

En cas de non-paiement :

Expiration
   ↓
Alerte
   ↓
72h GRACE_PERIOD
   ↓
Alertes
   ↓
Suspension

Nous avons également défini :

rappel toutes les 30 minutes pendant la période de suspension liée au non-paiement.

Nous devrons cependant concevoir cela intelligemment pour éviter de générer inutilement une charge énorme lorsque nous aurons beaucoup de commerçants.

# 27. Abonnement et suspension

Un abonnement dure :

30 jours

En cas de non-paiement :

Expiration
     ↓
GRACE_PERIOD
     ↓
72 heures
     ↓
Suspension

Les données ne sont pas supprimées.

Après paiement :

Paiement
   ↓
Réactivation
   ↓
Données conservées
# 28. Ce que nous avons maintenant

Notre système commence à ressembler à ceci :

                    BANGS 224
                       │
                       ▼
                  COMMERÇANT
                       │
          ┌────────────┼─────────────┐
          ▼            ▼             ▼
       Boutique A   Boutique B   Boutique C
          │
    ┌─────┼─────┬──────┬───────┐
    ▼     ▼     ▼      ▼       ▼
 Produits Stock Ventes Clients Employés
                       │
                       ▼
                 Fournisseurs
                       │
                       ▼
                  Achats
                       │
                       ▼
                  Réceptions
                       │
                       ▼
                    Stock
# 29. Mais notre cahier des charges n'est pas encore terminé

Je veux volontairement m'arrêter ici avant de considérer le cahier des charges comme terminé.

Il nous manque encore plusieurs décisions importantes :

A. Identité et inscription
Comment créer le compte ?
Email ?
Téléphone ?
WhatsApp ?
Vérification du numéro ?
Mot de passe ?
récupération du compte ?
B. Multi-boutiques
Un employé peut-il travailler dans plusieurs boutiques ?
Un vendeur peut-il changer de boutique ?
Un administrateur peut-il voir toutes les boutiques ?
C. Permissions

Nous avons les rôles, mais il faut construire la matrice complète des permissions.

D. Ventes
Retour produit ?
Annulation ?
Remboursement ?
Vente à crédit ?
Réduction ?
Taxes ?
Plusieurs moyens de paiement dans une même vente ?
E. Stock
Inventaire ?
Transfert de stock entre boutiques ?
Produit périssable ?
Lots ?
Numéros de série ?
Stock négatif autorisé ou interdit ?
F. Achats
Annulation ?
Réception partielle ?
Retour fournisseur ?
Facture fournisseur ?
G. Abonnement
Paiement échoué ?
Renouvellement automatique ?
Facture ?
Changement d'offre ?
Passage Web → Web+Mobile ?
Annulation ?
H. Offline

C'est un domaine particulièrement important :

Que peut-on faire hors connexion ?
Que ne peut-on pas faire ?
Comment synchroniser ?
Que se passe-t-il si deux appareils modifient la même donnée ?