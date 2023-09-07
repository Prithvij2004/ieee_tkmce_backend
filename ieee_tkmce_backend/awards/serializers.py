from rest_framework.serializers import ModelSerializer

from .models import Award


class AwardSerializer(ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"
