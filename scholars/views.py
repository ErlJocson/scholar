from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {
        'title':'Home',
    })

def profile_view(request):
    return 

def change_password(request):
    return

def logout(request):
    return