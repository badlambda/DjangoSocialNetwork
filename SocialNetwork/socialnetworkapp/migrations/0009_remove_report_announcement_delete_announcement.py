# Generated by Django 4.2.1 on 2023-06-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetworkapp', '0008_remove_post_reaction_post_reaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='announcement',
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
    ]
