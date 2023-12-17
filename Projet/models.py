from django.db import models
from datetime import datetime

import Projet
from Etudiant.models import Etudiant


class Projet(models.Model):

    type_list = (
        ("w", "web"),
        ("m", "mobile"),
        ("d", "desktop"),
    )

    besoin = models.CharField(max_length=100) #, choices=category_list
    effectif = models.CharField(max_length=100, default='manque')  #, choices=category_list
    type = models.CharField(max_length=100, choices=type_list)
    date_debut = models.DateField(null=True)   #auto_now_add=True
    date_fin = models.DateTimeField(null=True)

    developpeurs = models.ManyToManyField(Etudiant, related_name='developpeurs', through='Developpeur' )
    createur = models.ForeignKey(Etudiant, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.type + " et besoin" + self.besoin

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(date_fin__gt = datetime.now()), name= 'Please check Date fin' )]


class Developpeur(models.Model):
    date_adhesion = models.DateField(null=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, null=True)