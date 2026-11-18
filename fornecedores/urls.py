from django.urls import path
from . import views

urlpatterns = [ # Define a lista de URLs para o aplicativo fornecedores, que mapeia URLs para funções de visualização (views) correspondentes.
    path('cadastrar/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'), # Define a URL para cadastrar um fornecedor, que chama a função de visualização cadastrar_fornecedor e atribui o nome 'cadastrar_fornecedor' para referência.
    path('', views.listar_fornecedores, name='listar_fornecedores'), # Define a URL para listar todos os fornecedores, que chama a função de visualização listar_fornecedores e atribui o nome 'listar_fornecedores' para referência.
    path('editar/<int:id>/', views.editar_fornecedor, name='editar_fornecedor'), # Define a URL para editar um fornecedor específico, que chama a função de visualização editar_fornecedor e atribui o nome 'editar_fornecedor' para referência. O parâmetro <int:id> captura o ID do fornecedor a ser editado.
    path('deletar/<int:id>/', views.deletar_fornecedor, name='deletar_fornecedor'), # Define a URL para deletar um fornecedor específico, que chama a função de visualização deletar_fornecedor e atribui o nome 'deletar_fornecedor' para referência. O parâmetro <int:id> captura o ID do fornecedor a ser deletado.
]