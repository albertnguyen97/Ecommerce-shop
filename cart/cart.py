from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import User
from shop.models import Product

CART_SESSION_ID = settings.CART_SESSION_ID


class Cart:
    def __init__(self, request):
        self.request = request
        self.user = request.user if request.user.is_authenticated else None
        if self.user:
            self.cart_data = self.load_cart_from_user()
        else:
            self.cart_data = self.load_cart_from_session()

    def load_cart_from_user(self):
        return self.user.profile.cart_data if hasattr(self.user, 'profile') else {}

    def load_cart_from_session(self):
        cart = self.request.session.get(CART_SESSION_ID, {})
        return cart

    def save_cart(self):
        if self.user:
            self.user.profile.cart_data = self.cart_data
            self.user.profile.save()
        else:
            self.request.session[CART_SESSION_ID] = self.cart_data
            self.request.session.modified = True

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart_data:
            self.cart_data[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            if quantity <= product.quantity_product:
                self.cart_data[product_id]['quantity'] = quantity
        else:
            self.cart_data[product_id]['quantity'] += quantity
        self.save_cart()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart_data:
            del self.cart_data[product_id]
            self.save_cart()

    def __iter__(self):
        product_ids = self.cart_data.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_data = self.cart_data.copy()
        for product in products:
            cart_data[str(product.id)]['product'] = product
        for item in cart_data.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart_data.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart_data.values())

    def clear(self):
        if self.user:
            self.user.profile.cart_data = {}
            self.user.profile.save()
        else:
            del self.request.session[CART_SESSION_ID]
            self.request.session.modified = True
