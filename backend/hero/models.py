from django.db import models


class Hero(models.Model):

    tag = models.CharField(
        max_length=100,
        default="Trusted Veterinary Clinic"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = models.ImageField(
    upload_to="hero/",
    blank=True,
    null=True
)

    primary_button_text = models.CharField(
        max_length=50,
        default="Book Appointment"
    )

    primary_button_link = models.CharField(
        max_length=100,
        default="/contact"
    )

    secondary_button_text = models.CharField(
        max_length=50,
        default="Our Services"
    )

    secondary_button_link = models.CharField(
        max_length=100,
        default="/services"
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return "Hero Section"