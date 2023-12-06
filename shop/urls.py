from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('', views.product_list_shop, name='product_list_shop'),
    path('<slug:category_slug>/', views.product_list_shop,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail_shop,
         name='product_detail_shop'),
    path('product/like/', views.product_like, name='product_like'),
]
