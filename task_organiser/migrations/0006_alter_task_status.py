# Generated by Django 4.0.5 on 2022-10-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_organiser', '0005_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('to do', 'to do'), ('in progress', 'in progress')], max_length=20, null=True),
        ),
    ]
