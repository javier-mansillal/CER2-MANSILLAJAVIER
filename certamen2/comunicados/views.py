from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado,Categoria

def index(request):
    comunicados = Comunicado.objects.all().order_by("-id")
    categorias = Categoria.objects.all()
    nivel =     [("GEN","General"),
                ("PRE","Ciclo Preescolar",),
                ("BAS","Ciclo Básico"),
                ("MED","Ciclo Medio")]
    if request.method == "POST":
        categoria_elegida = request.POST.get('categoria')
        nivel_elegido = request.POST.get('nivel')
        comunicados = comunicados.filter(categoria=categoria_elegida, nivel=nivel_elegido)
        comunicados_exists = comunicados.exists()
        context = {'comunicados': comunicados, 'comunicados_exists': comunicados_exists, 'categorias': categorias, 'nivel': nivel}
    else:
        comunicados_exists = comunicados.exists()
        context = {'comunicados': comunicados, 'comunicados_exists': comunicados_exists, 'categorias': categorias, 'nivel': nivel}
    return render(request, "comunicados/index.html", context)
