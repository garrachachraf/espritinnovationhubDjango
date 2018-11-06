# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers, permissions

from .models import Project, Student, Coach

"""
Les classes de sérialisation pour User, Student, Project et Coach
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'is_staff')


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    project_owner = serializers.PrimaryKeyRelatedField(many=False,
                                                       queryset=Project.objects.all())
    user = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ('project_owner','user')


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Coach
        fields = ('user',)

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    createur = serializers.PrimaryKeyRelatedField(many=False,
                                                  allow_empty=True,
                                                  queryset=Student.objects.all())
    superviseur = serializers.PrimaryKeyRelatedField(many=False,
                                                     allow_null=True,
                                                     queryset=Coach.objects.all())


    #Call Student Serializer to Get members
    membres = StudentSerializer(read_only=True, many=True)
    class Meta:
        model = Project
        fields = ('nom_du_projet',
                  'temps_alloue_par_le_createur',
                  'createur',
                  'superviseur',
                  'membres')










