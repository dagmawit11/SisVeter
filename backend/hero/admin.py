from django.contrib import admin
from common.admin import SingletonAdmin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(SingletonAdmin):

    list_display = (
        "title",
        "updated_at",
    )

    search_fields = (
        "title",
    )