# Generated by Django 3.1 on 2020-10-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac', '0002_auto_20201006_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.IntegerField(null=True),
        ),
    ]
