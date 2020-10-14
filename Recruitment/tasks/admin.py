from django.contrib import admin
from .models import Candidate, Recruiter, Task, Grade

@admin.register (Candidate, Recruiter)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')

@admin.register (Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register (Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'recruiter', 'task', 'value')
    list_display_links = ('candidate', 'task', 'value')

# class CandidateAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name')
# admin.site.register(Candidate)

