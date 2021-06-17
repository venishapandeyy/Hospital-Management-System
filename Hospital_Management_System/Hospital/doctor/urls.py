from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "doctor"

urlpatterns = [
    path('', views.index, name="index"),
    path('doctor/', views.list_doc, name="list_doc"),
] 