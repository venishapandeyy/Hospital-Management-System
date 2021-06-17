from django.shortcuts import render
from doctor.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

#get all the data set
def api_data(request):
    doctor = Doctor.objects.all()
    dict_value = {"doctors": list(doctor.values("doc_id","doc_name","doc_email","specialisation","qualification"))}
    return JsonResponse(dict_value)  

#get specific data set
def api_spec_data(request,pk=None):
    doctor = Doctor.objects.get(pk=pk)
    return JsonResponse({"doc_id" : doctor.doc_id, "doc_name" : doctor.doc_name, "doc_email" : doctor.doc_email, "specialisation" : doctor.specialisation,"qualification" : doctor.qualification})  

#decorators
@csrf_exempt 
#adding new data set
def api_add(request):
    doctor = Doctor()
    if request.method == "POST":
        decoded_data = request.body.decode('utf-8')
        doctor_data = json.loads(decoded_data)
        doctor.doc_id = doctor_data['doc_id']
        doctor.doc_name = doctor_data['doc_name']
        doctor.doc_email = doctor_data['doc_email']
        doctor.specialisation = doctor_data['specialisation']
        doctor.qualification = doctor_data['qualification']
        doctor.save()
        return JsonResponse({"message" : "Completed"})
    else:
        return JsonResponse({"doc_id" : doctor.doc_id, "doc_name" : doctor.doc_name, "doc_email" : doctor.doc_email, "specialisation" : doctor.specialisation,"qualification" : doctor.qualification})
    
        
@csrf_exempt 
#updating the data set       
def api_update_data(request, pk=None):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == "PUT":
        decoded_data = request.body.decode('utf-8')
        doctor_data = json.loads(decoded_data)
        doctor.doc_id = doctor_data['doc_id']
        doctor.doc_name = doctor_data['doc_name']
        doctor.doc_email = doctor_data['doc_email']
        doctor.specialisation = doctor_data['specialisation']
        doctor.qualification = doctor_data['qualification']
        doctor.save()
        return JsonResponse({"message" : "Updated"})
    
    else:
        return JsonResponse({"doc_id" : doctor.doc_id, "doc_name" : doctor.doc_name, "doc_email" : doctor.doc_email, "specialisation" : doctor.specialisation,"qualification" : doctor.qualification})
    
@csrf_exempt
#deleting the data set        
def api_delete_data(request, pk=None):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == "DELETE":
        doctor.delete()
        return JsonResponse({"message" : "Deleted"})
    
    else:
        return JsonResponse({"doc_id" : doctor.doc_id, "doc_name" : doctor.doc_name, "doc_email" : doctor.doc_email, "specialisation" : doctor.specialisation,"qualification" : doctor.qualification})

#pagination    
def api_hospital_pagination(request, PAGENO):
    SIZE = 2
    skip = SIZE * (PAGENO-1)
    doctor = Doctor.objects.all()[skip:PAGENO*SIZE]
    dict = {
        "doctors": list(doctor.values("doc_id","doc_name","doc_email","specialisation","qualification"))
    }
    return JsonResponse(dict)