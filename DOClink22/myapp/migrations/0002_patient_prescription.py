# Generated by Django 5.0.3 on 2024-04-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='prescription',
            field=models.ImageField(blank=True, null=True, upload_to='prescriptions/'),
        ),
    ]
