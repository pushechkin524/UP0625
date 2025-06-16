from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from .views import user_list, user_create, user_update, user_delete
from .views import category_list, category_create, category_update, category_delete
from .views import review_list, review_create, review_update, review_delete
from .views import faq_list, faq_create, faq_update, faq_delete
from .views import season_list, season_create, season_update, season_delete, register_view, my_orders
from .views import ProductDetailView
from .views import (
    home_page,
    about_page,
    reviews_page, 
    toggle_favorite,
    contacts_page,
    product_list,
    favorite_add,
    catalog_view,
    product_detail,
    favorite_list,
    favorite_remove,
    product_create,
    product_update,
    product_delete,
    CustomLoginView,
    brand_list,
    brand_create,
    brand_update,
    brand_delete,
)

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),
    path('reviews/', reviews_page, name='reviews'),
    path('catalog/', catalog_view, name='catalog'),
    
    path('register/', register_view, name='register'),

    path('my-orders/', my_orders, name='my_orders'),

    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),

    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),


    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    
    path('products/<int:product_id>/favorite-toggle/', toggle_favorite, name='favorite_toggle'),
    path('favorite/add/<int:product_id>/', favorite_add, name='favorite_add'),
    path('favorites/', favorite_list, name='favorites'),
    path('favorite/remove/<int:pk>/', favorite_remove, name='favorite_remove'),
    path('favorites/', favorite_list, name='favorite_list'),

    path('brands/', brand_list, name='brand_list'),
    path('brands/create/', brand_create, name='brand_create'),
    path('brands/<int:pk>/edit/', brand_update, name='brand_update'),
    path('brands/<int:pk>/delete/', brand_delete, name='brand_delete'),

    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),

    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/<int:pk>/edit/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),

    path('reviewss/', review_list, name='review_list'),
    path('reviewss/create/', review_create, name='review_create'),
    path('reviewss/<int:pk>/edit/', review_update, name='review_update'),
    path('reviewss/<int:pk>/delete/', review_delete, name='review_delete'),

    path('faq/', faq_list, name='faq_list'),
    path('faq/create/', faq_create, name='faq_create'),
    path('faq/<int:pk>/edit/', faq_update, name='faq_update'),
    path('faq/<int:pk>/delete/', faq_delete, name='faq_delete'),

    path('seasons/', season_list, name='season_list'),
    path('seasons/create/', season_create, name='season_create'),
    path('seasons/<int:pk>/edit/', season_update, name='season_update'),
    path('seasons/<int:pk>/delete/', season_delete, name='season_delete'),
]
