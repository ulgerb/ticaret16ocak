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
   comments_product = Comment.objects.filter(product=product)

   # SIRALAMA START
   filtertop = request.GET.get("filtertop") 
   if filtertop == "new":
      comments_product = comments_product.order_by("-date_now")
   elif filtertop == "up":
      comments_product = comments_product.order_by("-rating")
   elif filtertop == "down":
      comments_product = comments_product.order_by("rating")
   # SIRALAMA END
   
   paginator = Paginator(comments_product, 2)
   pag_number = request.GET.get("page")
   comments = paginator.get_page(pag_number)
   
   context = {
       "title": "Ürün Detayı",
       "product": product,
       "comments": comments,
       "comments_product": comments_product,
       "color": color,
       "slug": slug,
   }

   if request.method == "POST":
      submit = request.POST.get("submit")

      if submit == "formComment":
         rating = request.POST.get("rating")
         text = request.POST.get("text")
         
         comment = Comment(text=text, product=product, user=request.user)
         if rating is not None:
            comment.rating = rating 
         comment.save()

         total_rating = 0
         for i in comments_product:
            total_rating += i.rating
         
         total_rating = round(total_rating / len(comments_product), 1)
         product.total_rating = total_rating
         product.save()
      elif submit == "formAddShop":
         size = request.POST.get("size")
         quanity = request.POST.get("quanity")
         print(size)
      
      return redirect("/detail/"+slug+"/")
      
   if color is not None:
      product_stok = Stok.objects.filter(product=product, color__title2=color)

      image_product = image_product.filter(color__title2=color)
      
      context.update({"product_stok": product_stok})
   context.update({"image_product": image_product})
   return render(request, 'detail.html', context)


def shopingPage(request):
   context={}
   return render(request, 'shoping.html', context)