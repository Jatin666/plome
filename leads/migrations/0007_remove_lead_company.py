# Generated by Django 4.2.4 on 2023-08-29 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_lead_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='company',
        ),
    ]