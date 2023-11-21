from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def inicio_view(request):
    return HttpResponse ("Bienvenidos")

def cursos_view(request):
   # return HttpResponse("Pagina de prueba")
   return render(request, "AppCoder/padre.html")

