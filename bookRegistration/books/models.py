from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=30)
    data = models.DateField()
    categoria = models.CharField(max_length=30)
    autor = models.CharField(max_length=30) 


def __str__(self):
       return self.nome
   