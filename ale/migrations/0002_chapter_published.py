# Generated by Django 2.2.6 on 2019-10-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]