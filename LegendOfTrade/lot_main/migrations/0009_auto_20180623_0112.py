# Generated by Django 2.0.6 on 2018-06-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot_main', '0008_user_bank_lucky_chance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='G2',
        ),
        migrations.AddField(
            model_name='box',
            name='G1_M',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='box',
            name='G3_M',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='box',
            name='G4_M',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='box',
            name='G5_M',
            field=models.IntegerField(default=0),
        ),
    ]