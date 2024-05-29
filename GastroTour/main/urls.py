from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('', views.index, name='home'),
     path('about', views.aboutus, name='aboutus'),
     path('tours', views.tours, name='tours'),
     path('tour-info/<str:tour_name>/', views.tourInfo, name='tourInfo'),
     path('cart', views.cart, name='cart'),
     path('pay/<str:restaurant_name>/', views.pay, name='pay'),
     path('add-to-cart/<str:restaurant_name>', views.add_to_cart, name='add_to_cart'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

