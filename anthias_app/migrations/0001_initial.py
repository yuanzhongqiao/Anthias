# Generated by Django 3.2.18 on 2024-08-23 18:45

import anthias_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.TextField(default=anthias_app.models.generate_asset_id, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('uri', models.TextField(blank=True, null=True)),
                ('md5', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('duration', models.TextField(blank=True, null=True)),
                ('mimetype', models.TextField(blank=True, null=True)),
                ('is_enabled', models.IntegerField(default=0)),
                ('is_processing', models.IntegerField(default=0)),
                ('nocache', models.IntegerField(default=0)),
                ('play_order', models.IntegerField(default=0)),
                ('skip_asset_check', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'assets',
            },
        ),
    ]