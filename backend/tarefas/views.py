from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Tarefa, Usuarios

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    usuario = request.user 
    tarefas = Tarefa.objects.filter(usuario_responsavel=usuario)
    
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_por_status(request,status):
    status_validos = [choice[0] for choice in Tarefa.STATUS_CHOICES]
    
    if status not in status_validos:
        return JsonResponse({'erro': 'status inválidos'}, status=400)
    
    tarefas = Tarefa.objects.filter(status=status).values()
    return JsonResponse(list[Any](tarefas), safe=False)