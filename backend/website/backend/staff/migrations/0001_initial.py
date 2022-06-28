# Generated by Django 3.1 on 2022-06-25 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kit_of_values', '0007_auto_20220625_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Имя')),
                ('kit_values', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff_values', to='kit_of_values.kit', verbose_name='Набор Значений Для Команды')),
            ],
            options={
                'verbose_name': 'Команда проекта',
                'verbose_name_plural': 'Команды проектов',
                'ordering': ('name',),
            },
        ),
    ]
