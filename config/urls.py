"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fornecedores/', include('fornecedores.urls')), # Inclui as URLs do aplicativo fornecedores, permitindo que as URLs definidas em fornecedores/urls.py sejam acessíveis a partir do caminho 'fornecedores/'.
    path('', views.pre_login, name='pre_login'), # Define a URL para a página inicial do sistema de gestão de estoque, que chama a função de visualização home e atribui o nome 'home' para referência.
    path('home/', views.home, name='home'),
    path('produtos/', include('produtos.urls')), # Inclui as URLs do aplicativo produtos, permitindo que as URLs definidas em produtos/urls.py sejam acessíveis a partir do caminho 'produtos/'.
]
