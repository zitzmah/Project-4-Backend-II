# Generated by Django 5.0.3 on 2024-04-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='app.logomakr.com/3EC6KR', upload_to='images'),
        ),
    ]