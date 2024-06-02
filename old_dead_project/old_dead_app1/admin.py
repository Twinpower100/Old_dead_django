from old_dead_app1.models import Worker, Department, Country
from django.contrib import admin
from django.utils.html import format_html


class CountryAdmin(admin.ModelAdmin):
    """Здесь мы делаем так, чтобы не ссылки на флаги, а сами флаги (изображения из директории ./media/flags)
    выводились рядом со странами в админке
    Объяснение кода
    Метод flag_thumbnail: Этот метод используется для создания HTML-кода, который отображает миниатюру флага.
    Метод format_html безопасно форматирует строку как HTML.
    list_display: Добавляет flag_thumbnail к списку полей, отображаемых в админке.
    short_description: Устанавливает заголовок колонки в админке."""

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
