# Generated by Django 5.0.3 on 2024-05-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_assistent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
    ]
