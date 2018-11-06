from django.test import TestCase
from .models import *


class ProjectModelTest(TestCase):
    def time_allocated_time(self):
        new_project = Project(nom_du_projet="Test",
                              temps_alloue_par_le_createur=3,
                              besoins="test",
                              description="Test de description du projet",
                              createur= Student.objects.first()
                              )
        self.assertIs(new_project.superviseur, None)
        self.assertIs(new_project.est_valide, False)
