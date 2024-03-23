from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from .forms import VendorUserForm
from django.contrib.auth import views as auth_views
from .models import vendor, shop
from LocalMarket.models import Product
from .utils import searchproducts
# Create your views here.
from django.contrib.auth.decorators import login_required
def loginVendor(request):

    page = 'login'
    user_auth = None
    #
    # if request.user.is_authenticated:
    #     return redirect('homepage')
    print("vendor")
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        print(username)
        # # username = username.lower()
        # password = request.POST.get('password')

        print(password)

        try:
            user = vendor.objects.get(username=username)
            print(user)
            user_auth = authenticate(request, username=username, password=password)
        except:
            print('vendor not found')
            # messages.error(request, "The Vendor not found!")

        if user_auth is not None:
            login(request, user_auth)
            return redirect('homepage')

        else:
            print('Username or Password is incorrect')
            messages.error(request, "Username or Password is invalid!")

    return render(request, 'vendor/login_signup.html', {'page':page})

def createVendor(request):
    page = 'register'
    form = VendorUserForm()
    print(request)
    if request.method == 'POST':
        form = VendorUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Vendor created successfully!')

            # login(request, user)
            # print(user)
            return redirect("loginVendor")
        else:
            messages.error(request, 'an error has occured while login')

    return render(request, 'vendor/login_signup.html', {'page':page, 'form':form})

def logoutVendor(request):
    logout(request)
    return redirect('loginVendor')

def newview(request):
    page = 'newview'
    return render(request, 'vendor/newview.html')

def shopview(request, pk):
    page = 'shopview'
    shop_n = shop.objects.get(shop_id=pk)
    products, search_query = searchproducts(request, pk)
    return render(request, 'vendor/shop_ind.html', {'page':page,'shop':shop_n, 'products':products, 'search_query':search_query})