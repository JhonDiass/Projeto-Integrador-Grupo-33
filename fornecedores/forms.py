from django import forms # Importa o módulo forms do Django, que fornece classes e funções para criar formulários web.
from .models import Fornecedor # Importa o modelo Fornecedor do aplicativo fornecedores para criar um formulário baseado nesse modelo.

class FornecedorForm(forms.ModelForm): # Define a classe FornecedorForm, que é um formulário baseado no modelo Fornecedor.
    class Meta: # Define a classe Meta, que contém informações sobre o formulário.
        model = Fornecedor # Especifica que o formulário é baseado no modelo Fornecedor.
        fields = ['nome', 'cnpj', 'telefone', 'email', 'endereco'] # Define os campos do formulário que serão exibidos e processados.