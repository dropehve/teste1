from django.urls import path
from . import views

urlpatterns = [
    path('listar-lesoes/', views.listar_lesoes, name='listar_lesoes'),
]

urlpatterns += [
    path('buscar/', views.buscar, name='buscar'),
    path('resultado/', views.resultado_busca, name='resultado'),
]