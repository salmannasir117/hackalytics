# Generated by Django 3.1.6 on 2021-02-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_auto_20210206_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='data_series',
            field=models.CharField(blank=True, choices=[('real GDP', 'REAL_GDP'), ('nominal GDP converted from real GDP', 'NOMINAL_GDP_CONVERTED'), ('nominal GDP', 'NOMINAL_GDP_RAW')], max_length=200),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='parameter_set',
            field=models.CharField(blank=True, choices=[('Traditional', 'TRADITIONAL'), ('Novel', 'NOVEL'), ('Unorthodox', 'UNORTHODOX')], max_length=200),
        ),
    ]
