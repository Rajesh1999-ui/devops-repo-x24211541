"""Models for accounts app."""
# pylint: disable=unused-argument, no-member
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from shop.models import Product
from .managers import UserManager


class User(AbstractBaseUser):
    """Custom User model with email as username field."""
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField(Product, blank=True, related_name='likes')
    # set a manager role for shop manager to access orders and products
    is_manager = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        """Return string representation of user."""
        return str(self.email)

    def has_perm(self, perm, obj=None):
        """Check if user has permission."""
        return True

    def has_module_perms(self, app_label):
        """Check if user has module permissions."""
        return True

    @property
    def is_staff(self):
        """Check if user is staff."""
        return self.is_admin

    def get_likes_count(self):
        """Get count of user's liked products."""
        return self.likes.count()
        