from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.last_name
       
class Recruiter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.last_name
    
class Task(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
class Grade(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    value = models.IntegerField(null=False, choices=list(zip(range(1,11), range(1,11))))
