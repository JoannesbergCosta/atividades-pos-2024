from django.shortcuts import render
from rest_framework import viewsets
from .models import Artista, Album, Musica
from .serializers import ArtistaSerializer, AlbumSerializer, MusicaSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        artista_ins = self.kwargs.get('artista_ins')
        if artista_ins is not None:
            return Album.objects.filter(artista=artista_ins)
        return super().get_queryset()

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

    def get_queryset(self):
        album_ins = self.kwargs.get('album_ins')
        if album_ins is not None:
            return Musica.objects.filter(album=self.kwargs['album_ins'])
        return super().get_queryset()