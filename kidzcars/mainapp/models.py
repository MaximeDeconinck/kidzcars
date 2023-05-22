from django.db import models

class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    generation = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} {self.generation} ({self.year})"
    
class CarPicture(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self):
        return f"Picture of {self.car}"