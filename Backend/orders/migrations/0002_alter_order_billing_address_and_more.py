# Generated by Django 4.0.5 on 2022-06-10 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='profiles.address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='custom_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.customprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_adress', to='profiles.address'),
        ),
    ]