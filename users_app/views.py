from django.shortcuts import render, redirect
from users_app.models import User, Book

def index(request):
        context = {"users": User.objects.all(), "books": Book.objects.all()}
        return render(request, "index.html", context)

def users(request):
        context = {"users": User.objects.all()}
        return render(request, "users.html", context )

def create_user(request):
       
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        

        user = User.objects.create(first_name=first_name, last_name = last_name, notes = notes)
        
        return redirect("/users")

def create_book(request):
       
        title = request.POST['title']
        description = request.POST['description']
        user_id = request.POST['user']

        user = User.objects.get(id=user_id)

        book = Book.objects.create(title = title, description = description, user = user)
        
        return redirect("/")
