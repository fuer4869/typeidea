# Generated by Django 2.2.5 on 2020-03-30 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (3, '最热文章'), (4, '最近评论'), (2, '最新文章')], default=1, verbose_name='展示类型'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(10, '展示'), (11, '隐藏')], default=10, verbose_name='状态'),
        ),
    ]
