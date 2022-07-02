from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authenticate_user.models import *
from .models import *
# Create your views here.

@login_required
def index_view(request):
    return render(request, 'index.html', {
        'title':'Home',
        
    })

@login_required
def profile_view(request):
    current_user = User.objects.get(id=request.user.id)
    other_information = OtherInformation.objects.get(user_id=current_user.id)
    return render(request, 'profile.html', {
        'title':'Student profile',
        'current_user':current_user,
        'other_information':other_information,
    })

@login_required
def educational_background_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    background = StudentEducationBackground.objects.get(user_id=request.user.id)
    return render(request, 'educational.html', {
        'title':'Educational Background',
        'background':background,
        'other_information':other_information,
    })

@login_required
def guardian_information_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    guardian = GuardianInformation.objects.get(user_id=request.user.id)
    return render(request, 'guardian.html', {
        'title':'Guardian information',
        'guardian':guardian,
        'other_information':other_information,
    })

@login_required
def additinal_information_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    additional = StudentAdditionalInformation.objects.get(user_id=request.user.id)
    return render(request, 'additional.html', {
        'title':'Additional information',
        'additional':additional,
        'other_information':other_information,
    })

@login_required
def requirements_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    return render(request, 'requirements.html', {
        'title':'Requirements',
        'other_information':other_information,
    })

@login_required
def application_status(request):
    return render(request, 'status.html', {
        'title':'Application status'
    })

def registration_form(request):
    if request.method == 'POST':
        registration = RegistrationForm.objects.create()
        registration.save()
    return redirect('requirement')

def parent_voters_id(request):
    return redirect('requirement')

def scholar_voters_id(request):
    return redirect('requirement')

def scholar_grades(request):
    return redirect('requirement')
