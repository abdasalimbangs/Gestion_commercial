from rest_framework import serializers
from .models import Utilisateur

#Classe pour transformation les donnée jSon en Objet
class UtilisateurSerializer(serializers.ModelSerializer):

    mot_de_passe = serializers.CharField(write_only=True)

    class Meta:
        model = Utilisateur
        fields = [
            "nom",
            "prenom",
            "telephone",
            "email",
            "adresse",
            "mot_de_passe",
        ]

    def create(self, validated_data):
        mot_de_passe = validated_data.pop("mot_de_passe")

        utilisateur = Utilisateur(**validated_data)
        utilisateur.set_password(mot_de_passe)
        utilisateur.save()

        return utilisateur
