from django.urls import path
from .views import post_list, user_posts

urlpatterns = [
    path('', post_list),
    path('user/<user>/', user_posts),
]