# Generated by Django 2.2.2 on 2020-07-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahj_gis', '0008_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='polygon',
            name='DIVISION',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='polygon',
            name='REGION',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='state',
            name='STATEABBR',
            field=models.CharField(default='', max_length=2),
        ),
    ]
