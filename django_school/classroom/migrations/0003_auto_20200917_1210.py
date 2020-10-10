# Generated by Django 2.2.7 on 2020-09-17 12:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_create_initial_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='student',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='text',
        ),
        migrations.RemoveField(
            model_name='takenquiz',
            name='date',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.FileField(default='teacher/default.jpg', upload_to='student'),
        ),
        migrations.AddField(
            model_name='answer',
            name='quiz_name',
            field=models.CharField(default='yo', max_length=20),
        ),
        migrations.AddField(
            model_name='answer',
            name='roll',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subject_fill', to='classroom.Subject'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='date',
            field=models.DateField(default='2020-09-17'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='end',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 9, 17, 12, 10, 35, 73914)),
        ),
        migrations.AddField(
            model_name='quiz',
            name='pdf',
            field=models.FileField(default='teacher/default.jpg', upload_to='teacher'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='start',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 9, 17, 12, 10, 35, 73889)),
        ),
        migrations.AddField(
            model_name='quiz',
            name='today',
            field=models.DateField(default='2020-09-17'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
    ]
