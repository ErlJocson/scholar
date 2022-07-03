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
            messages.success(request, 'Wrong password or username.')
            
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
        year_level = request.POST.get('year_level', False)
        units = request.POST['units']
        graduation_year = request.POST['graduation_year']
        graduating = request.POST['graduating']
        school_name = request.POST['school_name']
        school_add = request.POST['school_add']

        # password
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                new_user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )

                new_user.set_password(password)
                new_user.save()
            except:
                messages.warning(request, 'There was an error!')
                
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
            messages.success(request, 'Account created.')
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
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.filter(id=request.user.id)
        check_password = authenticate(request, username=user[0].username, password=password)
        if check_password and new_password == confirm_password:
            user[0].set_password(new_password)
            user[0].save()
            messages.success(request, 'Password updated.')
            login(request, user[0])
            return redirect('home')

        messages.warning(request, 'Wrong user password or Password did not match.')
    return redirect('home')

def change_password_form(request, id):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.filter(id=id)
        check_if_exist = authenticate(request, username=user[0].username, password=user[0].password)
        messages.success(request, f'{check_if_exist}')
        if check_if_exist and new_password == confirm_password:
            user[0].set_password(new_password)
            user[0].save()
            messages.success(request, 'Password changed.')
            return redirect('login')

    return render(request, 'forget-password-form.html', {
        'title':'Forget password',
    })

@login_required
def update_informations(request):
    current_user = User.objects.get(id=request.user.id)
    other = OtherInformation.objects.get(user_id=request.user.id)
    background = StudentEducationBackground.objects.get(user_id=request.user.id)
    guardian = GuardianInformation.objects.get(user_id=request.user.id)
    additional = StudentAdditionalInformation.objects.get(user_id=request.user.id)

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
        year_level = request.POST.get('year_level', False) 
        units = request.POST['units']
        graduation_year = request.POST['graduation_year']
        graduating = request.POST['graduating']
        school_name = request.POST['school_name']
        school_add = request.POST['school_add']

        current_user.username = username
        current_user.email = email
        current_user.first_name = first_name
        current_user.last_name = last_name

        other.middle_name = middle_name
        other.birthday = birthday
        other.birthplace = birthplace
        other.age = age
        other.student_contact = student_contact
        other.address = address
        other.sex = sex
        other.civil_status = civil_status

        background.elementary = elem 
        background.elem_school_location = elem_add 
        background.elem_year_graduated = elem_grad 
        background.secondary = secondary 
        background.secondary_school_location = secondary_add 
        background.secondary_year_graduated = secondary_grad 
        background.senior_high = senior 
        background.senior_school_location = senior_add 
        background.senior_year_graduated = senior_grad 

        guardian.mother_name = mother_name
        guardian.mother_ocupation = mother_occupation
        guardian.mother_income = mother_income
        guardian.father_name = father_name
        guardian.father_ocupation = father_occupation
        guardian.father_income = father_income
        guardian.contact = contact

        additional.course = course
        additional.year_level = year_level
        additional.units_enrolled = units
        additional.expected_year_graduation = graduation_year
        additional.graduating = graduating
        additional.school_name = school_name
        additional.school_address = school_add

        current_user.save()
        other.save()
        background.save()
        guardian.save()
        messages.success(request, 'Informations have been updated.')
        return redirect('profile')
    return render(request, 'update.html', {
        'title':'Update',
        'current_user':current_user,
        'other':other,
        'background':background,
        'guardian':guardian,
        'additional':additional,
    })

def forget_password_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        check_if_exist = User.objects.filter(username=username, first_name=first_name, last_name=last_name)
        if check_if_exist:
            return redirect('change-password-form', id=check_if_exist[0].id)
        messages.warning(request, 'Wrong credentials')
    return render(request, 'forget.html', {
        'title':'Forget password',
    })

