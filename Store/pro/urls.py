from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index),
    path ('new', views.new),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]