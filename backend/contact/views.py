from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializers import ContactSerializer


class ContactAPIView(APIView):

    def get(self, request):

        contact = Contact.objects.first()

        if not contact:
            return Response({})

        serializer = ContactSerializer(contact)

        return Response(serializer.data)