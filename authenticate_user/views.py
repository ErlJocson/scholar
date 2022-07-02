from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

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
        # personal information
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        birthday = request.POST['birthday']
        birthplace = request.POST['birthplace']
        age = request.POST['age']
        student_contact = request.POST['student_contact']
        address = request.POST['address']
        sex = request.POST['sex']
        civil_status = request.POST['civil_status']

        # educational background
        elem = request.POST['elementary']
        elem_add = request.POST['elem_add']
        elem_grad = request.POST['elem_grad']
        secondary = request.POST['secondary']
        secondary_add = request.POST['secondary_add']
        secondary_grad = request.POST['secondary_grad']
        senior = request.POST['senior']
        senior_add = request.POST['senior_add']
        senior_grad = request.POST['senior_grad']

        # guardian information
        mother_name = request.POST['mother_name']
        mother_occupation = request.POST['mother_occupation']
        mother_income = request.POST['mother_income']
        father_name = request.POST['father_name']
        father_occupation = request.POST['father_occupation']
        father_income = request.POST['father_income']
        contact = request.POST['contact']

        # students additional information
        course = request.POST['course']
        year_level = request.POST['year_level']
        units = request.POST['units']
        graduation_year = request.POST['graduation_year']
        graduating = request.POST['graduating']
        school_name = request.POST['school_name']
        school_add = request.POST['school_add']

        # password
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            new_user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            new_user.save()

            other_information = OtherInformation.objects.create(
                middle_name=middle_name,
                birthday=birthday,
                birth_place=birthplace,
                age=age,
                contact=student_contact,
                address=address,
                sex=sex,
                civil_status=civil_status,
                approved=False,
                user_id=new_user,
            )
            other_information.save()

            students_background_education = StudentEducationBackground(
                elementary=elem,
                elem_school_location=elem_add,
                elem_year_graduated=elem_grad,
                secondary=secondary,
                secondary_school_location=secondary_add,
                secondary_year_graduated=secondary_grad,
                senior_high=senior,
                senior_school_location=senior_add,
                senior_year_graduated=senior_grad,
                user_id=new_user,
            )
            students_background_education.save()

            guardian_information = GuardianInformation(
                mother_name=mother_name,
                mother_ocupation=mother_occupation,
                mother_income=mother_income,
                father_name=father_name,
                father_ocupation=father_occupation,
                father_income=father_income,
                contact=contact,
                user_id=new_user,
            )
            guardian_information.save()

            student_additional_information = StudentAdditionalInformation(
                course=course,
                year_level=year_level,
                units_enrolled=units,
                expected_year_graduation=graduation_year,
                graduating= True if graduating == 'Yes' else False,
                school_name=school_name,
                school_address=school_add,
                user_id=new_user,
            )
            student_additional_information.save()
            login(request, new_user)
            return redirect('home')
        else:
            messages.warning(request, 'Password does not match.')
            return redirect('register')
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

        user = User.objects.filter(id=request.user.id)

        if user and new_password == confirm_password:
            user[0].set_password(new_password)
            user[0].save()
            messages.success(request, 'Password changed.')
            login(request, user[0])
            return redirect('home')

        messages.warning(request, 'There was an error. Wrong user password or Password did not match.')
    return redirect('home')
