from django.shortcuts import render
from django.views import View
from .models import Comentario
from .forms import ComentarioForm

# Create your views here.

#  Crea las siguientes vistas:
#formulario: que muestre el formulario en una página web y lo procese cuando se envíe y almacene los comentarios en una base de datos.
#confirmación: Implementa una página de confirmación que muestre un mensaje de agradecimiento después de enviar el formulario.
#Lista_comentarios: crea una vista para una web que muestre un listado con todos los comentarios.

class Formulario(View):
   def get(self, request):
      form = ComentarioForm()
      return render(request, 'Comentarios/formulario.html', {'form': form})

def Lista_comentarios(request):
   comentarios = Comentario.objects.all()
   return render(request, 'Comentarios/lista_comentarios.html', {'comentarios': comentarios})

class Confirmacion(View):
   def post(self, request):
      form = ComentarioForm(request.POST)
      if form.is_valid():
         form.save()
         comentario = Comentario.objects.last()
         return render(request, 'Comentarios/confirmacion.html', {'form': form, 'comentario': comentario})
      return render(request, 'Comentarios/formulario.html', {'form': form})

   def get(self, request):
      form = ComentarioForm()
      return render(request, 'Comentarios/confirmacion.html', {'form': form})