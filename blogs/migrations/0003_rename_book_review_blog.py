# Generated by Django 5.0.6 on 2024-05-19 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book',
            new_name='blog',
        ),
    ]