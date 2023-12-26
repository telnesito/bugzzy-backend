from django.urls import path, include
from rest_framework import routers
from publicacion import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'p', views.PublicacionViewSet)
router.register(r'v_p', views.VideosPublicacionViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('docs', include_docs_urls(title='Publicacion API'))
]