from rest_framework import filters, generics

from .models import Event
from .serializers import Event_Single_Serializer, EventSerializer


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = Event_Single_Serializer
    filter_backends = [filters.OrderingFilter]
    ordering = "-pub_date"
    ordering_fields = ["start_date", "end_date"]


event_all_as_view = EventList.as_view()


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "slug"


event_each_as_view = EventDetail.as_view()
