from django.contrib import admin
from .models import Pumps, Groups, GroupsPumps, Status, PumpStatus 

class GroupPumpsInline(admin.StackedInline):
	model = GroupsPumps
	extra = 1

class GroupAdmin(admin.ModelAdmin):
	inlines = [GroupPumpsInline]
	list_display = ["name"]


class PumpStatusAdmin(admin.ModelAdmin):
    list_display = ( 'pumps', 'status', 'last_updated')


admin.site.register(Pumps)
admin.site.register(Groups, GroupAdmin)
admin.site.register(GroupsPumps)
admin.site.register(Status)
admin.site.register(PumpStatus, PumpStatusAdmin)
