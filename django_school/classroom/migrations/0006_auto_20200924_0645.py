# Generated by Django 2.2.7 on 2020-09-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20200917_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateField(default='2020-09-24'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='today',
            field=models.DateField(default='2020-09-24'),
        ),
    ]