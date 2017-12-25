# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.forms import ModelForm, modelformset_factory


# Create your views here.

from django.http import HttpResponse

from genepoum.models import *
from genepoum.forms import *


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


class Naissance(DetailView):
	model = Individu
	template_name = "naissance_form.html"
	def get_context_data(self, **kwargs):
		context = super(Naissance, self).get_context_data(**kwargs)
		le_sexe = context['object'].individu_sexe
		print '-Naissance-',le_sexe
		return context
		

def essai_naissance(request, pk):
	NEFormSet = modelformset_factory(Event, form = NaissanceEventForm, extra = 0)
	NIFormSet = modelformset_factory(Individu, form = NaissanceIndividuForm, extra = 0)
	if request.method == 'POST':
		neformset = NEFormSet(request.POST)
		niformset = NIFormSet(request.POST)
		if neformset.is_valid() and niformset.is_valid() :
			# do something with the formset.cleaned_data
			print 'Essai-Naissance post'
			pass
	else:
		qs = Individu.objects.filter(id=pk)
		personne = Individu.objects.get(id=pk)
		la_personne = personne.individu_prenom_usage+' '+personne.individu_nom
#		qs_naissance = personne.event_qui_set.filter(event_qui_fonction__contains='BEBE').values_list('event_qui_event__event_date','event_qui_event__event_type')
		id_naissance = personne.event_qui_set.filter(event_qui_fonction__contains='BEBE').values_list('event_qui_event__id')
		qs_naissance = Event.objects.filter(id=id_naissance)
		niformset = NIFormSet(queryset=qs)
		neformset = NEFormSet(queryset=qs_naissance)
		print '>>>>>>>',qs,qs_naissance
		print niformset
		print neformset

	return render(request, 'naissance_form.html', {'neformset': neformset , 'niformset': niformset, 'la_personne':la_personne})
	