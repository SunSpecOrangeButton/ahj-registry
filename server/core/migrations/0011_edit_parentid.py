# Generated by Django 2.2.2 on 2020-07-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200711_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit',
            name='ParentID',
            field=models.CharField(default='', max_length=45),
        ),
    ]
