# Generated by Django 4.2.3 on 2023-08-06 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_home', '0008_remove_randomtokengenerator_coupon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PsychologicalTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='psy_tasks/')),
                ('description', models.TextField()),
                ('amount', models.PositiveBigIntegerField(default=699)),
                ('validity', models.PositiveBigIntegerField(default=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('image', models.ImageField(upload_to='task_items/')),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('demo_link', models.URLField(null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_home.psychologicaltasks')),
            ],
        ),
    ]
