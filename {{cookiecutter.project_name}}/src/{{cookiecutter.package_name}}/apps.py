"""App configuration."""

from django.apps import AppConfig


class {{ cookiecutter.project_name.replace('-', ' ').title().replace(' ', '') }}Config(AppConfig):
    """App configuration for {{ cookiecutter.project_name }}."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.package_name }}"
