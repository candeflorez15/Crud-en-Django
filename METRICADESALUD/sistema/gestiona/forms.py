from dataclasses import field
from pyexpat import model
from socket import fromshare
from django import forms 
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'