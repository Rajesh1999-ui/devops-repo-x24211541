"""App configuration for dashboard app."""
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """Configuration class for dashboard app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'