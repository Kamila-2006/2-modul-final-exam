# Generated by Django 5.1.5 on 2025-02-06 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='maximum_students',
            new_name='max_students',
        ),
    ]
