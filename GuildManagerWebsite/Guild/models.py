from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


#choices used in the models
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

factions = (
    ('Alliance','Alliance'),
    ('Horde','Horde'),
    )

serverChoices = (
    ('Arugal','Arugal'),
    ('Yojamba','Yojamba'),
    ('Remulos','Remulos'),
    )

# Create your models here.
class guild(models.Model):
    guildName = models.CharField(max_length=50)
    server = models.CharField(max_length=50,choices=serverChoices)
    faction = models.CharField(max_length=50,choices=factions)

    def __str__(self):
        return self.guildName
    def getGuildName(self):
        name = self.guildName
        return name


class character(models.Model):
    characterName = models.CharField(max_length=30)
    characterClass = models.CharField(max_length=50,choices=class_choices)
    characterGuild = models.ForeignKey(guild,on_delete=models.CASCADE,blank=True, null=True)
    characterFaction = models.CharField(max_length=50,choices=factions)
    characterRealm = models.CharField(max_length=50,choices=serverChoices)


    def Guildless(self):
        if self.characterGuild.getGuildName() == "":
            return "Character is unguilded, would you like to join one?"
        else:
            return self.characterGuild

    def __str__(self):
        return f"{self.characterName} - {self.characterFaction} - {self.characterRealm} - {self.characterGuild}"