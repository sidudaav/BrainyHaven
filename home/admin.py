from django.contrib import admin
from .models import Pattern, Analogy, Riddle, IP

class PatternAdmin(admin.ModelAdmin):
    list_display = ['content', 'answer', 'is_active']
    list_filter = ['is_active']
    search_fields = ['content', 'answer']
    actions = ['approve', 'hide']

    def approve(self, request, queryset):
        queryset.update(is_active=True)

    def hide(self, request, queryset):
        queryset.update(is_active=False) 

class AnalogyAdmin(admin.ModelAdmin):
    list_display = ['content', 'answer', 'is_active']
    list_filter = ['is_active']
    search_fields = ['content', 'answer']
    actions = ['approve', 'hide']

    def approve(self, request, queryset):
        queryset.update(is_active=True)

    def hide(self, request, queryset):
        queryset.update(is_active=False) 

class RiddleAdmin(admin.ModelAdmin):
    list_display = ['content', 'answer', 'is_active']
    list_filter = ['is_active']
    search_fields = ['content', 'answer']
    actions = ['approve', 'hide']

    def approve(self, request, queryset):
        queryset.update(is_active=True)

    def hide(self, request, queryset):
        queryset.update(is_active=False) 

admin.site.register(Pattern, PatternAdmin)
admin.site.register(Analogy, AnalogyAdmin)
admin.site.register(Riddle, RiddleAdmin)