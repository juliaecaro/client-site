# Generated by Django 3.2.13 on 2023-10-22 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20231022_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='name',
            new_name='type',
        ),
    ]
