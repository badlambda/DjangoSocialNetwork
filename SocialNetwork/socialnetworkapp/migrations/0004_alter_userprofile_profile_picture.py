# Generated by Django 4.2.1 on 2023-06-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetworkapp', '0003_alter_chatroom_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]