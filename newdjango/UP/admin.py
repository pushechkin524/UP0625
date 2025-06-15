from django.contrib import admin
from .models import Category, Clothes, Collection
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    pass

