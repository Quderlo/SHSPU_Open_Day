from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ClickerStats

User = get_user_model()


@admin.register(ClickerStats)
class ClickerStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'money', 'total_clicks', 'click_power', 'passive_power')
    list_select_related = ('player',)
    search_fields = ('player__username',)
    list_filter = ('click_power', 'passive_power')
    fieldsets = (
        (None, {
            'fields': ('player', 'money')
        }),
        ('Статистика', {
            'fields': ('total_clicks', 'click_power', 'passive_power')
        }),
    )
