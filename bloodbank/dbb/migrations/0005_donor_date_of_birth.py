# Generated by Django 2.1.1 on 2018-09-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbb', '0004_auto_20180913_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
