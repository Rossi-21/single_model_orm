from django.urls import path
from . import views

urlpatterns = [

path('', views.index),
path('books/<int:id>', views.show_book),
path('users', views.users),
path('users/<int:id>', views.show_user),
path('create/user', views.create_user),
path('create/book', views.create_book),


]