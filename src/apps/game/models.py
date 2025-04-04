from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class ClickerStats(models.Model):
    player = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Игрок"
    )
    money = models.PositiveBigIntegerField(
        default=0,
        verbose_name="Деньги"
    )
    total_clicks = models.PositiveBigIntegerField(
        default=0,
        verbose_name="Всего кликов"
    )
    click_power = models.PositiveIntegerField(
        default=1,
        verbose_name="Сила клика"
    )
    passive_power = models.PositiveIntegerField(
        default=0,
        verbose_name="Пассивный доход"
    )

    class Meta:
        verbose_name = "Статистика кликера"
        verbose_name_plural = "Статистики кликеров"

    def __str__(self):
        return f"Статистика {self.player.username}"
