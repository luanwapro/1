# Generated by Django 2.2 on 2019-06-12 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190610_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
