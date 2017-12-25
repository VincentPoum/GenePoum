from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from genepoum.views import *

urlpatterns = [
    url(r'^/$', TemplateView.as_view(template_name="about.html")),
    url(r'^individus/$', IndividuList.as_view()),
    url(r'^individu/(?P<pk>[0-9]+)/$', IndividuDetail.as_view(), name='AffIndividu'),
    url(r'^naissance/(?P<pk>[0-9]+)/$', essai_naissance, name='naissance_form'),
#    url(r'^naissance/$', essai_naissance, name='naissance_form'),
]