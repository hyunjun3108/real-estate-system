# Generated by Django 4.2.1 on 2023-05-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_housetable_latitude_housetable_longtitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housetable',
            name='idx',
        ),
        migrations.AddField(
            model_name='housetable',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]