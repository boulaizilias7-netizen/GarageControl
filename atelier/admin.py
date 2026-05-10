from django.contrib import admin
from .models import Vehicule, TypePanne, Reparation

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'marque', 'modele', 'proprietaire')
    search_fields = ('immatriculation', 'proprietaire')

@admin.register(Reparation)
class ReparationAdmin(admin.ModelAdmin):
    
    list_display = ('vehicule', 'type_panne', 'date_reparation', 'cout_pieces', 'cout_main_oeuvre', 'est_validee')
    
    list_filter = ('type_panne', 'est_validee', 'date_reparation')
   
    search_fields = ('vehicule__immatriculation',)
    
    list_editable = ('est_validee',) 

admin.site.register(TypePanne)

