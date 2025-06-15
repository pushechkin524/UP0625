from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', first_page),
    path('/second_page/', second_page),
    path('clothes/', ClothesListView.as_view(), name='clothes_list'),
    path('clothes/<int:pk>/', ClothesDetailView.as_view(), name='clothes_detail'),
    path('clothes/create/', ClothesCreateView.as_view(), name='clothes_create'),
    path('clothes/update/<int:pk>/', ClothesUpdateView.as_view(), name='clothes_update'),
    path('clothes/delete/<int:pk>/', ClothesDeleteView.as_view(), name='clothes_delete'),
]