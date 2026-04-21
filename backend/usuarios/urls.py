from django.urls import path
from .views import listar_usuarios, listar_usuario_por_id

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('/usuarios/int:id/ ',listar_usuario_por_id),
]

""""Criar o arquivo urls.py no app usuarios com as rotas: 
• /usuarios/  
• 
E incluir essas rotas no arquivo principal do projeto. """