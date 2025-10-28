from django.db import models

class Receita(models.Model):
    CATEGORIAS = [
        ('Sopa', 'Sopa'),
        ('Doce', 'Doce'),
        ('Principal', 'Prato Principal'),
        ('Salada', 'Salada'),
    ]

    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagem = models.ImageField(upload_to='receitas/', blank=True, null=True)

    def __str__(self):
        return self.nome
