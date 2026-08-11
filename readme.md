# — Analyse métier
SaaS de gestion commerciale.
# Context :
# — Le contexte de l'entreprise

une petite entreprise qui vend des produits.

Aujourd'hui, elle gère ses activités avec :

Excel ;
cahiers ;
WhatsApp ;
fichiers dispersés.

Elle commence à avoir plusieurs problèmes :

elle ne sait pas toujours combien de produits restent en stock ;
certaines commandes sont oubliées ;
les informations clients sont dispersées ;
elle a du mal à suivre ses ventes ;
plusieurs employés travaillent sur les mêmes informations ;
elle ne sait pas clairement qui a effectué quelle action.

Notre mission sera donc de concevoir une application permettant de centraliser et sécuriser la gestion commerciale.

# 1. Qui va utiliser l'application ?

Il y aura plusieurs types d'utilisateurs :

# Administrateur : responsable de l'entreprise.
# Vendeur : s'occupe des ventes et des clients.
# Gestionnaire de stock : s'occupe des produits et du stock.

# 2. Quelles fonctionnalités ?

Le client veut principalement :

gérer les utilisateurs ;
gérer les produits ;
gérer les catégories ;
gérer les clients ;
gérer le stock ;
enregistrer les ventes ;
suivre les commandes ;
consulter des statistiques.

# 3. Quels sont les besoins ?

Le client veut :

centraliser les informations ;
éviter les erreurs de stock ;
savoir qui a effectué une opération ;
retrouver facilement un client ;
suivre les ventes ;
connaître les produits disponibles ;
avoir une vision globale de l'activité.

# 4. Qu'est-ce qu'on va gérer ?

Pour l'instant, on devra gérer :

Utilisateurs
Produits
Catégories
Clients
Stock
Ventes
Commandes

# 5. Est-ce qu'il y aura plusieurs utilisateurs ?

un point important :

Tous les utilisateurs n'auront pas les mêmes droits.

Par exemple :

Administrateur
      │
      ├── peut gérer les utilisateurs
      ├── peut consulter les statistiques
      └── peut gérer l'ensemble du système

Vendeur
      │
      ├── peut gérer les clients
      ├── peut enregistrer les ventes
      └── peut consulter les produits

Gestionnaire stock
      │
      ├── peut gérer les produits
      ├── peut modifier le stock
      └── peut consulter les ventes