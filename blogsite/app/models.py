from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default = False)
    datetime_first = models.DateTimeField(auto_now=True)
    body = RichTextUploadingField(default="content")

    class Meta:
        ordering = ['-datetime_first']


    def __str__(self):
        if(self.is_draft):
            return  self.title +' | ' + str(self.author) +' | Draft | ' + self.datetime_first.strftime("%d/%m/%Y")
        return  self.title +' | ' + str(self.author) + ' | ' + self.datetime_first.strftime("%d/%m/%Y")

class BlogMedia(models.Model):
    blog = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="media")
    file = models.ImageField(upload_to='image')

    def __str__(self):
        return self.blog.title
        
class BlogComment(models.Model):
    blog = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()  

    class Meta:
        ordering = ['-id']

    # def __str__(self):
    #     return self.name | self.comment


        
    
 