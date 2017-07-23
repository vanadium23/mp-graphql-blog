from django.db import models


class User(models.Model):
    username = models.TextField()
    avatar_url = models.TextField(blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.TextField()
    body = models.TextField()
    preview = models.TextField()


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
