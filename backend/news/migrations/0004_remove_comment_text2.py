# Generated by Django 4.2.4 on 2023-08-15 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment_text2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text2',
        ),
    ]
