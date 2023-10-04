from decimal import Context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader , RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.



def search(request):
    template = loader.get_template('search/searchPage.html')
    





    return HttpResponse(template.render())

@csrf_exempt
def searchResults(request):
    template = loader.get_template('search/results.html')
    '''
    Gets search bar from user
    Validates the input

    Searches through characters & guilds
    Returns both and displays both
    allows them to go directly to those specific pages
    '''
    userSearch = request.POST.get('search','')
    context ={
        'userSearch': userSearch
    }

    return HttpResponse(template.render(context,request))


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