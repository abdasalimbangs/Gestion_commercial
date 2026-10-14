import secrets
from datetime import timedelta
from django.utils import timezone
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

    est_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "telephone"

    objects = UtilisateurManager()

# Definition de la classe OTP pour la generer le code OTP
class VerificationTelephone(models.Model):
    verification_id = models.BigAutoField(primary_key=True)
    utilisateur = models.ForeignKey(
        "comptes.Utilisateur",
        on_delete=models.CASCADE,
        related_name="verifications_telephone"
    )
    code_hache = models.CharField(max_length=128)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    nombre_tentatives = models.PositiveSmallIntegerField(default=0)
    date_dernier_envoi = models.DateTimeField(default=timezone.now)
    est_utilise = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Vérification de téléphone"
        verbose_name_plural = "Vérifications de téléphone"
        ordering = ["-date_creation"]

    def __str__(self):
        return f"Vérification de {self.utilisateur.telephone}"

    @property
    def est_expire(self):
        return timezone.now() >= self.date_expiration
