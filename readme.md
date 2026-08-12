# 1. Notre véritable produit

      l'éditeur du logiciel.

                        Moi
                  Éditeur du SaaS
                        │
            ┌─────────┼─────────┐
            ↓         ↓         ↓
            Client A   Client B   Client C
            Commerce   Commerce   Commerce

      Chaque commerçant :

      achète une licence ;
      paie un abonnement mensuel, par exemple 15 $/mois ;
      possède son propre espace ;
      possède ses propres utilisateurs ;
      possède ses propres produits ;
      possède ses propres clients ;
      possède ses propres ventes ;
      ne doit jamais voir les données d'un autre commerçant.

# Par exemple :

 SaaS
 │
 ├── Entreprise A
 │      ├── Admin
 │      ├── Vendeurs
 │      ├── Stock
 │      ├── Produits
 │      └── Ventes
 │
 ├── Entreprise B
 │      ├── Admin
 │      ├── Vendeurs
 │      ├── Stock
 │      ├── Produits
 │      └── Ventes
 │
 └── Entreprise C
        ├── Admin
        ├── Vendeurs
        ├── Stock
        ├── Produits
        └── Ventes

# Entreprise A ne doit absolument jamais pouvoir accéder aux données de B.

# A. L'application du commerçant

      C'est ce que le client utilise.

      Commerçant
      ↓
      Application SaaS
      ↓
      API
      ↓
      Données de son entreprise

# B. Ton Back Office

      C'est mon espace à moi, en tant qu'éditeur du SaaS.

      MOI
      ↓
      Back Office
      ↓
      Gestion du SaaS

      Mon Back Office pourra progressivement permettre de gérer :

      les entreprises clientes ;
      les abonnements ;
      les licences ;
      les utilisateurs ;
      les plans ;
      l'état des comptes ;
      les paiements ;
      les instances ;
      les incidents ;
      les statistiques globales ;
      éventuellement le support.

# Architecture A — SaaS centralisé

                    INTERNET
                       │
                       ▼
                  Notre SaaS
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      Client A      Client B      Client C

# Tous utilisent la même plateforme.

      Architecture B — une instance par client
      Client A → Instance A
      Client B → Instance B
      Client C → Instance C

# Notre diagramme commence à devenir intéressant :

                         SYSTÈME
                            │
             ┌──────────────┴──────────────┐
             │                             │
       Éditeur SaaS                 Entreprise cliente
             │                             │
       Back Office                 ┌───────┼───────┐
                                   │       │       │
                                 Admin   Vendeur  Stock

# Niveau SaaS
      Super Admin / Éditeur

# Niveau entreprise
      Admin entreprise
      Vendeur
      Gestionnaire stock

# 1. Les décisions que je viens de prendre

Je les considère maintenant comme des décisions produit du projet.

# Modèle SaaS
      Visiteur
      ↓
      Création de compte
      ↓
      Choix abonnement
      ↓
      Paiement
      ↓
      Création de l'espace entreprise
      ↓
      Utilisation du SaaS
 
# Tarification actuelle

Offre	              Prix

Web	              15 $ / mois
      
Mobile	        35 $ / mois

# Impayé

Si l'abonnement n'est pas payé :

      Abonnement arrive à échéance
            ↓
      Paiement non effectué
            ↓
      Compte suspendu

# Nous partons plutôt sur :

                 BANGS 224
                     │
                Application
                     │
              ┌──────┴──────┐
              │     API      │
              └──────┬──────┘
                     │
                 Database
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
  Entreprise A   Entreprise B   Entreprise C
     espace          espace          espace

Et ça nous permettra d'introduire un concept très important :

Multi-tenancy

Chaque entreprise sera une tenant.

Par exemple :

Entreprise A
tenant_id = A

Entreprise B
tenant_id = B

Entreprise C
tenant_id = C

Une vente de A appartient à A.

Une vente de B appartient à B.

Et notre système doit garantir qu'une requête provenant de A ne puisse jamais récupérer les données de B.   
# Notre modèle métier commence à apparaître

Notre vision commence à devenir :

                         BANGS 224
                            │
             ┌──────────────┴──────────────┐
             │                             │
         BACK OFFICE                  CLIENTS SaaS
             │                             │
      Gestion globale                 Entreprises
             │                             │
      ┌──────┼──────┐              ┌───────┼───────┐
      │      │      │              │       │       │
   Clients Abonn. Paiements      Admin  Vendeur  Stock
                                      │
                              ┌───────┴────────┐
                              │                │
                             WEB             MOBILE
                           15 $/mois         35 $/mois
                              │                │
                              └───────┬────────┘
                                      │
                               MÊMES DONNÉES
                                      │
                                   API REST
                                      │
                                  DATABASE
Et avec :

multi-tenant ;
Web offline ;
Mobile offline ;
notifications ;
Français / Anglais ;
multi-pays ;
abonnement ;
paiement ;
période de grâce ;
suspension ;
réactivation.


# Je veux maintenant qu'on fasse quelque chose de très important avant de parler de base de données :

définir précisément les acteurs de Bangs 224.

Il y a actuellement :

Super Admin Bangs 224
Administrateur de l'entreprise cliente
Vendeur
Gestionnaire de stock
Client du commerçant
éventuellement Visiteur avant inscription.

Nous allons pour chacun définir :

Qui est-il ? Que peut-il faire ? Que ne peut-il pas faire ?

# Les acteurs de Bangs 224
# 1. Super Admin Bangs 224

Il travaille dans le Back Office Bangs 224.

Il pourrait gérer :

les entreprises clientes ;
les abonnements ;
les paiements ;
les suspensions ;
les réactivations ;
les utilisateurs ;
le support ;
les statistiques globales.

Mais attention :

Question importante

Est-ce que le Super Admin Bangs 224 doit pouvoir entrer dans l'espace commercial d'un client et voir :

ses produits ;
ses ventes ;
ses clients ;
son stock ?

Ou bien doit-il uniquement gérer le compte SaaS, sans accéder aux données commerciales du client ?

Je préfère personnellement la deuxième approche par défaut, pour des raisons de confidentialité et de sécurité, avec un mécanisme exceptionnel d'accès support/audit si nécessaire et traçable.

# 2. Administrateur de l'entreprise

C'est le propriétaire ou responsable du commerce.

Il possède son espace :

Entreprise A
    ↓
Administrateur

Il pourra probablement :

configurer son entreprise ;
gérer les utilisateurs ;
créer des vendeurs ;
créer des gestionnaires de stock ;
gérer les produits ;
gérer les catégories ;
gérer les clients ;
consulter les ventes ;
consulter les statistiques ;
gérer son abonnement.

Mais nous devons faire attention à une chose :

L'administrateur de l'entreprise n'est pas un Super Admin Bangs 224.

Il ne doit jamais pouvoir :

voir les autres entreprises ;
modifier l'abonnement d'une autre entreprise ;
accéder au Back Office Bangs 224 ;
modifier la plateforme globale.

# 3. Vendeur

Son objectif principal :

effectuer et gérer les ventes.

Il pourrait :

consulter les produits disponibles ;
rechercher un produit ;
créer une vente ;
consulter ses ventes ;
consulter certains clients ;
créer un client ;
consulter les informations nécessaires à la vente.

Mais nous avons déjà établi une règle :

❌ Il ne modifie pas directement le stock.

Pourquoi ?

Parce que nous avons une séparation des responsabilités :

Vendeur
   ↓
Vente
   ↓
Système
   ↓
Stock mis à jour

Le vendeur provoque une modification du stock par une vente, mais il ne doit pas pouvoir dire directement :

« Stock = 500 »

C'est une distinction métier très importante.

# 4. Gestionnaire de stock

Responsabilité principale :

gérer les stocks.

Il pourrait :

créer/modifier des produits ;
gérer les catégories ;
enregistrer les entrées de stock ;
enregistrer les sorties ;
consulter le stock ;
recevoir des alertes de stock faible.

Mais il ne doit pas pouvoir :

❌ gérer les ventes comme un vendeur.

# 5. Client du commerçant

Attention ici.

Le client du commerçant n'est pas forcément un utilisateur de Bangs 224.

Exemple :

Bangs 224
    │
    └── Commerce de Mamadou
            │
            ├── Admin
            ├── Vendeur
            ├── Stock
            │
            └── Clients
                  ├── Client A
                  ├── Client B
                  └── Client C

Le client A est simplement une donnée métier appartenant au commerçant.

Il n'a pas nécessairement de compte Bangs 224.

C'est important de ne pas confondre :

Utilisateur de Bangs 224

et

Client du commerçant.
# 6. Visiteur

Avant inscription :

Visiteur
   ↓
Site Bangs 224

Il peut :

consulter les offres ;
voir les fonctionnalités ;
créer un compte ;
choisir une formule ;
commencer le paiement.

Il n'a pas encore accès aux données commerciales.

# RBAC = Role-Based Access Control

C'est-à-dire :

Utilisateur
     ↓
Entreprise
     ↓
Rôle
     ↓
Permissions
     ↓
Actions autorisées