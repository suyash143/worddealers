# Generated by Django 3.2.5 on 2022-04-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20220411_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='logo',
        ),
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='clients'),
        ),
    ]
