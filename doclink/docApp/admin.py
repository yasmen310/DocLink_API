from django.contrib import admin
from .models import Specialization, User, Clinic, Location, Doctor, Appointment, Patient, Hospital, Bed ,ClinicSchedule,Notification

admin.site.register(Specialization)
admin.site.register(User)
admin.site.register(Clinic)
admin.site.register(Location)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Bed)
admin.site.register(ClinicSchedule)
admin.site.register(Notification)