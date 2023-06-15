from django.db import models
from accounts.models import Account
# Create your models here.
class Event(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default='Anonymous'
    )
    images          = models.ImageField(upload_to='photos/events',null=True, blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name