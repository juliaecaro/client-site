# Generated by Django 3.2.13 on 2023-10-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_alter_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]