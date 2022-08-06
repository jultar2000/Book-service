# Generated by Django 4.0.5 on 2022-08-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('THR', 'Thriller'), ('HIS', 'Historical'), ('SCF', 'Science-fiction'), ('HOR', 'Horror'), ('FAN', 'Fantasy')], max_length=3, null=True),
        ),
    ]
