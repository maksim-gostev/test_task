from django.db import models


class Birds(models.Model):
    name = models.CharField(max_length=100)
    feather_color = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='bird_pictures/', null=True, blank=True)
