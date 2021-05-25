from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Pagina principal",
        "content": "Bem-vindo a pagina principal"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Pagina sobre",
                 "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def contact_page(request):
    context = {
        "title": "Pagina contato",
                 "content": "Bem-vindo a página contado"
    }
    return render(request, "contact/view.html", context)
