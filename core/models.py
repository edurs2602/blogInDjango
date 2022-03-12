from django.db import models


class Post(models.Model):
    user = models.CharField('User', max_length=100)
    titulo = models.CharField('Titulo', max_length=25)
    texto = models.TextField('Texto', max_length=280)
    dataPub = models.DateField(auto_now=True)


    def __str__(self):
        return f'user: {self.user} / titulo: {self.titulo} / texto: {self.texto}'

class Port(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.TextField('description', max_length=200)
    link = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Titulo: {self.title} / descrição: {self.description} / link: {self.link}'