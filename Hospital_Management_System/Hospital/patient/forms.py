from django import forms
from .models import Patient, Appointment, Report

#form for creating appointment 
class AppForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'appointment_time')

#form for updating appointment        
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'appointment_time')

#form for uploading reports        
class RepForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('rep_type', 'pdf')