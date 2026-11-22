from django.shortcuts import render, redirect, get_object_or_404 # Importa as funções render, redirect e get_object_or_404 do módulo django.shortcuts. A função render é usada para renderizar templates HTML, a função redirect é usada para redirecionar o usuário para outra URL, e a função get_object_or_404 é usada para recuperar um objeto do banco de dados ou retornar um erro 404 se o objeto não for encontrado.
from .forms import ProdutoForm
from .models import Produto, Fornecedor
from django.contrib.auth.decorators import user_passes_test # Define o decorador user_passes_test, que é usado para restringir o acesso a determinadas visualizações com base em uma função de teste personalizada.
from django.contrib import messages # Importa o módulo messages do Django, que fornece uma maneira de exibir mensagens temporárias para os usuários, como mensagens de sucesso ou erro.

@user_passes_test(lambda u: u.is_superuser) # Aplica o decorador user_passes_test à função cadastrar_produto, permitindo o acesso apenas a usuários que são superusuários.
def cadastrar_produto(request): # Define a função cadastrar_produto, que é responsável por lidar com a lógica de cadastro de produtos no sistema de gestão de estoque.
    if request.method == 'POST': # Verifica se o método da requisição é POST, indicando que o formulário foi enviado.
        form = ProdutoForm(request.POST) # Cria uma instância do formulário ProdutoForm com os dados enviados na requisição.
        if form.is_valid(): # Verifica se o formulário é válido, ou seja, se todos os campos obrigatórios foram preenchidos corretamente.
            form.save() # Salva os dados do formulário no banco de dados, criando um novo registro de produto.
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('listar_produtos') # Redireciona para a página de listagem de produtos, informando ao usuário que o produto foi cadastrado com sucesso.

    else: # Se o método da requisição não for POST, significa que o usuário está acessando a página de cadastro pela primeira vez.
        form = ProdutoForm() # Cria uma instância vazia do formulário ProdutoForm, que será exibida para o usuário preencher os dados do produto.

    return render(request, 'produtos/cadastrar_produto.html', {'form': form}) # Renderiza a página de cadastro de produto, passando o formulário como contexto para que ele seja exibido na página.

@user_passes_test(lambda u: u.is_superuser)
def listar_produtos(request): # Define a função listar_produtos, que é responsável por lidar com a lógica de listagem de produtos no sistema de gestão de estoque.
    produtos = Produto.objects.select_related('fornecedor').all() # Recupera todos os registros de produtos do banco de dados, utilizando o método all() do gerenciador de objetos do modelo Produto. O método select_related('fornecedor') é usado para otimizar a consulta, buscando os dados do fornecedor relacionado a cada produto em uma única consulta ao banco de dados.
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos}) # Renderiza a página de listagem de produtos, passando a lista de produtos como contexto para que eles sejam exibidos na página.

@user_passes_test(lambda u: u.is_superuser)
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id) # Recupera o objeto Produto com o ID fornecido ou retorna um erro 404 se não for encontrado.
    if request.method == 'POST': # Verifica se o método da requisição é POST, indicando que o formulário foi enviado.
        form = ProdutoForm(request.POST, instance=produto) # Cria uma instância do formulário ProdutoForm com os dados enviados na requisição e o objeto produto existente.
        if form.is_valid(): # Verifica se o formulário é válido.
            form.save() # Salva as alterações no banco de dados.
            messages.success(request, 'Produto editado com sucesso!')
            return redirect('listar_produtos') # Redireciona o usuário para a página de listagem de produtos.
    else:
        form = ProdutoForm(instance=produto) # Cria uma instância do formulário ProdutoForm com os dados do objeto produto existente.
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto}) # Renderiza a página de edição de produto, passando o formulário e o objeto produto como contexto para que eles sejam exibidos na página.

@user_passes_test(lambda u: u.is_superuser)
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id) # Recupera o objeto Produto com o ID fornecido ou retorna um erro 404 se não for encontrado.
    if request.method == 'POST': # Verifica se o método da requisição é POST, indicando que a confirmação de exclusão foi enviada.
        produto.delete() # Exclui o objeto produto do banco de dados.
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('listar_produtos') # Redireciona o usuário para a página de listagem de produtos.
    return render(request, 'produtos/deletar_produto.html', {'produto': produto}) # Renderiza a página de confirmação de exclusão de produto, passando o objeto produto como contexto para que ele seja exibido na página.
