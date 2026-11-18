from django.db import models # Importa o módulo models do Django, que fornece classes e funções para definir modelos de banco de dados.
from fornecedores.models import Fornecedor # Importa o modelo Fornecedor do aplicativo fornecedores para criar uma relação entre produtos e fornecedores.

# Create your models here.
class Produto(models.Model): # Define a classe Produto, que representa um produto no sistema de gestão de estoque.
    codigo = models.CharField(max_length=13, unique=True) # Define o código do produto, que é um campo de texto com no máximo 13 caracteres e deve ser único.
    nome = models.CharField(max_length=100) # Define o nome do produto, que é um campo de texto com no máximo 100 caracteres.
    descricao = models.TextField() # Define a descrição do produto, que é um campo de texto que pode conter várias linhas.
    categoria = models.CharField(max_length=50) # Define a categoria do produto, que é um campo de texto com no máximo 50 caracteres.
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Define o preço do produto, que é um número decimal com até 10 dígitos no total e 2 casas decimais.
    quantidade_estoque = models.PositiveIntegerField() # Define a quantidade de produtos em estoque, que deve ser um número inteiro positivo.
    fornecedor = models.ForeignKey('fornecedores.Fornecedor', on_delete=models.PROTECT, related_name='produtos') # Cria uma relação com o modelo Fornecedor, e impede que um fornecedor seja deletado se houver produtos associados a ele.
    data_cadastro = models.DateTimeField(auto_now_add=True) # Define a data de cadastro do produto, que é preenchida automaticamente com a data e hora atuais quando o produto é criado.

    def __str__(self): # Define o método __str__ para retornar uma representação legível do objeto Produto, que neste caso é o nome do produto.
        return self.nome # Retorna o nome do produto quando o objeto for convertido para string.