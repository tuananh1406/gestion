from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

class Post(models.Model):
   
    cin = models.CharField(max_length = 8)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=70,blank=True,unique=True)
    request = models.CharField(max_length=100)

    Motivation = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
          return reverse('post-detail',kwargs={'pk':self.pk})   




