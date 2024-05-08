from django.urls import path
from .views import usuarios, registrar_usuario


urlpatterns = [
 path("usuarios", usuarios, name="usuarios"),
 path("registrar_usuario", registrar_usuario, name="registrar_usuario")
]