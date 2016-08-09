from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic a user is learning about"""
    text = models.CharField(max_length= 250)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return the string representation of model"""
        return self.text

class Entry(models.Model):
    """Specific things learned in one topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return the string representaion of model"""
        return self.text[:50] + "....."
