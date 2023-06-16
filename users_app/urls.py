from django.urls import path
from . import views

urlpatterns = [

path('', views.index),
path('create/user', views.create_user),
path('create/book', views.create_book),


]