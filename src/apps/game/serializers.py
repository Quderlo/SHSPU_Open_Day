from rest_framework import serializers

from apps.game.models import ClickerStats


class ClickerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickerStats
        fields = ['player', 'money', 'total_clicks', 'click_power', 'passive_power']

        lookup_field = ('id', )
