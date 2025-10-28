from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita
from .forms import ReceitaForm

# Lista todas as receitas
def listar_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/lista.html', {'receitas': receitas})

# Detalhes de uma receita
def detalhe_receita(request, id):
    receita = get_object_or_404(Receita, id=id)
    return render(request, 'receitas/detalhe.html', {'receita': receita})

# Cadastrar nova receita
def nova_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('receitas:lista')
    else:
        form = ReceitaForm()
    return render(request, 'receitas/nova_receita.html', {'form': form})
