from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita
from .forms import ReceitaForm

def listar_receitas(request):
    categoria = request.GET.get('categoria')
    if categoria:
        receitas = Receita.objects.filter(categoria=categoria)
    else:
        receitas = Receita.objects.all()
    
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()
    
    context = {
        'receitas': receitas,
        'categorias': categorias
    }
    return render(request, 'lista.html', context)

def detalhe_receita(request, id):
    receita = get_object_or_404(Receita, id=id)
    return render(request, 'detalhes.html', {'receita': receita})

def nova_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('receitas:lista')
    else:
        form = ReceitaForm()
    return render(request, 'nova_receita.html', {'form': form})
def excluir_receita(request, id):
    receita = get_object_or_404(Receita, id=id)

    if request.method == 'POST':
        receita.delete()
        return redirect('receitas:lista') 


    return redirect('receitas:detalhe', id=id)