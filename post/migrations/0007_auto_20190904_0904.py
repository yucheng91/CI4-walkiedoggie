# Generated by Django 2.2.4 on 2019-09-04 09:04

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20190904_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='cover',
            field=pyuploadcare.dj.models.ImageField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
