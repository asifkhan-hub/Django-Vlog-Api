from django.db import models

# Create your models here.
class Vlog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    upload_date = models.DateTimeField(auto_now_add=True)
    