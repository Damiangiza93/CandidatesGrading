"""Recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import (
    AddMarkView, GradeAdded, 
    CandidatesListView, AddCandidateView, 
    AddRecruiterView, AddTaskView,
    Home
    )
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('add-mark/', AddMarkView.as_view(), name='add-mark'),
    path('add-mark/add-candidate/', AddCandidateView.as_view(), name='add-candidate'),
    path('add-mark/add-recruiter/', AddRecruiterView.as_view(), name='add-recruiter'),
    path('add-mark/add-task/', AddTaskView.as_view(), name='add-task'),
    path('gradeadded/', GradeAdded, name='gradeadded'),
    path('candidates-list/', CandidatesListView, name='candidates-list'),
    path('', Home, name='home')
    
]
