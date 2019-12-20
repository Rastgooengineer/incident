from django.db import models

class IncidentsInf(models.Model):
    videodatetime = models.DateTimeField(auto_now_add=True, null=False)
    name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=100, null=False)
    video_name = models.CharField(max_length=100, blank=True)
    video_path = models.CharField(max_length=200,null=True, default= "/")
    check = models.IntegerField()
    objects = models.Manager()
