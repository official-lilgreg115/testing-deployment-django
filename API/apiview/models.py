from django.db import models

# Create your models here.
class SmallestData(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
     

    def __str__(self):
        return f"{self.title}"

class SmallData(models.Model):
    title = models.CharField(max_length=100) 
    inside =models.ForeignKey(SmallestData, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"

class Data(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    insert = models.ForeignKey(SmallData, on_delete=models.CASCADE)
    inside =models.ForeignKey(SmallestData, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} ({self.age})"