# Generated by Django 4.0.5 on 2022-06-15 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(default=None, max_length=40)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default=None, max_length=1, null=True)),
                ('image', versatileimagefield.fields.VersatileImageField(default=None, null=True, upload_to='')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('custom_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=50)),
                ('city_name', models.CharField(max_length=50)),
                ('apartment_num', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('house_num', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=100)),
                ('custom_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.customprofile')),
            ],
        ),
    ]
