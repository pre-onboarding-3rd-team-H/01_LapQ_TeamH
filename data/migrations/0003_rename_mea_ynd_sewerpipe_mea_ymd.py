# Generated by Django 3.2.13 on 2022-06-30 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20220630_0217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sewerpipe',
            old_name='mea_ynd',
            new_name='mea_ymd',
        ),
    ]
