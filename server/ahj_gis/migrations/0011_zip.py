# Generated by Django 2.2.2 on 2020-08-12 22:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahj_gis', '0010_state_mpoly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ZCTA5CE', models.CharField(max_length=5)),
                ('GEOID', models.CharField(max_length=5)),
                ('CLASSFP', models.CharField(max_length=2)),
                ('MTFCC', models.CharField(max_length=5)),
                ('FUNCSTAT', models.CharField(max_length=1)),
                ('ALAND', models.BigIntegerField()),
                ('AWATER', models.BigIntegerField()),
                ('INTPTLAT', models.CharField(max_length=11)),
                ('INTPTLON', models.CharField(max_length=12)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
