from django.contrib import admin

from schedule.models import Calendar, Event, CalendarRelation, Rule


class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']


class EventAdmin(admin.ModelAdmin):
    model = Event
    exclude = ('calendar',)

admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Rule)
admin.site.register(Event, EventAdmin)
#admin.site.register([Rule, Event, CalendarRelation])
