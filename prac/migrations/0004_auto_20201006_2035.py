# Generated by Django 3.1 on 2020-10-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac', '0003_auto_20201006_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='email',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='name',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment_type',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_status',
            field=models.IntegerField(null=True),
        ),
    ]
