from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum


def is_esprit_email(value):
    """
    Tests if An Email Ends with @esprit.tn
    """
    if str(value).endswith("@esprit.tn") == False:
        raise ValidationError( 'Votre Email doit être @Esprit.tn',params={'value': value})


class Student(models.Model):
    nom = models.CharField('Prénom', max_length=30)
    prenom = models.CharField('Nom',max_length=30)
    email = models.EmailField('Email', validators=[is_esprit_email])

    def __str__(self):
        return self.nom


class Coach(models.Model):
    nom = models.CharField('Prénom', max_length=30)
    prenom = models.CharField('Nom', max_length=30)
    email = models.EmailField('Email', validators=[is_esprit_email])

    def __str__(self):
        return self.nom


class Project(models.Model):
    nom_du_projet = models.CharField('Titre du projet', max_length=30)
    duree_du_projet = models.IntegerField('Durée estimée', default=0)
    temps_alloue_par_le_createur = models.IntegerField('Temps alloué',validators=[MinValueValidator(1), MaxValueValidator(10)])
    besoins = models.TextField(max_length=250)
    description = models.TextField(max_length=250)

    # Validation State of the project
    est_valide = models.BooleanField(default=False)

    createur = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )

    superviseur = models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='project_coach'
    )

    membres = models.ManyToManyField(
        Student,
        through='MembershipInProject',
        # added to differ with the lead relation
        related_name='les_membres',
        blank=True,
    )

    def total_allocated_by_members(self):
        list_members_in_p = MembershipInProject.objects.filter(projet=self.pk)
        sum_invested_by_members = list_members_in_p.all().aggregate(Sum('time_allocated_by_member'))
        # Utiliser Aggregate pour regroupe les valeurs à aggrégé dans un dictionnaire
        return sum_invested_by_members['time_allocated_by_member__sum'] or 0
        # Récupération de la valeur à partir du dictionnnaire

    def __str__(self):
        return self.nom_du_projet



class MembershipInProject(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_allocated_by_member = models.IntegerField('Temps alloué par le membre')

    def __str__(self):
        return 'Membre ' + self.etudiant.nom

    class Meta:
        unique_together = ("projet", "etudiant")
    #Exhaustive list about Metaclasses https://docs.djangoproject.com/en/1.11/ref/models/options/

















