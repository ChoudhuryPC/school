# Generated by Django 2.2.7 on 2020-09-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200917_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start',
            field=models.TimeField(blank=True),
        ),
    ]