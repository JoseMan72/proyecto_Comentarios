from django.urls import path
from .views import Lista_comentarios, Formulario, DetailsConfirmacion, EditComentario, DeleteComentario

urlpatterns = [
   path('', Lista_comentarios.as_view(), name='lista_comentarios'),
   path('formulario/', Formulario.as_view(), name='formulario'),
   path('confirmacion/<int:pk>/', DetailsConfirmacion.as_view(), name='confirmacion'),
   path('comentario/<int:pk>/edit/', EditComentario.as_view(), name='comentario_edit'),
   path('comentario/<int:pk>/delete/', DeleteComentario.as_view(), name='comentario_delete'),
]