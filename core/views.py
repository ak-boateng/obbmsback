from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Profile, Donor
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def donor(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        area_or = request.POST['area_or']
        town = request.POST['town']
        id_number = request.POST['id_number']
        donor_number = request.POST['donor_number']
        donor_card = request.POST['donor_card']
        name_of_patient = request.POST['patientname']
        hospital = request.POST['hospital']
        ward = request.POST['ward']

        donor = Donor(firstname=firstname, middlename=middlename, lastname=lastname, 
                      email=email,phone_number=phone_number, area_or=area_or, town=town, 
                      id_number=id_number, donor_number=donor_number, donor_card=donor_card, 
                      name_of_patient=name_of_patient, hospital=hospital, ward=ward)
        donor.save()
        return redirect('/')
    else:
        return render(request, 'donor.html')

def adminsignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('adminsignup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username has already been taken')
                return redirect('adminsignup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/login')
    else:
        return render(request, 'adminsignup.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/administrator')
        else: 
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')   
def logout(request):
    auth.logout(request)
    return redirect('adminsignup')

@login_required(login_url='login')
def administrator(request):
    return render(request, 'admin.html')

@login_required(login_url='login')
def admins(request):
    donor = Donor.objects.all()
    return render(request, 'admins.html', {'donor': donor})

def details(request, dn):
    donor = Donor.objects.get(id=dn)
    return render(request, 'details.html', {'donor': donor})