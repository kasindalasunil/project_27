# Generated by Django 4.2.6 on 2024-01-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default='123@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='school',
            name='reenteremail',
            field=models.EmailField(default='123@gmail.com', max_length=254),
        ),
    ]
