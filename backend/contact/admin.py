from django.contrib import admin
from common.admin import SingletonAdmin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(SingletonAdmin):

    fieldsets = (

        ("Contact Information", {

            "fields": (
                "phone",
                "email",
                "address",
            )

        }),

        ("Working Hours", {

            "fields": (
                "working_days",
                "working_hours",
                "emergency_text",
            )

        }),

        ("WhatsApp", {

            "fields": (
                "whatsapp",
            )

        }),

    )