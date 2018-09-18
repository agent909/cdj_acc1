# Generated by Django 2.1 on 2018-09-18 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
        ('entry', '0002_auto_20180906_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReceivableEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('credit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date', models.DateTimeField(verbose_name='Entry Date')),
                ('account_receivable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.AccountReceivable')),
            ],
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('credit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date', models.DateTimeField(verbose_name='Document Date')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Client')),
            ],
        ),
        migrations.RemoveField(
            model_name='accountpayable',
            name='client',
        ),
        migrations.RemoveField(
            model_name='cashadvance',
            name='client',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.RemoveField(
            model_name='loanspayable',
            name='client',
        ),
        migrations.DeleteModel(
            name='AccountPayable',
        ),
        migrations.DeleteModel(
            name='CashAdvance',
        ),
        migrations.DeleteModel(
            name='LoansPayable',
        ),
    ]
