from django.shortcuts import render, redirect
from .forms import RegForm, ProfileForm, DashForm, UpdateForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from doctor.models import Doctor
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
# Create your views here.

#user registration
def reg_patient(request):
    if request.method == 'POST':
        form = RegForm(data=request.POST)
        #start
        formProfile = ProfileForm(data=request.POST)
        if form.is_valid() and formProfile.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            prof = formProfile.save(commit=False)
            prof.user = User.objects.get(pk=user.id)
            prof.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            user=authenticate(username=username,email=email,password=password)
            login(request,user)
            return redirect('account:logged_in')
        else:
            return render(request, "account/register.html",{'error':"Username/Email already in use. Please try another username/email!"})
            
    else:
        form = RegForm()
        formProfile = ProfileForm()
        return render(request, "account/register.html", {"form":form,"formProfile":formProfile})

#user login
def patient_login(request):
    if request.method=='POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request,username=un,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('account:dashboard')
            
        else:
            return render(request, "account/login.html",{'error':"Invalid Username or Password"})
    else:
        return render(request, "account/login.html")

#user logout
def patient_logout(request):
    logout(request)
    return render(request,"doctor/index.html",{"patient_logout":patient_logout})

#user login display after logging in           
def logged_in(request):
    return render(request,"account/logged_in.html",{"logged_in":logged_in})

#decorators
@login_required(login_url='account:patient_login')
@admin_only
#admin dashboard 
def dashboard(request):
    return render(request, 'account/dashboard.html', {"doctor" : Doctor.objects.all()})

@login_required(login_url='account:patient_login')
@admin_only
#add doctors from admin site
def addDoc(request):
    form = DashForm(request.POST,request.FILES)
    if form.is_valid():
        doc_id = form.cleaned_data.get('doc_id')
        doc_name = form.cleaned_data.get('doc_name')
        doc_email = form.cleaned_data.get('doc_email')
        specialisation = form.cleaned_data.get('specialisation')
        qualification = form.cleaned_data.get('qualification')
        image = form.cleaned_data.get('image')
        form.save()
        return redirect('account:dashboard')
        
    else:
        form = DashForm()
        return render(request, "account/addDoc.html", {"form":form})
    

@login_required(login_url='account:patient_login')
@admin_only
#update doctors from admin site
def updateDoc(request, pk=None):
    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES)
        if form.is_valid():
            d = Doctor.objects.get(pk=pk)
            d.doc_name = form.cleaned_data['doc_name']
            d.doc_email = form.cleaned_data['doc_email']
            d.specialisation = form.cleaned_data['specialisation']
            d.qualification = form.cleaned_data['qualification']
            d.save()
            return redirect('account:dashboard')

    else:
        form = UpdateForm()
        return render(request, 'account/updateDoc.html', {"form":form})
    
@login_required(login_url='account:patient_login')
@admin_only
#delete doctors from admin site
def deleteDoc(request, pk=None):
    d = Doctor.objects.get(pk=pk)
    d.delete()
    return redirect('account:dashboard')

        
        
