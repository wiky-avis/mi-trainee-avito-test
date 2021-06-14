from django.contrib import admin

from .models import Choice, Poll


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['description']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)


