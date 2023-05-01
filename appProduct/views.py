from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator

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
   comments = Comment.objects.filter(product=product)

   # SIRALAMA START
   filtertop = request.GET.get("filtertop") 
   if filtertop == "new":
      comments = comments.order_by("-date_now")
   elif filtertop == "up":
      comments = comments.order_by("-rating")
   elif filtertop == "down":
      comments = comments.order_by("rating")
   # SIRALAMA END
   
   paginator = Paginator(comments, 2)
   pag_number = request.GET.get("page")
   comments = paginator.get_page(pag_number)
   
   context = {
       "title": "Ürün Detayı",
       "product": product,
       "comments": comments,
       "color": color,
       "slug": slug,
   }

   if request.method == "POST":
      rating = request.POST.get("rating")
      text = request.POST.get("text")
      
      comment = Comment(text=text, product=product, user=request.user)
      if rating is not None:
         comment.rating = rating 
      comment.save()
      
      return redirect("/detail/"+slug+"/")
      
   if color is not None:
      product_stok = Stok.objects.filter(product=product, color__title2=color)

      image_product = image_product.filter(color__title2=color)
      
      context.update({"product_stok": product_stok})
   context.update({"image_product": image_product})
   print("FOTOĞRAFLAR:  ",image_product)
   return render(request, 'detail.html', context)


def shopingPage(request):
   context={}
   return render(request, 'shoping.html', context)