# Generated by Django 5.1 on 2024-08-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
