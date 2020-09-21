from django.shortcuts import render

# Create your views here.

#step 2: create home view
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name='home.html'# add template



class AboutView(TemplateView):
    template_name='about.html'# add template