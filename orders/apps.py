"""App configuration for orders app."""
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """Configuration class for orders app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'