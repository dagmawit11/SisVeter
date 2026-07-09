from rest_framework.generics import RetrieveAPIView
from .models import Hero
from .serializers import HeroSerializer


class HeroAPIView(RetrieveAPIView):
    serializer_class = HeroSerializer

    def get_object(self):
        return Hero.objects.first()