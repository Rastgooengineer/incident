from django.http import Http404
from django.shortcuts import render
from .models import IncidentsInf
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core import serializers

def index(request):
    videoname = IncidentsInf.objects.filter(check = 0)
    for obj in videoname:
        name = obj.video_name.split('_')[0]
        year = str(obj.videodatetime).split('-')[0]
        month =  str(obj.videodatetime).split('-')[1]
        print (name , year , month)
        obj.video_path = "{}/{}/{}".format(name,year,month)
        obj.check = 1
        obj.save()

    try:
        type_stop = json.dumps(list(IncidentsInf.objects.filter(type = "Stop").values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        allvideos = IncidentsInf.objects.all().values()
        print(type_stop)
        print ("############")
        print ((allvideos))
    except IncidentsInf.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'home.html',  {'allvideos': allvideos, 'type_stop': type_stop})
