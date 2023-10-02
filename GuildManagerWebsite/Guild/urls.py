from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("search",views.search,name="search"),

    path("guildIndex/",views.guildIndex,name="guildIndex"),
    path("<int:guildId>/guild",views.guildPage,name="guildPage"),

    path("characterIndex/",views.characterIndex,name="characterIndex"),
    path("<int:characterId>/character",views.characterPage,name="characterPage")
    ]