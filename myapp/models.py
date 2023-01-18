from json import JSONEncoder
from django.db import models


class MyEncoder(JSONEncoder):
    @classmethod
    def default(cls, o):
        return o.__dict__


    # Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

