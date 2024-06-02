from old_dead_app1.models import Worker, Department, Country
from django.contrib import admin
from django.utils.html import format_html


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'flag_thumbnail')

    def flag_thumbnail(self, obj):
        if obj.flag:
            return format_html('<img src="{}" width="50" height="30" />'.format(obj.flag.url))
        return 'No Image'
    flag_thumbnail.short_description = 'Flag'


# Register your models here.
admin.site.register(Worker)
admin.site.register(Department)
admin.site.register(Country, CountryAdmin)
