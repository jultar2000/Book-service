# Generated by Django 4.0.5 on 2022-09-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_alter_address_address_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('S', 'Shipping'), ('B', 'Billing')], max_length=1),
        ),
    ]
