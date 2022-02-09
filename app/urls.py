from django.urls import path
from . import views, utils


urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('product/<int:product_id>',
         views.product_details, name='product'),
    path('accounts/profile/', views.profile, name='profile'),
    path('shop/', views.shop, name='shop'),
    path('aboutus/', views.About, name='About'),
    path('order/', views.Order, name='order'),
    path('add_cart/<int:product_id>', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('delete/<int:product_id>', views.delete_product, name='delete_view'),
    # path('update_item/', views.updateItem, name='update_item'),
    # path('process_order/', views.processOrder, name='process_order'),
]
