from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# Définition de la classe manager de l'utilisation
class UtilisateurManager(BaseUserManager):  

    def create_user(self, nom, prenom, telephone, mot_de_passe):

        utilisateur = self.model(
            nom = nom,
            prenom = prenom,
            telephone = telephone
        )
        utilisateur.set_password(mot_de_passe)
        utilisateur.save()

        return utilisateur
    

# Définition de la classe Utilisateur 
class Utilisateur(AbstractBaseUser,PermissionsMixin ):
    
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    USERNAME_FIELD = "telephone"

    objects = UtilisateurManager()
