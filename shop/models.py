from django.db import models


# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=10, verbose_name="Назване")
    designation = models.CharField(max_length=10, verbose_name="Обозначение")

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Item(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="Цена")
    currency = models.ForeignKey(Currency, models.PROTECT, verbose_name="Валюта")

    def __str__(self):
        return self.name

    def get_stripe_cost(self):
        return int(self.price * 100)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
