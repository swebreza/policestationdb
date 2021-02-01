from django.shortcuts import render, redirect
from my_django_app.models import hellow
from my_django_app.models import fir
from my_django_app.models import officer
from django.contrib import messages
from my_django_app.forms import crform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def criminal(request):
    results = hellow.objects.all()
    return render(request, "criminal.html", {"hellow": results})


@login_required(login_url='login')
def firClass(request):
    results = fir.objects.all()
    return render(request, "fir.html", {"fir": results})


@login_required(login_url='login')
def officerClass(request):
    results = officer.objects.all()
    return render(request, "officer.html", {"officer": results})


@login_required(login_url='login')
def index(request):
    return render(request, "index.html")


def login1(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            # username = request.POST['username']
            # password= request.POST['password']
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('password'):
            # reg = RegisterPage()
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            x = User.objects.create_superuser(username, email, password)
            print("x", x)
            print("SSSSSS")
            # reg.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Register successfull")
            return redirect('display')
    # context = {
    #     'form': form
    # }
    return render(request, 'register.html')


h = hellow()


def insert(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('date') and request.POST.get('fir') and request.POST.get('punishment') and request.POST.get('location'):
            criminal = h
            criminal.name = request.POST.get('name')
            criminal.date = request.POST.get('date')
            criminal.fir = request.POST.get('fir')
            criminal.punishment = request.POST.get('punishment')
            criminal.location = request.POST.get('location')
            criminal.save()
            messages.success(request, "The Record ** " +
                             criminal.name+" ** is saved successfully!!!")
            return render(request, "create.html")
    else:
        return render(request, "create.html")


def update(request, id):
    getcriminaldetails = hellow.objects.get(id=id)
    return render(request, 'update.html', {"hellow": getcriminaldetails})


def requpdate(request, id):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('date') and request.POST.get('fir') and request.POST.get('punishment') and request.POST.get('location'):

            updatereq = hellow.objects.get(id=id)
            updatereq.name = request.POST.get('name')
            updatereq.date = request.POST.get('date')
            updatereq.fir = request.POST.get('fir')
            updatereq.punishment = request.POST.get('punishment')
            updatereq.location = request.POST.get('location')
            updatereq.save()
            messages.success(request, "The Record ** " +
                             updatereq.name+" ** is saved successfully!!!")
            # return render(request, "criminal.html")
            results = hellow.objects.all()
            return render(request, "criminal.html", {"hellow": results})
    else:
        return render(request, "criminal.html")


def crdel(request, id):
    delcriminal = hellow.objects.get(id=id)
    delcriminal.delete()
    results = hellow.objects.all()
    return render(request, "criminal.html", {"hellow": results})


# --officer---
off = officer()


def insertofficer(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('surname') and request.POST.get('designation') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('location'):
            officer = off
            officer.name = request.POST.get('name')
            officer.surname = request.POST.get('surname')
            officer.designation = request.POST.get('designation')
            officer.age = request.POST.get('age')
            officer.gender = request.POST.get('gender')
            officer.location = request.POST.get('location')
            officer.save()
            messages.success(request, "The Record ** " +
                             officer.name+" ** is saved successfully!!!")
            return render(request, "createofficer.html")
    else:
        return render(request, "createofficer.html")


# def updateofficer(request, id):
#     getcriminaldetails = officer.objects.get(id=id)
#     return render(request, 'updateofficer.html', {"officer": getcriminaldetails})


# def requpdateofficer(request, id):
#     updatereq = officer.objects.get(id=id)
#     form = crform(request.POST)
#     if form.is_valid():
#         form.save()
#         delofficer = officer.objects.get(id=id)
#         delofficer.delete()
#         results = officer.objects.all()
#         messages.success(
#             request, "Officer record is updated successfully..!!!")
#         return render(request, "updateofficer.html", {"officer": requpdateofficer})
#     else:
#         messages.success(
#             request, "officer record is updated  is not successful.")


def crdelofficer(request, id):
    delofficer = officer.objects.get(id=id)
    delofficer.delete()
    results = officer.objects.all()
    return render(request, "officer.html", {"officer": results})


# ----fir view----
f = fir()


def insertfir(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('surname') and request.POST.get('address') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('crime_details') and request.POST.get('officer_name'):
            fir = f
            fir.name = request.POST.get('name')
            fir.surname = request.POST.get('surname')
            fir.address = request.POST.get('address')
            fir.age = request.POST.get('age')
            fir.gender = request.POST.get('gender')
            fir.crime_details = request.POST.get('crime_details')
            fir.officer_name = request.POST.get('officer_name')
            fir.save()
            messages.success(request, "The Record ** " +
                             fir.name+" ** is saved successfully!!!")
            return render(request, "createfir.html")
    else:
        return render(request, "createfir.html")


# def updatefir(request, id):
#     getcriminaldetails = fir.objects.get(id=id)
#     return render(request, 'updatefir.html', {"fir": getcriminaldetails})


# def requpdatefir(request, id):
#     updatereq = fir.objects.get(id=id)
#     form = crform(request.POST)
#     if form.is_valid():
#         form.save()
#         delfir = fir.objects.get(id=id)
#         delfir.delete()
#         results = fir.objects.all()
#         messages.success(
#             request, "FIR record is updated successfully..!!!")
#         return render(request, "updatefir.html", {"fir": requpdatefir})
#     else:
#         messages.success(
#             request, "Criminal record is updated  is not successful.")


def crdelfir(request, id):
    delfir = fir.objects.get(id=id)
    delfir.delete()
    results = fir.objects.all()
    return render(request, "fir.html", {"fir": results})


def logout_view(request):
    logout(request)
    return redirect('login')
