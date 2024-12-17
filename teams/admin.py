from django.contrib import admin
from .models import Team, Player

# Register the Team and Player model in the admin panel.
admin.site.register(Team)
admin.site.register(Player)
