from django.views.generic import TemplateView

# 1. Create your views from the prospective HTML files here to have a class that can be imported by urls.py


class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
