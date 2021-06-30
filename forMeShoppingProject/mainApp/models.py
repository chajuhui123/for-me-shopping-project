from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    shop_url = models.URLField()

class Measure(models.Model):
    objects = models.Manager()
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING, null=True)
    size = models.CharField(max_length=10)
    length = models.IntegerField()
    shoulder = models.IntegerField()
    chest = models.IntegerField()
    sleeve = models.IntegerField()
    waist = models.IntegerField()
    rise = models.IntegerField()
    hem = models.IntegerField()


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