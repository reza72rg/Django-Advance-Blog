from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model

# getting user models
#user = get_user_model()
# Create your models here.
class Post(models.Model): 
    image = models.ImageField(blank=True,null=True)
    author = models.ForeignKey('accounts.Profile',on_delete=models.SET_NULL,null=True, related_name='posts_author')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)  
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name