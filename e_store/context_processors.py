"""Context processors for e_store project."""
from cart.utils.cart import Cart
from shop.models import Category


def return_cart(request):
    """Return cart count for all templates."""
    cart = len(list(Cart(request)))
    return {'cart_count': cart}


def return_categories(request):
    """Return categories for all templates."""
    categories = Category.objects.all()
    return {'categories': categories}
    