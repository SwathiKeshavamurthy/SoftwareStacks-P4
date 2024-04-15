from django.apps import AppConfig


# This class provides metadata and configuration for the application.
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
