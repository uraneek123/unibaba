from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',) #list items to admin in alphabetical order
        verbose_name_plural = 'Categories' #fixes some dumbass spelling
        
    def __str__(self): #actuallly displays the name of the categories
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) 
    #Foreign key references another table
    name=models.CharField(max_length=255)
    description=models.TextField(blank=False,null=False)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=False,null=False)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self): #actuallly displays the name of the categories
        return self.name