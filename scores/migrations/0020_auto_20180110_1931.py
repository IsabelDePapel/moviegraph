# Generated by Django 2.0.1 on 2018-01-11 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0019_remove_principal_e'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='primary_name',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
