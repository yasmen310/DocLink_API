# Generated by Django 5.0.3 on 2024-04-28 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_doctor_doctorimg_patient_patientimg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='medical_information',
            new_name='report',
        ),
        migrations.AddField(
            model_name='clinic',
            name='related_hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.hospital'),
        ),
    ]