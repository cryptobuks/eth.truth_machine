# Generated by Django 3.2.15 on 2022-09-19 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=250)),
                ('facebook', models.CharField(max_length=250)),
                ('instagram', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MetamaskAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_wallet_address', models.CharField(blank=True, max_length=255, null=True)),
                ('balance', models.FloatField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_account', models.CharField(blank=True, max_length=250, null=True)),
                ('gas', models.IntegerField(blank=True, default=0, null=True)),
                ('value', models.FloatField(blank=True, default=0, null=True)),
                ('gas_price', models.IntegerField(blank=True, default=0, null=True)),
                ('res_hash', models.CharField(blank=True, max_length=250, null=True)),
                ('data', models.CharField(blank=True, max_length=5000, null=True)),
                ('text', models.CharField(blank=True, max_length=250, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.metamaskaccount')),
            ],
        ),
    ]