# Generated by Django 2.1.4 on 2019-01-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='activate',
            new_name='active',
        ),
    ]
