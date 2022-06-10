# Generated by Django 4.0.5 on 2022-06-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('SCF', 'Science-fiction'), ('THR', 'Thriller'), ('HOR', 'Horror'), ('HIS', 'Historical'), ('FAN', 'Fantasy')], default=None, max_length=3, null=True),
        ),
    ]
