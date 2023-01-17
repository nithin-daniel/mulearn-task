from django.db import models

# Create your models here.


# class kjhdaksdjfhsdaf()
#  name
#  is completed
# date time 


class Todo(models.Model):
    name = models.CharField(max_length=200)
    # is_completed = models.BooleanField(default=False)
    description = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
            return self.name
    
    
class Completed(models.Model):
    name = models.CharField(max_length=200)
    # is_completed = models.BooleanField(default=False)
    description = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
            return self.name
    
    
