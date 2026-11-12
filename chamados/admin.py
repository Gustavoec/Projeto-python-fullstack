from django.contrib import admin
from .models import Cliente, OrdemServico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email', 'data_cadastro')
    search_fields = ('nome', 'telefone', 'email')

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'titulo_equipamento', 'status', 'valor_orcamento', 'data_abertura')
    list_filter = ('status', 'data_abertura')
    search_fields = ('titulo_equipamento', 'cliente__nome', 'numero_serie')
    list_editable = ('status',)