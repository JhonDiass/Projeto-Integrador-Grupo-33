from django.shortcuts import render, redirect, get_object_or_404
from .forms import FornecedorForm
from .models import Fornecedor
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models.deletion import ProtectedError


# Create your views here.
@user_passes_test(lambda u: u.is_staff) 
def cadastrar_fornecedor(request): # Define a função cadastrar_fornecedor, que é responsável por lidar com a lógica de cadastro de fornecedores no sistema de gestão de estoque.
    if request.method == 'POST': # Verifica se o método da requisição é POST, indicando que o formulário foi enviado.
        form = FornecedorForm(request.POST) # Cria uma instância do formulário FornecedorForm com os dados enviados na requisição.
        if form.is_valid(): # Verifica se o formulário é válido, ou seja, se todos os campos obrigatórios foram preenchidos corretamente.
            form.save() # Salva os dados do formulário no banco de dados, criando um novo registro de fornecedor.
            messages.success(request, 'Fornecedor cadastrado com sucesso!')
            return redirect('listar_fornecedores') # Redireciona para a página de listagem de fornecedores, informando ao usuário que o fornecedor foi cadastrado com sucesso.

    else: # Se o método da requisição não for POST, significa que o usuário está acessando a página de cadastro pela primeira vez.
        form = FornecedorForm() # Cria uma instância vazia do formulário FornecedorForm, que será exibida para o usuário preencher os dados do fornecedor.

    return render(request, 'fornecedores/cadastrar_fornecedor.html', {'form': form}) # Renderiza a página de cadastro de fornecedor, passando o formulário como contexto para que ele seja exibido na página.

@user_passes_test(lambda u: u.is_staff)
def listar_fornecedores(request): # Define a função listar_fornecedores, que é responsável por lidar com a lógica de listagem de fornecedores no sistema de gestão de estoque.
    fornecedores = Fornecedor.objects.all() # Recupera todos os registros de fornecedores do banco de dados, utilizando o método all() do gerenciador de objetos do modelo Fornecedor.
    return render(request, 'fornecedores/listar_fornecedores.html', {'fornecedores': fornecedores}) # Renderiza a página de listagem de fornecedores, passando a lista de fornecedores como contexto para que eles sejam exibidos na página.

@user_passes_test(lambda u: u.is_staff)
def editar_fornecedor(request, id): # Define a função editar_fornecedor, que é responsável
    fornecedor = get_object_or_404(Fornecedor, id=id) # Recupera o objeto Fornecedor com o ID fornecido ou retorna um erro 404 se não for encontrado.
    if request.method == 'POST': # Verifica se o método da requisição é POST, indicando que o formulário foi enviado.
        form = FornecedorForm(request.POST, instance=fornecedor) # Cria uma instância do formulário FornecedorForm com os dados enviados na requisição e o objeto fornecedor existente.
        if form.is_valid(): # Verifica se o formulário é válido.
            form.save() # Salva as alterações no banco de dados.
            messages.success(request, 'Fornecedor editado com sucesso!')
            return redirect('listar_fornecedores') # Redireciona para a página de listagem de fornecedores, informando ao usuário que o fornecedor foi editado com sucesso.
    else:
        form = FornecedorForm(instance=fornecedor) # Cria uma instância do formulário FornecedorForm com os dados do objeto fornecedor existente.

    return render(request, 'fornecedores/editar_fornecedor.html', {'form': form, 'fornecedor': fornecedor}) # Renderiza a página de edição de fornecedor, passando o formulário e o objeto fornecedor como contexto para que eles sejam exibidos na página.

@user_passes_test(lambda u: u.is_staff)
def deletar_fornecedor(request, id): # Define a função deletar_fornecedor, que é responsável por lidar com a lógica de exclusão de fornecedores no sistema de gestão de estoque.
    fornecedor = get_object_or_404(Fornecedor, id=id) # Recupera o objeto Fornecedor com o ID fornecido ou retorna um erro 404 se não for encontrado.
    if request.method == 'POST': # Verifica se o método da requisição é POST, indicando que a confirmação de exclusão foi enviada.
        try:
            fornecedor.delete() # Tenta excluir o objeto fornecedor do banco de dados.
            messages.success(request, 'Fornecedor excluído com sucesso!')
        except ProtectedError: # Se ocorrer um erro de exclusão protegido, significa que o fornecedor está associado a produtos e não pode ser excluído.
            messages.error(request, 'Não é possível excluir este fornecedor, pois ele está associado a produtos.')
        return redirect('listar_fornecedores') # Redireciona o usuário para a página de listagem de fornecedores.
    return render(request, 'fornecedores/deletar_fornecedor.html', {'fornecedor': fornecedor}) # Renderiza a página de confirmação de exclusão de fornecedor, passando o objeto fornecedor como contexto para que ele seja exibido na página.
    