from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

from .serializers import UtilisateurSerializer

# notre vue accepte uniquement les requêtes HTTP POST.
# Définition de la fonction pour l'inscription d'un client
@extend_schema(
    request = UtilisateurSerializer,
    responses = {201: None},
)

@api_view(["POST"])
@permission_classes([AllowAny])
def inscription(request):
    serializer = UtilisateurSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(
        {"message": "Compte créé avec succès"},
        status=status.HTTP_201_CREATED
    )
