from django.urls import path, include
from petStore import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('products/', views.products, name='products'),
]
