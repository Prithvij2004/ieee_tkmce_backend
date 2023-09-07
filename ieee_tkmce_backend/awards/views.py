from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Award
from .serializers import AwardSerializer


class AwardList(ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["priority"]


award_all_as_view = AwardList.as_view()


class AwardDetail(RetrieveAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    lookup_field = "slug"


award_each_as_view = AwardDetail.as_view()
