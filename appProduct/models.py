from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Brand(models.Model):
   title = models.CharField(("Marka"), max_length=50)
   slug = models.SlugField(("Marka Slug"), blank=True)

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super(Brand, self).save(*args, **kwargs)

   def __str__(self):
      return self.title
   
class Color(models.Model):
   title1 = models.CharField(("Renkler Türkçe"), max_length=50)
   title2 = models.CharField(("Renkler İngilizce"), max_length=50)

   def __str__(self):
      return self.title1
   
class Size(models.Model):
   title = models.CharField(("Beden"), max_length=50)

   def __str__(self):
      return self.title
# s m l

class Product(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kulanıcı"), on_delete=models.CASCADE)
   brand = models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE)
   title = models.CharField(("Ürün Başlığı"), max_length=50)
   text = models.TextField(("İçerik"))
   price = models.FloatField(("Ürün fiyatı"),default=0)
   total_rating = models.FloatField(("Ürün Puanı"), default=0)
   image = models.ImageField(("Ürün Resmi"), upload_to='product', max_length=250)
   slug = models.SlugField(("Title Slug"), blank=True, null=True)
   colors = models.ManyToManyField(Color, verbose_name=("Renkler"))
   sizes = models.ManyToManyField(Size, verbose_name=("Bedenler"))

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super(Product, self).save(*args, **kwargs)
      
   def __str__(self):
      return self.title

class Stok(models.Model):
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   size = models.ForeignKey(Size, verbose_name=("Beden"), on_delete=models.CASCADE)
   color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
   stok = models.IntegerField(("Stok Sayısı"), default=0)

   def __str__(self):
      return self.product.title

class ImageProduct(models.Model):
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   color = models.ForeignKey(Color, verbose_name=("Renk"), on_delete=models.CASCADE)
   image = models.ImageField(("Ürün Resmi"), upload_to='product', max_length=250)

   def __str__(self):
      return self.product.title
   
class Comment(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kulanıcı"), on_delete=models.CASCADE)
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   title = models.CharField(("Başlık"), max_length=50)
   text = models.TextField(("Yorum"))
   rating = models.IntegerField(("Yorum Puanı"), default=5)

   def __str__(self):
      return self.product.title
   
   