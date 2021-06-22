from django.contrib import admin
from gaokao.models import ProfessInformation, ArtInformation, SportsInformation
# Register your models here.

admin.site.register(ProfessInformation)
admin.site.register(ArtInformation)
admin.site.register(SportsInformation)

class ProfessInformationAdmin(admin.ModelAdmin):
    # fields = ('parea', 'pschool', 'pprofess_name', 'psubject')
    list_display =  ('parea', 'pschool', 'pprofess_name', 'psubject')
    search_fields = ('parea', 'pschool')
    list_per_page = 10
    fieldsets = (
        ['Main', {
            'fields': ('parea', 'pschool'),
        }],
        ['advance', {
            'classes': ('collapse',),
            'fields': ('psubject',),
        }]
    )