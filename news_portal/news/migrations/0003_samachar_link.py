# Generated by Django 4.2 on 2023-04-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_news_samachar'),
    ]

    operations = [
        migrations.AddField(
            model_name='samachar',
            name='link',
            field=models.CharField(default='', max_length=200),
        ),
    ]