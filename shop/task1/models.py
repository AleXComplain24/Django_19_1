from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.IntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер игры
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение 18+
    buyer = models.ManyToManyField(Buyer, related_name="games")  # Many-to-Many связь с Buyer

    def __str__(self):
        return self.title

