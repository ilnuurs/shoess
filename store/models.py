from django.db import models
from django.contrib.auth.models import User

class Sneaker(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    sizes = models.JSONField(default=list, verbose_name="Доступные размеры")
    gallery = models.JSONField(default=list, blank=True, verbose_name="Галерея изображений")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='sneakers/', verbose_name="Картинка")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.PositiveIntegerField(default=0, verbose_name="Скидка (%)")
    feature = models.CharField(max_length=100, blank=True, null=True, verbose_name="Особенность / Тег")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.brand} - {self.title}"

    class Meta:
        verbose_name = "Кроссовки"
        verbose_name_plural = "Кроссовки"

