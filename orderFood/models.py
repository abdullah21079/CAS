from django.db import models
from menu.models import Menu
# Create your models here.
class Order_food(models.Model):
    food_id=models.IntegerField(primary_key=True)
    food_name=models.CharField(max_length=100)
    food_price=models.IntegerField(max_length=6)
    menu_no=models.ForeignKey(Menu,on_delete=models.CASCADE)
