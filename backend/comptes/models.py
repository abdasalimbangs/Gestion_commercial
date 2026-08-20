from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

# Définition de la classe Utilisateur 
class Utilisateur(AbstractBaseUser,PermissionsMixin ):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)


    