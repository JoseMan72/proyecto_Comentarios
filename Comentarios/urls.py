from django.urls import path
from . import views

urlpatterns = [
   path('', views.Lista_comentarios, name='lista_comentarios'),
   path('formulario/', views.Formulario.as_view(), name='formulario'),
   path('confirmacion/', views.confirmacion, name='confirmacion'),
]