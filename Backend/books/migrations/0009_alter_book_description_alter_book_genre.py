# Generated by Django 4.0.5 on 2022-08-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('HIS', 'Historical'), ('FAN', 'Fantasy'), ('THR', 'Thriller'), ('SCF', 'Science-fiction'), ('HOR', 'Horror')], max_length=3),
        ),
    ]
