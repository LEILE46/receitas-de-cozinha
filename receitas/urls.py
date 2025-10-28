from django.urls import path
from . import views

app_name = 'receitas'

urlpatterns = [
    path('', views.listar_receitas, name='lista'),
    path('nova/', views.nova_receita, name='nova'),
    path('<int:id>/', views.detalhe_receita, name='detalhe'),
]