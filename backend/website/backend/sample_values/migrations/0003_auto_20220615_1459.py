# Generated by Django 3.1 on 2022-06-15 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sample_values', '0002_keyandmanyvalue_keyandvalue_keyvalue_kitofvalues'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='basevalue',
            options={'ordering': ('-pk', 'name'), 'verbose_name': 'Свободные значение', 'verbose_name_plural': 'Свободные значения'},
        ),
        migrations.AlterModelOptions(
            name='keyvalue',
            options={'ordering': ('kay', '-pk', 'name'), 'verbose_name': 'Ключ', 'verbose_name_plural': 'Ключи'},
        ),
        migrations.AlterField(
            model_name='keyandvalue',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='key_and_value', to='sample_values.basevalue', verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='kitofvalues',
            name='value',
            field=models.ManyToManyField(related_name='kit_of_values', to='sample_values.KeyValue', verbose_name='values'),
        ),
        migrations.AddField(
            model_name='basevalue',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='values', to='sample_values.group', verbose_name='Группа'),
        ),
    ]
