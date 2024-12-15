# Generated by Django 5.1 on 2024-12-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='replied',
            field=models.BooleanField(default=False, verbose_name='respondido'),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='reply',
            field=models.TextField(blank=True, max_length=600, verbose_name='resposta'),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='reply_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='respondido em'),
        ),
    ]
