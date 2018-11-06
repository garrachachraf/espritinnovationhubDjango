from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from ProjectsApp import api_views


"""
Usage de la classe Router pour une affectation des URL
Ceci est possible avec l'usage des ViewSets
"""
router = DefaultRouter()
router.register(r'api/usersSet', api_views.UserViewSet)

api_urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^api/users/$', api_views.users_list)
    #url(r'^api/users/$', api_views.UserList.as_view()),
    #url(r'^api/users/(?P<pk>[0-9]+)/$', api_views.UserDetail.as_view()),
    url(r'^api/students/$', api_views.StudentList.as_view()),
    url(r'^api/students/(?P<pk>[0-9]+)/$', api_views.StudentDetail.as_view()),
    url(r'^api/projects/$', api_views.ProjectList.as_view()),
    url(r'^api/projects/(?P<pk>[0-9]+)/$', api_views.ProjectDetail.as_view()),
]

api_urlpatterns += [
    url(r'^api/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]