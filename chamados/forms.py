from django import forms
from .models import Cliente, OrdemServico

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(33) 99999-9999'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Endereço'}),
        }

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['cliente', 'titulo_equipamento', 'descricao', 'status', 'valor_orcamento']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'titulo_equipamento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Notebook Dell i5'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descreva o defeito...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'valor_orcamento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
        }