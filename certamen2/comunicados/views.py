from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado,Categoria

def index(request):
    comunicados = Comunicado.objects.all().order_by("-id")
    context = {'comunicados': comunicados}
    return render(request, "comunicados/index.html", context)
