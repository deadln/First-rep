from django.db import models
from django.contrib.auth.models import User #Lj,fdktybt vjltkb gjkmpjdfntkz

class Post(models.Model): #Создание класса поста
    author = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)
    description = models.TextField()

# Create your models here.
