# Generated by Django 5.1 on 2024-12-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contactmodel_reply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='reply',
            field=models.TextField(blank=True, verbose_name='resposta'),
        ),
    ]
