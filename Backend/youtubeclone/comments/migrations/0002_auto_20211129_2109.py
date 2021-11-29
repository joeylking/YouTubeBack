# Generated by Django 3.2.9 on 2021-11-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='_comments_comment_dislikes_+', to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='_comments_comment_likes_+', to='comments.Comment'),
        ),
    ]