from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .models import Reparation, Vehicule, TypePanne
from .forms import ReparationForm, VehiculeForm, TypePanneForm
from django.db.models import F

# --- VUES GÉNÉRALES (Accessibles par tous les utilisateurs connectés) ---

@login_required
def home(request):
    """Page d'accueil du GarageControl."""
    return render(request, 'atelier/index.html')

@login_required
def liste_reparations(request):
    # On crée un champ temporaire "total" qui fait le même calcul que ta fonction
    reparations = Reparation.objects.annotate(
        total=F('cout_pieces') + F('cout_main_oeuvre')
    ).order_by('-date_reparation')

    query = request.GET.get('q')
    prix_min = request.GET.get('prix_min')

    # Recherche par plaque
    if query:
        reparations = reparations.filter(vehicule__immatriculation__icontains=query)

    # Recherche par prix (ton erreur jaune disparaîtra ici)
    if prix_min:
        reparations = reparations.filter(total__gte=prix_min)

    return render(request, 'atelier/liste_reparations.html', {'reparations': reparations})

@login_required
def liste_vehicules(request):
    """Affiche la liste des véhicules enregistrés[cite: 15]."""
    vehicules = Vehicule.objects.all()
    return render(request, 'atelier/vehicules.html', {'vehicules': vehicules})

@login_required
def planning_ponts(request):
    """Planification : suit la durée des travaux non validés."""
    reparations_actives = Reparation.objects.filter(est_validee=False).order_by('date_reparation')
    return render(request, 'atelier/planning.html', {'reparations': reparations_actives})


# --- VUES MÉCANICIEN ET ADMIN (Ajout et Modification) ---

@login_required
@permission_required('atelier.add_reparation', raise_exception=True)
def ajouter_reparation(request):
    """Enregistre une nouvelle intervention[cite: 7]."""
    if request.method == "POST":
        form = ReparationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_reparations')
    else:
        form = ReparationForm()
    return render(request, 'atelier/ajouter_reparation.html', {'form': form})

@login_required
@permission_required('atelier.change_reparation', raise_exception=True)
def modifier_reparation(request, pk):
    """Saisit les coûts et détails techniques[cite: 8]."""
    reparation = get_object_or_404(Reparation, pk=pk)
    if request.method == "POST":
        form = ReparationForm(request.POST, instance=reparation)
        if form.is_valid():
            form.save()
            return redirect('liste_reparations')
    else:
        form = ReparationForm(instance=reparation)
    return render(request, 'atelier/modifier_reparation.html', {'form': form, 'reparation': reparation})

@login_required
@permission_required('atelier.add_vehicule', raise_exception=True)
def ajouter_vehicule(request):
    """Enregistre un nouveau véhicule à l'arrivée[cite: 7, 15]."""
    if request.method == "POST":
        form = VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_vehicules')
    else:
        form = VehiculeForm()
    return render(request, 'atelier/ajouter_vehicule.html', {'form': form})

@login_required
@permission_required('atelier.change_vehicule', raise_exception=True)
def modifier_vehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    if request.method == "POST":
        form = VehiculeForm(request.POST, instance=vehicule)
        if form.is_valid():
            form.save()
            return redirect('liste_vehicules')
    else:
        form = VehiculeForm(instance=vehicule)
    return render(request, 'atelier/modifier_vehicule.html', {'form': form, 'vehicule': vehicule})


# --- VUES RÉSERVÉES AU CHEF D'ATELIER (ADMIN) ---

@login_required
@user_passes_test(lambda u: u.is_superuser)
def supprimer_reparation(request, pk):
    """Seul l'admin peut supprimer une intervention."""
    reparation = get_object_or_404(Reparation, pk=pk)
    if request.method == "POST":
        reparation.delete()
        return redirect('liste_reparations')
    return render(request, 'atelier/confirmer_suppression_reparation.html', {'objet': reparation, 'type': 'la réparation'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def supprimer_vehicule(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    if request.method == "POST":
        vehicule.delete()
        return redirect('liste_vehicules')
    return render(request, 'atelier/confirmer_suppression.html', {'objet': vehicule})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def liste_types_panne(request):
    """L'admin gère les catégories pour les statistiques[cite: 15]."""
    types = TypePanne.objects.all()
    return render(request, 'atelier/types_panne.html', {'types': types})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def ajouter_type_panne(request):
    if request.method == "POST":
        form = TypePanneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_types_panne')
    else:
        form = TypePanneForm()
    return render(request, 'atelier/ajouter_type_panne.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def modifier_type_panne(request, pk):
    type_p = get_object_or_404(TypePanne, pk=pk)
    if request.method == "POST":
        form = TypePanneForm(request.POST, instance=type_p)
        if form.is_valid():
            form.save()
            return redirect('liste_types_panne')
    else:
        form = TypePanneForm(instance=type_p)
    return render(request, 'atelier/ajouter_type_panne.html', {'form': form, 'type_p': type_p})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def supprimer_type_panne(request, pk):
    type_p = get_object_or_404(TypePanne, pk=pk)
    if request.method == "POST":
        type_p.delete()
        return redirect('liste_types_panne')
    return render(request, 'atelier/confirmer_suppression_panne.html', {'objet': type_p, 'type': 'la catégorie'})