# Generated by Django 4.1.1 on 2022-09-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0006_alter_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(null=True, to='labels.label', verbose_name='Метки'),
        ),
    ]
