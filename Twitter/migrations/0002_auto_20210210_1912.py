# Generated by Django 3.1.6 on 2021-02-10 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Twitter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tweet_id',
            new_name='twitter_id',
        ),
    ]
