"""Cart utility for handling shopping cart."""
from shop.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    """Shopping cart class for session-based cart management."""
    def __init__(self, request):
        self.session = request.session
        self.cart = self.add_cart_session()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def add_cart_session(self):
        """Get or create cart session."""
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        return cart

    def add(self, product, quantity):
        """Add product to cart."""
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        self.cart.get(product_id)['quantity'] += quantity
        self.save()

    def remove(self, product):
        """Remove product from cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """Save cart to session."""
        self.session.modified = True

    def get_total_price(self):
        """Calculate total price of all items in cart."""
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Clear the cart."""
        del self.session[CART_SESSION_ID]
        self.save()
        