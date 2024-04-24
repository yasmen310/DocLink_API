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

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()
    departments = serializers.SerializerMethodField()
    class Meta:
        model = Hospital
        fields = ['id','hospitalName', 'location_details','departments','available_departments','location']
    def get_location_details(self, obj):
        location = obj.location
        if location:
            return {
                'street': location.street,
                'city': location.city,
                'country': location.country
            }
        else:
            return {}
    def get_departments(self, obj):
        departments = obj.available_departments.all()
        return [department.specializationName for department in departments]

class BedSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField()
    hospital_name = serializers.SerializerMethodField()
    class Meta:
        model = Bed
        fields =['bed_id','bedStatus', 'hospital_name', 'specialization_name','hospital','specialization']
    def get_specialization_name(self, obj):
        return obj.specialization.specializationName
    def get_hospital_name(self, obj):
        return obj.hospital.hospitalName

class ClinicSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField()
    location_details = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = ['id', 'clinicName', 'specialization_name', 'location_details', 'specialization','location']
        extra_kwargs = {
            'location': {'required': True}  # Mark location as required
        }
    def get_specialization_name(self, obj):
        return obj.specialization.specializationName
    def get_location_details(self, obj):
        return {
            'street': obj.location.street,
            'city': obj.location.city,
            'country': obj.location.country
        }


class DoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.SerializerMethodField()
    hospital_name = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = [ 'doctor_id', 'doctorName','email', 'specialization_name', 'hospital_name','specialization','hospital']
    def get_specialization_name(self, obj):
        return obj.specialization.specializationName
    def get_hospital_name(self, obj):
        return obj.hospital.hospitalName

class PatientSerializer(serializers.ModelSerializer):
    location_details = serializers.SerializerMethodField()
    prescription = serializers.ImageField(required=False, allow_null=True) 
    class Meta:
        model = Patient
        fields = ['patient_id', 'patientName', 'medical_information', 'location_details','prescription','location', 'email']
        extra_kwargs = {
            'location': {'required': True}  # Mark location as required
        }

    def get_location_details(self, obj):
        return {
            'street': obj.location.street,
            'city': obj.location.city,
            'country': obj.location.country
        }

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ClinicScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicSchedule
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'



