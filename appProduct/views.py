from django.shortcuts import render

# Create your views here.


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
   context = {
      "title":"Ürünler",
   }
   return render(request, 'products.html', context)

def detailPage(request):
   context = {
      "title":"Ürün Detayı",
   }
   return render(request, 'detail.html', context)