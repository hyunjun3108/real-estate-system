# Generated by Django 4.2.1 on 2023-05-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housetable',
            name='currentlyUpdate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='housetable',
            name='firstUpdate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='housetable',
            name='jungong',
            field=models.CharField(max_length=50),
        ),
    ]