from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "patient"

urlpatterns = [
    path('appointment/create/<int:pk>', views.create_appointment, name="create_appointment"),
    path('appointment/',views.list_appointment,name="list"),
    path('appointment/<int:pk>/', views.delete_appointment, name="delete_appointment"),
    path('update/<int:pk>/', views.update_appointment, name="update_appointment"), 
    path('report/upload/', views.upload_report, name="upload"),
    path('report/', views.list_report, name="rep_list"),
] 