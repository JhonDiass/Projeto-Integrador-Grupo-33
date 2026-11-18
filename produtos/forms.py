from django import forms
from .models import Produto 

class ProdutoForm(forms.ModelForm): # Define a classe ProdutoForm, que é um formulário baseado no modelo Produto.
    class Meta: # Define a classe Meta, que contém informações sobre o formulário.
        model = Produto # Especifica que o formulário é baseado no modelo Produto.
        fields = ['codigo', 'nome', 'descricao', 'categoria', 'preco', 'quantidade_estoque', 'fornecedor'] # Define os campos do formulário que serão exibidos e processados.