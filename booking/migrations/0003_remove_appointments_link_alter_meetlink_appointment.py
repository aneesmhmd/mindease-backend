# Generated by Django 4.2.3 on 2023-08-30 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_appointments_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='link',
        ),
        migrations.AlterField(
            model_name='meetlink',
            name='appointment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.appointments'),
        ),
    ]
