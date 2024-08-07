from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
    ('Other','Other'),
    ('Work','Work'),
    ('Sport','Sport'),
    ('Birthday','Birthday'),
    ('Wedding','Wedding'),
    ('Anniversary','Anniversary'),
    ('Concert','Concert'),
    ('Holiday','Holiday'),
)

# Events
class Event(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField('Date')
    location = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guests = models.ManyToManyField(User, related_name='guest_events', blank=True)
    category = models.CharField(
        max_length=20, 
        choices=CATEGORIES,
        default=CATEGORIES[0][0])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'event_id': self.id})


# Comments
class Comment(models.Model):
    comment = models.TextField(max_length=256)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by  for {self.event}"

