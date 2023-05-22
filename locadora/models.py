from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Locacao(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=50)
    valor = models.FloatField()
    locacao = models.ManyToManyField(Locacao)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo