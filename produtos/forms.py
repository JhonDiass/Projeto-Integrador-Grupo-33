from django import forms
from .models import Produto, Fornecedor

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'descricao', 'categoria', 'preco', 'quantidade_estoque', 'fornecedor']

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: PRO-001'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva o produto...', 'rows': 4}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Eletrônicos'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0,00', 'step': '0.01'}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
        }