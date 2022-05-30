from django.db import models

# Create your models here.
class Result(models.Model):
    part_id = models.IntegerField()
    title = models.CharField(max_length=64)
    text = models.TextField()
    sentence = models.TextField()
    cur_state = models.CharField(max_length=64)
    condition = models.CharField(max_length=1024)
    new_state = models.CharField(max_length=64)

