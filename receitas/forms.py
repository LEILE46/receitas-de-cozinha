from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'categoria', 'ingredientes', 'modo_preparo', 'imagem']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome da receita deve ter pelo menos 3 caracteres.")
        return nome

    def clean_ingredientes(self):
        ingredientes = self.cleaned_data.get('ingredientes')
        if "veneno" in ingredientes.lower():
            raise forms.ValidationError("Ingredientes inválidos! 😅")
        return ingredientes