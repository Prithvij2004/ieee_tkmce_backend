from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Stats
from .serializers import StatsSerializer


class StatsListView(ListAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer


stats_all_as_view = StatsListView.as_view()


class StatsDetailView(RetrieveAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
    lookup_field = "slug"


stats_each_as_view = StatsDetailView.as_view()
