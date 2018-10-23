from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from ProjectsApp.forms import AddProjectForm
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
    if request.method == "GET":
        form = AddProjectForm()
        return render(request, 'add_project.html', {'form': form})
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            postProject = form.save(commit=False)
            postProject.save()
            return HttpResponseRedirect(reverse('liste'))
        else:
            return render(request, 'add_project.html', {'msg_erreur': 'Erreur lors de la création du projet'})




