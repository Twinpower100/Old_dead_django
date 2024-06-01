from django.contrib import admin

from old_dead_app1.models import Worker, Department, Country

# Register your models here.
admin.site.register(Worker)
admin.site.register(Department)
admin.site.register(Country)
