# Generated by Django 4.2.1 on 2023-06-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetworkapp', '0004_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
