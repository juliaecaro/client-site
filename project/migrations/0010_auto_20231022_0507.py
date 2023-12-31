# Generated by Django 3.2.13 on 2023-10-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_itemtype_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemType',
            new_name='Type',
        ),
        migrations.RemoveField(
            model_name='item',
            name='ItemType',
        ),
        migrations.AddField(
            model_name='item',
            name='Type',
            field=models.ManyToManyField(help_text='Select an item type for this item.', to='project.Type'),
        ),
    ]
