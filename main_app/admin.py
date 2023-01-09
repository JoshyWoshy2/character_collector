from django.contrib import admin
from .models import Character, Healing, Weapon

# Register your models here.
admin.site.register(Character)
admin.site.register(Healing)
admin.site.register(Weapon)