# Generated by Django 4.2.4 on 2023-09-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_customusertypes_can_fetch'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusertypes',
            name='can_fetch',
            field=models.BooleanField(default=False),
        ),
    ]