from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "description",
        "category",
        "media_type",
        "order",
    )

    list_editable = (
        "order",
    )

    list_filter = (
        "category",
        "media_type",
    )

    search_fields = (
        "description",
    )