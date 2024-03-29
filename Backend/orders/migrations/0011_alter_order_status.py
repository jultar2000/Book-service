# Generated by Django 4.0.5 on 2022-08-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_order_active_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('R', 'RECEIVED'), ('S', 'BEING DELIVERED'), ('P', 'BEING PREPARED')], default=None, max_length=1),
        ),
    ]
