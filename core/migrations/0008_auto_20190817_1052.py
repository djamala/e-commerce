# Generated by Django 2.1.7 on 2019-08-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190817_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='percentage_reduction',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
