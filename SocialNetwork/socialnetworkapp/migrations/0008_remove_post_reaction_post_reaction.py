# Generated by Django 4.2.1 on 2023-06-08 23:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialnetworkapp', '0007_rename_user_educator_uid_rename_user_student_uid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reaction',
        ),
        migrations.AddField(
            model_name='post',
            name='reaction',
            field=models.ManyToManyField(related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
