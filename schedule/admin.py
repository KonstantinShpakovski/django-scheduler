from django.contrib import admin

from schedule.models import Event, Rule, Category


# class CalendarAdminOptions(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     search_fields = ['name']


class EventAdmin(admin.ModelAdmin):
    model = Event
    fields = ('category', 'title', 'description', 'locations', 'admission_price', 'start', 'end', 'rule', 'end_recurring_period')

#admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Rule)
admin.site.register(Event, EventAdmin)
#admin.site.register([Rule, Event, CalendarRelation])
admin.site.register(Category)