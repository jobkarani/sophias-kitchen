from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','description','category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Profile)
admin.site.register(Product, ProductAdmin )
admin.site.register(Category, CategoryAdmin)
