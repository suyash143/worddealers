# Generated by Django 3.2.5 on 2022-04-11 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_client_client_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_logo',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_name',
            new_name='name',
        ),
    ]
