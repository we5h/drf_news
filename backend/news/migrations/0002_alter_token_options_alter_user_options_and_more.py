# Generated by Django 4.2.4 on 2023-08-15 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='token',
            options={'ordering': ['date'], 'verbose_name': 'Токен', 'verbose_name_plural': 'Токены'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.news', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(db_index=True, max_length=256, unique=True, verbose_name='Заголовок'),
        ),
    ]
