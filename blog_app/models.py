from django.db import models
from django.utils import timezone


class Post(models.Model):
    selected = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog_app.Post', on_delete='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class MyItem(models.Model):
    name = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    # slug = models.SlugField(max_length=300, unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return 'blog_app:item', (self.slug,)
