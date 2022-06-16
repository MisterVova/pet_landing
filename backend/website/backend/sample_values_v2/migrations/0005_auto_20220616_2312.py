# Generated by Django 3.1 on 2022-06-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_values_v2', '0004_kit_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='kit',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=150, unique=True, verbose_name='ЧПУ'),
        ),
        migrations.AlterField(
            model_name='kit',
            name='values',
            field=models.ManyToManyField(blank=True, related_name='kits', to='sample_values_v2.Value', verbose_name='values'),
        ),
    ]
