# Generated by Django 2.0.6 on 2018-07-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipick_Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='DAY',
            field=models.CharField(default='`', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='PICK',
            field=models.IntegerField(default=0),
        ),
    ]
