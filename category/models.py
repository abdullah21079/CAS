from django.db import models
from orderFood.models import Order_food
# Create your models here.
class Category(models.Model):
    cat_id=models.IntegerField(primary_key=True)
    cat_name=models.CharField(max_length=100)
    food_name=models.ForeignKey(Order_food,on_delete=models.CASCADE)
