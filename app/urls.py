from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('product/<int:product_id>', views.product, name='product'),
    path('accounts/profile/', views.profile, name='profile'),
    path('store/', views.store, name='store'),
    path('aboutus/', views.About, name='About'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('update_item/', views.updateItem, name='update_item'),
    # path('process_order/', views.processOrder, name='process_order'),
]
