from django.urls import path

from . import views


urlpatterns = [
    path("search",views.search,name="search"),
    path("searchResults",views.searchResults,name="searchResults"),

    path("guildIndex/",views.guildIndex,name="guildIndex"),
    path("<int:guildId>/guild",views.guildPage,name="guildPage"),

    path("characterIndex/",views.characterIndex,name="characterIndex"),
    path("<int:characterId>/character",views.characterPage,name="characterPage"),

    path('instances/', views.instance_list, name='instance_list'),
    ]