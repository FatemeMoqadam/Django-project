# Generated by Django 3.2.8 on 2021-11-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getbetter', '0005_auto_20211111_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeling',
            name='linkmovie',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeling',
            name='linkmusic',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeling',
            name='movie',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeling',
            name='music',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]