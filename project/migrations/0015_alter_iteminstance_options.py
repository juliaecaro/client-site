# Generated by Django 3.2.13 on 2023-10-24 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_iteminstance_renter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iteminstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set item as returned'),)},
        ),
    ]
