from cProfile import Profile
import os
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
    try:
        image = ProfilePicture.objects.get(user_id=current_user.id)
    except:
        image = False
    return render(request, 'profile.html', {
        'title':'Student profile',
        'current_user':current_user,
        'other_information':other_information,
        'image':image
    })

@login_required
def educational_background_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    background = StudentEducationBackground.objects.get(user_id=request.user.id)
    try:
        image = ProfilePicture.objects.get(user_id=request.user.id)
    except:
        image = False
    return render(request, 'educational.html', {
        'title':'Educational Background',
        'background':background,
        'other_information':other_information,
        'image':image
    })

@login_required
def guardian_information_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    guardian = GuardianInformation.objects.get(user_id=request.user.id)
    try:
        image = ProfilePicture.objects.get(user_id=request.user.id)
    except:
        image = False
    return render(request, 'guardian.html', {
        'title':'Guardian information',
        'guardian':guardian,
        'other_information':other_information,
        "image":image
    })

@login_required
def additinal_information_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    additional = StudentAdditionalInformation.objects.get(user_id=request.user.id)
    try:
        image = ProfilePicture.objects.get(user_id=request.user.id)
    except:
        image = False
    return render(request, 'additional.html', {
        'title':'Additional information',
        'additional':additional,
        'other_information':other_information,
        'image':image
    })

@login_required
def requirements_profile(request):
    other_information = OtherInformation.objects.get(user_id=request.user.id)

    if RegistrationForm.objects.filter(user_id=request.user.id):
        register = RegistrationForm.objects.get(user_id=request.user.id)
    else:
        register = False

    if ParentsVotersID.objects.filter(user_id=request.user.id):
        parent = ParentsVotersID.objects.get(user_id=request.user.id)
    else:
        parent = False
    if ScholarVotersID.objects.filter(user_id=request.user.id):
        scholar = ScholarVotersID.objects.get(user_id=request.user.id)
    else:
        scholar = False
    if CopyOfGrades.objects.filter(user_id=request.user.id):
        grade = CopyOfGrades.objects.get(user_id=request.user.id)
    else:
        grade = False
        
    try:
        image = ProfilePicture.objects.get(user_id=request.user.id)
    except:
        image = False

    plastic_kilo = KiloOfPlastic.objects.filter(user_id=request.user.id)
    if plastic_kilo:
        total_plastic_kilo = 0
        for kilo in plastic_kilo:
            total_plastic_kilo = total_plastic_kilo + kilo.kilo
    else:
        total_plastic_kilo = 0

    return render(request, 'requirements.html', {
        'title':'Requirements',
        'total_plastic_kilo':total_plastic_kilo,
        'other_information':other_information,
        'register': register,
        'parent': parent,
        'scholar': scholar,
        'grade': grade,
        'image':image
    })

@login_required
def application_status(request):
    try:
        image = ProfilePicture.objects.get(user_id=request.user.id)
    except:
        image = False
    
    other_information = OtherInformation.objects.get(user_id=request.user.id)
    status = other_information.approved
    try:
        grants_schedule = DateOfGrants.objects.filter(show=True)[0]
    except:
        grants_schedule = False
    return render(request, 'status.html', {
        'title':'Application status',
        'status':status,
        'image':image,
        'grant_schedule':grants_schedule,
    })

@login_required
def registration_form(request):
    check_file = RegistrationForm.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        if check_file:
            check_file[0].delete()

        user_file = request.FILES['file']
        registration = RegistrationForm.objects.create(
            image=user_file,
            user_id=request.user,
        )
        registration.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

@login_required
def parent_voters_id(request):
    check_file = ParentsVotersID.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        if check_file:
            check_file[0].delete()

        user_file = request.FILES['file']
        voters_id = ParentsVotersID.objects.create(
            image = user_file,
            user_id = request.user,
        )
        voters_id.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

@login_required
def scholar_voters_id(request):
    check_file = ScholarVotersID.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        if check_file:
            check_file[0].delete()
        user_file = request.FILES['file']
        voters_id = ScholarVotersID.objects.create(
            image = user_file,
            user_id = request.user,
        )
        voters_id.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

@login_required
def scholar_grades(request):
    check_file = CopyOfGrades.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        if check_file:
            check_file[0].delete()
        user_file = request.FILES['file']
        grade = CopyOfGrades.objects.create(
            image = user_file,
            user_id = request.user,
        )
        grade.save()
        messages.success(request, 'File uploaded.')
    return redirect('requirement')

@login_required
def change_picture(request):
    check_file = ProfilePicture.objects.filter(user_id=request.user.id)
    if request.method =='POST':
        if check_file:
            check_file[0].delete()
        picture = request.FILES.get('file', False)
        image_to_save = ProfilePicture.objects.create(
            image=picture,
            user_id=request.user,
        )
        image_to_save.save()
        messages.success(request, 'Image updated.')
    return redirect('profile')