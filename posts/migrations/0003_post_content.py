# Generated by Django 2.0.5 on 2018-05-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180527_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='kishan'),
            preserve_default=False,
        ),
    ]
