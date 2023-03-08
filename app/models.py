from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    images = models.ImageField(upload_to='blog',null=True, blank=True)
    text = models.TextField()
    auther = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} --- {self.auther}"



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} --- {self.email}"

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

