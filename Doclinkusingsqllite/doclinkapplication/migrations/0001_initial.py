# Generated by Django 5.0.3 on 2024-04-18 14:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinicName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospitalName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specializationName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicSchedule',
            fields=[
                ('clinic_schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_id', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\d{8}$', 'doctor_id must be exactly 8 digits')])),
                ('doctor_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('available_slots', models.IntegerField(default=0)),
                ('booked_slots', models.IntegerField(default=0)),
                ('max_capacity', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=20)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.clinic')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorName', models.CharField(max_length=100)),
                ('doctor_id', models.CharField(max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{8}$', 'doctor_id must be exactly 8 digits')])),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.hospital')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.specialization')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.location'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.location'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientName', models.CharField(max_length=100)),
                ('patient_id', models.CharField(max_length=14, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{14}$', 'patient_id must be exactly 14 digits')])),
                ('medical_information', models.TextField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.location')),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='available_departments',
            field=models.ManyToManyField(to='doclinkapplication.specialization'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.specialization'),
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('bedStatus', models.CharField(default='unavailable', max_length=100)),
                ('bed_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.hospital')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.clinic')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.patient')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doclinkapplication.user')),
            ],
        ),
    ]
