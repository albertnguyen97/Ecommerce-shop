from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.product_list_market, name='product_list_market'),
    path('<slug:category_slug>/', views.product_list_market,
         name='product_list_by_category_market'),
    path('<int:id>/<slug:slug>/', views.product_detail_market,
         name='product_detail_market'),
    path('product/like/', views.product_like, name='product_like_market'),
]