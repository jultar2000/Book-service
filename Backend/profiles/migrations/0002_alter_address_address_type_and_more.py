# Generated by Django 4.0.5 on 2022-06-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('S', 'Shipping'), ('B', 'Billing')], max_length=1),
        ),
        migrations.AlterField(
            model_name='address',
            name='apartment_num',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='house_num',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customprofile',
            name='birth_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customprofile',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
    ]
