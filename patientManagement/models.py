from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uniqueID = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)

    def __str__(self):
        self.toString = str(self.uniqueID) + " " + str(self.first_name) + " " + str(self.last_name)
        return self.toString
