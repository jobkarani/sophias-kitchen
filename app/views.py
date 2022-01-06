from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.http import JsonResponse
import json
from .forms import *
# from .utils import cookieCart, cartData, guestOrder


# Create your views here.
def index(request):

    products = Product.objects.all()
    context = {
        'products': products,
        # 'cartItems': cartItems,
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

# def store(request):
#     data = cartData(request)
#     cartItems = data['cartItems']

#     products = Product.objects.all()
#     context = {
#         'products': products,
#         'cartItems': cartItems,
#     }
#     return render(request, 'all-temps/store.html', context)


# def cart(request):
#     data = cartData(request)

#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']

#     context = {
#         'items': items,
#         'order': order,
#         'cartItems': cartItems,
#     }
#     return render(request, 'all-temps/cart.html', context)


# def checkout(request):
#     data = cartData(request)

#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']

#     context = {
#         'items': items,
#         'order': order,
#         'cartItems': cartItems,
#     }
#     return render(request, 'all-temps/checkout.html', context)


# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']

#     print('Action:', action)
#     print('Product:', productId)

#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(
#         customer=customer, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(
#         order=order, product=product)

#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)

#     orderItem.save()

#     if orderItem.quantity <= 0:
#         orderItem.delete()

#     return JsonResponse('Item was added', safe=False)


# def processOrder(request):
#     transaction_id = datetime.datetime.now().timestamp()
#     data = json.loads(request.body)

#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(
#             customer=customer, complete=False)

#     else:
#         customer, order = guestOrder(request, data)

#     total = float(data['form']['total'])
#     order.transaction_id = transaction_id

#     if total == order.get_cart_total:
#         order.complete = True
#     order.save()

#     if order.shipping == True:
#         ShippingAddress.objects.create(
#             customer=customer,
#             order=order,
#             address=data['shipping']['address'],
#             city=data['shipping']['city'],
#             state=data['shipping']['state'],
#             zipcode=data['shipping']['zipcode'],
#         )

#     return JsonResponse('Payment complete', safe=False)
