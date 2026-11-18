from django.db import models

# Create your models here.
class Fornecedor(models.Model): # Define a classe Fornecedor, que representa um fornecedor no sistema de gestão de estoque.
    nome = models.CharField(max_length=100) # Define o nome do fornecedor, que é um campo de texto com no máximo 100 caracteres.
    cnpj = models.CharField(max_length=18, unique=True) # Define o CNPJ do fornecedor, que é um campo de texto com no máximo 18 caracteres e deve ser único.
    telefone = models.CharField(max_length=20) # Define o telefone do fornecedor, que é um campo de texto com no máximo 20 caracteres.
    email = models.EmailField(max_length=100, unique=True) # Define o email do fornecedor, que é um campo de email com no máximo 100 caracteres e deve ser único.
    endereco = models.CharField(max_length=200) # Define o endereço do fornecedor, que é um campo de texto com no máximo 200 caracteres.
    data_cadastro = models.DateTimeField(auto_now_add=True) # Define a data de cadastro do fornecedor, que é preenchida automaticamente com a data e hora atuais quando o fornecedor é criado.

    def __str__(self): # Define o método __str__ para retornar uma representação legível do objeto Fornecedor, que neste caso é o nome do fornecedor.
        return self.nome # Retorna o nome do fornecedor quando o objeto for convertido para string.

