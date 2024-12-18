from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

# Criação do roteador principal
router = routers.DefaultRouter()
router.register(r'artistas', views.ArtistaViewSet)
router.register(r'albuns', views.AlbumViewSet)
router.register(r'musicas', views.MusicaViewSet)

# Configuração das URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Inclui todas as URLs registradas no router
]
