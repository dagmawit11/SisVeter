from django.db import models


class Contact(models.Model):

    phone = models.CharField(max_length=30)

    email = models.EmailField()

    address = models.CharField(max_length=255)

    working_days = models.CharField(
        max_length=100,
        default="Monday - Saturday"
    )

    working_hours = models.CharField(
        max_length=100,
        default="8:30 AM - 5:30 PM"
    )

    emergency_text = models.CharField(
        max_length=100,
        blank=True
    )

    whatsapp = models.CharField(max_length=30)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Clinic Contact Information"