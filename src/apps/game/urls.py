from django.urls import path

from apps.game.views import ClickerGameView

urlpatterns = [
    path('', ClickerGameView.as_view(), name='clicker-game'),
]