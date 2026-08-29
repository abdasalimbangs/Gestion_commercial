from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# Définition de la classe manager de l'utilisation
    class UtilisateurManager(BaseUserManager):  

        def create_user(self, nom, prenom, telephone, mot_de_passe, email=None, adresse=None):

            utilisateur = self.model(
                nom = nom,
                prenom = prenom,
                telephone = telephone,
                email = email,
                adresse = adresse
            )
            utilisateur.set_password(mot_de_passe)
            utilisateur.save()

            return utilisateur

        def create_superuser(self, nom, prenom, telephone, mot_de_passe, email=None, adresse=None):

            utilisateur = self.create_user(
                nom, 
                prenom, 
                telephone, 
                mot_de_passe, 
                email, 
                adresse
            )
            
            utilisateur.is_staff = True 
            utilisateur.is_superuser = True

            utilisateur.save()

            return utilisateur

    

# Définition de la classe Utilisateur 
class Utilisateur(AbstractBaseUser,PermissionsMixin ):
    
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)

    telephone = models.CharField(
        max_length=15, 
        unique=True
    )
    email = models.EmailField(
        unique=True, 
        null=True, 
        blank=True
    )
    adresse = models.CharField(
        max_length=225,
        null=True,
        blank=True
    )

    est_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "telephone"

    objects = UtilisateurManager()
