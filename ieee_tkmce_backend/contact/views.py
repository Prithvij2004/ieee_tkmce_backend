from rest_framework.generics import ListAPIView

from .models import Contact
from .serializers import ContactSerializer


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


contact_as_view = ContactListView.as_view()
