# Generated by Django 4.2.4 on 2023-09-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_company', '0002_appeleffectuele_doisser_inscriptionvisioentree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscriptionvisioentree',
            name='num_facture',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]