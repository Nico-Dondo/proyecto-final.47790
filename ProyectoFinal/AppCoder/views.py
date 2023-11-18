from django.shortcuts import render
from django.http import HttpResponse

def inicio_view(request):
    return HttpResponse ("Bienvenidos")

def cursos_view(request):
   # return HttpResponse("Pagina de prueba")
   return render(request, "AppCoder/padre.html")

