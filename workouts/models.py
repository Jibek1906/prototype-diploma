from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title