from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('projects/', views.list_projects, name='liste'),
    path('projects/<int:pId>/', views.project_details, name='details')
]
