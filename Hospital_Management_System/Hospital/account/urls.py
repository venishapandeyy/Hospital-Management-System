from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "account"

urlpatterns = [
    path('register/', views.reg_patient, name="reg_patient"),
    path('login/',views.patient_login,name="patient_login"),
    path('logged_in/',views.logged_in,name="logged_in"),
    path('logout/',views.patient_logout,name="patient_logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/add_doc', views.addDoc, name="addDoc"),
    path('dashboard/update/<int:pk>', views.updateDoc, name="updateDoc"),
    path('dashboard/delete/<int:pk>', views.deleteDoc, name="deleteDoc")
] 