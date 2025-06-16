from django.contrib import admin
from .models import User, Category, Brand, Product, Review, Favorite, Season, Faq
from .models import Order, PosOrder

admin.site.register(Order)
admin.site.register(PosOrder)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Season)
admin.site.register(Faq)
