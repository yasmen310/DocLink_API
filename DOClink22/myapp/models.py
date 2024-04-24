from django.db import models
from django.core.validators import RegexValidator

class Specialization(models.Model):
    specializationName = models.CharField(max_length=50)

    def __str__(self):
        return self.specializationName 

class User(models.Model):
    username = models.CharField(max_length=150)  
    password = models.CharField(max_length=128) 
    registration_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)


class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Hospital(models.Model):
    hospitalName = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE ,null=True, blank=True) 
    available_departments = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"{self.hospitalName }, {self.location}"


class Bed(models.Model):
    bedStatus = models.CharField(max_length=100, default="unavailable")
    bed_id = models.CharField(primary_key=True, max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.bed_id

class Clinic(models.Model):
    clinicName = models.CharField(max_length=50)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.clinicName} - {self.location.street}, {self.location.city}, {self.location.country}"


class Doctor(models.Model):
    doctorName = models.CharField(max_length=100)
    doctor_id = models.CharField(primary_key=True,max_length=8, validators=[
        RegexValidator(r'^\d{8}$', 'doctor_id must be exactly 8 digits')
    ])
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE ,null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.doctorName


class Patient(models.Model):
    patientName = models.CharField(max_length=100)
    patient_id = models.CharField(primary_key=True,max_length=14, validators=[
        RegexValidator(r'^\d{14}$', 'patient_id must be exactly 14 digits')
    ])
    medical_information = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE) 
    prescription = models.ImageField(upload_to='prescriptions/', blank=True, null=True)   
    email = models.EmailField(blank=True, null=True) 
    def __str__(self):
        return self.patientName  


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}"


class ClinicSchedule(models.Model):
    clinic_schedule_id = models.AutoField(primary_key=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor_id = models.CharField(max_length=8, validators=[
        RegexValidator(r'^\d{8}$', 'doctor_id must be exactly 8 digits')
    ])
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField(null=True, blank=True)
    available_slots = models.IntegerField(default=0)
    booked_slots = models.IntegerField(default=0)
    max_capacity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default='active')  

    def __str__(self):
        return f"{self.clinic_schedule_id} - {self.date}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"


