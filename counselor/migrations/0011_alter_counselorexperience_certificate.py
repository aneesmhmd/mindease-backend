# Generated by Django 4.2.3 on 2023-08-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselor', '0010_counselorexperience_certificate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counselorexperience',
            name='certificate',
            field=models.ImageField(upload_to='exp_certificates'),
        ),
    ]