# Generated by Django 4.2.4 on 2023-09-29 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0038_userfacebookpagemapping'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFacebookPageMapping',
        ),
    ]