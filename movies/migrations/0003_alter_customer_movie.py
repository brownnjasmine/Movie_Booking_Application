# Generated by Django 3.2.13 on 2023-10-18 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20231018_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]