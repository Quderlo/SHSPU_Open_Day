from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import ClickerStats, UpgradeType, UserUpgrade

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


@admin.register(UpgradeType)
class UpgradeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'upgrade_type', 'base_cost', 'power_increment', 'max_level', 'image_preview')
    list_editable = ('base_cost', 'power_increment', 'max_level')
    list_filter = ('upgrade_type',)
    search_fields = ('name', 'description')
    readonly_fields = ('image_preview',)

    fieldsets = (
        (None, {
            'fields': ('name', 'upgrade_type', 'description')
        }),
        ('Характеристики', {
            'fields': ('base_cost', 'power_increment', 'max_level', 'passive_interval')
        }),
        ('Изображение', {
            'fields': ('image', 'image_preview')
        }),
    )

    def image_preview(self, obj):
        return obj.image and f'<img src="{obj.image.url}" style="max-height: 100px;"/>'

    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True


@admin.register(UserUpgrade)
class UserUpgradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'upgrade', 'level',)
    list_filter = ('upgrade', 'level')
    search_fields = ('user__username', 'upgrade__name')
    raw_id_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'upgrade')
        }),
        ('Детали', {
            'fields': ('level',)
        }),
    )