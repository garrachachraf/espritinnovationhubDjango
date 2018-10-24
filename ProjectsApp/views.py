from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView

from ProjectsApp.forms import AddProjectForm
from ProjectsApp.models import *


def index(request):
    return render(request, 'index.html')


def list_projects(request):
    projects_list = Project.objects.all()
    return render(request, 'projects.html', {'projects_list': projects_list})


def project_details(request, pId):
    project = get_object_or_404(Project, pk=pId)
    return render(request, 'project_details.html', {'project': project})



def add_project(request):
    #Edit this Method : Only Authenticated users can add a project
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
            return render(request, 'add_project.html',
                          {'msg_erreur': 'Erreur lors de la création du projet',
                           'form':form})


def edit_project(request, pId):
    """
    Methode permettant à un étudiant de éditer son propre projet
    :param request:
    :param p_id:
    :return:
    """
    #edit this method : Only the student can Edit its own project!
    project = get_object_or_404(Project, pk=pId)
    genForm = AddProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': genForm, 'p_id': pId})


def submit_edition_project(request, p_id):
    """
    Méthode pemettant de saouvegarder les modifications apportés par un étudiant
    sur son propre projet
    :param request:
    :param p_id:
    :return:
    """
    project = get_object_or_404(Project, pk=p_id)
    if request.method == 'POST':
        genForm = AddProjectForm(request.POST or None, instance=project)
        if genForm.is_valid():
            genForm.save()
            return HttpResponseRedirect(reverse('liste'))
        else:
            return HttpResponseRedirect(reverse('liste'))
    else:
        return HttpResponseRedirect(reverse('liste'))

class ProjectsListView(generic.ListView):
    """
    Usage de classe générique ListView pour lister les projets
    Redéfinition de la méthode get_queryset afin de restreindre l'accées aux données
    aux utilisateurs authentifiées (Cas de Coach et d'étudiant
    """
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        #Edit this to display:
        # Only valid projects for students
        #All projects for SuperUser
        return Project.objects.all()




class ProjectDetailView(DetailView):
    """
    Usage de la classe générique DetailView pour afficher les détails relatifs à un projet
    Redéfinition de la méthode get_context_data afin d'envoyer une donnée supplémentaire
    dans le contexte qui permet de différencier côté template entre un coach et un étudiant
    """
    model = Project
    template_name = 'project_details.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        project = super(ProjectDetailView, self).get_object()
        context['project'] = project

        #Have to add some code Here!
        return context




def authenticate_user(request):
    """
    Méthode d'authentification d'un utiulisateur à partir du formulaire
    :param request:
    :return:
    """
    # Add the login code here
    return HttpResponseRedirect(reverse('index'))


def logout_view(request):
    """
    Méthode de déconnexion de l'utilisateur
    :param request:
    :return:
    """
    # Add the logout code here
    return HttpResponseRedirect(reverse('index'))


def join_project(request, project_id):
    """
    Méthode permettant à un étudiant de joindre un projet
    :param request:
    :param project_id:
    :return:
    """
    #Add the code for joining project Here
    return HttpResponseRedirect(reverse('liste'))


def validate_project(request, project_id):
    """
    Méthode permettant à un coach ou un superutilisateur de valider un projet
    :param request:
    :param project_id:
    :return:
    """
    #Add the code for validating project here
    return HttpResponseRedirect(reverse('liste'))

