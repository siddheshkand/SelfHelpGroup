# Generated by Django 2.1.1 on 2019-01-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
    ]
