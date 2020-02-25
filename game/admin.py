from django.contrib import admin
from .models import Session,Policy,Building,LeftTerritory,RightTerritory,CenterTerritory


admin.site.register(Session)
admin.site.register(Policy)
admin.site.register(Building)
admin.site.register(LeftTerritory)
admin.site.register(RightTerritory)
admin.site.register(CenterTerritory)
# Register your models here.
