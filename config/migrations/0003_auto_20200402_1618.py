# Generated by Django 2.2.5 on 2020-04-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20200330_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(3, '最热文章'), (2, '最新文章'), (4, '最近评论'), (1, 'HTML')], default=1, verbose_name='展示类型'),
        ),
    ]
