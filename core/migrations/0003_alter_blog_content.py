# Generated by Django 4.1.7 on 2023-03-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_blog_thumbnail_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
