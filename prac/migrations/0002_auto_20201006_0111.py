# Generated by Django 3.1 on 2020-10-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='order_id',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
