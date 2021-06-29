from django.db import models

# Create your models here.
    
class Store(models.Model):
    Name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.Name


class FittingModel(models.Model):
    blog_id = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    Mnumber = models.IntegerField()
    Mname = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    type = models.CharField(max_length=300)

    def __str__(self):
        return self.Mname
    
