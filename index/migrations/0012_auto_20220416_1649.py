# Generated by Django 3.2.5 on 2022-04-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
