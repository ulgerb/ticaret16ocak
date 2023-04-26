from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
   context = {
      "title":"Anasayfa",
   }
   return render(request, 'index.html', context)

def aboutPage(request):
   context = {
      "title":"Hakkında",
   }
   return render(request, 'about.html', context)

def contactPage(request):
   context = {
      "title":"İletişim",
   }
   return render(request, 'contact.html', context)

def productsPage(request):
   products = Product.objects.all()
   
   context = {
      "title":"Ürünler",
      "products": products,
   }
   return render(request, 'products.html', context)


def detailPage(request, slug, color=None):

   product = get_object_or_404(Product, slug=slug)
   image_product = ImageProduct.objects.filter(product=product)
   # product_stok tamamlanıcak fotoğraflar çekilicek
   context = {
       "title": "Ürün Detayı",
       "product": product,
       "color": color,
       "slug": slug,
   }
   
   if color is not None:
      size = "md"
      product_stok = Stok.objects.filter(product=product, color__title2=color)

      image_product = image_product.filter(color__title2=color)
      
      context.update({"product_stok": product_stok})
   context.update({"image_product": image_product})
   print("FOTOĞRAFLAR:  ",image_product)
   return render(request, 'detail.html', context)