# Generated by Django 4.2.4 on 2023-10-29 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('data', models.CharField(max_length=1000000)),
            ],
        ),
    ]
