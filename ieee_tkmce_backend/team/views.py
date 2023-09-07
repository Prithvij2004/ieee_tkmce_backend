from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .models import Team
from .serializers import TeamSerializer


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["year"]  # year = 2019 or 2019-2020


team_as_view = TeamListView.as_view()
