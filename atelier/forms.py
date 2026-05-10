from django import forms
from .models import Reparation,Vehicule,TypePanne 

class ReparationForm(forms.ModelForm):
    class Meta:
        model = Reparation
        # On liste les champs que le mécanicien doit remplir
        fields = ['vehicule', 'type_panne', 'panne', 'cout_pieces', 'cout_main_oeuvre', 'duree_estimee', 'date_reparation']
        # Ce petit bout de code ajoute un calendrier pour la date
        widgets = {
            'date_reparation': forms.DateInput(attrs={'type': 'date'}),
        }


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatriculation', 'marque', 'modele', 'proprietaire']

class TypePanneForm(forms.ModelForm):
    class Meta:
        model = TypePanne
        fields = ['libelle']