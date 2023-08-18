from django.db import models

class Wanted(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    state = models.CharField(max_length=60)
    reward = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name 


class Captured(models.Model):
    fugitive = models.ForeignKey(Wanted, on_delete=models.CASCADE)
    capture_time = models.DateTimeField()
    inJail = models.BooleanField(default=False)
