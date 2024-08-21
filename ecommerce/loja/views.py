from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    banners = Banner.objects.filter(ativo=True)
    context = {"banners": banners}
    return render(request, 'homepage.html', context)

def loja(request, nome_categoria=None):
    produtos = Produto.objects.filter(ativo=True)
    if nome_categoria:
        produtos = produtos.filter(categoria__nome=nome_categoria)
    context = {"produtos":produtos}
    return render(request, 'loja.html', context)

def ver_produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    if len(itens_estoque) > 0:
        possui_estoque = True
        cores = {item.cor for item in itens_estoque}
    else:
        possui_estoque = False
        cores = []
    context = {"produto": produto, "itens_estoque": itens_estoque, "possui_estoque": possui_estoque, "cores": cores}
    return render(request, 'ver_produto.html', context)

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

def minha_conta(request):
    return render(request, 'usuario/minhaconta.html')

def login(request):
    return render(request, 'usuario/login.html')