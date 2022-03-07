from tabnanny import verbose
from unicodedata import category
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

FLAVOUR_CHOICES = (
    ('CHOCOLATE FUDGE', 'CHOCOLATE FUDGE'),
    ('CHOCOLATE MINT', 'CHOCOLATE MINT'),
    ('CHOCOLATE CHIP', 'CHOCOLATE CHIP'),
    ('RED VELVET', 'RED VELVET'),
    ('BLUE VELVET', 'BLUE VELVET'),
    ('GREEN VELVET', 'GREEN VELVET'),
    ('VANILLA', 'VANILLA'),
    ('COFFEE', 'COFFEE'),
    ('COCONUT', 'COCONUT'),
    ('GINGER', 'GINGER'),
    ('ZEBRA', 'ZEBRA'),
    ('CINNAMON', 'CINNAMON'),
    ('SPICE', 'SPICE'),
    ('MARBLE', 'MARBLE'),
    ('PINA COLADA', 'PINA COLADA'),
    ('LEMON', 'LEMON'),
    ('LIME', 'LIME'),
    ('BANANA', 'BANANA'),
    ('ORANGE', 'ORANGE'),
    ('PASSION JUICE', 'PASSION JUICE'),
    ('BUBBLEGUM', 'BUBBLEGUM'),
    ('CARROT', 'CARROT'),
    ('MINT', 'MINT'),
    ('OREO', 'OREO'),
    ('CARAMEL', 'CARAMEL'),
    ('BLUEBERRY', 'BLUEBERRY'),
    ('STRAWBERRY', 'STRAWBERRY'),
    ('BUTTER', 'BUTTER'),
    ('FRUIT', 'FRUIT'),
    ('BLACK FOREST', 'BLACK FOREST'),
    ('WHITE FOREST', 'WHITE FOREST'),
    ('BLUEBERRY FOREST', 'BLUEBERRY FOREST'),
    ('PASSION FRUIT FOREST', 'PASSION FRUIT FOREST'),
)

TOPPINGS_CHOICES = (
    ('SKITTLES', 'SKITTLES'),
    ('GUMMIES', 'GUMMIES'),
    ('FRUITS', 'FRUITS'),
    ('NUTS', 'NUTS'),
    ('OREOS', 'OREOS'),
    ('CHERRIES', 'CHERRIES'),
    ('CAKE SAIL', 'CAKE SAIL'),
    ('CAKE TOPPERS', 'CAKE TOPPERS'),
    ('ASSORTED CHOCOLATES', 'ASSORTED CHOCOLATES'),
)


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_photo = CloudinaryField('image')
    email = models.EmailField(max_length=256, null=True)
    phone_number = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image')
    description = models.TextField(max_length=500, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
