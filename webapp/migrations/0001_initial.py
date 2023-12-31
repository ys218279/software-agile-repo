# Generated by Django 4.2.5 on 2023-09-29 00:19

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
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(choices=[('Monitor', 'monitor'), ('Laptop', 'laptop'), ('Desktop', 'desktop'), ('Keyboard', 'keyboard'), ('Mouse', 'mouse')], max_length=8)),
                ('location_use', models.CharField(choices=[('Home', 'home'), ('Office', 'office')], max_length=6)),
                ('date_hired', models.DateField(max_length=8)),
                ('date_returned', models.DateField(max_length=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=225)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=225)),
                ('postcode', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=125)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
