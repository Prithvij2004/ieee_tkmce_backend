from django.shortcuts import render
from rest_framework.views import APIView
from ieee_tkmce_backend import awards, stories,updates,society,stats,contact
from .serializers import GodSerializer
from rest_framework.response import Response
def check_server(request):  # Indication of Running Server By Returning server date time and docs location
    now = datetime.datetime.now()

    return HttpResponse(
        f'''<div style="text-align:center;">
        <h3>Server is up and running :) {now}</h3>
        <a href = "/docs" style="padding:10px;border-radius:5px;background-color:#5CDB94">Documentation</a>
        </div>''')

class GodList(APIView):
    def get(self, request, format=None):
        return Response(self.master_serializer())
    def master_serializer(self):
        updates_ser = updates.models.Event.objects.all()[:3]
        awards_ser = awards.models.Award.objects.all()[:5]
        strs_ser = stories.models.Event.objects.all()[:5]
        society_ser = society.models.Society.objects.all()
        stats_ser = stats.models.Stats.objects.all()
        contacts_ser = contact.models.Contact.objects.all()

        aws = awards.serializers.AwardSerializer(awards_ser,many=True)
        ups = updates.serializers.Event_Single_Serializer(updates_ser,many=True)
        strs = stories.serializers.Story_Single_Serializer(strs_ser,many=True)
        societies = society.serializers.SocietySerializer(society_ser,many=True)
        statistics = stats.serializers.StatsSerializer(stats_ser,many=True)
        contacts = contact.serializers.ContactSerializer(contacts_ser,many=True)

        return {"updates": ups.data,
                "stories":strs.data,
                "societies":societies.data,
                "awards":aws.data,
                "statistics":statistics.data,
                "contacts":contacts.data
                }

god_as_view = GodList.as_view()
# Updates - > 3 ennam (Single images)
# Stories ->  ennam (single)
# Societies -> motham
# awards ->  5 ennam
# statics -> muyvanum
# contacts -> muyvanum
