from django.db import models


class Passenger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    rewardPoints = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
    
    class Meta:
        db_table = 'passenger'