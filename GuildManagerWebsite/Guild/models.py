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

instanceType = (
    ('10', '10'),
    ('25', '25'),
    ('Dungeon','Dungeon'),
    ('Heroic','Heroic'),
    ('Mythic', 'Mythic'),
    ('Mythic+', 'Mythic+'),
    ('Mythic++', 'Mythic++'),
    ('Mythic+++', 'Mythic+++'),
    ('Mythic++++', 'Mythic++++')
)

bossesICC = (
    (0,"Lord Marrowgar"),
    (1,"Lady Deathwhisper"),
    (2,"Gunship Battle"),
    (3,"Deathbringer Saurfang"),
    (4,"Festergut"),
    (5,"Rotface"),
    (6,"Professor Putricide"),
    (7,"Blood Prince Council"),
    (8,"Blood-Queen Lana'thel"),
    (9,"Valithria Dreamwalker"),
    (10,"Sindragosa"),
    (11,"The Lich King")
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
    
class instance(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    instance_type = models.CharField(max_length=20, choices=instanceType)
    description = models.TextField()

    def __str__(self):
        return f"{self.short_name}({self.instance_type})"

class instanceBoss(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    instance = models.ForeignKey('instance', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}({self.instance})"
    
    def GetInstance(self):
        return self.instance


class instanceLoot(models.Model):
    item_name = models.CharField(max_length=50)
    item_type = models.CharField(max_length=20)
    item_level = models.IntegerField()
    raid = models.ForeignKey('instance', on_delete=models.CASCADE)
    boss = models.ForeignKey('instanceBoss', on_delete=models.CASCADE)
    wowhead_link = models.URLField(null=False)

    def __str__(self):
        return f"{self.item_name} - {self.item_type} (item level: {self.item_level})"
    
    def getLink(self):
        return self.wowhead_link
