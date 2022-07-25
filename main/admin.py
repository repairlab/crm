from django.contrib import admin

from .models import Lid
from .models import Manager
from .models import Status
from .models import Theme
from .models import Region
from .models import Reception
from .models import RukManager
from .models import Istochnik


class LidAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'region', 'vopros', 'comment', 'manager','theme','status','reception','rukmanager', 'datecreate','istochnik', 'datezapisi')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'region', 'number','manager','region','status','rukmanager','istochnik',)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id','name','region')
    list_display_links = ('id', 'name')
    search_fields = ('name','region',)
    
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','status')
    list_display_links = ('id', 'status')
    search_fields = ('status',)
    
class IstochnikAdmin(admin.ModelAdmin):
    list_display = ('id','istochnik')
    list_display_links = ('id', 'istochnik')
    search_fields = ('istochnik',)
    
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id','theme')
    list_display_links = ('id', 'theme')
    search_fields = ('theme',)
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','region')
    list_display_links = ('id', 'region')
    search_fields = ('region',)
    
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('id','name','region')
    list_display_links = ('id', 'name')
    search_fields = ('name','region',)

class RukManagerAdmin(admin.ModelAdmin):
    list_display = ('id','name','region')
    list_display_links = ('id', 'name')
    search_fields = ('name','region',)
    
admin.site.register(Lid, LidAdmin)
admin.site.register(Istochnik, IstochnikAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Reception, ReceptionAdmin)
admin.site.register(RukManager, RukManagerAdmin)
