from django.db import models

# Create your models here.

#modelos son la manera de gestionar los datos en la bd 

class Post(models.Model):
    title = models.CharField(max_length=200) #  titulo de la publicacion
    content = models.TextField # contenido de la publi
    author = models.CharField(max_length=100) # campo para el autor de la publi
    creater_at = models.DateTimeField(auto_now_add=True) # auto_now_add para q sea automaticamente puesta la fecha

    def __str__(self):
        return self.title
    #retorna el titulo de la publicacion a string