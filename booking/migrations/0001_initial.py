# Generated by Django 4.2.9 on 2024-02-01 23:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('One vs One', 'One vs One'), ('Defending Training', 'Defending Training'), ('Finnishing and Passing', 'Finnishing and Passing'), ('Teknik and Dribbling', 'Teknik and Dribbling')], default='One vs One', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('5 PM', '5 PM'), ('7 PM', '7 PM')], default='3 PM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
