from rest_framework import viewsets
from .serializer import PublicacionSerializer, VideosPublicacionSerializer, ComentariosPublicacionSerializer
from .models import Publicacion, capitulosPublicacion, Comentarios
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from usuarios.models import Usuarios
# Create your views here.

class PublicacionViewSet(viewsets.ModelViewSet):
  queryset = Publicacion.objects.all()
  serializer_class = PublicacionSerializer
  parser_classes  = (MultiPartParser, FormParser)
  
  def create(self, request, *args, **kwargs):
   cedulaCreador_id = request.data['cedulaCreador']
   tituloPublicacion = request.data['tituloPublicacion']
   descripcionPublicacion =  request.data['descripcionPublicacion']
   tipoPublicacion = request.data['tipoPublicacion']
   fechaPublicacion = request.data['fechaPublicacion']
   miniatura = request.data['miniatura']
   
   cedulaCreador = Usuarios.objects.get(cedula=cedulaCreador_id)
   
   Publicacion.objects.create(cedulaCreador = cedulaCreador, tituloPublicacion = tituloPublicacion, descripcionPublicacion = descripcionPublicacion, tipoPublicacion = tipoPublicacion, fechaPublicacion = fechaPublicacion, miniatura = miniatura)
   return Response('Publicacion creada..')

class VideosPublicacionViewSet(viewsets.ModelViewSet):
  queryset = capitulosPublicacion.objects.all()
  serializer_class = VideosPublicacionSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
  queryset = Comentarios.objects.all()
  serializer_class = ComentariosPublicacionSerializer