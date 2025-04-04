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

class UpgradeType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    TYPE_CHOICES = (
        ('click', 'Усиление клика'),
        ('passive', 'Пассивный доход'),
        ('multiplier', 'Множитель'),
    )
    upgrade_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name="Тип улучшения"
    )

    base_cost = models.PositiveIntegerField(
        verbose_name="Базовая стоимость"
    )

    power_increment = models.FloatField(
        verbose_name="Прирост силы"
    )

    image = models.ImageField(
        upload_to='upgrades/',
        verbose_name="Изображение"
    )

    max_level = models.PositiveIntegerField(
        default=0,
        verbose_name="Максимальный уровень"
    )

    passive_interval = models.PositiveIntegerField(
        default=1,
        help_text="Интервал в секундах для генерации дохода",
        verbose_name="Интервал пассивного дохода"
    )

    class Meta:
        verbose_name = "Тип улучшения"
        verbose_name_plural = "Типы улучшений"

    def __str__(self):
        return self.name

class UserUpgrade(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='upgrades',
        verbose_name="Пользователь"
    )

    upgrade = models.ForeignKey(
        UpgradeType,
        on_delete=models.CASCADE,
        verbose_name="Улучшение"
    )

    level = models.PositiveIntegerField(
        default=1,
        verbose_name="Уровень"
    )

    class Meta:
        unique_together = ('user', 'upgrade')
        verbose_name = "Улучшение пользователя"
        verbose_name_plural = "Улучшения пользователей"

    def get_current_cost(self):
        return int(self.upgrade.base_cost * (1.15 ** self.level))

    def get_current_power(self):
        return self.upgrade.power_increment * self.level

    def __str__(self):
        return f"{self.user} - {self.upgrade} (ур. {self.level})"