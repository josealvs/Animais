from urllib import request
from django import forms
from .models import Resgate, Denuncia

class ResgateForm(forms.ModelForm):
    class Meta:
        model = Resgate
        fields = {'animal', 'estado', 'descricao', 'cidade', 'data', 'local'}

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = {'animal', 'descricao', 'data', 'local', 'cidade'}