from collections import UserDict, UserList
import datetime
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email
from django.http import JsonResponse
import json
from .forms import *
from .utils import *
# from .utils import cookieCart, cartData, guestOrder


# Create your views here.
def index(request):

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'all-temps/index.html', context)


@login_required
def reviews(request, product_id):
    form = ReviewForm()
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
    return redirect('index')


@login_required(login_url='/accounts/login/')
def product(request, product_id):
    product = Product.objects.all()
    review = Review.objects.filter(product=product)
    return render(request, "all-temps/product.html", {"product": product, "review": review})


@login_required(login_url="/accounts/login/")
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'all-temps/create_profile.html', {"form": form, "title": title})


@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    product = Product.objects.filter(id=current_user.id).all()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('profile')
    else:
        form = ProfileForm()

    return render(request, "all-temps/profile.html", {"profile": profile, "product": product, "letterForm": form})


@login_required(login_url="/accounts/login/")
def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    ctx = {"form": form}
    return render(request, 'all-temps/update_prof.html', ctx)


def About(request):

    return render(request, 'all-temps/aboutus.html',)


def order(request, order_flavour):
    flavour = Order.objects.get(flavour=order_flavour)
    user = request.user
    product = Product.objects.all()
    return render(request, 'all-temps/order.html', {'product': product, 'flavour': flavour})


def shop(request):
    data = cartData(request)

    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'all-temps/shop.html', context)


def product_details(request, product_id):
    item = Product.objects.all()
    ctx = {
        'item': item
    }
    return render(request, 'all-temps/product.html', ctx)


def cart(request, product_id):
    data = cartData(request)
    orderItems = data['orderItems']
    orders = OrderItem.objects.filter(user=request.user)
    product = Product.objects.get(id=product_id)
    cartItems = OrderItem(product=product, user=request.user)
    cartItems.save()
    # return redirect()

    context = {
        'orders': orders
    }
    return render(request, 'all-temps/cart.html', context)


def checkout(request):
    data = cartData(request)

    orderItems = data['orderItems']
    order = data['order']

    context = {
        'order': order,
        'orderItems': orderItems,
    }
    return render(request, 'all-temps/checkout.html', context)


def delete_product(request, product_id):
    cartItems = Product.objects.get(id=product_id)
    cartItems.delete()
    return render(request, 'all-temps/cart.html')


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            user=UserDict, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            user=UserList,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete', safe=False)
