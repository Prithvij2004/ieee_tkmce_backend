from rest_framework.generics import CreateAPIView

from .models import Message
from .serializers import MessageSerializer


class MessageListView(CreateAPIView):
    serializer_class = MessageSerializer


message_as_view = MessageListView.as_view()
