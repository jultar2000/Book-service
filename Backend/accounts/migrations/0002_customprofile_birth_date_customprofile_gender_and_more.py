# Generated by Django 4.0.5 on 2022-06-03 10:07

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customprofile',
            name='birth_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='customprofile',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default=None, max_length=6),
        ),
        migrations.AddField(
            model_name='customprofile',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='customprofile',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=40),
        ),
    ]
