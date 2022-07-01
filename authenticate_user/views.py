from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('home')
        else:
            messages.success(request, 'Wrong credentials.')
            
    return render(request, 'login.html', {
        'title':'Login',
    })

def register_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass
    return render(request, 'register.html', {
        'title':'Register',
    })

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.filter(id=request.user.id, password=password)

        if not user:
            messages.warning(request, 'Wrong password.')

        if new_password == confirm_password:
            user[0].set_password(password)
            user[0].save()
            messages.success(request, 'Password updated')
        else:
            messages.warning(request, 'Password does not match.')
    return redirect('home')
