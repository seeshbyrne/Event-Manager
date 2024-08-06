from django.db import models
from django.urls import reverse


# EVENT MODEL ####################################################################################

class Event(models.Model):
    name = models.CharField(max_length=256) # this max length bit is a kwarg
    date = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'event_id': self.id})
    
#################################################################################################

# COMMENT MODEL ####################################################################################

class Comment(models.Model):
    comment = models.TextField(max_length=256)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comments for {self.event}"





#################################################################################################