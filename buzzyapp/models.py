from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=444)

    def __str__(self):
        return self.type_id
    

class BuzzyUser(AbstractUser):
    usertype = models.ForeignKey(UserType, on_delete=models.DO_NOTHING, related_name ="user_role_type",default =1)
    address = models.CharField(max_length = 200)
    # phone = models.CharField(max_length = 20)