from django.db import models

# Create your models here.

class LoginUser(models.Model):
    FullName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    Created_date = models.DateField()

    def __str__(self):
        return self.UserName