# Generated by Django 5.0.3 on 2024-04-06 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_remove_blog_image_blog_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_url',
            field=models.TextField(blank=True, default='app.logomakr.com/3EC6KR', max_length=6000, null=True),
        ),
    ]
