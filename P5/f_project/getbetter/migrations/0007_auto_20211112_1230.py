# Generated by Django 3.2.8 on 2021-11-12 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getbetter', '0006_auto_20211112_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeling',
            name='linkmovie',
        ),
        migrations.RemoveField(
            model_name='feeling',
            name='linkmusic',
        ),
        migrations.RemoveField(
            model_name='feeling',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='feeling',
            name='music',
        ),
    ]
