from decimal import Decimal
from django.conf import settings
from up1.models import Product

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:
            basket = self.session[settings.CART_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'count': 0, 'price': str(product.price)}
        if update_count:
            self.basket[product_id]['count'] = count
        else:
            self.basket[product_id]['count'] += count
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            item = self.basket[str(product.id)]
            item['product'] = product
            item['total_price'] = Decimal(item['price']) * item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.basket.values())
