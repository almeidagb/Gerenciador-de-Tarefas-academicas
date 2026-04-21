from django.db import models

# Create your models here.
""""• nome (CharField)  
• email (EmailField, único)  
• ativo (BooleanField, padrão True)  
• data_criacao (DateTimeField, auto_now_add=True) 
Implementar o método: 
def __str__(self): 
return self.nome"""

class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=60)
    ativo = models.BooleanField(auto_now_add=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    

    