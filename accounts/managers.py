"""Custom user manager for accounts app."""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Custom user manager for User model."""
    def create_user(self, email, full_name, password):
        """Create and save a regular user."""
        if not email:
            raise ValueError('Email is required!')
        if not full_name:
            raise ValueError('full name is required!')

        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, full_name, password):
        """Create and save a superuser."""
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self.db)
        return user