# Generated by Django 3.2.6 on 2021-09-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210905_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='my_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]