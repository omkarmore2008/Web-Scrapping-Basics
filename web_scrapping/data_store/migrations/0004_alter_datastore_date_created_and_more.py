# Generated by Django 4.1.6 on 2023-02-13 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_store', '0003_alter_datastore_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastore',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 5, 48, 59, 684122)),
        ),
        migrations.AlterField(
            model_name='datastore',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 5, 48, 59, 684130)),
        ),
    ]
