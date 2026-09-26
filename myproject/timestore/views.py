from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Product,Category
from django.db.models import Q


def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product-detail.html',{'product':product})

# Home
def home(request):
    return render(request, 'index.html')




def product(request):
    products = Product.objects.all()
    return render(request, 'premium-watches.html', {'products': products})



# # Day-to-Day Watches
# def day_to_day_watches(request):
#     return render(request, 'day-to-day-watches.html')


# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(
                request,
                f'Welcome back, {user.username}!'
            )
            return redirect('home')

        else:
            messages.error(
                request,
                'Invalid email or password.'
            )

    return render(request, 'login.html')


# Logout
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')

def create_account(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            messages.success(
                request,
                'Your account has been created successfully!'
            )

            return redirect('login')

    else:

        form = CustomUserCreationForm()

    return render(
        request,
        'create account.html',
        {
            'form': form
        }
    )





# Checkout
def checkout(request):
    return render(request, 'checkout.html')


def category(request, foo):

    category = Category.objects.get(name=foo)

    products = Product.objects.filter(category=category)

    return render(
        request,
        'category.html',
        {
            'products': products,
            'category': category
        }
    )


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()


        if searched == "":
            messages.warning(request, "Please enter a product name.")
            return render(request, "search.html", {})


        products = Product.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )


        if not products:
            messages.error(request, "No matching products found.")
            return render(request, "search.html", {})


        return render(request, "search.html", {'searched': products})


    return render(request, "search.html", {})





