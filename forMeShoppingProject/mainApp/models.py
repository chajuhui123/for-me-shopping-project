from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

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