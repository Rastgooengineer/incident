from django.http import Http404
from django.shortcuts import render
from .models import cam01_incidents_2019
def index(request):
  #  return HttpResponse("Hello, world. You're at the polls index.")
    try:
        allvideos = cam01_incidents_2019.objects.all()
        print(allvideos)
    except cam01_incidents_2019.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'home.html',  {'allvideos': allvideos})
