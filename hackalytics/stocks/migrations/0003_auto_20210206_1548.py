# Generated by Django 3.1.6 on 2021-02-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20210206_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='data',
            field=models.FileField(upload_to='../static/stocks'),
        ),
    ]
