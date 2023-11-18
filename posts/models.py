from django.db import models
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager

# Create your models here.


class Post (models.Model) :
    
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post')
    tags = TaggableManager()

    category = models.ForeignKey('Category',related_name='post_category',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Category (models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
