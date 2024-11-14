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

def seleccionarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})

def editarMateria(request):
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    materia.save() # actualiza registros
    return redirect("/")

def borrarMaterias(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete() # borra el registro

    return redirect("/")