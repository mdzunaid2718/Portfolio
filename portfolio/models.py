from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 70)
    email = models.CharField(max_length= 70)
    subject = models.EmailField(max_length = 100)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    