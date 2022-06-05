from django.contrib import admin

# Register your models here.
from .models import Project, Milestone, Case, Plan, Result

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'owner',
        'planned'
        )

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display =('name', 'description')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('case', 'milestone', 'plan_to_exec', 'plan_to_end')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('status',)

    @admin.display(empty_value='???')
    def case_name(self, obj):
        return obj.plan.case