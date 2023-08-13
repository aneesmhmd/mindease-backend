# Generated by Django 4.2.3 on 2023-08-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallBackReqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('is_contacted', models.BooleanField(default=False)),
            ],
        ),
    ]