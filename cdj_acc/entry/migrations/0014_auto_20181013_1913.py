# Generated by Django 2.1 on 2018-10-13 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0013_paymenttoaccountreceivable_documentnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashinbank',
            old_name='amount',
            new_name='cash',
        ),
        migrations.RenameField(
            model_name='cashonhand',
            old_name='amount',
            new_name='cash',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='amount',
            new_name='cash',
        ),
    ]