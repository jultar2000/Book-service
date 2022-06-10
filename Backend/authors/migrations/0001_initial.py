# Generated by Django 4.0.5 on 2022-06-07 19:14

from django.db import migrations, models
import django_countries.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('birth_date', models.DateField(blank=True, default=None, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], default=None, max_length=6, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, default=None, null=True, upload_to='')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
    ]