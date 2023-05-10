"""ticaret16ocak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appProduct.views import *
from appUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="indexPage"),
    path('about/', aboutPage, name="aboutPage"),
    path('contact/', contactPage, name="contactPage"),
    path('products/', productsPage, name="productsPage"),
    path('detail/<slug>/', detailPage, name="detailPage"),
    path('detail/<slug>/<color>/', detailPage, name="detailPage2"),
    path('shoping/', shopingPage, name="shopingPage"),
    path('shopingDelete/<id>/', shopingDelete, name="shopingDelete"),
    path('shopingDelete2/', shopingDelete2, name="shopingDelete2"),
    
    # USER
    path('login/', loginUser, name="loginUser"),
    path('register/', registerUser, name="registerUser"),
    path('logout/', logoutUser, name="logoutUser"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
