from django.contrib import admin

from .models import Post #Импортирование модели поста

admin.site.register(Post) #Регистрация модели поста
