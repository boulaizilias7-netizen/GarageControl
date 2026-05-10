from django.db import models

class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, unique=True)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    proprietaire = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.immatriculation} ({self.modele})"

class TypePanne(models.Model):
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle

class Reparation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_panne = models.ForeignKey(TypePanne, on_delete=models.SET_NULL, null=True)
    panne = models.TextField()
    cout_pieces = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cout_main_oeuvre = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duree_estimee = models.DurationField(help_text="Format: HH:MM:SS") 
    date_reparation = models.DateField()
    est_validee = models.BooleanField(default=False) 

    def total_cost(self):
        return self.cout_pieces + self.cout_main_oeuvre

    def __str__(self):
        return f"Réparation {self.vehicule.immatriculation} - {self.date_reparation}"