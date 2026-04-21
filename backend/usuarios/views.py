from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Usuarios
# Create your views here.


def listar_usuarios(request):
    usuarios = Usuarios.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

"""" Criar Endpoint para Buscar Usuário por ID 
Criar uma view: buscar_usuario_por_id(request, id) 
Regras: 
• Retornar usuário se existir  
• Retornar erro 404 caso não exista  """

def listar_usuario_por_id(request, id): 
    try:
        post = Usuarios.objects.get(id=id)
    except Usuarios.DoesNotExist:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)
























    # GET → ver post + comentários
    if request.method == 'GET':
        comentarios = list(post.comentarios.values())

        return JsonResponse({
            'id': post.id,
            'titulo': post.titulo,
            'conteudo': post.conteudo,
            'comentarios': comentarios
        })