from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index_view(request):
    return render(request, 'index.html', {
        'title':'Home',
    })

@login_required
def profile_view(request):
    return render(request, 'profile.html', {
        'title':'Profile'
    })
