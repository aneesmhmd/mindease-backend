# Generated by Django 4.2.3 on 2023-08-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_timeslots_counselor'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentpayments',
            name='is_booked',
            field=models.BooleanField(default=True),
        ),
    ]
