from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

# Create your views here.

def main(request):
    template = loader.get_template("main.html")

    context = {
        "featuredProjects" : Project.objects.filter(projectFeatured=True),
        "extraProjects" : Project.objects.filter(projectFeatured=False)
    }
    return HttpResponse(template.render(context, request))
