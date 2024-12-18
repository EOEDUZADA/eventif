# Generated by Django 5.1 on 2024-12-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactmodel_replied_contactmodel_reply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='reply',
            field=models.TextField(blank=True, max_length=500, verbose_name='resposta'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='reply_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='foi respondido em'),
        ),
    ]
