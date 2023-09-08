from rest_framework.serializers import Serializer, SerializerMethodField, CharField
from ieee_tkmce_backend.awards.serializers import AwardSerializer
from ieee_tkmce_backend.updates.serializers import Event_Single_Serializer


class GodSerializer(Serializer):
    student = CharField(max_length=100)
    award = SerializerMethodField('get_awards')
    update = SerializerMethodField('get_updates')

    def __init__(self, *args, **kwargs):
        self.awards = kwargs.pop("awards_ser")
        self.updates = kwargs.pop("updates_ser")
        self.a = AwardSerializer(self.awards, many=True).data
        print(self.a)
        super(GodSerializer, self).__init__(*args, **kwargs)

    def get_awards(self, obj):
        print("\n\n\n\n\nss\n\n\n\n\n")
        return AwardSerializer(self.awards, many=True).data

    def get_updates(self, obj):
        return Event_Single_Serializer(self.updates, many=True).data
