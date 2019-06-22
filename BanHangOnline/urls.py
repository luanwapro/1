"""BanHangOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from home import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('home/register/', views.register, name='register'),
    path('home/login/', auth_views.LoginView.as_view(template_name='home/dangnhap.html'), name='login'),
    path('home/logout/', auth_views.LogoutView.as_view(next_page='/home'), name='logout'),
    path('home/product/<int:product_id>/login/', auth_views.LoginView.as_view(template_name='home/dangnhap.html'), name='login'),
    path('home/product/<int:product_id>/logout/', auth_views.LogoutView.as_view(next_page='/home'), name='logout'),
    path('xulysoluong/', views.show_cart),

    path('home/<int:cate_id>/login/', auth_views.LoginView.as_view(template_name='home/dangnhap.html'), name='login'),
    path('home/<int:cate_id>/logout/', auth_views.LogoutView.as_view(next_page='/home'), name='logout'),


    path('shipment/login/', auth_views.LoginView.as_view(template_name='home/loginship.html'), name='loginship'),
    path('shipment/logout/', auth_views.LogoutView.as_view(next_page='/shipment/login'), name='logoutship'),
    path('shipmet/register/', views.registership, name='registership'),

    path('shipment/listship/', views.ShowListShip),
    path('shipment/listship/<int:user_id>', views.ListShip),
    path('shipment/listship/<int:user_id>/detail/<int:order_id>/', views.ShipDetail, name='detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)