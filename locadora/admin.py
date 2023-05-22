from django.contrib import admin
from .models import Filme, Categoria, Cliente, Locacao

# Register your models here.
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ("nome",)

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ("nome", "email")

@admin.register(Locacao)
class Locacao(admin.ModelAdmin):
    list_display = ("nome", "data", "cliente")

@admin.register(Filme)
class Filme(admin.ModelAdmin):
    list_display = ("titulo", "valor", "categoria")