# Generated by Django 2.0.6 on 2018-06-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot_main', '0006_auto_20180621_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userkey', models.CharField(max_length=50)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='recent',
            field=models.CharField(default='1', max_length=30),
        ),
    ]