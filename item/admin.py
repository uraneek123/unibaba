from django.contrib import admin

# Register your models here.

from .models import Category, Item

admin.site.register(Category) #allows the admin to manage the category field of items
admin.site.register(Item)