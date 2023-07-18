from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    owner = models.CharField(max_length=100)
    created = models.DateField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return '{}-{} - {}, belongs to {}'.format(self.brand,self.model, self.year, self.owner)