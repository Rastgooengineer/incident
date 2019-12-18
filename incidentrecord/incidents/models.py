from django.db import models

class cam01_incidents_2019(models.Model):
    time = models.DateTimeField(auto_now_add=True, null=False)
    name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=100, null=False)
    incident_avi = models.CharField(max_length=100, blank=True)
    objects = models.Manager()