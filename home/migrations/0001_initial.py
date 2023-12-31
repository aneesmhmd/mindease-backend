# Generated by Django 4.2.3 on 2023-08-25 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_home', '0001_initial'),
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
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='services/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.PositiveBigIntegerField()),
                ('validity', models.PositiveBigIntegerField()),
                ('subscribed_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField(null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_home.psychologicaltasks')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
