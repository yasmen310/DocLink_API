"""
URL configuration for DOClink22 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'myapp'  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/specialization/',views.SpecializationListView.as_view(), name='api-SpecializationListView'),
    path('api/specialization/<int:pk>/',views.SpecializationDetailView.as_view(), name='api-SpecializationDetailView'),
]
urlpatterns += [
    path('api/users/',views.UserListCreate.as_view(), name='api-user-list-create'),
]
urlpatterns += [
    path('api/clinic/',views.ClinicListView.as_view(), name='api-ClinicListView'),
    path('api/clinic/<int:pk>/',views.ClinicDetailView.as_view(), name='api-ClinicDetailView'),
]
urlpatterns += [
    path('api/location/',views.LocationListView.as_view(), name='api-LocationListView'),
    path('api/location/<int:pk>/',views.LocationDetailView.as_view(), name='api-LocationDetailView'),
]
urlpatterns += [
    path('api/doctor/',views.DoctorListView.as_view(), name='api-DoctorListView'),
    path('api/doctor/<int:pk>/',views.DoctorDetailView.as_view(), name='api-DoctorDetailView'),
]
urlpatterns += [
    path('api/bed/',views.BedListView.as_view(), name='api-BedListView'),
    path('api/bed/<int:pk>/',views.BedDetailView.as_view(), name='api-BedDetailView'),
]
urlpatterns += [
    path('api/hospital/',views.HospitalListView.as_view(), name='api-HospitalListView'),
    path('api/hospital/<int:pk>/',views.HospitalDetailView.as_view(), name='api-HospitalDetailView'),
]
urlpatterns += [
    path('api/patient/',views.PatientListView.as_view(), name='api-PatientListView'),
    path('api/patient/<int:pk>/',views.PatientDetailView.as_view(), name='api-PatientDetailView'),
]
urlpatterns += [
    path('api/appointment/',views.AppointmentListView.as_view(), name='api-AppointmentListView'),
    path('api/appointment/<int:pk>/',views.AppointmentDetailView.as_view(), name='api-AppointmentDetailView'),
]
urlpatterns += [
    path('api/clinicSchedule/',views.ClinicScheduleListView.as_view(), name='api-ClinicScheduleListView'),
    path('api/clinicSchedule/<int:pk>/',views.ClinicScheduleDetailView.as_view(), name='api-ClinicScheduleDetailView'),
]
urlpatterns += [
    path('api/notifications/', views.NotificationListCreate.as_view(), name='api-notification-list-create'),
]
