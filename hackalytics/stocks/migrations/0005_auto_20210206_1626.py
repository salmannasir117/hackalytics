# Generated by Django 3.1.6 on 2021-02-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_auto_20210206_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='data',
            field=models.BinaryField(),
        ),
    ]