from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import AddMarkForm, AddCandidateForm, AddRecruiterForm, AddTaskForm
from .models import Candidate, Grade  

class AddMarkView(SuccessMessageMixin, FormView):
    template_name = 'add_mark.html'
    form_class = AddMarkForm
    success_url = '/add-mark/'
    success_message = 'Mark added sucessfully'
            
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
    
class AddCandidateView(SuccessMessageMixin, FormView):
    template_name = 'add_candidate.html'
    form_class = AddCandidateForm
    success_url = '/add-mark/'
    success_message = 'Candidate added sucessfully'
    
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
    
class AddRecruiterView(SuccessMessageMixin, FormView):
    template_name = 'add_recruiter.html'
    form_class = AddRecruiterForm
    success_url = '/add-mark/'
    success_message = 'Recruiter added sucessfully'
    
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

class AddTaskView(SuccessMessageMixin, FormView):
    template_name = 'add_task.html'
    form_class = AddTaskForm
    success_url = '/add-mark/'
    success_message = 'Task added sucessfully'
    
    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

def Average(lst):
    if len(lst) != 0:
        return sum(lst) / len(lst)    

def CandidatesListView(request):
    
    candidate_d = Candidate.objects.filter()
    grade_d = Grade.objects.filter()
    candidates_d = []
    
    for candidate in candidate_d:
        grades_d = []
        for grade in grade_d:
            if grade.candidate == candidate:
                grades_d.append(grade.value)
        
        avg_grade = Average(grades_d)
        
        json_can = dict(
            pk = candidate.id,
            full_name = candidate.first_name + " " + candidate.last_name,
            avg_grade = avg_grade,
            grades = grades_d
            )
               
        candidates_d.append(json_can)
        
    return JsonResponse([{"data": candidates_d }] 
        ,safe=False, json_dumps_params={'indent': 1})

def GradeAdded(request):
    # context = {
    #     'tasks': Task.objects.get()     
    #     }
    return render(request, 'gradeadded.html')    

