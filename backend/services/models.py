from django.db import models


class Service(models.Model):

    ICON_CHOICES = [
        ("dog", "Dog"),
        ("syringe", "Syringe"),
        ("stethoscope", "Stethoscope"),
        ("tooth", "Tooth"),
        ("cut", "Cut"),
        ("ambulance", "Ambulance"),
    ]

    icon = models.CharField(
        max_length=30,
        choices=ICON_CHOICES,
        default="dog"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title