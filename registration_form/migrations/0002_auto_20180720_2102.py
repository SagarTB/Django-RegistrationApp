# Generated by Django 2.0.7 on 2018-07-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('m', 'MALE'), ('f', 'FEMALE'), ('o', 'OTHERS')], default='m', max_length=100),
        ),
    ]
