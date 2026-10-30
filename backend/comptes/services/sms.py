# Importe la bibliothèque qui permet d'envoyer des requêtes HTTP.
import requests

# Importe l'objet settings qui donne accès à la configuration Django.
from django.conf import settings


# Définit une erreur personnalisée pour les problèmes d'envoi de SMS.
class ErreurEnvoiSMS(Exception):
    # Décrit le rôle de cette classe d'erreur.
    """Erreur rencontrée lors de l'envoi d'un SMS."""


# Définit la fonction chargée d'envoyer un SMS.
def envoyer_sms(telephone, message):

    # Récupère la clé API depuis la configuration Django.
    cle_api = settings.ESMS_API_KEY

    # Vérifie que la clé API est disponible.
    if not cle_api:

        # Arrête l'exécution si la clé API est absente.
        raise ErreurEnvoiSMS(
            # Fournit un message expliquant la cause de l'erreur.
            "La clé API eSMS Africa n'est pas configurée."
        )

    # Définit l'adresse du service d'envoi SMS.
    url = "https://sms.esmsafrica.io/api/messages/send"

    # Prépare les informations qui accompagneront la requête HTTP.
    entetes = {

        # Transmet la clé API pour authentifier la demande.
        "Authorization": f"Bearer {cle_api}",

        # Indique que les données envoyées sont au format JSON.
        "Content-Type": "application/json",
    }

    # Prépare les données du SMS à transmettre au fournisseur.
    donnees = {

        # Indique le numéro de téléphone du destinataire.
        "to": telephone,

        # Indique le contenu du message à envoyer.
        "text": message,
    }

    # Commence le bloc de gestion des erreurs réseau.
    try:

        # Envoie la requête POST au service SMS.
        reponse = requests.post(

            # Indique l'adresse du service destinataire.
            url,

            # Ajoute les informations d'authentification et de format.
            headers=entetes,

            # Convertit les données en JSON pour la requête.
            json=donnees,

            # Interrompt l'attente après 15 secondes.
            timeout=15,
        )

    # Intercepte les erreurs réseau gérées par la bibliothèque requests.
    except requests.RequestException as erreur:

        # Transforme l'erreur technique en erreur propre à notre application.
        raise ErreurEnvoiSMS(

            # Fournit un message compréhensible à l'application.
            "Impossible de joindre le service SMS."

        # Conserve l'erreur initiale comme cause pour le diagnostic.
        ) from erreur

    # Vérifie si le serveur a répondu avec un statut HTTP de réussite.
    if not reponse.ok:

        raise ErreurEnvoiSMS(

            f"eSMS Africa a refusé la requête "
            f"(HTTP {reponse.status_code})."
        )

    # Vérifer que le fournisseur à renvoyer un contenu 
    if not reponse.content.strip():

        raise ErreurEnvoiSMS(
            
            "eSMS Africa a renvoyé une réponse vide."
        )
    # Tente de convertir la réponse en objet Python.
    try:
        resultat = reponse.json()

    # Intercepte une réponse qui ne contient pas de JSON valide.
    except ValueError as erreur:

        raise ErreurEnvoiSMS(

            "La réponse d'eSMS Africa n'est pas un JSON valide."
        ) from erreur

    # Retourne les données reçues pour que l'appelant puisse les exploiter.
    return resultat