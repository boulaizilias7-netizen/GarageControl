from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reparations/', views.liste_reparations, name='liste_reparations'),
    path('reparation/ajouter/', views.ajouter_reparation, name='ajouter_reparation'),
    path('reparation/modifier/<int:pk>/', views.modifier_reparation, name='modifier_reparation'),
    path('reparation/supprimer/<int:pk>/', views.supprimer_reparation, name='supprimer_reparation'),
    path('planning/', views.planning_ponts, name='planning_ponts'), # On pointe vers home en attendant
    path('vehicules/', views.liste_vehicules, name='liste_vehicules'),
    path('vehicule/ajouter/', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('vehicule/<int:pk>/modifier/', views.modifier_vehicule, name='modifier_vehicule'),
    path('vehicule/<int:pk>/supprimer/', views.supprimer_vehicule, name='supprimer_vehicule'),
    path('types/', views.liste_types_panne, name='liste_types_panne'),
    path('types/ajouter/', views.ajouter_type_panne, name='ajouter_type_panne'),
    path('types/modifier/<int:pk>/', views.modifier_type_panne, name='modifier_type_panne'),
    path('types/supprimer/<int:pk>/', views.supprimer_type_panne, name='supprimer_type_panne'),
]