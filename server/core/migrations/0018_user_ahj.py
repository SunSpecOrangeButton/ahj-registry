# Generated by Django 2.2.2 on 2020-07-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200721_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='AHJ',
            field=models.ManyToManyField(to='core.AHJ'),
        ),
    ]
