# Generated by Django 4.2.4 on 2023-08-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_token_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text2',
            field=models.TextField(default='text2', max_length=3500, verbose_name='Текст комментария'),
        ),
    ]
