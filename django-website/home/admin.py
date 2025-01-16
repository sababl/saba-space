from django.contrib import admin
from .models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'about')
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name')
        }),
        ('Content', {
            'fields': ('about',)
        }),
    )