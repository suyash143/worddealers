# Generated by Django 4.0.6 on 2022-07-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20220417_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_page_heading', models.CharField(max_length=50)),
                ('contact_page_para', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150, null=True)),
                ('map_link', models.URLField(default=0)),
                ('email', models.CharField(max_length=150, null=True)),
                ('number', models.CharField(max_length=150, null=True)),
                ('work_time', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat_text', models.CharField(max_length=20)),
                ('stat_number', models.CharField(max_length=20)),
                ('stat_icon', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='index',
            name='address',
        ),
        migrations.RemoveField(
            model_name='index',
            name='number',
        ),
        migrations.RemoveField(
            model_name='index',
            name='subscribe_heading',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='index',
            name='stats',
            field=models.ManyToManyField(null=True, to='index.stat'),
        ),
    ]
