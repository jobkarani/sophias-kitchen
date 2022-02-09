from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.

FLAVOUR_CHOICES = (
    ('CHOCOLATE FUDGE CAKE', 'CHOCOLATE FUDGE CAKE'),
    ('BEACH WAVE RED VELVET SPONGE CAKE', 'BEACH WAVE RED VELVET SPONGE CAKE'),
    ('VANILLA SPONGE CAKE WITH CANDLES', 'VANILLA SPONGE CAKE WITH CANDLES'),
    ('VANILLA BLUEBERRY FLORAL CAKE', 'VANILLA BLUEBERRY FLORAL CAKE'),
    ('COFFEE CAKE', 'COFFEE CAKE'),
    ('BABY SHOWER FRUIT CAKE', 'BABY SHOWER FRUIT CAKE'),
    ('RED VELVET SPONGE CAKE', 'RED VELVET SPONGE CAKE'),
    ('FLORAL COCONUT SPONGE CAKE', 'FLORAL COCONUT SPONGE CAKE'),
    ('VANILLA SPONGE CAKE', 'VANILLA SPONGE CAKE'),
    ('CUSTOMIZED RED VELVET CAKE', 'CUSTOMIZED RED VELVET CAKE'),
    ('CUSTOMIZED VANILLA PJ MASK CAKE', 'CUSTOMIZED VANILLA PJ MASK CAKE'),
    ('SQUARE VANILLA CAKE WITH STRAWBERRIES',
     'SQUARE VANILLA CAKE WITH STRAWBERRIES'),
    ('FONDANT MARBLE CAKE', 'FONDANT MARBLE CAKE'),
    ('FlORAL SEMI NAKED VANILLA CAKE', 'FlORAL SEMI NAKED VANILLA CAKE'),
    ('CINNAMON BREAD', 'CINNAMON BREAD'),
    ('CUSTOMIZED VANILLA CUPCAKES', 'CUSTOMIZED VANILLA CUPCAKES'),
    ('BROWNIES', 'BROWNIES'),
    ('MARBLE SWISS ROLLS', 'MARBLE SWISS ROLLS'),
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

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    def update(self):
        self.save()

    def __str__(self):
        return self.user.username
#


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField()
    price = models.FloatField()
    review = models.IntegerField(blank=True, null=True, default=True)

    class Meta:
        ordering = ('name',)

    def save_product(self):
        self.save()

    def delete_product(self):
        self.save()

    def update(self):
        self.save()

    @property
    def saved_reviews(self):
        return self.reviews.all()

    def __str__(self):
        return self.name


class Review(models.Model):
    review = models.CharField(max_length=250)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')

    @classmethod
    def display_review(cls, product_id):
        reviews = cls.objects.filter(product_id=product_id)
        return reviews


class OrderItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    flavour = models.CharField(
        choices=FLAVOUR_CHOICES, default='BROWNIES', null=True, max_length=100)
    orderitems = models.ForeignKey(
        OrderItem, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=256, null=True)

    def save_order(self):
        self.save()

    def delete_order(self):
        self.save()

    def update(self):
        self.save()

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()

        for item in orderitems:
            if item.product.digital == False:
                shipping = True

        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class ShippingAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)
    state = models.CharField(max_length=256, null=True)
    zipcode = models.CharField(max_length=256, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
