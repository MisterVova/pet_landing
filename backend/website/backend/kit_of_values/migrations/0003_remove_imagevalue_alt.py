# Generated by Django 3.1 on 2022-06-23 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kit_of_values', '0002_imagevalue_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagevalue',
            name='alt',
        ),
    ]
