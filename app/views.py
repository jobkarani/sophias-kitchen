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
    product = Product.objects.get(id=product_id)
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


def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems,
    }
    return render(request, 'all-temps/shop.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'all-temps/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'all-temps/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete', safe=False)
