# Generated by Django 3.1.4 on 2020-12-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
