# Generated by Django 2.1 on 2018-10-03 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0008_auto_20181002_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentToAccountReceivable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Document Date')),
                ('cash', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('receivable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entry.AccountReceivable')),
                ('transaction_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='entry.Transactions')),
            ],
        ),
    ]