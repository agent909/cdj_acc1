# Generated by Django 2.1 on 2018-10-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0007_auto_20181002_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(verbose_name='Document Date'),
        ),
    ]
