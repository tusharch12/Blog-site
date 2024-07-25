from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_first = models.DateTimeField(auto_now=True)
    body = RichTextUploadingField(default="content")


    def __str__(self):
        return  self.title +' | ' + str(self.author)

class BlogMedia(models.Model):
    blog = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="media")
    file = models.ImageField(upload_to='image')

    def __str__(self):
        return self.blog.title


        
    
 