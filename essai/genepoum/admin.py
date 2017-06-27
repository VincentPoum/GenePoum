# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Individu, Event, Event_Qui, Foyer, Domicile



class Participant(admin.TabularInline):
	model = Event_Qui
	extra = 0
	
class EventAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': (('event_type','event_date'),'event_comment')}),
	]
	inlines = [Participant]
	ordering = ['event_date']
	

admin.site.register(Event,EventAdmin)

class Evenement(admin.TabularInline):
	model = Event
	extra = 0
	
class IndividuAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nom', {'fields': (('individu_nom','individu_prenom_usage','individu_sexe'),'individu_prenom_supp')}), 
		('Parents', {'fields': (('individu_pere','individu_mere'),)}),
		('Commentaires', {'fields': ['individu_comment']}),
	]
	inlines = [Participant]
	list_display = ('individu_nom', 'individu_prenom_usage', 'ses_evenements', 'ses_enfants')
	list_filter = ['individu_nom']
	
admin.site.register(Individu,IndividuAdmin)

admin.site.register(Foyer)

admin.site.register(Domicile)
	