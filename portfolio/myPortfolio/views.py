from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Skill
from .models import Project

# Create your views here.

def main(request):
    template = loader.get_template("main.html")

    context = {
        "frontEndSkills" : Skill.objects.filter(skillSet="Front End"),
        "backEndSkills" : Skill.objects.filter(skillSet="Back End"),
        "databaseSkills" : Skill.objects.filter(skillSet="Database"),
        "toolTechSkills" : Skill.objects.filter(skillSet="ToolTech"),
        "featuredProjects" : Project.objects.filter(projectFeatured=True),
        "extraProjects" : Project.objects.filter(projectFeatured=False)
    }
    return HttpResponse(template.render(context, request))
