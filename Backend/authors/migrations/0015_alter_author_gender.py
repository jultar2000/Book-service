# Generated by Django 4.0.5 on 2022-09-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0014_alter_author_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=6),
        ),
    ]
