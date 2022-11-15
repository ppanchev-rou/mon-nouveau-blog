from django.contrib import admin
from .models import Billet

##Pour ajouter, modifier et supprimer les billets que nous venons de créer,
# nous allons utiliser l'interface Django admin.
admin.site.register(Billet)