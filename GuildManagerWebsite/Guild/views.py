from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    
    return HttpResponse("Hello world. You are in the guild index")

def search(request):
    return HttpResponse("This is the search page")



def characterIndex(request):
    characterList = character.objects.all()
    template = loader.get_template('characters/index.html')
    context = {
        'characterList': characterList,
        }

    return HttpResponse(template.render(context,request))

def characterPage(request,characterId):

    characterList = character.objects.filter(id=characterId)
    template = loader.get_template('characters/characterPage.html')
    context = {
        'characterList': characterList,
        }
    return HttpResponse(template.render(context,request))

def guildIndex(request):
    guildList = guild.objects.all()
    template = loader.get_template('guilds/index.html')
    context = {
        'guildList': guildList,
        }

    return HttpResponse(template.render(context,request))

def guildPage(request,guildId):
    guildList = guild.objects.filter(id=guildId)
    template = loader.get_template('guilds/guildPage.html')
    context = {
        'guildList': guildList,
        }

    return HttpResponse(template.render(context,request))