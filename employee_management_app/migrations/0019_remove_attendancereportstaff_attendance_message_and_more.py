# Generated by Django 4.0.6 on 2022-11-14 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0018_remove_leavereportstaff_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereportstaff',
            name='attendance_message',
        ),
        migrations.RemoveField(
            model_name='attendancereportstaff',
            name='attendance_status',
        ),
    ]