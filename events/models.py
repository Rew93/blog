from django.db import models


# Create your models here.
class EventsModel(models.Model):
    events_image = models.ImageField(upload_to='events_image')
    descriptions = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.descriptions[:15]}'
