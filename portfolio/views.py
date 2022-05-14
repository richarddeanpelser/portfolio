from django.shortcuts import render, redirect
from .models import Project, Role, Skill
from .forms import ProjectForm, SkillForm
from django.contrib import messages

# Create your views here.


def home_page(request):
    projects = Project.objects.all()
    detailed_skills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    

    context = {'projects': projects, 'skills': skills,
               'detailed_skills': detailed_skills}
    return render(request, 'home.html', context)

def project_page(request):
    projects = Project.objects.all()



    context = {'projects': projects}
    return render(request, 'projects.html', context)

def project_details(request, pk):
    project = Project.objects.get(id=pk)



    context = {'project': project}
    return render(request, 'project_details.html', context)
