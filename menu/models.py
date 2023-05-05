from django.db import models
from orderFood.models import Order_food
# Create your models here.
class Menu(models.Model):
    menu_no=models.IntegerField(primary_key=True)
    food_id=models.ForeignKey(Order_food,on_delete=models.CASCADE)