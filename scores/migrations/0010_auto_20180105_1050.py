# Generated by Django 2.0.1 on 2018-01-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0009_name_professions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='known_for',
            field=models.BooleanField(default=0),
        ),
    ]
