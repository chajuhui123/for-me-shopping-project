from django.contrib import admin
from .models import Item, Measure,FittingModel,Store

# Register your models here.

admin.site.register(Item), 
admin.site.register(Measure),

admin.site.register(FittingModel),
admin.site.register(Store),