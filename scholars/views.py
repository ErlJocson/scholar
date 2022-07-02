from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authenticate_user.models import *
from .models import *
from django.contrib import messages

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
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    status = other_information.approved
    return render(request, 'status.html', {
        'title':'Application status',
        'status':status,
    })

# passing the requirements
def registration_form(request):
    if request.method == 'POST':
        user_file = request.FILES['file']
        registration = RegistrationForm.objects.create(
            image=user_file,
            user_id=request.user.id,
        )
        registration.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

def parent_voters_id(request):
    if request.method == 'POST':
        user_file = request.FILE['file']
        voters_id = ParentsVotersID.objects.create(
            image = user_file,
            user_id = request.user.id,
        )
        voters_id.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

def scholar_voters_id(request):
    if request.method == 'POST':
        user_file = request.FILE['file']
        voters_id = ScholarVotersID.objects.create(
            image = user_file,
            user_id = request.user.id,
        )
        voters_id.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

def scholar_grades(request):
    if request.method == 'POST':
        user_file = request.FILE['file']
        grade = CopyOfGrades.objects.create(
            image = user_file,
            user_id = request.user.id,
        )
        grade.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')
