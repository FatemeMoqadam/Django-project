from django.db import models
from django.utils import timezone
import datetime


class feeling(models.Model):
    feeling_text = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('date published' ,null=True ,blank=True)
    def __str__(self):
        return self.feeling_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class solution(models.Model):
    feeling = models.ForeignKey(feeling, on_delete=models.CASCADE, related_name='solutions',null=True ,blank=True)
    suggested_movie=models.CharField(max_length=200,null=True ,blank=True)
    link = models.URLField(max_length=200,null=True ,blank=True)
    def __str__(self):
        return self.suggested_movie and self.link


class solutionsong(models.Model):
    feeling = models.ForeignKey(feeling, on_delete=models.CASCADE, related_name='solutionsongs',null=True ,blank=True)
    suggested_song=models.CharField(max_length=200,null=True ,blank=True)
    link = models.URLField(max_length=200,null=True ,blank=True)
    def __str__(self):
        return self.suggested_song and self.link

