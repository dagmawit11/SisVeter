from django.urls import path

from .views import ServiceListAPIView


urlpatterns = [

    path("", ServiceListAPIView.as_view()),

]