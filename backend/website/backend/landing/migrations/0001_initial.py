# Generated by Django 3.1 on 2022-06-23 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('garpix_page', '0001_initial'),
        ('show', '0001_initial'),
        ('kit_of_values', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
                ('html_template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='landing_pages_html', to='show.template', verbose_name='html_template')),
                ('kit_template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='landing_page_templates', to='kit_of_values.kit', verbose_name='Набор Шаблонов')),
                ('kit_values', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='landing_page_values', to='kit_of_values.kit', verbose_name='Набор Значений')),
            ],
            options={
                'verbose_name': 'Landing',
                'verbose_name_plural': 'Landings',
                'ordering': ('-created_at',),
            },
            bases=('garpix_page.basepage',),
        ),
    ]
