from django.contrib import admin


class SingletonAdmin(admin.ModelAdmin):
    """
    Prevent adding more than one object.
    """

    def has_add_permission(self, request):
        return self.model.objects.count() == 0