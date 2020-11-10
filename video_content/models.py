from django.db import models

# Create your models here.

from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class Video(models.Model):

    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title

    class Meta:
        
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'