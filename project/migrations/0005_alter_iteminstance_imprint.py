# Generated by Django 3.2.13 on 2023-10-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20231021_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminstance',
            name='imprint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
