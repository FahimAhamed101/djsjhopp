# Generated by Django 5.1.4 on 2025-01-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default/default-user.png', upload_to='userprofile'),
        ),
    ]
