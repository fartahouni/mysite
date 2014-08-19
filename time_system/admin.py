__author__ = 'farzanehtahooni'

from django.contrib import admin

from time_system.models import To_Do , To_Do_Pack


class AdminTo_Do(admin.ModelAdmin):
    list_display = ('title' , 'start_time' , 'end_time' ,)
    # ordering = ('To_Do.objects.all().title',)

admin.site.register(To_Do , AdminTo_Do)
admin.site.register(To_Do_Pack)

