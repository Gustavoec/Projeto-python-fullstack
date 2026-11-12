from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do Cliente")
    telefone = models.CharField(max_length=20, verbose_name="Telefone / WhatsApp")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    endereco = models.TextField(blank=True, null=True, verbose_name="Endereço")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    def __str__(self):
        return f"{self.nome} ({self.telefone})"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto / Pendente'),
        ('ANALISE', 'Em Análise / Bancada'),
        ('ANDAMENTO', 'Em Andamento'),
        ('AGUARDANDO_PECA', 'Aguardando Peças'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    titulo_equipamento = models.CharField(max_length=100, verbose_name="Equipamento / Modelo (ex: Notebook Dell i5)")
    numero_serie = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número de Série")
    descricao = models.TextField(verbose_name="Relato do Problema / Defeito")
    laudo_tecnico = models.TextField(blank=True, null=True, verbose_name="Laudo Técnico / Solução Aplicada")
    custo_pecas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Custo de Peças (R$)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTO', verbose_name="Status")
    valor_orcamento = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                                          verbose_name="Valor do Orçamento (R$)")

    tecnico_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                            verbose_name="Técnico Responsável")
    data_abertura = models.DateTimeField(auto_now_add=True, verbose_name="Data de Abertura")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome} ({self.titulo_equipamento})"

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"