# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.forms import ModelForm

# Create your views here.

from django.http import HttpResponse

from genepoum.models import *


def index(request):
    return HttpResponse("Genepoum index.")
    

class IndividuList(ListView):
	queryset = Individu.objects.order_by('individu_nom','individu_prenom_usage')
	def get_context_data(self, **kwargs):
		context = super(IndividuList, self).get_context_data(**kwargs)
		liste_noms = context['object_list'].values_list('individu_nom')
		liste = []
		for element in liste_noms : 
			if element[0] not in liste :
				liste.append(element[0])
		liste.sort()
		context['noms_liste'] = liste
		print context
		return context
		

class IndividuDetail(DetailView):
	model = Individu
	def get_context_data(self, **kwargs):
		context = super(IndividuDetail, self).get_context_data(**kwargs)
		le_sexe = context['object'].individu_sexe
		l_id = context['object'].id
		mariage = context['object'].ses_evenements().filter(event_qui_event__event_type__contains='M')
		if mariage.count() > 0 :
			marie_id = mariage.values_list('event_qui_event__id')
			mariage_part = Event_Qui.objects.filter(event_qui_event_id=marie_id)
			if le_sexe == 'F' :
				mariage_part = mariage_part.filter(event_qui_fonction__contains='EPOUX').values_list('event_qui_event__event_date','event_qui_individu__individu_prenom_usage','event_qui_individu__individu_nom','event_qui_individu_id')				
				context['mariage_list'] = mariage_part
			elif le_sexe == 'M' :
				mariage_part = mariage_part.filter(event_qui_fonction__contains='EPOUSE').values_list('event_qui_event__event_date','event_qui_individu__individu_prenom_usage','event_qui_individu__individu_nom','event_qui_individu_id')					
				context['mariage_list'] = mariage_part
		enfants = context['object'].ses_enfants()
		enfants = enfants.filter(event_qui__event_qui_fonction__contains='BEBE').order_by('event_qui__event_qui_event__event_date')
		enfants = enfants.values_list('id','individu_prenom_usage','event_qui__event_qui_event__event_date')
		nb_enfants = enfants.count()
		# pour une disposition équilibrée
		if nb_enfants > 8 :
			nb_enfants = 6
		context['les_enfants'] = enfants
		context['nb_enfants'] = nb_enfants
		print le_sexe,l_id,mariage,'---',context
		return context


class NaissanceView(CreateView):
    model = Individu
    template_name = 'naissance.html'
    fields = ['individu_sexe','individu_nom','individu_prenom_usage','individu_pere','individu_mere','event_qui__event_qui_fonction']
