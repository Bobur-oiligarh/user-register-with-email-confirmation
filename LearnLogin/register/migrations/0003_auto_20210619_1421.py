# Generated by Django 3.2.4 on 2021-06-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210619_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
