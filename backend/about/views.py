from rest_framework.generics import RetrieveAPIView
from .models import About
from .serializers import AboutSerializer


class AboutView(RetrieveAPIView):

    serializer_class = AboutSerializer

    def get_object(self):

        return About.objects.first()