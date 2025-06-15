from django.shortcuts import render, get_object_or_404, redirect
from django.core.handlers.wsgi import WSGIHandler
from .models import Product
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand
from .forms import BrandForm
from django.contrib.auth.decorators import login_required
from .models import Favorite
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from .models import Favorite
from .forms import UserForm
from .models import Category
from .forms import CategoryForm
from .models import Review
from .forms import ReviewForm
from .models import Faq
from .forms import FaqForm
from .models import Season
from .forms import SeasonForm

def season_list(request):
    seasons = Season.objects.all()
    return render(request, 'seasons/season_list.html', {'seasons': seasons})

def season_create(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('season_list')
    else:
        form = SeasonForm()
    return render(request, 'seasons/season_form.html', {'form': form, 'title': 'Добавить сезон'})

def season_update(request, pk):
    season = get_object_or_404(Season, pk=pk)
    if request.method == 'POST':
        form = SeasonForm(request.POST, instance=season)
        if form.is_valid():
            form.save()
            return redirect('season_list')
    else:
        form = SeasonForm(instance=season)
    return render(request, 'seasons/season_form.html', {'form': form, 'title': 'Редактировать сезон'})

def season_delete(request, pk):
    season = get_object_or_404(Season, pk=pk)
    if request.method == 'POST':
        season.delete()
        return redirect('season_list')
    return render(request, 'seasons/season_confirm_delete.html', {'season': season})


@login_required
def faq_list(request):
    faqs = Faq.objects.all()
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

@login_required
def faq_create(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FaqForm()
    return render(request, 'faq/faq_form.html', {'form': form, 'title': 'Добавить вопрос'})

@login_required
def faq_update(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FaqForm(instance=faq)
    return render(request, 'faq/faq_form.html', {'form': form, 'title': 'Редактировать вопрос'})

@login_required
def faq_delete(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    return render(request, 'faq/faq_confirm_delete.html', {'faq': faq})


def home_page(request: WSGIHandler):
    return render(request, 'home.html')

def about_page(request: WSGIHandler):
    return render(request, 'about.html')

def contacts_page(request: WSGIHandler):
    return render(request, 'contacts.html')

def reviews_page(request: WSGIHandler):
    return render(request, 'reviews.html')

# --- CRUD для Product ---

def product_list(request: WSGIHandler):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request: WSGIHandler):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request: WSGIHandler, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request: WSGIHandler, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm


def catalog_view(request):
    category_id = request.GET.get('category')  # ожидаем ?category=1
    categories = Category.objects.all()

    products = Product.objects.all()
    selected_category = None

    if category_id:
        try:
            selected_category = Category.objects.get(id=int(category_id.strip()))
            products = products.filter(category=selected_category)
        except (Category.DoesNotExist, ValueError):
            selected_category = None  # если id неверный или категории нет

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'catalog.html', context)

def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if not created:
        favorite.delete()
    return redirect('product_detail', pk=product_id)  

@login_required
def favorite_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('catalog')  

def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    return render(request, 'favorites.html', {'favorites': favorites})

@login_required
def favorite_remove(request, pk):
    favorite = get_object_or_404(Favorite, user=request.user, product_id=pk)
    favorite.delete()
    return redirect('favorites')

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brand_list.html', {'brands': brands})


@login_required
def brand_create(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('brand_list')
    return render(request, 'brands/brand_form.html', {'form': form, 'title': 'Добавить бренд'})


@login_required
def brand_update(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    form = BrandForm(request.POST or None, instance=brand)
    if form.is_valid():
        form.save()
        return redirect('brand_list')
    return render(request, 'brands/brand_form.html', {'form': form, 'title': 'Редактировать бренд'})


@login_required
def brand_delete(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')
    return render(request, 'brands/brand_confirm_delete.html', {'brand': brand})

User = get_user_model()

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Добавить пользователя'})


@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Редактировать пользователя'})


@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})



@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Создание категории'})


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Редактирование категории'})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})

@login_required
def review_list(request):
    reviews = Review.objects.select_related('user', 'product')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})


@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'title': 'Добавить отзыв'})


@login_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'title': 'Редактировать отзыв'})


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'reviews/review_confirm_delete.html', {'review': review})

def catalog_view(request):
    category_id = request.GET.get('category')
    sort = request.GET.get('sort')
    
    products = Product.objects.all()
    categories = Category.objects.all()
    current_category = None

    if category_id:
        products = products.filter(category_id=category_id)
        current_category = Category.objects.get(id=category_id)

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'catalog.html', context)
