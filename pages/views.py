from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePagesView(TemplateView):
    template_name = 'home.html'
class WikiPageView(TemplateView):
    template_name = 'wiki.html'
class PicturePageView(TemplateView):
    template_name = 'picuture.html'
class ContactPageView(TemplateView):
    template_name = 'contact.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'