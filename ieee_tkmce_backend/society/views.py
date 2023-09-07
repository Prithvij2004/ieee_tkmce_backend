from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Society
from .serializers import SocietySerializer


class SocietyListView(ListAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer


society_as_view = SocietyListView.as_view()


class SocietyDetailView(RetrieveAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    lookup_field = "slug"


society_each_as_view = SocietyDetailView.as_view()
