from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>/', views.shop, name='products_by_category'),
    path('shop/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('aboutus/', views.About, name='About'),
]
