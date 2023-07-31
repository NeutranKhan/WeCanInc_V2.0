from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
