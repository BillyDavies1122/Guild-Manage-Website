from django.contrib import admin

from .models import guild,character,instance

# Register your models here.
admin.site.register(guild)
admin.site.register(character)
admin.site.register(instance)