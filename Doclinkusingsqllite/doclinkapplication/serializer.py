from rest_framework import serializers

from .models import Specialization, User, Clinic, Location, Doctor, Appointment, Patient, Hospital, Bed, ClinicSchedule, Notification


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClinicSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='specialization.specializationName')
    # doctor_name = serializers.CharField(source='doctor.doctorName', allow_null=True)
    # doctor_id = serializers.CharField(source='doctor.doctor_id', allow_null=True)
    
    class Meta:
        model = Clinic
        fields = ['id', 'clinicName', 'specialization_name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='specialization.specializationName')
    hospital_name = serializers.CharField(source='hospital.hospitalName')

    class Meta:
        model = Doctor
        fields = [ 'doctor_id', 'doctorName', 'specialization_name', 'hospital_name']


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.doctorName')
    patient_name = serializers.CharField(source='patient.patientName')
    clinic_name = serializers.CharField(source='clinic.clinicName', allow_null=True)
    specialization_name = serializers.CharField(source='doctor.specialization.specializationName')

    class Meta:
        model = Appointment
        fields = ['appointment_id', 'date_time', 'doctor_name', 'patient_name','clinic_name', 'specialization_name']


class PatientSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()
    class Meta:
        model = Patient
        fields = ['patient_id','patientName', 'medical_information', 'location_details']
    def get_location_details(self, obj):
        return {
            'street': obj.location.street,
            'city': obj.location.city,
            'country': obj.location.country
        }


class HospitalSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()
    available_departments = SpecializationSerializer(many=True)
    class Meta:
        model = Hospital
        fields = ['id','hospitalName', 'location_details', 'available_departments']
    def get_location_details(self, obj):
        return {
            'street': obj.location.street,
            'city': obj.location.city,
            'country': obj.location.country
        }

class BedSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='specialization.specializationName')
    hospital_name = serializers.CharField(source='hospital.hospitalName')
    class Meta:
        model = Bed
        fields =['bed_id','bedStatus', 'hospital_name', 'specialization_name']



class ClinicScheduleSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.clinicName', read_only=True)
    class Meta:
        model = ClinicSchedule
        fields = ['clinic_schedule_id','clinic_name', 'doctor_id', 'doctor_name', 'date', 'start_time', 'end_time', 'duration', 'available_slots', 'booked_slots', 'max_capacity', 'status']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

