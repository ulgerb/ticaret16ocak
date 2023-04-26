from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

   list_display = ('user', 'title', 'brand', 'price', 'total_rating', 'id')
   

@admin.register(Stok)
class StokAdmin(admin.ModelAdmin):

   list_display = ('product', 'size', 'stok', 'color', 'id')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

   list_display = ('title', 'slug', 'id')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):

   list_display = ('title1', 'title2', 'id')

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):

   list_display = ('title', 'id')
   
@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):

   list_display = ('product','color', 'id')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): 

   list_display = ('user','product','title','rating', 'id')
   
   
   