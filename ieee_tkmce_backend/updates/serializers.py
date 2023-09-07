from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, SlugRelatedField

from .models import Event


class EventSerializer(ModelSerializer):
    pix = SlugRelatedField(many=True, read_only=True, slug_field="name")  # One to Many Serialized

    class Meta:
        model = Event
        fields = "__all__"


class Event_Single_Serializer(ModelSerializer):
    pic = serializers.SerializerMethodField("get_single_image")

    def get_single_image(self, obj):
        sing_img = obj.pix.all().first()
        if sing_img:
            return sing_img.name
        else:
            return None

    class Meta:
        model = Event
        fields = "__all__"
