from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


# class kjhdaksdjfhsdaf()
#  name
#  is completed
# date time 


class Todo(models.Model):
    name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    description = models.TextField()
    date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

# Time expire code
    # def is_expired(self):
    #     # if self.date < datetime.datetime.now()
    #     return False if self.date.date()<date.today() else True

    def __str__(self):
        return self.name
    



    

