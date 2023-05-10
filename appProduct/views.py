from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q 

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
   query = request.GET.get("q")
   if query is not None:
      products = products.filter(Q(title__icontains=query) | Q(brand__title__icontains=query)) # __icontains içerisinde geçip geçmediğini kontrol eder
   
   context = {
      "title":"Ürünler",
      "products": products,
   }
   return render(request, 'products.html', context)


def detailPage(request, slug, color=None):
   if color is not None:
      get_object_or_404(Color, title2=color)
   product = get_object_or_404(Product, slug=slug)
   image_product = ImageProduct.objects.filter(product=product)
   comments_product = Comment.objects.filter(product=product).order_by('-date_now')
   
   # SIRALAMA START
   filtertop = request.GET.get("filtertop") 
   if filtertop == "new":
      comments_product = comments_product.order_by("-date_now")
   elif filtertop == "up":
      comments_product = comments_product.order_by("-rating")
   elif filtertop == "down":
      comments_product = comments_product.order_by("rating")
   # SIRALAMA END
   
   paginator = Paginator(comments_product, 5)
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
         product_size = request.POST.get("size").lower()
         quanity = int(request.POST.get("quanity"))
         all_price = product.price * quanity
         if product_size != None and color != None:
            product_size = Size.objects.get(title=product_size)
            colorobj = Color.objects.get(title2=color.lower())
            shoping = Shoping.objects.filter(user=request.user, product=product, color=colorobj, size=product_size)
            if shoping.exists():
               shoping = shoping[0]
               if (shoping.quanity + quanity) <= 10:
                  shoping.quanity += quanity
                  shoping.all_price += all_price
                  shoping.save()
               else:
                  messages.warning(request, "En fazla 10 ürün alınabilir!")
            elif color is not None:  
               shoping = Shoping(user=request.user, product=product,
                                 color=colorobj,
                                 size=product_size,
                                 quanity=quanity, all_price=all_price,  
                                 imageproduct=image_product.filter(color__title2=color)[0],
                                 )
               shoping.save()
            
            
      return redirect("/detail/"+slug+"/")
      
   if color is not None:
      product_stok = Stok.objects.filter(product=product, color__title2=color)

      image_product = image_product.filter(color__title2=color)
      
      context.update({"product_stok": product_stok})
   context.update({"image_product": image_product})
   return render(request, 'detail.html', context)


def shopingPage(request):
   shoping = Shoping.objects.filter(user=request.user)
   total_price = 0

   for i in shoping:
      total_price += i.all_price
   
   if request.method == "POST":
      for i,v in request.POST.items():
         if i != "csrfmiddlewaretoken":
            v = int(v)
            shopid = i[8:]
            shopget = shoping.get(id=shopid)
            shopget.quanity = v
            shopget.all_price = v * shopget.product.price
            shopget.save()
      return redirect("shopingPage")      
      
            
   context={
       "shoping": shoping,
       "total_price": total_price,
   }
   return render(request, 'shoping.html', context)

def shopingDelete(request, id):
   shoping = Shoping.objects.get(id=id)
   shoping.delete()
   return redirect("shopingPage")

def shopingDelete2(request):
   
   for i,v in request.GET.items():
      print(i,v)
   # shopid = request.GET.get("shopid")
   # shoping = Shoping.objects.get(id=shopid)
   # shoping.delete()
   return redirect("shopingPage")
   