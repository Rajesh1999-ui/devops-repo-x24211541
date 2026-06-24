"""Views for shop app."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from shop.models import Product, Category
from cart.forms import QuantityForm


def paginat(request, list_objects):
    """Paginate a list of objects."""
    p = Paginator(list_objects, 20)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj


def home_page(request):
    """Display home page with products."""
    products = Product.objects.all()
    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)


def product_detail(request, slug):
    """Display product detail page."""
    form = QuantityForm()
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).all()[:5]
    context = {
        'title': product.title,
        'product': product,
        'form': form,
        'favorites': 'favorites',
        'related_products': related_products
    }
    if request.user.likes.filter(id=product.id).first():
        context['favorites'] = 'remove'
    return render(request, 'product_detail.html', context)


@login_required
def add_to_favorites(request, product_id):
    """Add product to user's favorites."""
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.add(product)
    return redirect('shop:product_detail', slug=product.slug)


@login_required
def remove_from_favorites(request, product_id):
    """Remove product from user's favorites."""
    product = get_object_or_404(Product, id=product_id)
    request.user.likes.remove(product)
    return redirect('shop:favorites')


@login_required
def favorites(request):
    """Display user's favorites."""
    products = request.user.likes.all()
    context = {'title': 'Favorites', 'products': products}
    return render(request, 'favorites.html', context)


def search(request):
    """Search products by query."""
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query).all()
    context = {'products': paginat(request, products)}
    return render(request, 'home_page.html', context)


def filter_by_category(request, slug):
    """Filter products by category including subcategories."""
    result = []
    category = Category.objects.filter(slug=slug).first()
    # Add products from main category
    for product in Product.objects.filter(category=category.id).all():
        result.append(product)

    # Check if category is parent then get all sub-categories
    if not category.is_sub:
        sub_categories = category.sub_categories.all()
        # Get all sub-categories products
        for sub_category in sub_categories:
            for product in Product.objects.filter(category=sub_category).all():
                result.append(product)

    context = {'products': paginat(request, result)}
    return render(request, 'home_page.html', context)