import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    pub_date =models.DateTimeField('date created')
    Working_Days=models.IntegerField()
    Salary=models.IntegerField()
    def __str__(self):
        return self.First_Name
    def was_created_recently(self):
        return self.pub_date>=timezone.now() - datetime.timedelta(days=1)
