# Generated by Django 4.1.6 on 2023-02-13 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_store', '0004_alter_datastore_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datastore',
            name='status',
            field=models.CharField(default='Fetching', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='datastore',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 7, 7, 34, 608428)),
        ),
        migrations.AlterField(
            model_name='datastore',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2023, 2, 13, 7, 7, 34, 608437)),
        ),
    ]
