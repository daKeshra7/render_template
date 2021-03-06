# Generated by Django 3.1 on 2020-08-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='about_you',
            field=models.TextField(default='Not more than 250 characters', max_length=250),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(max_length=255, upload_to='pictures'),
        ),
    ]
