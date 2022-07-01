# Generated by Django 4.0.5 on 2022-06-30 23:02

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
            name='StudentEducationBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elementary', models.CharField(max_length=256)),
                ('secondary', models.CharField(max_length=256)),
                ('senior_high', models.CharField(max_length=256)),
                ('school_location', models.CharField(max_length=256)),
                ('year_graduated', models.CharField(max_length=256)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentBackgroundEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mother_name', models.CharField(max_length=256)),
                ('mother_ocupation', models.CharField(max_length=256)),
                ('mother_income', models.CharField(max_length=256)),
                ('father_name', models.CharField(max_length=256)),
                ('father_ocupation', models.CharField(max_length=256)),
                ('father_income', models.CharField(max_length=256)),
                ('contact', models.CharField(max_length=256)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAdditionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=256)),
                ('year_level', models.CharField(max_length=256)),
                ('units_enrolled', models.CharField(max_length=256)),
                ('expected_year_graduation', models.CharField(max_length=256)),
                ('graduating', models.BooleanField()),
                ('school_name', models.CharField(max_length=256)),
                ('school_address', models.CharField(max_length=256)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=256)),
                ('birthday', models.DateField()),
                ('birth_place', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('contact', models.CharField(max_length=256)),
                ('sex', models.CharField(max_length=256)),
                ('civil_status', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]