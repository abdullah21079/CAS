from django.db import models
from user.models import User
# Create your models here.
class User_profile(models.Model):
    id=models.IntegerField(primary_key=True)
    user_phn_number=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
