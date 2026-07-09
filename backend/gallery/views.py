from rest_framework.generics import ListAPIView

from .models import Gallery
from .serializers import GallerySerializer


class GalleryListAPIView(ListAPIView):

    queryset = Gallery.objects.all()

    serializer_class = GallerySerializer