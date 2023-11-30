# Generated by Django 3.2.13 on 2023-10-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20231028_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='emailaddress@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.FloatField(default='0000000000'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default='some message'),
        ),
    ]