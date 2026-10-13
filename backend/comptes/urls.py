from .views import inscription
from django.urls import path

urlpatterns = [
    path("inscription/", inscription, name="inscription")
]