from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)

    def __str__(self):
        return f'{self.name} - {self.rating}%, {self.year}'
