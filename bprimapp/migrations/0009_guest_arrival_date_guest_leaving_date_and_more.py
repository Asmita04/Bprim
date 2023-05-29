# Generated by Django 4.1.2 on 2023-01-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bprimapp', '0008_hospitalitykit'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='arrival_date',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AddField(
            model_name='guest',
            name='leaving_date',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AddField(
            model_name='pastguest',
            name='arrival_date',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AddField(
            model_name='pastguest',
            name='leaving_date',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='duration',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='pastguest',
            name='duration',
            field=models.DateField(blank=True),
        ),
    ]
