from django.db import models
from django.conf import settings

class Capsule(models.Model):
    capsule_title = models.CharField(max_length=70, blank=False, null=False)
    capsule_content = models.TextField(blank=False, null=False)
    recipient = models.EmailField(null=False, blank=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()

    def __str__(self): 
        return self.capsule_title