# Generated by Django 4.1.5 on 2023-01-14 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_course_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programs',
            old_name='course',
            new_name='course_name',
        ),
    ]