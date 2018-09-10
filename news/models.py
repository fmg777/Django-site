from django.db import models

# Create your models here.



class Novosti (models.Model):
    title = models.CharField (max_length=70)
    body = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return self.title