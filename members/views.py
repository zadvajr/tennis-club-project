from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Member

# Create your views here.
def home(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))

def details(request, pk):
    mymember = Member.objects.get(pk=pk)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember
    }
    return HttpResponse(template.render(context, request))

def testing(request):
    mydata = Member.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        "mymembers": mydata,
    }

    return HttpResponse(template.render(context, request))