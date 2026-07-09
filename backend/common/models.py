from django.db import models
from django.core.exceptions import ValidationError


class SingletonModel(models.Model):
    """
    Abstract model that allows only one instance.
    """

    class Meta:
        abstract = True

    def clean(self):
        if self.__class__.objects.exclude(pk=self.pk).exists():
            raise ValidationError(
                f"Only one {self.__class__.__name__} instance is allowed."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)