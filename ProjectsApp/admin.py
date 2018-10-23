from django.contrib import admin
from .models import Student, Project, Coach, MembershipInProject


# Register your models here.

class MembershipInline(admin.TabularInline):
    model = MembershipInProject
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom_du_projet', 'duree_du_projet', 'description','est_valide', 'createur', 'total_allocated_by_members')
    actions = ['set_to_valid']
    inlines = (MembershipInline,)

    fieldsets = (
        ('Etat', {'fields': ('est_valide',)}),
        ('A propos', {
            'fields': ('nom_du_projet', ('createur', 'superviseur'), 'besoins', 'description',),
        }),
        ('Durées', {
            'fields': (('duree_du_projet', 'temps_alloue_par_le_createur'),)
        }),
    )

    list_filter = ('createur',)
    search_fields = ['nom_du_projet', 'createur__nom']


    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)
    set_to_valid.short_description = "Valider"


class CoachAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    fields = (('nom', 'prenom'), 'email')
    ordering = ['prenom']

admin.site.register(Coach)
admin.site.register(Student)
admin.site.register(Project, ProjectAdmin)