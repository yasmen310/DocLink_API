from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication

from .models import Specialization, User, Clinic, Location, Doctor, Appointment, Patient, Hospital, Bed, ClinicSchedule, Notification
from .serializer import SpecializationSerializer,UserSerializer, ClinicSerializer, LocationSerializer, DoctorSerializer, AppointmentSerializer, PatientSerializer, HospitalSerializer, BedSerializer, ClinicScheduleSerializer, NotificationSerializer
from .permissions import IsAuthorOrReadOnly

class SpecializationListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
  

class SpecializationDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class UserListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClinicListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
  

class ClinicDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    


class LocationListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    

class DoctorListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        doctor_specialization = serializer.validated_data.get("specialization")
        doctor_location = serializer.validated_data.get("location")
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    

class BedListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Bed.objects.all()
    serializer_class = BedSerializer


class BedDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
  

class PatientListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer



class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
  

class AppointmentListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class HospitalListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
  

class ClinicScheduleListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = ClinicSchedule.objects.all()
    serializer_class = ClinicScheduleSerializer
  

class ClinicScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = ClinicSchedule.objects.all()
    serializer_class = ClinicScheduleSerializer
  


class NotificationListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer



