# Generated by Django 4.1.1 on 2023-09-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0016_facebookpage_access_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookpage',
            name='access_token',
        ),
    ]
