# Generated by Django 4.1.7 on 2023-06-26 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]
