from rest_framework.generics import ListAPIView

from .models import Service
from .serializers import ServiceSerializer


class ServiceListAPIView(ListAPIView):

    serializer_class = ServiceSerializer

    queryset = Service.objects.all().order_by("order")