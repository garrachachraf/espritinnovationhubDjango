from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from ProjectsApp.models import *


def index(request):
    #return HttpResponse("You're looking to the index page.")
    return render(request, 'index.html')


def list_projects(request):
    """projects_list = Project.objects.all()
    output = ', '.join([p.nom_du_projet for p in projects_list])
    return HttpResponse(output)"""
    #return HttpResponse("You're looking list projects")
    projects_list = Project.objects.all()
    return render(request, 'projects.html', {'projects_list': projects_list})


def project_details(request, pId):
    project = get_object_or_404(Project, pk=pId)
    return render(request, 'project_details.html', {'project': project})

    #return HttpResponse("You're looking to the project having ID: {}".format(pId))


def edit_project(request, pId):
    return HttpResponse("You're editing the project having ID: {}".format(pId))

def add_project(request):
    return HttpResponse("You're adding a project")


