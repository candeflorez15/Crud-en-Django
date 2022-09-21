from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def metrica(request):
    metrica = Paciente.objects.all()
    return render(request, 'metrica/index.html', {'metrica': metrica})

def crear(request):
    formulario = PacienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('metrica')
    return render(request, 'metrica/crear.html', {'formulario': formulario})

def editar(request, id):
    paciente = Paciente.objects.get(id=id)
    formulario = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('metrica')
    return render(request, 'metrica/editar.html', {'formulario': formulario})
def eliminar(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return redirect('metrica')