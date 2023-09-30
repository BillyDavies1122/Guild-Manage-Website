from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class_choices = (
    ("Mage","Mage"),
    ("Warrior","Warrior"),
    ("Warlock","Warlock"),
    ("Rogue","Rogue"),
    ("DeathKnight","Death Knight"),
    ("Priest","Priest"),
    ("Hunter","Hunter"),
    ("Shaman","Shaman"),
    ("Paladin","Paladin"),
    ("Druid","Druid"),
    )


class guild(models.Model):
    guildName = models.CharField(max_length=50)

    def __str__(self):
        return self.guildName


class character(models.Model):
    characterName = models.CharField(max_length=30)
    characterClass = models.CharField(max_length=50,choices=class_choices)
    characterGuild = models.ForeignKey(guild,on_delete=models.CASCADE)

    def Guildless(self):
        if self.characterGuild == " ":
            return "Character is unguilded, would you like to join one?"
        else:
            return self.characterGuild

    def __str__(self):
        return f"Character is called {self.characterName} and is a member of {self.characterGuild}"