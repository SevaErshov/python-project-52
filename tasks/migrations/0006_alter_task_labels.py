# Generated by Django 4.1 on 2022-09-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0005_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(to='labels.label', verbose_name='Метки'),
        ),
    ]