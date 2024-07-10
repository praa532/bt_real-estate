from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank= True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.name