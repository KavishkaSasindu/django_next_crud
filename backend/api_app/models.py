from django.db import models

# Create your models here.
class Api(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.CharField(max_length=10)
    description = models.TextField(max_length = 200)
    
    def __str__(self):
        return self.first_name
    
