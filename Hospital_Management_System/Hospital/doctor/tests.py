from django.test import TestCase
from .models import *
from patient.models import *
from datetime import date

# Create your tests here.
class DocTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(doc_id=501, doc_name="Dr Tom", doc_email="tom2@gmail.com", specialisation="Neurologist",                               qualification="MD",image="")
        self.user = User.objects.create_user(first_name="John", last_name="Doe", username="anonym", email="anonym@gmail.com", password="123")
        self.patient = Patient.objects.create(user_id=self.user.id, address="Pokhara", contact=9841793851)
        self.report = Report.objects.create(patient_id_id=self.patient.id, rep_type="ENT Report", pdf="")
        self.appointment = Appointment.objects.create(patient_id_id=self.patient.id,doc_id_id=self.doctor.doc_id, appointment_date="2020-02-14", appointment_time="16:16")
       
    def testDoctors(self):
        d = Doctor.objects.get(doc_name="Dr Tom")
        self.assertEqual(d.doc_name, 'Dr Tom')
        
    def testUser(self):
        u = User.objects.get(username="anonym")
        self.assertEqual(u.username, 'anonym')
        
    def testPatient(self):
        p = Patient.objects.get(user_id=self.user.id)
        self.assertEqual(p.address, 'Pokhara')
        
    def testReport(self):
        r = Report.objects.get(patient_id_id=self.patient.id)
        self.assertEqual(r.rep_type, 'ENT Report')
        
    def testAppointment(self):
        a = Appointment.objects.get(patient_id_id=self.patient.id)
        self.assertEqual(a.appointment_date, date(2020,2,14))
