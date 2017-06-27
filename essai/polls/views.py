# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

# le raccourci render remplace
# from django.http import HttpResponse
# from django.template import loader
# le raccourci get_object_or_404 remplace
# from django.http import Http404
# par
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# le raccourci render remplace
	# template = loader.get_template('polls/index.html')
	# context = { 'latest_question_list':latest_question_list, }
	# return HttpResponse(template.render(context, request))
	# par
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	
	
def detail(request, question_id):
	# le raccourci get_object_or_404 remplace
	# try:
	#	 question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	 raise Http404("Le sondage n'existe pas")
	# par
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
	
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
	
	
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
