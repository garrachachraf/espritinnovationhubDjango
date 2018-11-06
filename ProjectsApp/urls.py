from django.urls import path, re_path

from ProjectsApp.api_urls import api_urlpatterns
from ProjectsApp.views import ProjectDetailView
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('projects/', views.ProjectsListView.as_view(), name='liste'),
    #path('projects/<int:pId>/', views.project_details, name='details'),
    re_path(r'^projects/(?P<pId>[0-9]+)/edit/$', views.edit_project, name='edit'),
    re_path(r'^projects/(?P<p_id>[0-9]+)/edit/submit$', views.submit_edition_project, name='submit_edition'),
    re_path(r'^projects/create/$', views.add_project, name='create'),
    re_path(r'^projects/(?P<pk>[0-9]+)/$', ProjectDetailView.as_view(), name='details'),
    re_path(r'^authentificate/$', views.authenticate_user, name='authentificate'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^projects/(?P<project_id>[0-9]+)/join/$', views.join_project, name='p_join'),
    re_path(r'^projects/(?P<project_id>[0-9]+)/validate/$', views.validate_project, name='p_validate'),

]

urlpatterns += api_urlpatterns

