# Generated by Django 2.1.7 on 2019-03-26 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_Book', '0010_auto_20190326_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='book',
        ),
        migrations.AddField(
            model_name='shop',
            name='books',
            field=models.ManyToManyField(null=True, to='shop_Book.Book'),
        ),
    ]