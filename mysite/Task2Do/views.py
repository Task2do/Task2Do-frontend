from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader



def index(request):
    projects_list ={"project1":{"task1":150,"task2":124},"project1":{"task1":130,"task2":134}}
    template = loader.get_template("Task2Do/index.html")
    context = {
        "projects_list": projects_list,
    }
    return HttpResponse(template.render(context, request))