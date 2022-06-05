from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True)
    planned = models.BooleanField(default=False)
    phase = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name



class Milestone(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



class Case(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    automated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Plan(models.Model):
    plan_to_exec = models.DateTimeField(blank=True, null=True)
    plan_to_end = models.DateTimeField(blank=True, null=True)

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)


RESULT_STATUS = [
   (0, 'pass') ,
   (1, 'failed') ,
]


class Result(models.Model):
    status = models.IntegerField(choices=RESULT_STATUS)
    tester = models.CharField(max_length=50)
    case_name = models.CharField(max_length=500, null=True, blank=True)    # for non-planned case
    project_name = models.CharField(max_length=100, null=True, blank=True) # for non-planned case
    completed_date = models.DateTimeField(null=True, blank=True)

    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
