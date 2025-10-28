from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'modo_preparo', 'categoria', 'imagem']