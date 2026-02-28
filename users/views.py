from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


# 1️⃣ Hello Route
def hello(request):
    return HttpResponse("Hello World!")


# 2️⃣ List All Users
def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})


# 3️⃣ Get Specific User by ID
def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
        return HttpResponse(f"{user.name} - {user.email} - {user.role}")
    except User.DoesNotExist:
        return HttpResponse("User not found")


# 4️⃣ Create New User (Form + Save to DB)
def new_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')

        User.objects.create(name=name, email=email, role=role)
        return redirect('users_list')

    return render(request, 'new_user.html')