# Generated by Django 2.1.8 on 2019-08-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honeytip', '0005_auto_20190809_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='group',
            field=models.CharField(choices=[('귀차니즘', '귀차니즘'), ('시간절약', '시간절약'), ('간지폭발', '간지폭발')], max_length=10),
        ),
    ]
