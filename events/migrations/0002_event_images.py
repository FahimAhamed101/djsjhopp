# Generated by Django 3.2 on 2023-06-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='photos/events'),
        ),
    ]
