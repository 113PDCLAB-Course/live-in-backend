# Generated by Django 3.2.16 on 2022-10-24 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_add_url_feild'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='scroe',
            new_name='score',
        ),
    ]
