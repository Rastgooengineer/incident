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
        #if "stopCheck" in request.POST:
        stopType = json.dumps(list(IncidentsInf.objects.filter(type="Stop").values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
         #    return render(request, 'home.html', { 'stopType': stopType})
        #if "queueCheck" in request.POST:
        queueType = json.dumps(list(IncidentsInf.objects.filter(type="Queue").values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
         #    return render(request, 'home.html', {'queueType': queueType})
        #if "wrongCheck" in request.POST:
        wrongType = json.dumps(list(IncidentsInf.objects.filter(type="WrongWay").values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
         #    return render(request, 'home.html', {'wrongType': wrongType})
        #if "pedestrainCheck" in request.POST:
        pedestrianType = json.dumps(list(IncidentsInf.objects.filter(type="Pedestrian").values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
         #    return render(request, 'home.html', {'': wrongType})
        #if "imageCheck" in request.POST:
        imageType = json.dumps(list(IncidentsInf.objects.filter(type="ImageDegradation").values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        #    return render(request, 'home.html', {'imageType': imageType})
        allIncidents = json.dumps(list(IncidentsInf.objects.all().values()), sort_keys=True, indent=1, cls=DjangoJSONEncoder)

        allvideos = IncidentsInf.objects.all().values()
    except IncidentsInf.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'home.html',  {'allvideos': allvideos, 'allIncidents': allIncidents, 'stopType': stopType, 'queueType': queueType, 'wrongType': wrongType, 'pedestrianType': pedestrianType, 'imageType': imageType})