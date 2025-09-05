"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from myapp import views
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('crud', views.crud, name='crud'),
    path('create', views.create, name='create'),
    path('update<int:id>', views.update, name='update'),
    path('delete<int:id>', views.delete, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    path('blog', views.blog, name='blog'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main'),
    path('shopdetails', views.shopdetails, name='shopdetails'),
    path('shopgrid', views.shopgrid, name='shopgrid'),
    path('shopingcart', views.shopingcart, name='shopingcart'),
    path('department', views.department, name='department'),
    path('color', views.color, name='color'),
    path('pro', views.pro, name='pro'),
    path('size1', views.size1, name='size1'),
    path('price', views.price, name='price'),
    path('details/<int:id>', views.details, name='details'),
    path('add_wishlist/<int:id>', views.add_wishlist, name='add_wishlist'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('pluscart/<int:id>', views.pluscart, name='pluscart'),
    path('minuscart/<int:id>', views.minuscart, name='minuscart'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('otp-verify/', views.otp_verify, name='otp_verify'),

    
]

