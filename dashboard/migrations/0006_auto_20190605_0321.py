# Generated by Django 2.0.3 on 2019-06-05 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190603_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthdata',
            name='fit',
            field=models.CharField(blank=True, choices=[('B', 'beginner'), ('BtoI', 'between beginner and intermediate'), ('I', 'intermediate'), ('ItoA', 'between intermediate and advanced'), ('A', 'advanced')], max_length=1),
        ),
        migrations.AddField(
            model_name='healthdata',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
