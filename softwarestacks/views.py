from django.shortcuts import render


def custom_403_view(request, exception):
    """Custom 403 Forbidden view."""
    return render(request, 'tests/403.html', status=403)
