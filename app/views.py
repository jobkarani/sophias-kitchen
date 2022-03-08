from multiprocessing import context
from django.forms import SlugField
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email
from .forms import *

# auth 

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


# pages 

def index(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count':product_count,
    }
    return render(request, 'all-temps/index.html', context)


def shop(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count':product_count,
    }
    return render(request, 'all-temps/shop.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'all-temps/product.html',context)

 
def cart(request):

    return render(request, 'all-temps/cart.html')