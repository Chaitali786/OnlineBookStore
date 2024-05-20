from django.contrib import admin
from .models import Book,CartItem
# Register your models here.
admin.site.register(Book)
admin.site.register(CartItem)