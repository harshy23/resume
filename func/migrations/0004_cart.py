# Generated by Django 4.2 on 2024-12-05 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('func', '0003_alter_comic_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='func.comic')),
            ],
        ),
    ]
