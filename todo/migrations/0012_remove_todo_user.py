# Generated by Django 3.2.3 on 2021-09-01 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20210901_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
