from django.shortcuts import render, redirect
from users_app.models import User, Book

def index(request):
        context = {"users": User.objects.all()}
        return render(request, "index.html", context)

def create_user(request):
       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        location = request.POST['location']
        email = request.POST['email']
        age = request.POST['age']

        user = User.objects.create(first_name=first_name, last_name = last_name, location = location, email = email, age = age)
        
        return redirect("/")

def create_book(request):
       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        location = request.POST['location']
        email = request.POST['email']
        age = request.POST['age']

        user = User.objects.create(first_name=first_name, last_name = last_name, location = location, email = email, age = age)
        
        return redirect("/")
