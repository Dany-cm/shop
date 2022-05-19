from atexit import register
from django.contrib import admin

from product.models import Category
from product.models import Products

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
