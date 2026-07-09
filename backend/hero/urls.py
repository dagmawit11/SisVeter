from django.urls import path
from .views import HeroAPIView

urlpatterns = [
    path("", HeroAPIView.as_view()),
]