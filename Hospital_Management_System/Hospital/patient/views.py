from django.shortcuts import render, redirect
from .forms import AppForm, UpdateForm, RepForm
from .models import Appointment,Patient, Report
from doctor.models import Doctor
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from account.decorators import user_only

# Create your views here.

#decorators
@login_required(login_url='account:patient_login')
@user_only
#create appointment
def create_appointment(request, pk=None):
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            p = Patient.objects.get(user_id = request.user.id)
            a = Appointment(patient_id_id = p.id)
            a.doc_id_id = pk
            a.appointment_date = form.cleaned_data['appointment_date']
            a.appointment_time = form.cleaned_data['appointment_time']
            a.save()
            return redirect('patient:list')
        
    else:
        form = AppForm()
    return render(request, "patient/appointment.html", {"form":form})

@login_required(login_url='account:patient_login')
@user_only
#listing all the created appointments
def list_appointment(request):
    p = Patient.objects.get(user_id = request.user.id)
    appointment = Appointment.objects.filter(patient_id_id = p.id)
    return render(request, "patient/list.html", {"appointments":appointment})

@login_required(login_url='account:patient_login')
@user_only
#delete appointment
def delete_appointment(request, pk=None):
    appointment = Appointment.objects.get(pk=pk)
    appointment.delete()
    return redirect('patient:list')

@login_required(login_url='account:patient_login')  
@user_only
#update appointment
def update_appointment(request, pk=None):
    if request.method == 'POST':
        form = UpdateForm(request.POST)

        if form.is_valid():
            a = Appointment.objects.get(pk=pk)
            a.appointment_date = form.cleaned_data['appointment_date']
            a.appointment_time = form.cleaned_data['appointment_time']
            a.save()
            return redirect('patient:list')

    else:
        form = UpdateForm()
        return render(request, 'patient/update_appointment.html', {'form': form})
    
    
@login_required(login_url='account:patient_login') 
@user_only
#report upload
def upload_report(request):
    if request.method == "POST":
        form = RepForm(request.POST, request.FILES)
        if form.is_valid():
            p = Patient.objects.get(user_id = request.user.id)
            r = Report(patient_id_id = p.id)
            r.rep_type = form.cleaned_data['rep_type']
            r.pdf = form.cleaned_data['pdf']
            r.save()
            return redirect('patient:rep_list')
        
    else:
        form = RepForm()
    return render(request, "patient/report.html", {"form":form})

@login_required(login_url='account:patient_login') 
@user_only
#listing all the uploaded reports
def list_report(request):
    p = Patient.objects.get(user_id = request.user.id)
    report = Report.objects.filter(patient_id_id = p.id)
    return render(request, "patient/rep_list.html", {"reports":report})