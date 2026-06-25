"""Models for shop app."""
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    """Category model for products."""
    title = models.CharField(max_length=200)
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='sub_categories', null=True, blank=True
    )
    is_sub = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        """Return string representation of category."""
        return str(self.title)

    def get_absolute_url(self):
        """Get absolute URL for category."""
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Save category with auto-generated slug."""
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Product(models.Model):
    """Product model for shop items."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='products')
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        """Meta class for Product."""
        ordering = ('-date_created',)

    def __str__(self):
        """Return string representation of product."""
        return str(self.slug)

    def get_absolute_url(self):
        """Get absolute URL for product."""
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Save product with auto-generated slug."""
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        