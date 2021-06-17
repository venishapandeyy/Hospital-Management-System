from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Doctor
from django.db.models import Q
from account.decorators import user_only

# Create your views here.
#decorator
@user_only
#index page
def index(request):
    return render(request=request, template_name="doctor/index.html", context={})

#listing all the doctors
def list_doc(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET['q']    
    
    
    doctor = get_data_queryset(query)
    context['doctors'] = doctor
    return render(request, "doctor/search_doctor.html", context)

#search query for doctors
def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        doctors = Doctor.objects.filter(Q( doc_name__icontains=q) | Q(doc_email__icontains=q) | Q(specialisation__icontains=q))
        
        for doctor in doctors:
            queryset.append(doctor)
    
    return list(set(queryset)) 