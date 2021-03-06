# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Domicile(models.Model):
	domicile_adresse = models.CharField(max_length=40)
	domicile_gps = models.CharField(max_length=100,blank=True)
	domicile_description = models.CharField(max_length=100,blank=True)
	domicile_comment = models.TextField(blank=True)
	def __str__(self):
		return self.domicile_adresse



@python_2_unicode_compatible  # only if you need to support Python 2
class Event(models.Model):
	NAISSANCE = 'N'
	BAPTEME = 'B'
	MARIAGE = 'M'
	DECES = 'D'
	SEPULTURE = 'S'
	AUTRE = 'X'
	TYPE_LISTE =(
		(NAISSANCE, 'Naissance'),
		(BAPTEME, 'Baptème'),
		(MARIAGE, 'Mariage'),
		(DECES, 'Décès'),
		(SEPULTURE, 'Sépulture'),
		(AUTRE,'Autre'),
	)
	event_date = models.CharField(max_length=40)
	event_type = models.CharField(max_length=1, choices=TYPE_LISTE, default=AUTRE)
	event_lieu = models.ForeignKey(Domicile, blank=True, null=True)
	event_comment= models.TextField(blank=True)
	def __str__(self):
		return self.event_type+' '+self.event_date



# Un individu est caractérisé par son sexe, son nom et ses prénoms.
# Tout le reste n'est qu'évènement ou documents (photos, ...)

@python_2_unicode_compatible  # only if you need to support Python 2
class Individu(models.Model):
	MASCULIN = 'M'
	FEMININ = 'F'
	AUTRE = 'X'
	SEXE_LISTE =(
		(MASCULIN, 'Masculin'),
		(FEMININ, 'Féminin'),
		(AUTRE,'Autre'),
	)
	individu_sexe = models.CharField(max_length=1, choices=SEXE_LISTE, default=AUTRE)
	individu_nom = models.CharField(max_length=50)
	individu_prenom_usage = models.CharField(max_length=25,blank=True)
	individu_prenom_supp = models.TextField(blank=True)
	individu_pere = models.ForeignKey("self", blank=True, null=True, related_name="pere")
	individu_mere = models.ForeignKey("self", blank=True, null=True, related_name="mere")
	individu_comment= models.TextField(blank=True)
	def __str__(self):
		return str(self.id)+' '+self.individu_nom+' '+self.individu_prenom_usage+' '+self.naissance()
	def ses_evenements(self):
		ses_evenements = self.event_qui_set.values_list('id','event_qui_fonction','event_qui_event__event_type','event_qui_event__event_date')
		return ses_evenements
	def naissance(self):
		qs_naissance = self.ses_evenements().filter(event_qui_fonction__contains='BEBE').values_list('event_qui_event__event_date')
		nb_naissance = qs_naissance.count()
		if nb_naissance == 0 :
			naissance = ' en ?'			
		elif nb_naissance > 1 :
			qs_naissance = qs_naissance.filter(event_qui_event__event_type__contains='N')
			# à noter dans le journal des incohérences
			naissance=qs_naissance.get()[0]
		else :
			naissance=qs_naissance.get()[0]
		return naissance
	def ses_enfants(self):
		if self.individu_sexe == 'F' :
#			ses_enfants = self.ses_evenements().filter(event_qui_fonction__contains='mere').order_by('event_qui_event__event_date')
			ses_enfants = Individu.objects.filter(individu_mere=self.id)
		elif self.individu_sexe == 'M' :
#			ses_enfants = self.ses_evenements().filter(event_qui_fonction__contains='pere').order_by('event_qui_event__event_date')
			ses_enfants = Individu.objects.filter(individu_pere=self.id)
		return ses_enfants
	class Meta:
		ordering = ['individu_nom','individu_prenom_usage']
		
		

@python_2_unicode_compatible  # only if you need to support Python 2
class Event_Qui(models.Model):
	BEBE = 'BEBE'
	BAPTISE = 'BAPTISE'
	EPOUSE = 'EPOUSE'
	EPOUX = 'EPOUX'
	MERE = 'MERE'
	PERE = 'PERE'
	ENFANT = 'ENFANT'
	FRERE = 'FRERE'
	SOEUR = 'SOEUR'
	COUSIN = 'COUSIN'
	FAMILLE = 'FAMILLE'
	TEMOIN = 'TEMOIN'
	NOTAIRE = 'NOTAIRE'
	MAIRE = 'MAIRE'
	CURE = 'CURE'
	MORT = 'MORT'
	AUTRE = 'AUTRE'
	FONCTION_LISTE =(
		(BEBE, 'Bébé (réservé à la naissance)'),
		(BAPTISE, 'Baptisé'),
		(EPOUSE, 'Epouse'),
		(EPOUX, 'Epoux'),
		(MERE, 'Mère'),
		(PERE, 'Père'),
		(ENFANT, 'Enfant'),
		(FRERE, 'Frère'),
		(SOEUR, 'Soeur'),
		(COUSIN, 'Cousin'),
		(FAMILLE, 'Membre de la famille'),
		(TEMOIN, 'Témoin'),
		(NOTAIRE, 'Notaire'),
		(MAIRE, 'Maire'),
		(CURE, 'Curé'),
		(MORT, 'Mort'),
		(AUTRE, 'AUTRE'),
	)
	event_qui_event = models.ForeignKey(Event)
	event_qui_individu = models.ForeignKey(Individu)
	event_qui_fonction = models.CharField(max_length=100, choices=FONCTION_LISTE, default=AUTRE)
	event_qui_comment = models.TextField(blank=True)
	def __str__(self):
		return self.event_qui_event.event_type



@python_2_unicode_compatible  # only if you need to support Python 2
class Foyer(models.Model):
	foyer_domicile = models.ForeignKey(Domicile)
	foyer_periode = models.CharField(max_length=40)
	foyer_individu = models.ForeignKey(Individu)
	foyer_fonction = models.CharField(max_length=100,blank=True)
	foyer_comment = models.TextField(blank=True)
	def __str__(self):
		return self.foyer_domicile.adresse+' '+self.foyer_periode
		


