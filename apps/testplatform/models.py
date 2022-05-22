from statistics import mode
from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100,)
    description = models.CharField(max_length=200, blank=True)
    owner = models.CharField(max_length=50, blank=True)
    started = models.BooleanField(default=False)
    current_milestone = models.ForeignKey('Milestone', on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.name




class Milestone(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name



class CaseBase(models.Model):
    pass