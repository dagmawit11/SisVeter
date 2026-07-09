from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),

    path("api/hero/", include("hero.urls")),
    path("api/about/", include("about.urls")),
    path("api/services/", include("services.urls")),
    path("api/gallery/", include("gallery.urls")),
    path("api/contact/", include("contact.urls")),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )