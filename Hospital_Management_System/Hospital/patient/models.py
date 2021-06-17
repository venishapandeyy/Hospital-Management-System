from django.db import models
from doctor.models import Doctor 
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    contact = models.IntegerField()
    doc_id = models.ManyToManyField(Doctor) 

    def __str__(self):
        return self.user.first_name

class Appointment(models.Model):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    

    def __str__(self):
        return 'Appointment Confirmed'

class Report(models.Model):
    rep_type = models.CharField(max_length=25)
    pdf = models.FileField(upload_to="report/pdfs/")
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.report_id 