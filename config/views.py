from django.shortcuts import render

def home(request): # Define a função home, que é responsável por lidar com a lógica da página inicial do sistema de gestão de estoque.
    return render(request, 'home.html') # Renderiza a página inicial, utilizando o template home.html.