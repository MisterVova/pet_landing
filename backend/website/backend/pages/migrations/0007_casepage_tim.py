# Generated by Django 3.1 on 2022-06-25 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('pages', '0006_auto_20220625_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='casepage',
            name='tim',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='case_page_staffs', to='staff.staff', verbose_name='Команда проекта'),
            preserve_default=False,
        ),
    ]
