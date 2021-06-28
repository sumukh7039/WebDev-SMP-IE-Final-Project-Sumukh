from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    snippet = TextField(
        max_length=500, default="Click the above link to read the post")
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, related_name='dislike_posts')

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title + ' by ' + str(self.author)

    def get_absolute_url(self):
        return reverse("article-detail", args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile_pics/")
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")
