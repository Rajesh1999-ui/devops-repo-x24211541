"""Models for orders app."""
# pylint: disable=no-member, too-few-public-methods
from django.db import models

from accounts.models import User
from shop.models import Product


class Order(models.Model):
    """Order model for customer purchases."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        """Meta class for Order."""
        ordering = ('-created',)

    def __str__(self):
        """Return string representation of order."""
        return f"{self.user.full_name} - order id: {self.id}"

    @property
    def get_total_price(self):
        """Calculate total price of order."""
        total = sum(item.get_cost() for item in self.items.all())
        return total


class OrderItem(models.Model):
    """Order item model for individual items in an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        """Return string representation of order item."""
        return str(self.id)

    def get_cost(self):
        """Calculate cost of this order item."""
        return self.price * self.quantity
        