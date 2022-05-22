from django.contrib import admin

# Register your models here.
from .models import Project, Milestone

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'owner',
        'started',
        'current_milestone',
        )

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'project_id')