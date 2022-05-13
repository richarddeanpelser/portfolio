# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("This is the home page")


from django.views import generic
from .models import Project


class ProjectList(generic.ListView):
    """
    Return all Projects that are with status 1 (published) and order from the latest one.
    """
    queryset = Project.objects.filter(status=1).order_by('period')
    template_name = 'index.html'


class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'Project_detail.html'