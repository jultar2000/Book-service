# Generated by Django 4.0.5 on 2022-06-10 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_billing_address_and_more'),
        ('accounts', '0012_alter_customprofile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customprofile',
            name='custom_user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='CustomProfile',
        ),
    ]