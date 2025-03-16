from django.db import models
from item.models import Item
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Rating(models.Model):
    item=models.ForeignKey(Item, related_name='ratings',on_delete=models.CASCADE) #ratings with an s
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    members=models.ManyToManyField(User, related_name='ratings')
    description=models.TextField(blank=True,null=True)
    score = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ])
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        ordering=('-modified_at',)
    