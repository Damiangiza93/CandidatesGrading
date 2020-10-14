from django import forms
from .models import Candidate, Recruiter, Grade, Task  

class AddMarkForm(forms.ModelForm):
    
    class Meta:
        model = Grade
        fields = ('candidate', 'recruiter', 'task', 'value')
    
class AddCandidateForm(forms.ModelForm):
    
    class Meta:
        model = Candidate
        fields = ('first_name', 'last_name')
        
class AddRecruiterForm(forms.ModelForm):
    
    class Meta:
        model = Recruiter
        fields = ('first_name', 'last_name')  

class AddTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title']
    
    
    
    # Candidate.first_name = forms.CharField(max_length=30)
    # Candidate.last_name = forms.CharField(max_length=30)
    # Recruiter.first_name = forms.CharField(max_length=30)
    # Recruiter.last_name = forms.CharField(max_length=30)
    # Task.title = forms.CharField(max_length=150)
    # Grade.value = forms.IntegerField()
    
