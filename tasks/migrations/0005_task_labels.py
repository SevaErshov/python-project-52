# Generated by Django 4.1 on 2022-09-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0004_alter_task_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(to='labels.label', verbose_name='Labels'),
        ),
    ]