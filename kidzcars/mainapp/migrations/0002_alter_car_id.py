# Generated by Django 4.2.1 on 2023-05-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]