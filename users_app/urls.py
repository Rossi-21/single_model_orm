from django.urls import path
from . import views

urlpatterns = [

path('', views.index),
path('users',views.users),
path('create/user', views.create_user),
path('create/book', views.create_book),


]