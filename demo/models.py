from django.db import models

# Create your models here.
class Result(models.Model):
    part_id = models.IntegerField()
    title = models.CharField(max_length=64)
    text = models.TextField()
    sentence = models.TextField()
    cur_state = models.CharField(max_length=64)
    event = models.CharField(max_length=1024)
    new_state = models.CharField(max_length=64)

# class Rfcs(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=64)
#
# class Text(models.Model):
#     id = models.IntegerField()
#     rid = models.IntegerField()
#     text = models.TextField()

class Transition(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=64)
    text = models.TextField()
    sentence = models.TextField()
    cur_state = models.CharField(max_length=64)
    event = models.CharField(max_length=1024)
    new_state = models.CharField(max_length=64)


