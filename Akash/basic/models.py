from enum import auto
from django.db import models

# Create your models here.

class Game(models.Model):
    name=models.CharField(max_length=255)
    year=models.IntegerField(max_length=4)
    device=models.TextField()
    topplayer=models.CharField(max_length=255)
    
    class Meta:
        db_table="games"
        
    def __str__(self):
        return self.name+" has choosed"