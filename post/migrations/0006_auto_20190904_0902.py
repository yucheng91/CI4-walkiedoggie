# Generated by Django 2.2.4 on 2019-09-04 09:02

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20190904_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpost',
            name='cover',
            field=pyuploadcare.dj.models.ImageField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=pyuploadcare.dj.models.ImageField(default=''),
        ),
    ]
