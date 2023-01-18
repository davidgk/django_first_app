from json import JSONEncoder
from django.db import models


class MyEncoder(JSONEncoder):
    @classmethod
    def default(cls, o):
        return o.__dict__


    # Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)




class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

