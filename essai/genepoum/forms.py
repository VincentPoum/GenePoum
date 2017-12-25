from django import forms
from django.forms import formset_factory
from genepoum.models import *

class NaissanceEventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('event_date','event_type')

class NaissanceIndividuForm(forms.ModelForm):
	class Meta:
		model = Individu
		fields = ('individu_pere','individu_mere')

