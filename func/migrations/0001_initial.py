# Generated by Django 4.2 on 2024-11-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10000)),
                ('lastname', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=10000)),
                ('value', models.CharField(max_length=100000)),
            ],
        ),
    ]
