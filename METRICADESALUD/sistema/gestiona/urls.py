from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('metrica', views.metrica, name='metrica'),
    path('metrica/crear', views.crear, name='crear'),
    path('metrica/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('metrica/editar/<int:id>', views.editar, name='editar'),


]
