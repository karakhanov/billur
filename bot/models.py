from django.db import models


# Create your models here.
class botUser(models.Model):
    user_id = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)
    firstname = models.CharField(max_length=120, null=True, blank=True)
    lastname = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    long = models.CharField(max_length=120, null=True, blank=True)
    lat = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.firstname)

