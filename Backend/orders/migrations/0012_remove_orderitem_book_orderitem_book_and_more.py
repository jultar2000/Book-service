# Generated by Django 4.0.5 on 2022-08-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_genre'),
        ('orders', '0011_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='book',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='book',
            field=models.ManyToManyField(null=True, related_name='book', to='books.book'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='book_cover',
            field=models.CharField(choices=[('S', 'SOFT'), ('H', 'HARD')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='book_language',
            field=models.CharField(choices=[('E', 'ENGLISH'), ('P', 'POLISH')], default=None, max_length=1),
        ),
    ]
