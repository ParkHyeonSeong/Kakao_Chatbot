# Generated by Django 2.0.6 on 2018-06-20 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
