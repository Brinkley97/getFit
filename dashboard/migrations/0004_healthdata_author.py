# Generated by Django 2.0.3 on 2019-06-03 00:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_remove_healthdata_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthdata',
            name='author',
            field=models.ForeignKey(default=None, on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
