from django.db import models


class About(models.Model):

    welcome_text = models.CharField(
        max_length=200,
        default="WELCOME TO ODY MOBILE VETERINARY CLINIC"
    )

    title = models.CharField(
    max_length=250,
    blank=True,
    null=True
)

    description = models.TextField(
    blank=True,
    null=True
)

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    feature1 = models.CharField(
        max_length=100,
        default="Experienced Veterinarians"
    )

    feature2 = models.CharField(
        max_length=100,
        default="Modern Equipment"
    )

    feature3 = models.CharField(
        max_length=100,
        default="Emergency Services"
    )

    feature4 = models.CharField(
        max_length=100,
        default="Affordable Pricing"
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Section"