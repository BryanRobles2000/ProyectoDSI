from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Noticias</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/populares/">Populares</a></li>
        <li><a href="/internacionales/">Internacionales</a></li>
        <li><a href="/deportes/">Deportes</a></li>
        <li><a href="/insolitos">Insolitos</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/inicio.html")

def populares(request):
    return render(request, "core/populares.html")

def internacionales(request):
    return render(request, "core/internacionales.html")

def deportes(request):
    return render(request, "core/deportes.html")

def insolitos(request):
    return render(request, "core/insolitos.html")