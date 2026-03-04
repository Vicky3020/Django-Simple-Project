from django.db import models

class Bus(models.Model):
    routes = models.CharField(max_length=100) 
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    durations = models.CharField(max_length=100)
    person = models.IntegerField(null=True,blank=True)
    date = models.DateField()

    def __str__(self):
        return self.routes 
