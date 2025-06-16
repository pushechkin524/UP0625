from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.product}"

class Season(models.Model):
    SEASON_CHOICES = [
        ('winter', 'Зима'),
        ('spring', 'Весна'),
        ('summer', 'Лето'),
        ('autumn', 'Осень'),
    ]

    name = models.CharField(max_length=50, choices=SEASON_CHOICES, unique=True)
    products = models.ManyToManyField('Product', related_name='seasons')

    def __str__(self):
        return self.get_name_display()


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')


    def __str__(self):
        return f"{self.user.username} ♥ {self.product.name}"
    

from django.db import models
from .models import Product  # Предполагается, что Product уже есть
from django.conf import settings  # Для использования кастомной модели User

MAX_LENGTH = 255  # Общая длина для полей с ограничением

class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"

    TYPE_DELIVERY = [
        (SHOP, 'Вывоз из магазина'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]

    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия покупателя')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя покупателя')
    buyer_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество покупателя')

    comment = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Комментарий к заказу')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')

    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')

    products = models.ManyToManyField(Product, through='PosOrder', verbose_name='Товары')

    def __str__(self):
        return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name} ({self.date_create.strftime("%Y-%m-%d")})'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class PosOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на товар (%)')

    def __str__(self):
        return f'Заказ #{self.order.pk} - {self.product.name} ({self.order.buyer_firstname} {self.order.buyer_name})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
