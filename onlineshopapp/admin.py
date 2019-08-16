from django.contrib import admin


# Register your models here.
from . models import Profile,Item,Order,OrderItem
  

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)