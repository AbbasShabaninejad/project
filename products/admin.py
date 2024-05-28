from django.contrib import admin

from . import models
from .models import Product, Category


admin.site.register(Product)
admin.site.register(Category)

