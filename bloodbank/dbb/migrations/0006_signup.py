# Generated by Django 2.1.1 on 2018-09-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbb', '0005_donor_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('password', models.CharField(max_length=120)),
                ('confirmpassword', models.CharField(max_length=120)),
            ],
        ),
    ]
