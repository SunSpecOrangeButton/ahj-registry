# Generated by Django 2.2.2 on 2020-07-08 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahj_gis', '0007_polygon'),
        ('core', '0002_auto_20200701_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ahj',
            name='city_mpoly',
        ),
        migrations.RemoveField(
            model_name='ahj',
            name='county_mpoly',
        ),
        migrations.RemoveField(
            model_name='historicalahj',
            name='city_mpoly',
        ),
        migrations.RemoveField(
            model_name='historicalahj',
            name='county_mpoly',
        ),
        migrations.AddField(
            model_name='ahj',
            name='mpoly',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_gis.Polygon'),
        ),
        migrations.AddField(
            model_name='historicalahj',
            name='mpoly',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ahj_gis.Polygon'),
        ),
    ]
