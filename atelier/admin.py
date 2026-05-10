from django.contrib import admin
from .models import Vehicule, TypePanne, Reparation

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'marque', 'modele', 'proprietaire')
    search_fields = ('immatriculation', 'proprietaire')

@admin.register(Reparation)
class ReparationAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('vehicule', 'type_panne', 'date_reparation', 'cout_pieces', 'cout_main_oeuvre', 'est_validee')
    # Filtres sur le côté (Type de panne et état de validation) [cite: 9]
    list_filter = ('type_panne', 'est_validee', 'date_reparation')
    # Recherche par immatriculation [cite: 9]
    search_fields = ('vehicule__immatriculation',)
    # Permet de valider directement depuis la liste
    list_editable = ('est_validee',) 

admin.site.register(TypePanne)
# Register your models here.
