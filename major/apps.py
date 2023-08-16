from django.apps import AppConfig


class MajorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "major"
    verbose_name="전공 게시물"