# Generated by Django 5.0.7 on 2024-07-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('middle_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('contact_number', models.CharField(default='', max_length=15)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('sex', models.CharField(default='', max_length=100)),
                ('birthday', models.CharField(default='', max_length=100)),
                ('place_of_birth', models.CharField(default='', max_length=100)),
                ('citizenship', models.CharField(default='', max_length=100)),
                ('blood_type', models.CharField(default='', max_length=100)),
                ('religion', models.CharField(default='', max_length=100)),
                ('civil_status', models.CharField(default='', max_length=100)),
                ('occupation', models.CharField(default='', max_length=100)),
                ('height', models.CharField(default='', max_length=100)),
                ('weight', models.CharField(default='', max_length=100)),
                ('father_surname', models.CharField(default='', max_length=100)),
                ('father_middle', models.CharField(default='', max_length=100)),
                ('mother_surname', models.CharField(default='', max_length=100)),
                ('mother_first', models.CharField(default='', max_length=100)),
                ('mother_middle', models.CharField(default='', max_length=100)),
                ('elementary', models.CharField(default='', max_length=100)),
                ('secondary', models.CharField(default='', max_length=100)),
                ('college', models.CharField(default='', max_length=100)),
                ('vocational_course', models.CharField(default='', max_length=100)),
                ('graduate_studies', models.CharField(default='', max_length=100)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('sss_number', models.CharField(default='', max_length=100)),
                ('name_of_children', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
