# Generated by Django 4.2.1 on 2023-06-08 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetworkapp', '0006_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='educator',
            old_name='user',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='uid',
        ),
    ]
