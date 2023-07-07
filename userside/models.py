from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    adh=models.CharField(max_length=122)
    req=models.TextField()

    def __str__(self):
        return self.name

