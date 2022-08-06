# Generated by Django 4.0.5 on 2022-08-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FAN', 'Fantasy'), ('SCF', 'Science-fiction'), ('THR', 'Thriller'), ('HOR', 'Horror'), ('HIS', 'Historical')], max_length=3, null=True),
        ),
    ]