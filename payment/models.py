from django.db import models
from user.models import User
# Create your models here.
class Payment(models.Model):
    payment_id=models.IntegerField(primary_key=True)
    payment_type=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
