from django.shortcuts import render,redirect
from .models import Materia

# Create your views here.
def inicio_vista(request):
    LasMaterias=Materia.objects.all()
    return render(request,"GestionarMateria.html",{"mismaterias":LasMaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarMateria=Materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)#GUARDA EL REGISTRO

    return redirect("/")