from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from vendor.models import shop, vendor
from .forms import CustomerUserForm, ProfileForm
from django.contrib.auth import views as auth_views
# Create your views here.
from django.contrib.auth.decorators import login_required
from .utils import searchshops
from .models import Customer


# class PasswordResetView(auth_views.PasswordResetView):

def loginUser(request):

    page = 'login'
    user_auth = None
    #
    if request.user.is_authenticated:
        return redirect('homepage')
    print("hello")
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        print(username)
        # # username = username.lower()
        # password = request.POST.get('password')

        print(password)

        try:
            user = Customer.objects.get(username=username)
            print(user)
            user_auth = authenticate(request, username=username, password=password)
        except:
            print('User not found')

        if user_auth is not None:
            login(request, user_auth)
            return redirect('customerprofile')

        else:
            print('User does not exists')
            messages.error(request, "Username or Password is invalid!")

    return render(request,'LocalMarket/login-signup.html', {'page':page})

def createUser(request):
    page = 'register'
    form = CustomerUserForm()
    print(request)
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,'User created successfully!')
            # login(request, user)
            print(user)
            return redirect("loginUser")
        else:
            print(request,'an error has occured while login')

    return render(request, 'LocalMarket/login-signup.html', {'page':page, 'form':form})

def logoutUser(request):
    logout(request)
    return redirect('loginUser')
def homepage(request):
    page = 'homepage'
    user_role = None
    if request.user.is_authenticated:
        try:
            user_consumer = Customer.objects.get(username=request.user.username)
            user_role = 'customer'
        except:
            user_consumer = vendor.objects.get(username=request.user.username)
            user_role = 'vendor'
        print(user_consumer)

    # return render(request, 'navbar.html', {})
    print(user_role)
    print(request.user.username)
    shops_all = shop.objects.all()
    shops, search_query = searchshops(request)
    print(shops)
    # return HttpResponse('<h1>This is homepage</h1>')
    return render(request, '../templates/homepage.html', {'page':page, 'shops_all': shops_all, 'user_role': user_role, 'search_query': search_query, 'shops': shops})

@login_required(login_url='loginUser')
def customer_profile(request):
    user = request.user
    print(user)
    customer = Customer.objects.get(username=user)
    print(customer)
    return render(request, 'LocalMarket/customer_profile.html', {'customer':customer})

@login_required(login_url='loginUser')
def edit_profile(request):
    user = request.user
    customer = Customer.objects.get(username=user.username)
    form = ProfileForm(instance=customer)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=customer)
        print(form.is_valid())
        if form.is_valid():

            form.save()

            return redirect('homepage')

    context = {'form': form, 'customer': customer}
    return render(request, 'LocalMarket/profile_form.html', context)