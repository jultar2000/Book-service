# Generated by Django 4.0.5 on 2022-06-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('THR', 'Thriller'), ('SCF', 'Science-fiction'), ('HIS', 'Historical'), ('HOR', 'Horror'), ('FAN', 'Fantasy')], default=None, max_length=3, null=True),
        ),
    ]