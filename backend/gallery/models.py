from django.db import models


class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ("Pets", "Pets"),
        ("Surgery", "Surgery"),
        ("Videos", "Videos"),
    ]

    MEDIA_TYPE = [
        ("image", "Image"),
        ("video", "Video"),
    ]

    title = models.CharField(max_length=200, blank=True)

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="Pets"
    )

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPE,
        default="image"
    )

    file = models.FileField(upload_to="gallery/")

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.description[:40]