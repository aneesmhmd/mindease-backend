# Generated by Django 4.2.3 on 2023-07-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_home', '0002_randomtokengenerator_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randomtokengenerator',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
