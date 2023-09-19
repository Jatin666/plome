# Generated by Django 4.2.4 on 2023-09-07 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0028_remove_facebookpage_user_facebookpage_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookpage',
            name='users',
        ),
        migrations.AddField(
            model_name='facebookpage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]